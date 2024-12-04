from sqlalchemy import MetaData, Table, Column, Integer, String
metadata = MetaData()

genre_table = Table(
    "genre",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, primary_key=True)
)