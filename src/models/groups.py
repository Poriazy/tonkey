from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, BigInteger, \
Float, Integer, SmallInteger, String, Text, DateTime, FetchedValue, text, func

metadata = MetaData()

connection_string = 'postgresql://debman:password@localhost/bsg'
engine = create_engine(
    connection_string, echo=True, pool_size=6, max_overflow=10)

groups = Table("groups", metadata,
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
                   #String(100, collation="fa_IR.utf8"),
                   #Text(collation="fa_IR.utf8"),
                   #Text(),
                   String(100),
                   index=True,
                   nullable=False),
            Column("description",
                   Text(),
                   nullable=False,
                   # TODO: correct other tables like below
                   server_default="",
                   server_onupdate=""),
            Column("pe",
                   Float(),
                   nullable=False,
                   # TODO: correct other tables like below
                   server_default=text("0")),
            Column("time_stamp",
                   DateTime(),
                   nullable=False,
                   # TODO: check this
                   #server_onupdate=FetchedValue()))
                   #default=datetime.now,
                   # TODO: correct other tables like below
                   server_default=func.now(),
                   server_onupdate=func.now()))

metadata.create_all(engine)

