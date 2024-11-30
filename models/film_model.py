from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey 
metadata = MetaData()

film_table = Table(
    "film",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("year", Integer),
    Column("description_id", Integer, ForeignKey("description.id")),
)