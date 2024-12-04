from sqlalchemy import MetaData, Table, Column, Integer, String
metadata = MetaData()

user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False, primary_key=True),
    Column("hashed_password", String, nullable=False),
)