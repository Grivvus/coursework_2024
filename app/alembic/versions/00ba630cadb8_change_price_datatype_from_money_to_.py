"""change price datatype from money to numeric

Revision ID: 00ba630cadb8
Revises: 6f4687827d49
Create Date: 2024-05-02 19:31:38.700347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '00ba630cadb8'
down_revision: Union[str, None] = '6f4687827d49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'price',
               existing_type=postgresql.MONEY(),
               type_=sa.NUMERIC(precision=2, scale=10),
               existing_nullable=False)
    op.add_column('user', sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'updated_at')
    op.alter_column('product', 'price',
               existing_type=sa.NUMERIC(precision=2, scale=10),
               type_=postgresql.MONEY(),
               existing_nullable=False)
    # ### end Alembic commands ###
