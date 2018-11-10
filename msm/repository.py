from msm import config
from msm.util import db, log


def init():
    log.info('Create table')
    sqlite_file = config.database_path + config.database_name
    connection, cursor = db.connect(sqlite_file)
    create_table = 'CREATE TABLE settings (name TEXT, file TEXT, isSelected INTEGER);'
    db.execute_statement(cursor, create_table)
    db.close(connection, cursor)


def create(alias, file):
    log.info('Add new data: alias={A}, file={F}'.format(A=alias, F=file))
    sqlite_file = config.database_path + config.database_name
    conn, cur = db.connect(sqlite_file)
    insert_data = 'INSERT INTO settings VALUES ({N}, {F}, {S});'.format(N=alias, F=file, S=0)
    db.execute_statement(cur, insert_data)
    db.close(conn, cur)


def list_all():
    log.info('Listing all data')
    sqlite_file = config.database_path + config.database_name
    conn, cur = db.connect(sqlite_file)
    select_all = 'SELECT * FROM settings;'
    results = db.execute_query(cur, select_all)
    db.close(conn, cur)

    return map(lambda data: (data[0], data[1]), results)


def update(alias, file, is_selected):
    log.info('Update data: alias={A}, file={F} with: isSelected={S}'.format(A=alias, F=file, S=is_selected))
    sqlite_file = config.database_path + config.database_name
    conn, cur = db.connect(sqlite_file)
    update_data = 'UPDATE settings SET is_selected = {S} WHERE name = {N} AND file = {F};'.format(N=alias, F=file,
                                                                                                  S=is_selected)
    db.execute_statement(cur, update_data)
    db.close(conn, cur)


def delete(alias, file):
    log.info('Delete data: alias={A}, file={F}'.format(A=alias, F=file))
    sqlite_file = config.database_path + config.database_name
    conn, cur = db.connect(sqlite_file)
    delete_data = 'DELETE FROM settings WHERE name = {N} AND file = {F};'.format(N=alias, F=file)
    db.execute_statement(cur, delete_data)
    db.close(conn, cur)
