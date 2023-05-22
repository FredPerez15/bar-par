"""fixed ingri

Revision ID: 6393f58f54d8
Revises: c7bb421dcbdd
Create Date: 2023-05-22 12:21:03.423078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6393f58f54d8'
down_revision = 'c7bb421dcbdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inventories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ingredient_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('inventories_ingridient_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'ingredients', ['ingredient_id'], ['id'])
        batch_op.drop_column('ingridient_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inventories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ingridient_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('inventories_ingridient_id_fkey', 'ingredients', ['ingridient_id'], ['id'])
        batch_op.drop_column('ingredient_id')

    # ### end Alembic commands ###