"""fix name mistake

Revision ID: 7bb9fa0075ac
Revises: 0d938e2ad55a
Create Date: 2024-05-06 12:08:24.856395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7bb9fa0075ac'
down_revision: Union[str, None] = '0d938e2ad55a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('description', sa.String(), nullable=False))
    op.drop_column('product', 'descrption')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('descrption', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('product', 'description')
    # ### end Alembic commands ###
