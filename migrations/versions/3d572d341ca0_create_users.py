"""'create_users'

Revision ID: 3d572d341ca0
Revises: d2021c0ba5ca
Create Date: 2021-06-26 07:48:39.066908

"""
from alembic import op

# revision identifiers, used by Alembic.
from sqlalchemy import table, column, Integer, String, Boolean
from werkzeug.security import generate_password_hash

revision = '3d572d341ca0'
down_revision = '0a437f9cd25e'
branch_labels = None
depends_on = None

users = table('users',
              column('id', Integer),
              column('username', String),
              column('first_name', String),
              column('last_name', String),
              column('email', String),
              column('password', String),
              column('is_staff', Boolean)
              )


def upgrade():
    op.bulk_insert(users, [{'id': 2,
                            'username': 'Test1',
                            'first_name': 'Ivan',
                            'last_name': 'Ivanov',
                            'email': 'test1@test.com',
                            'password': generate_password_hash('test1'),
                            'is_staff': False},
                           {'id': 3,
                            'username': 'Test2',
                            'first_name': 'Petr',
                            'last_name': 'Ivanov',
                            'email': 'test2@test.com',
                            'password': generate_password_hash('test2'),
                            'is_staff': False},
                           {'id': 4,
                            'username': 'Test3',
                            'first_name': 'Ilya',
                            'last_name': 'Ivanov',
                            'email': 'test3@test.com',
                            'password': generate_password_hash('test3'),
                            'is_staff': False},
                           {'id': 5,
                            'username': 'Test4',
                            'first_name': 'Oleg',
                            'last_name': 'Ivanov',
                            'email': 'test4@test.com',
                            'password': generate_password_hash('test4'),
                            'is_staff': False}])


def downgrade():
    pass
