"""add rating

Revision ID: de9053151d46
Revises: e694e745054d
Create Date: 2024-11-16 11:18:57.151985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'de9053151d46'
down_revision: Union[str, None] = 'e694e745054d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating_web', sa.Integer(), nullable=True),
    sa.Column('rating_user', sa.Integer(), nullable=True),
    sa.Column('review', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['film.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint('uq_director_name', 'director', ['name'])
    op.create_unique_constraint('uq_description_name', 'description', ['name'])
    op.create_unique_constraint('uq_genre_name', 'genre', ['name'])
    op.create_foreign_key(None, 'director_description', 'director', ['director_name'], ['name'])
    op.create_foreign_key(None, 'director_description', 'description', ['description_name'], ['name'])
    op.create_foreign_key(None, 'genre_director', 'genre', ['genre_name'], ['name'])
    op.create_foreign_key(None, 'genre_director', 'director', ['director_name'], ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'genre_director', type_='foreignkey')
    op.drop_constraint(None, 'genre_director', type_='foreignkey')
    op.drop_constraint(None, 'director_description', type_='foreignkey')
    op.drop_constraint(None, 'director_description', type_='foreignkey')
    op.drop_table('rating')
    # ### end Alembic commands ###
