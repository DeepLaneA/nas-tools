"""1.0.0

Revision ID: 6940fa00ebb9
Revises: 
Create Date: 2022-10-21 23:08:34.663081

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = '6940fa00ebb9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'CUSTOM_WORDS' not in tables:
        op.create_table('CUSTOM_WORDS',
                        sa.Column('ID', sa.Integer(), nullable=False),
                        sa.Column('REPLACED', sa.Text(), nullable=True),
                        sa.Column('REPLACE', sa.Text(), nullable=True),
                        sa.Column('FRONT', sa.Text(), nullable=True),
                        sa.Column('BACK', sa.Text(), nullable=True),
                        sa.Column('OFFSET', sa.Integer(), nullable=True),
                        sa.Column('TYPE', sa.Integer(), nullable=True),
                        sa.Column('GROUP_ID', sa.Integer(), nullable=True),
                        sa.Column('SEASON', sa.Integer(), nullable=True),
                        sa.Column('ENABLED', sa.Integer(), nullable=True),
                        sa.Column('REGEX', sa.Integer(), nullable=True),
                        sa.Column('HELP', sa.Text(), nullable=True),
                        sa.Column('NOTE', sa.Text(), nullable=True),
                        sa.PrimaryKeyConstraint('ID'))
    if 'CUSTOM_WORD_GROUPS' not in tables:
        op.create_table('CUSTOM_WORD_GROUPS',
                        sa.Column('ID', sa.Integer(), nullable=False),
                        sa.Column('TITLE', sa.Text(), nullable=True),
                        sa.Column('YEAR', sa.Text(), nullable=True),
                        sa.Column('TYPE', sa.Integer(), nullable=True),
                        sa.Column('TMDBID', sa.Integer(), nullable=True),
                        sa.Column('SEASON_COUNT', sa.Integer(), nullable=True),
                        sa.Column('NOTE', sa.Text(), nullable=True),
                        sa.PrimaryKeyConstraint('ID'))
    if 'IGNORED_WORDS' in tables:
        op.drop_table('IGNORED_WORDS')
    if 'REPLACED_WORDS' in tables:
        op.drop_table('REPLACED_WORDS')
    if 'OFFSET_WORDS' in tables:
        op.drop_table('OFFSET_WORDS')
    with op.batch_alter_table("CUSTOM_WORDS") as batch_op:
        batch_op.alter_column('OFFSET', type_=sa.Text, existing_type=sa.Integer)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("CUSTOM_WORDS") as batch_op:
        batch_op.alter_column('OFFSET', type=sa.Integer, existing_type=sa.Text)
    # ### end Alembic commands ###
