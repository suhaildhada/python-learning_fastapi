"""create post table

Revision ID: 5d2a25932c65
Revises: 
Create Date: 2022-03-06 17:43:11.670236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d2a25932c65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String, nullable=False))


def downgrade():
    op.drop_table("posts")
