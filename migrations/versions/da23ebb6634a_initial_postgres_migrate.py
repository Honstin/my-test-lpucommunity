"""initial postgres migrate

Revision ID: da23ebb6634a
Revises: 
Create Date: 2020-07-09 18:19:33.803487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da23ebb6634a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locks_owned',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lockname', sa.String(length=64), nullable=True),
    sa.Column('ownedBy', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_locks_owned_lockname'), 'locks_owned', ['lockname'], unique=False)
    op.create_index(op.f('ix_locks_owned_ownedBy'), 'locks_owned', ['ownedBy'], unique=False)
    op.create_table('res_tool',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company', sa.String(length=64), nullable=True),
    sa.Column('url', sa.String(length=100), nullable=False),
    sa.Column('basedIn', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id', 'url')
    )
    op.create_index(op.f('ix_res_tool_basedIn'), 'res_tool', ['basedIn'], unique=False)
    op.create_index(op.f('ix_res_tool_company'), 'res_tool', ['company'], unique=True)
    op.create_index(op.f('ix_res_tool_url'), 'res_tool', ['url'], unique=False)
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('createdOn', sa.DateTime(), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_online', sa.DateTime(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_createdOn'), 'user', ['createdOn'], unique=False)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('locks_for_sale',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lockname', sa.String(length=64), nullable=True),
    sa.Column('ownedBy', sa.String(length=64), nullable=True),
    sa.Column('LfS', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['LfS'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_locks_for_sale_lockname'), 'locks_for_sale', ['lockname'], unique=False)
    op.create_index(op.f('ix_locks_for_sale_ownedBy'), 'locks_for_sale', ['ownedBy'], unique=False)
    op.create_table('locks_on_loan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lockname', sa.String(length=64), nullable=True),
    sa.Column('ownedBy', sa.String(length=64), nullable=True),
    sa.Column('loanedTo', sa.String(length=64), nullable=True),
    sa.Column('LoL', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['LoL'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_locks_on_loan_loanedTo'), 'locks_on_loan', ['loanedTo'], unique=False)
    op.create_index(op.f('ix_locks_on_loan_lockname'), 'locks_on_loan', ['lockname'], unique=False)
    op.create_index(op.f('ix_locks_on_loan_ownedBy'), 'locks_on_loan', ['ownedBy'], unique=False)
    op.create_table('user_belt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('belt_name', sa.String(length=16), nullable=True),
    sa.Column('UsrBelt', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['UsrBelt'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_belt_belt_name'), 'user_belt', ['belt_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_belt_belt_name'), table_name='user_belt')
    op.drop_table('user_belt')
    op.drop_index(op.f('ix_locks_on_loan_ownedBy'), table_name='locks_on_loan')
    op.drop_index(op.f('ix_locks_on_loan_lockname'), table_name='locks_on_loan')
    op.drop_index(op.f('ix_locks_on_loan_loanedTo'), table_name='locks_on_loan')
    op.drop_table('locks_on_loan')
    op.drop_index(op.f('ix_locks_for_sale_ownedBy'), table_name='locks_for_sale')
    op.drop_index(op.f('ix_locks_for_sale_lockname'), table_name='locks_for_sale')
    op.drop_table('locks_for_sale')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_createdOn'), table_name='user')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_index(op.f('ix_res_tool_url'), table_name='res_tool')
    op.drop_index(op.f('ix_res_tool_company'), table_name='res_tool')
    op.drop_index(op.f('ix_res_tool_basedIn'), table_name='res_tool')
    op.drop_table('res_tool')
    op.drop_index(op.f('ix_locks_owned_ownedBy'), table_name='locks_owned')
    op.drop_index(op.f('ix_locks_owned_lockname'), table_name='locks_owned')
    op.drop_table('locks_owned')
    # ### end Alembic commands ###
