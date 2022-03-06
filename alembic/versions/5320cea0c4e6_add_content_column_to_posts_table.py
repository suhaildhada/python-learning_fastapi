"""add content column to posts table

Revision ID: 5320cea0c4e6
Revises: 5d2a25932c65
Create Date: 2022-03-06 17:52:07.288083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5320cea0c4e6'
down_revision = '5d2a25932c65'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String, nullable=False))


def downgrade():
    op.drop_column("posts", "content")
