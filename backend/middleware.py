from collections import defaultdict
from time import time
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import ValidationException
from fastapi.encoders import jsonable_encoder

async def validation_exception_handler(request: Request, exc: ValidationException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )

request_counter = defaultdict(list)
limit = 5
time_lim = 1

async def limit_request(request: Request, call_next):
    user_ip = request.client.host 
    current_time = time()
    request_counter[user_ip] = [
        timestamp for timestamp in request_counter[user_ip]
        if timestamp > current_time - time_lim
    ]
    if len(request_counter[user_ip]) >= limit:
        return JSONResponse(
            content="Too Many Requests. Please try again later.",
            status_code=429
)
    request_counter[user_ip].append(current_time)
    return await call_next(request)

