from msa.file_manager import FileManager
from msa.repository.setting_repository import SettingRepository
from msa.util.log import Log


def execute(args):
    log = Log(args)
    file_manager = FileManager(log)
    repository = SettingRepository()

    if repository.find_one(args.alias):
        print('Setting already added')
        return

    setting = file_manager.create_setting(args.alias, args.file)
    repository.create(setting)
