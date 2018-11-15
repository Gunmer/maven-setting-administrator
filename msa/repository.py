from msa import config
from msa.setting import Setting
from msa.util import db, log


def init():
    log.debug('Create table')
    connection, cursor = db.connect(config.database_path)
    create_table = 'CREATE TABLE settings (name TEXT, file TEXT, isSelected INTEGER);'
    cursor.execute(create_table)
    connection.commit()
    db.close(connection, cursor)


def create(setting):
    log.debug('Add new data: {}'.format(setting))
    conn, cur = db.connect(config.database_path)
    insert_data = 'INSERT INTO settings (name, file, isSelected) VALUES (?, ?, ?);'
    cur.execute(insert_data, (setting.alias, setting.file, int(setting.selected)))
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

    return map(lambda result: Setting(result[0], result[1], bool(result[2])), results)


def find_selected():
    log.debug('Find selected')
    conn, cur = db.connect(config.database_path)
    select_find_selected = 'SELECT * FROM settings WHERE isSelected = 1;'
    cur.execute(select_find_selected)
    data = cur.fetchone()
    log.debug('Data: {}'.format(data))
    db.close(conn, cur)

    if data is None:
        return None

    return Setting(data[0], data[1], bool(data[2]))


def find_one(alias):
    log.debug('Find one with alias {}'.format(alias))
    conn, cur = db.connect(config.database_path)
    select_find_selected = 'SELECT * FROM settings WHERE name = ?;'
    cur.execute(select_find_selected, (alias,))
    data = cur.fetchone()
    log.debug('Data: {}'.format(data))
    db.close(conn, cur)

    if data is None:
        return None

    return Setting(data[0], data[1], bool(data[2]))


def update(setting):
    log.debug('Update data: {}'.format(setting))
    conn, cur = db.connect(config.database_path)
    update_data = 'UPDATE settings SET isSelected = ? WHERE name = ?;'
    cur.execute(update_data, (int(setting.selected), setting.alias))
    conn.commit()
    db.close(conn, cur)


def delete(setting):
    log.debug('Delete data: {}'.format(setting))
    conn, cur = db.connect(config.database_path)
    delete_data = 'DELETE FROM settings WHERE name = ?;'
    cur.execute(delete_data, (setting.alias,))
    conn.commit()
    db.close(conn, cur)
