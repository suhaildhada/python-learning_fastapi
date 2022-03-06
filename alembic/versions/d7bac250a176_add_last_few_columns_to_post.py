"""add last few columns to post

Revision ID: d7bac250a176
Revises: d60d7f0b150b
Create Date: 2022-03-06 18:20:24.154150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7bac250a176'
down_revision = 'd60d7f0b150b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
                  sa.Column("published", sa.Boolean(),
                            nullable=False, server_default="TRUE")
                  )
    op.add_column("posts",
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                            nullable=False, server_default=sa.text("now()"))
                  )


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
