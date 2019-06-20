"""create products

Revision ID: 598f5cd5a82d
Revises: 
Create Date: 2019-06-20 15:30:13.862821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '598f5cd5a82d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
