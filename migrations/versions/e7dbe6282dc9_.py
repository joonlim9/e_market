"""empty message

Revision ID: e7dbe6282dc9
Revises: 07df287802d5
Create Date: 2021-09-06 00:30:04.650331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7dbe6282dc9'
down_revision = '07df287802d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('username', sa.String(length=30), nullable=False))
    op.drop_constraint(None, 'blog_post', type_='foreignkey')
    op.create_foreign_key(None, 'blog_post', 'users', ['username'], ['username'])
    op.drop_column('blog_post', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('user_id', sa.INTEGER(), nullable=False))
    op.drop_constraint(None, 'blog_post', type_='foreignkey')
    op.create_foreign_key(None, 'blog_post', 'users', ['user_id'], ['id'])
    op.drop_column('blog_post', 'username')
    # ### end Alembic commands ###