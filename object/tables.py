#
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


metadata = MetaData()
users = Table('users', metadata,
    Column('FIRST_NAME', String(60), primary_key=True),
    Column('LAST_NAME', String(60)),
    Column('AGE', Integer, nullable=False),
    Column('SEX', String(60), nullable=False),
    Column('INCOME', String(255), nullable=False),
    )


