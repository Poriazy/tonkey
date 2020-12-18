from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, BigInteger, \
    Float, Integer, SmallInteger, String, Text, DateTime, ForeignKey

metadata = MetaData()

connection_string = 'postgresql://debman:password@localhost/bsg'
engine = create_engine(
    connection_string, echo=True, pool_size=6, max_overflow=10)

stocks = Table("stocks", metadata,
               # TODO: check this
               #PrimaryKeyConstraint("id", name="pk_id"),
               #Index("idx", "code", "symbol"),
               Column("id",
                      Integer(),
                      primary_key=True),
               Column("code",
                      # TSE code which used on URL like 71957984642204600
                      # TODO: check this
                      # Unicode(100),
                      #String(100, collation='utf-8'),
                      # String(100),
                      String(20),
                      index=True,
                      unique=True,
                      nullable=False),
               Column("industry_id",
                      # Iran Industry Org. ID like: IRO7APTP0001
                      # TODO: check this
                      # Unicode(100),
                      #String(100, collation='utf-8'),
                      # String(100),
                      String(15),
                      unique=True,
                      nullable=False,
                      default="",
                      onupdate=""),
               Column("symbol",
                      # TODO: check this
                      # Unicode(100),
                      #String(100, collation='utf-8'),
                      # String(100),
                      String(50),
                      index=True,
                      nullable=False),
               Column("title",
                      Text(),
                      nullable=False,
                      default="",
                      onupdate=""),
               Column("group_code",
                      # TODO: check this
                      # SmallInteger(),
                      # ForeignKey(groups.c.code),
                      ForeignKey("groups.code"),
                      nullable=False),
               Column("market_code",
                      # TODO: check this
                      # SmallInteger(),
                      # ForeignKey(markets.c.code),
                      ForeignKey("markets.code"),
                      nullable=False),
               Column("shares_count",
                      BigInteger(),
                      nullable=False,
                      default=0,
                      onupdate=0),
               Column("base_volume",
                      BigInteger(),
                      nullable=False,
                      default=0,
                      onupdate=0),
               Column("pe",
                      Float(),
                      nullable=False,
                      default=0),
               Column("eps",
                      Float(),
                      nullable=False,
                      default=0),
               Column("nav",
                      Float(),
                      nullable=False,
                      default=0),
               Column("floatage",
                      Float(),
                      nullable=False,
                      default=0),
               Column("price_yesterday",
                      # TODO: check thi
                      # Numeric(),
                      Float(),
                      nullable=False,
                      default=0),
               Column("price_min",
                      # TODO: check thi
                      # Numeric(),
                      Float(),
                      nullable=False,
                      default=0),
               Column("price_max",
                      # TODO: check thi
                      # Numeric(),
                      Float(),
                      nullable=False,
                      default=0),
               Column("time_record",
                      DateTime(),
                      nullable=False,
                      default=0),
               Column("time_stamp",
                      DateTime(),
                      nullable=False,
                      default=datetime.now,
                      onupdate=datetime.now))

metadata.create_all(engine)
