"""empty message

Revision ID: e8c7370998e5
Revises: c76ceb114b9c
Create Date: 2023-12-28 11:47:18.521243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8c7370998e5'
down_revision = 'c76ceb114b9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_partenaire')
    with op.batch_alter_table('partenaire', schema=None) as batch_op:
        batch_op.create_unique_constraint('unique_code_type', ['code', 'type'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('partenaire', schema=None) as batch_op:
        batch_op.drop_constraint('unique_code_type', type_='unique')

    op.create_table('_alembic_tmp_partenaire',
    sa.Column('partenaire_id', sa.INTEGER(), nullable=False),
    sa.Column('code', sa.VARCHAR(length=100), nullable=True),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('contact', sa.VARCHAR(length=50), nullable=True),
    sa.Column('logo', sa.VARCHAR(length=200), nullable=True),
    sa.Column('icon', sa.VARCHAR(length=10), nullable=True),
    sa.Column('type', sa.VARCHAR(length=10), nullable=True),
    sa.PrimaryKeyConstraint('partenaire_id'),
    sa.UniqueConstraint('code', 'type', name='unique_code_type')
    )
    # ### end Alembic commands ###
