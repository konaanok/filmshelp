from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from models import director_table, description_table
metadata = MetaData()


director_description = Table(
    "director_description",
    metadata,
    Column("director_id", Integer, ForeignKey(director_table.c.id), primary_key=True),
    Column("description_id", Integer, ForeignKey(description_table.c.id), primary_key=True),
    Column("director_name", String, ForeignKey(director_table.c.name), primary_key=True),
    Column("description_name", String, ForeignKey(description_table.c.name), primary_key=True),
) 
