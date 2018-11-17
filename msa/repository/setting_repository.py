import sqlite3

from msa import config
from msa.setting import Setting


class SettingRepository(object):

    def __init__(self):
        self.connection = sqlite3.connect(config.database_path)

    def create_settings_table(self):
        cursor = self.connection.cursor()
        create_table = 'CREATE TABLE settings (name TEXT, file TEXT, isSelected INTEGER);'
        cursor.execute(create_table)
        self.connection.commit()

    def create(self, setting):
        cursor = self.connection.cursor()
        insert_data = 'INSERT INTO settings (name, file, isSelected) VALUES (?, ?, ?);'
        cursor.execute(insert_data, (setting.alias, setting.file, int(setting.selected)))
        self.connection.commit()

    def list_all(self):
        cursor = self.connection.cursor()
        select_all = 'SELECT * FROM settings;'
        cursor.execute(select_all)
        results = cursor.fetchall()

        return map(self._map_data_to_setting, results)

    def _map_data_to_setting(self, data):
        return Setting(data[0], data[1], data[2])

    def find_selected(self):
        cursor = self.connection.cursor()
        select_find_selected = 'SELECT * FROM settings WHERE isSelected = 1;'
        cursor.execute(select_find_selected)
        data = cursor.fetchone()

        if data is None:
            return None

        return self._map_data_to_setting(data)

    def find_one(self, alias):
        cursor = self.connection.cursor()
        select_find_selected = 'SELECT * FROM settings WHERE name = ?;'
        cursor.execute(select_find_selected, (alias,))
        data = cursor.fetchone()

        if data is None:
            return None

        return self._map_data_to_setting(data)

    def update(self, setting):
        cursor = self.connection.cursor()
        update_data = 'UPDATE settings SET isSelected = ? WHERE name = ?;'
        cursor.execute(update_data, (setting.selected, setting.alias))
        self.connection.commit()

    def delete(self, setting):
        cursor = self.connection.cursor()
        delete_data = 'DELETE FROM settings WHERE name = ?;'
        cursor.execute(delete_data, (setting.alias,))
        self.connection.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
