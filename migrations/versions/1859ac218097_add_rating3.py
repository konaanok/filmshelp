"""add rating3

Revision ID: 1859ac218097
Revises: 90ce4ecf2968
Create Date: 2024-11-16 12:51:20.961007

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1859ac218097'
down_revision: Union[str, None] = '90ce4ecf2968'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rating', sa.Column('film_id', sa.Integer(), nullable=True))
    op.drop_constraint('rating_id_fkey', 'rating', type_='foreignkey')
    op.create_foreign_key(None, 'rating', 'film', ['film_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rating', type_='foreignkey')
    op.create_foreign_key('rating_id_fkey', 'rating', 'film', ['id'], ['id'])
    op.drop_column('rating', 'film_id')
    # ### end Alembic commands ###
