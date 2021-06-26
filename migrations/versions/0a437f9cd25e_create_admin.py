"""'create-admin'

Revision ID: 0a437f9cd25e
Revises: a3654faef6b4
Create Date: 2021-05-23 10:22:34.571764
"""
from alembic import op

# revision identifiers, used by Alembic.
from sqlalchemy import column, String, Integer, table, Boolean

revision = '0a437f9cd25e'
down_revision = '46e86d0169c8'
branch_labels = None
depends_on = None

users = table('users',
              column('id', Integer),
              column('username', String),
              column('email', String),
              column('password', String),
              column('is_staff', Boolean)
              )


def upgrade():
    from werkzeug.security import generate_password_hash

    op.bulk_insert(users, [{'id': 1,
                            'username': 'admin',
                            'email': 'admin@admin.com',
                            'password': generate_password_hash('admin'),
                            'is_staff': True}])


def downgrade():
    pass
