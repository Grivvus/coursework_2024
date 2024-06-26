"""add admin relationship, change some models

Revision ID: 8286411b3eec
Revises: 00ba630cadb8
Create Date: 2024-05-03 16:37:16.312913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8286411b3eec'
down_revision: Union[str, None] = '00ba630cadb8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('passport_series', sa.String(length=4), nullable=False),
    sa.Column('passport_number', sa.String(length=6), nullable=False),
    sa.Column('living_address', sa.String(), nullable=False),
    sa.Column('place_of_residence', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('second_name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=70), nullable=False),
    sa.Column('phone_number', sa.String(length=13), nullable=False),
    sa.Column('password', sa.String(length=32), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('feedback', sa.Column('rate', sa.Integer(), nullable=False))
    op.alter_column('feedback', 'text',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'updated_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    op.drop_column('user', 'is_super_user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_super_user', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.alter_column('user', 'updated_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
    op.alter_column('feedback', 'text',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('feedback', 'rate')
    op.drop_table('admin')
    # ### end Alembic commands ###
