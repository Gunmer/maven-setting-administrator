from msa import file_manager
from msa.setting import Setting
from msa.setting_repository import SettingRepository

repository = SettingRepository()

if file_manager.init():
    print('... Creating directory ...')
    repository.create_settings_table()
    print('... Creating database ...')

if repository.find_one('default') is None:
    print('... Adding default settings ...')
    repository.create(Setting('default', ''))
