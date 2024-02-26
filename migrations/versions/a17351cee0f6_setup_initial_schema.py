"""Setup initial schema

Revision ID: a17351cee0f6
Revises: 
Create Date: 2024-02-26 03:18:57.443609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a17351cee0f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_code', sa.String(length=120), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('session_code')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('song_title', sa.String(length=120), nullable=False),
    sa.Column('artist', sa.String(length=120), nullable=False),
    sa.Column('video_link', sa.String(length=255), nullable=True),
    sa.Column('played_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('participant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('joined_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['session_id'], ['session.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('songs_queue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.Column('song_title', sa.String(length=120), nullable=False),
    sa.Column('artist', sa.String(length=120), nullable=False),
    sa.Column('video_link', sa.String(length=255), nullable=True),
    sa.Column('video_thumbnail', sa.String(length=255), nullable=True),
    sa.Column('added_by', sa.Integer(), nullable=False),
    sa.Column('queued_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['added_by'], ['participant.id'], ),
    sa.ForeignKeyConstraint(['session_id'], ['session.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('songs_queue')
    op.drop_table('participant')
    op.drop_table('history')
    op.drop_table('user')
    op.drop_table('session')
    # ### end Alembic commands ###