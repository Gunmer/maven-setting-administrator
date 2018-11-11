from msm import config
from msm.util import db, log


def init():
    log.debug('Create table')
    connection, cursor = db.connect(config.database_path)
    create_table = 'CREATE TABLE settings (name TEXT, file TEXT, isSelected INTEGER);'
    cursor.execute(create_table)
    connection.commit()
    db.close(connection, cursor)


def create(alias, file):
    log.debug('Add new data: alias={A}, file={F}'.format(A=alias, F=file))
    conn, cur = db.connect(config.database_path)
    insert_data = "INSERT INTO settings (name, file, isSelected) VALUES (?, ?, ?);"
    cur.execute(insert_data, (alias, file, 0))
    conn.commit()
    db.close(conn, cur)


def list_all():
    log.debug('Listing all data')
    conn, cur = db.connect(config.database_path)
    select_all = 'SELECT * FROM settings;'
    cur.execute(select_all)
    results = cur.fetchall()
    log.debug('Data: {}'.format(results))
    db.close(conn, cur)

    return results


def find_selected():
    log.debug('Find selected data')
    conn, cur = db.connect(config.database_path)
    select_find_selected = 'SELECT * FROM settings WHERE isSelected = 1;'
    cur.execute(select_find_selected)
    data = cur.fetchone()
    log.debug('Data: {}'.format(data))
    db.close(conn, cur)

    return data


def find_one(alias):
    log.debug('Find selected data')
    conn, cur = db.connect(config.database_path)
    select_find_selected = 'SELECT * FROM settings WHERE name = ?;'
    cur.execute(select_find_selected, (alias,))
    data = cur.fetchone()
    log.debug('Data: {}'.format(data))
    db.close(conn, cur)

    return data


def update(alias, is_selected):
    log.debug('Update data: alias={A} with: isSelected={S}'.format(A=alias, S=is_selected))
    conn, cur = db.connect(config.database_path)
    update_data = 'UPDATE settings SET isSelected = ? WHERE name = ?;'
    cur.execute(update_data, (is_selected, alias))
    conn.commit()
    db.close(conn, cur)


def delete(alias):
    log.debug('Delete data: alias={A}'.format(A=alias))
    conn, cur = db.connect(config.database_path)
    delete_data = 'DELETE FROM settings WHERE name = ?;'
    cur.execute(delete_data, (alias,))
    conn.commit()
    db.close(conn, cur)
