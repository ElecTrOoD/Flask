"""'create_tags'

Revision ID: 3fe44ac0c7b2
Revises: 3d572d341ca0
Create Date: 2021-07-03 00:22:39.804343

"""
from alembic import op

# revision identifiers, used by Alembic.
from sqlalchemy import table, column, String, Integer

revision = '3fe44ac0c7b2'
down_revision = '3d572d341ca0'
branch_labels = None
depends_on = None

tags = table('tags',
             column('id', Integer),
             column('name', String)
             )


def upgrade():
    op.bulk_insert(tags, [{'id': 1,
                           'name': 'flask'},
                          {'id': 2,
                           'name': 'django'},
                          {'id': 3,
                           'name': 'python'},
                          {'id': 4,
                           'name': 'geekbrains'},
                          {'id': 5,
                           'name': 'sqlite'}])


def downgrade():
    pass
