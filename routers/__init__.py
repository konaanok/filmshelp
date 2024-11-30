from .description_routers import description_router
from .director_routers import director_router
from .film_routers import film_router
from .genre_routers import genre_router
from .rating_routers import rating_router
from .user_router import auth_router

__all__ = ["description_router", "director_router", "film_router", "genre_router", "rating_router", "auth_router"]