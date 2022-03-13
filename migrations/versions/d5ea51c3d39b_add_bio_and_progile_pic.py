"""add bio and progile_pic

Revision ID: d5ea51c3d39b
Revises: 18ef261309b3
Create Date: 2022-03-13 20:46:25.636132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5ea51c3d39b'
down_revision = '18ef261309b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###