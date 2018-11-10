from msm import config
from msm.util import db, log


def init():
    log.debug('Create table')
    sqlite_file = config.database_path + config.database_name
    connection, cursor = db.connect(sqlite_file)
    create_table = 'CREATE TABLE settings (name TEXT, file TEXT, isSelected INTEGER);'
    cursor.execute(create_table)
    connection.commit()
    db.close(connection, cursor)


def create(alias, file):
    log.debug('Add new data: alias={A}, file={F}'.format(A=alias, F=file))
    sqlite_file = config.database_path + config.database_name
    conn, cur = db.connect(sqlite_file)
    insert_data = "INSERT INTO settings (name, file, isSelected) VALUES (?, ?, ?);"
    cur.execute(insert_data, (alias, file, 0))
    conn.commit()
    db.close(conn, cur)


def list_all():
    log.debug('Listing all data')
    sqlite_file = config.database_path + config.database_name
    conn, cur = db.connect(sqlite_file)
    select_all = 'SELECT * FROM settings;'
    results = db.execute_query(cur, select_all)
    db.close(conn, cur)

    return map(lambda data: (data[0], data[1]), results)


def update(alias, file, is_selected):
    log.debug('Update data: alias={A}, file={F} with: isSelected={S}'.format(A=alias, F=file, S=is_selected))
    sqlite_file = config.database_path + config.database_name
    conn, cur = db.connect(sqlite_file)
    update_data = 'UPDATE settings SET isSelected = ? WHERE name = ? AND file = ?;'
    cur.execute(update_data, (is_selected, alias, file))
    conn.commit()
    db.close(conn, cur)


def delete(alias, file):
    log.debug('Delete data: alias={A}, file={F}'.format(A=alias, F=file))
    sqlite_file = config.database_path + config.database_name
    conn, cur = db.connect(sqlite_file)
    delete_data = 'DELETE FROM settings WHERE name = ? AND file = ?;'
    cur.execute(delete_data, (alias, file))
    conn.commit()
    db.close(conn, cur)
