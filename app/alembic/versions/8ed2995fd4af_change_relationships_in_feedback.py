"""change relationships in feedback

Revision ID: 8ed2995fd4af
Revises: 8286411b3eec
Create Date: 2024-05-03 20:44:33.186791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ed2995fd4af'
down_revision: Union[str, None] = '8286411b3eec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedback', sa.Column('product', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'feedback', 'product', ['product'], ['id'])
    op.alter_column('picup_point', 'physical_address',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=100),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('picup_point', 'physical_address',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
    op.drop_constraint(None, 'feedback', type_='foreignkey')
    op.drop_column('feedback', 'product')
    # ### end Alembic commands ###
