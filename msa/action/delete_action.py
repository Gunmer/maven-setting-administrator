from msa.file_manager import FileManager
from msa.repository.setting_repository import SettingRepository
from msa.util.log import Log


def execute(args):
    log = Log(args)

    repository = SettingRepository()
    file_manager = FileManager(log)

    setting = repository.find_one(args.setting)

    if setting is None:
        print('Setting not found!!!')
        return

    repository.delete(setting)
    file_manager.remove_setting(setting)
