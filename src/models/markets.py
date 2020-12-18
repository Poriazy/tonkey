from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, SmallInteger, \
    Text, DateTime, String

metadata = MetaData()

connection_string = 'postgresql://debman:password@localhost/bsg'
engine = create_engine(
    connection_string, echo=True, pool_size=6, max_overflow=10)

markets = Table("markets", metadata,
                Column("id",
                       SmallInteger(),
                       primary_key=True),
                Column("code",
                       SmallInteger(),
                       index=True,
                       unique=True,
                       nullable=False),
                Column("title",
                       # TODO check this
                       #String(100, collation='utf-8'),
                       # String(100),
                       Text(),
                       index=True,
                       nullable=False),
                Column("description",
                       Text(),
                       nullable=False,
                       default="",
                       onupdate=""),
                Column("time_stamp",
                       DateTime(),
                       nullable=False,
                       default=datetime.now,
                       onupdate=datetime.now))

metadata.create_all(engine)
