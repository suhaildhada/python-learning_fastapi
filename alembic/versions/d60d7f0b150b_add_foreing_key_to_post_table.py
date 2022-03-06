"""add foreing key to post table

Revision ID: d60d7f0b150b
Revises: c888b032e35d
Create Date: 2022-03-06 18:07:30.446507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd60d7f0b150b'
down_revision = 'c888b032e35d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
                  sa.Column("owner_id", sa.Integer, nullable=False)
                  )
    op.create_foreign_key("post_user_fk", source_table="posts", referent_table="users", local_cols=[
                          "owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint("post_user_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
