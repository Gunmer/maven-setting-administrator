import sqlite3

from msm.util import log


def connect(sqlite_file):
    log.debug('Opening the connection to {}'.format(sqlite_file))
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()

    return connection, cursor


def close(connection, cursor):
    log.debug('Close th connection to db')
    cursor.close()
    connection.close()


def execute_statement(cursor, sql):
    log.debug('Will execute statement: {}'.format(sql))
    cursor.execute(sql)
    cursor.commit()
    log.debug('Statement did executed')


def execute_query(cursor, sql):
    log.debug('Will execute query: {}'.format(sql))
    cursor.execute(sql)
    rows = cursor.fetchall()
    log.debug('Result of query: {}'.format(rows))

    return rows
