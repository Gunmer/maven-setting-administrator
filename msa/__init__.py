from msa import file_manager
from msa.repository.setting_repository import SettingRepository
from msa.setting import Setting

repository = SettingRepository()

if file_manager.init():
    print('... Creating directory ...')
    repository.create_settings_table()
    print('... Creating database ...')

if repository.find_one('default') is None:
    print('... Adding default settings ...')
    repository.create(Setting('default', ''))
