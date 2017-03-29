from oslo_config import cfg
from oslo_db import api as db_api
from oslo_db.sqlalchemy import session
from oslo_db.sqlalchemy import enginefacade
from sqlalchemy import select, or_, between, func, distinct
from sqlalchemy import create_engine
from oslo_db import options
import tables
import create_tables


# implement DEFAULT config
cfg.CONF.register_group(cfg.OptGroup(
 name='storage:sqlalchemy', title="Configuration for SQLAlchemy Storage"
))
cfg.CONF.register_opts(options.database_opts, group='storage:sqlalchemy')
# Authenticating with test.conf
cfg.CONF(['--config-file', 'test.conf'])
CONF = cfg.CONF
storage_db = CONF['storage:sqlalchemy'].connection

engine = create_engine(storage_db, echo=True)
conn = engine.connect()


query = tables.users.c


@enginefacade.reader
def refresh_from_db(context, cache):
    sel = tables.select([query.FIRST_NAME, query.LAST_NAME])
    res = context.connection.execute(sel).fetchall()
    cache.id_cache = {r[1]: r[0] for r in res}
    cache.str_cache = {r[0]: r[1] for r in res}
    return refresh_from_db(context)


# Method to add new table into mysql
def create():
    engine.execute("DROP TABLE IF EXISTS EMPLOYEE")
    try:
        engine.execute(create_tables.users)
        engine.execute(create_tables.domains)
        create()
        conn.commit()
    except:
        conn.close()
create()


# method to add to mysql
def call_operation1():
    engine.execute("insert into EMPLOYEE (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) "
                   "values('trung','nguyen','29','female','1')")
    try:
        conn.commit()
    except:
        conn.close()


def call_operation2():
    engine.execute("insert into domains (id,name,master,last_check,type, notified_serial,account) "
                   "values('1','trung','CA','100','DNS','2','trungnv')")
    try:
        conn.commit()
    except:
        conn.close()
call_operation1()
call_operation2()


def queries():
    # query data from mysql
    engine.execute = select([query.FIRST_NAME, query.LAST_NAME, query.AGE, query.SEX])
#    s = select([query.id, query.name, query.fullname, query.email_address])
#    result = conn.execute(s)
queries()


conn.close()
