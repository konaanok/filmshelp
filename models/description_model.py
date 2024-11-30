from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from models import director_table
metadata = MetaData()

description_table = Table(
    "description",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String, nullable=False),
    Column("name", String, nullable=True, primary_key=True),
    Column("director_id", Integer, ForeignKey(director_table.c.id))  
)