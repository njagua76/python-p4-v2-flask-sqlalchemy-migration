"""rename department

Revision ID: a0005622b984
Revises: f3fbc1153ff6
Create Date: 2025-11-18 23:54:02.219056

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a0005622b984'
down_revision = 'f3fbc1153ff6'
branch_labels = None
depends_on = None


def upgrade():
    # Rename table only
    op.rename_table('department', 'departments')


def downgrade():
    # Revert table name
    op.rename_table('departments', 'department')
