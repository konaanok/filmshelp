from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from models.genre_model import genre_table
from models.director_model import director_table
metadata = MetaData()

genre_director = Table(
    "genre_director",
    metadata,
    Column("genre_id", Integer, ForeignKey(genre_table.c.id), primary_key=True),
    Column("director_id", Integer, ForeignKey(director_table.c.id), primary_key=True),
    Column("genre_name", String, ForeignKey(genre_table.c.name), primary_key=True),
    Column("director_name", String, ForeignKey(director_table.c.name), primary_key=True),
)