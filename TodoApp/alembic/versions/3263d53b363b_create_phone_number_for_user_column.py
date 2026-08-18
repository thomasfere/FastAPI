"""Create phone number for user column

Revision ID: 3263d53b363b
Revises: 
Create Date: 2026-06-21 19:29:29.755977

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3263d53b363b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String, nullable=True))

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')