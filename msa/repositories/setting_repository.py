import sqlite3

from msa.model.setting import Setting


class SettingRepository(object):

    def __init__(self, logger, config):
        self.config = config
        self.connection = sqlite3.connect(config.database_path)
        self.log = logger

    def create_settings_table(self):
        cursor = self.connection.cursor()
        create_table = 'CREATE TABLE settings (name TEXT, file TEXT, isSelected INTEGER);'
        self.log.debug('Execute {}'.format(create_table))
        cursor.execute(create_table)
        self.connection.commit()

    def clear_setting_table(self):
        cursor = self.connection.cursor()
        delete_table = 'DELETE FROM settings;'
        self.log.debug('Execute {}'.format(delete_table))
        cursor.execute(delete_table)
        self.connection.commit()

    def create(self, setting):
        cursor = self.connection.cursor()
        insert_data = 'INSERT INTO settings (name, file, isSelected) VALUES (?, ?, ?);'
        self.log.debug('Map {D} to {S}'.format(D=insert_data, S=(setting.alias, setting.file, setting.selected)))
        cursor.execute(insert_data, (setting.alias, setting.file, setting.selected))
        self.connection.commit()

    def list_all(self):
        cursor = self.connection.cursor()
        select_all = 'SELECT * FROM settings;'
        self.log.debug('Execute {}'.format(select_all))
        cursor.execute(select_all)
        results = cursor.fetchall()

        return map(self._map_data_to_setting, results)

    def _map_data_to_setting(self, data):
        setting = Setting(data[0], data[1], data[2])
        self.log.debug('Map {D} to {S}'.format(D=data, S=setting))
        return setting

    def find_selected(self):
        cursor = self.connection.cursor()
        select_find_selected = 'SELECT * FROM settings WHERE isSelected = 1;'
        self.log.debug('Execute {}'.format(select_find_selected))
        cursor.execute(select_find_selected)
        data = cursor.fetchone()

        if data is None:
            self.log.debug('Not found results')
            return None

        return self._map_data_to_setting(data)

    def find_one_by(self, alias):
        cursor = self.connection.cursor()
        select_find_one = 'SELECT * FROM settings WHERE name = ?;'
        self.log.debug('Execute {Q} with {P}'.format(Q=select_find_one, P=alias))
        cursor.execute(select_find_one, (alias,))
        data = cursor.fetchone()

        if data is None:
            self.log.debug('Not found results')
            return None

        return self._map_data_to_setting(data)

    def update(self, setting):
        cursor = self.connection.cursor()
        update_data = 'UPDATE settings SET isSelected = ? WHERE name = ?;'
        self.log.debug('Execute {Q} with {P}'.format(Q=update_data, P=(setting.selected, setting.alias)))
        cursor.execute(update_data, (setting.selected, setting.alias))
        self.connection.commit()

    def delete(self, setting):
        cursor = self.connection.cursor()
        delete_data = 'DELETE FROM settings WHERE name = ?;'
        self.log.debug('Execute {Q} with {P}'.format(Q=delete_data, P=setting.alias))
        cursor.execute(delete_data, (setting.alias,))
        self.connection.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
