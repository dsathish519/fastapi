"""create post table

Revision ID: 559819b40cdc
Revises: 
Create Date: 2023-07-08 17:51:14.532615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '559819b40cdc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable = True, primary_key=True),
                    sa.Column('title', sa.String(), nullable=True),
                    sa.Column('content', sa.String(), nullable=False),
                    sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'))
                    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
