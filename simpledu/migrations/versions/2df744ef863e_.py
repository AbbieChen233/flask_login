"""empty message

Revision ID: 2df744ef863e
Revises: 
Create Date: 2018-05-10 15:39:52.786627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2df744ef863e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=128), nullable=False))
    op.add_column('user', sa.Column('password', sa.String(length=256), nullable=False))
    op.add_column('user', sa.Column('role', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'role')
    op.drop_column('user', 'password')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###