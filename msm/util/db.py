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
