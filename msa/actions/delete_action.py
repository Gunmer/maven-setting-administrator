from msa.file_manager import FileManager
from msa.repositories.setting_repository import SettingRepository


def execute(args):
    repository = SettingRepository(logger=args.log, config=args.config)
    file_manager = FileManager(logger=args.log, config=args.config)

    setting = repository.find_one(args.setting)

    if setting is None:
        print('Setting not found!!!')
        return

    repository.delete(setting)
    file_manager.remove_setting(setting)
