from oslo_db.sqlalchemy import models
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


#class(models.TimestampMixin, models.ModelBase):
#    id = Column(Integer, primary_key=True)
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(60)),
    Column('fullname', String(255), nullable=False),
    Column('email_address', String(255), nullable=False),
    )

tumhiho = Table('tumhiho', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(60)),
    Column('fullname', String(255), nullable=False),
    Column('email_address', String(255), nullable=False),
    )
