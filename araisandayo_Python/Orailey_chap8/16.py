import sqlalchemy as sa

conn = sa.create_engine('sqlite://')
meta = sa.MetaData()

zo = sa.table('zoo', meta,
              sa.Column('critter', sa.String, primary_key=True),
              sa.Column('count', sa.Integer),
              sa.Column('damages', sa.Float)
              )

meta.create_all(conn)
