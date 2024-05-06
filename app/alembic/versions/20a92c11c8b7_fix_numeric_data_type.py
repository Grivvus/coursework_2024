"""fix numeric data type

Revision ID: 20a92c11c8b7
Revises: 7bb9fa0075ac
Create Date: 2024-05-06 12:16:29.804525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20a92c11c8b7'
down_revision: Union[str, None] = '7bb9fa0075ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'price',
               existing_type=sa.NUMERIC(precision=2, scale=10),
               type_=sa.NUMERIC(precision=10, scale=2),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'price',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               type_=sa.NUMERIC(precision=2, scale=10),
               existing_nullable=False)
    # ### end Alembic commands ###
