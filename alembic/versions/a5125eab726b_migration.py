"""migration

Revision ID: a5125eab726b
Revises: 22b20d38c9ee
Create Date: 2024-07-19 06:09:47.796098

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5125eab726b'
down_revision: Union[str, None] = '22b20d38c9ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('title', sa.String(), nullable=True))
    op.add_column('projects', sa.Column('description', sa.String(), nullable=True))
    op.add_column('projects', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.drop_index('ix_projects_name', table_name='projects')
    op.create_index(op.f('ix_projects_description'), 'projects', ['description'], unique=False)
    op.create_index(op.f('ix_projects_title'), 'projects', ['title'], unique=False)
    op.create_foreign_key(None, 'projects', 'users', ['owner_id'], ['id'])
    op.drop_column('projects', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'projects', type_='foreignkey')
    op.drop_index(op.f('ix_projects_title'), table_name='projects')
    op.drop_index(op.f('ix_projects_description'), table_name='projects')
    op.create_index('ix_projects_name', 'projects', ['name'], unique=False)
    op.drop_column('projects', 'owner_id')
    op.drop_column('projects', 'description')
    op.drop_column('projects', 'title')
    # ### end Alembic commands ###