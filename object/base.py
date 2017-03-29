from oslo_config import cfg
from oslo_db import api as db_api
from oslo_db.sqlalchemy import session
from oslo_db.sqlalchemy import enginefacade
from sqlalchemy import select, or_, between, func, distinct
from sqlalchemy import create_engine
from oslo_db import options
import tables

# implement DEFAULT config
cfg.CONF.register_group(cfg.OptGroup(
 name='storage:sqlalchemy', title="Configuration for SQLAlchemy Storage"
))
cfg.CONF.register_opts(options.database_opts, group='storage:sqlalchemy')
# Authenticating with test.conf
cfg.CONF(['--config-file', 'test.conf'])
CONF = cfg.CONF
storage_db = CONF['storage:sqlalchemy'].connection
engine = create_engine(storage_db, echo = True)
conn = engine.connect()


query = tables.users.c


def queries():
    # query data from mysql
    engine.execute = select([query.id, query.name, query.fullname, query.email_address])
#    s = select([query.id, query.name, query.fullname, query.email_address])
#    result = conn.execute(s)
queries()


@enginefacade.reader.connection
def refresh_from_db(context, cache):
    sel = tables.select([query.id, query.name])
    res = context.connection.execute(sel).fetchall()
    cache.id_cache = {r[1]: r[0] for r in res}
    cache.str_cache = {r[0]: r[1] for r in res}
# refresh_from_db(context=None)


# method to add to mysql
def call_operation():
    engine.execute("insert into users (id,name,fullname,email_address) values('2','hhh','tianhsd','gmail')")
    try:
        call_operation()
        conn.commit()
    except:
        conn.close()
# call_operation()


# Method to add new table into mysql
def create():
    # engine.execute("create table IF NOT EXISTS test (email varchar(70),pwd varchar(20));")
    engine.execute("create table IF NOT EXISTS trung (email varchar(70),pwd varchar(20));")
    try:
        create()
        conn.commit()
    except:
        conn.close()
create()


conn.close()
