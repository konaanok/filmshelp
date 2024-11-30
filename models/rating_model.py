from sqlalchemy import Float, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB 
from models import film_table, user_table

metadata = MetaData()

rating_table = Table(
    "rating",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("rating_user", Float, nullable=True),
    Column("review", JSONB, nullable=True),
    Column("film_id", Integer, ForeignKey(film_table.c.id)),
    Column("username", String, ForeignKey(user_table.c.username))
)

rating_average_table = Table(
    "rating_average",
    metadata,
    Column("film_id", Integer, ForeignKey("film.id", ondelete="CASCADE"), primary_key=True),  
    Column("rating_average", Float, default=0.0),  
    Column("rating_count", Integer, default=0),    
    Column("rating_web", Float)
)