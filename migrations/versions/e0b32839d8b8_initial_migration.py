"""initial migration

Revision ID: e0b32839d8b8
Revises: 
Create Date: 2023-12-27 17:21:28.368132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0b32839d8b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('partenaire', schema=None) as batch_op:
        batch_op.alter_column('code',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('contact',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('logo',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
        batch_op.alter_column('icon',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
        batch_op.alter_column('type',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('partenaire', schema=None) as batch_op:
        batch_op.alter_column('type',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
        batch_op.alter_column('icon',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
        batch_op.alter_column('logo',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
        batch_op.alter_column('contact',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('code',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###
