"""empty message

Revision ID: a340cbdd7531
Revises: 
Create Date: 2023-02-08 14:59:15.582174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a340cbdd7531'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('last_name', sa.String(length=255), nullable=True))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###