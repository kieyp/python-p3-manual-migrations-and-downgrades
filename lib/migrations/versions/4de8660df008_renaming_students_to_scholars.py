"""Renaming students to scholars


Revision ID: 4de8660df008
Revises: 791279dd0760
Create Date: 2024-02-11 12:01:57.344285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4de8660df008'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
