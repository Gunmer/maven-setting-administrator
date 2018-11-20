from msa.file_manager import FileManager
from msa.repositories.setting_repository import SettingRepository


def execute(args):
    repository = SettingRepository(logger=args.log, config=args.config)
    file_manager = FileManager(logger=args.log, config=args.config)

    if repository.find_one(args.alias):
        print('Setting already added')
        return

    setting = file_manager.create_setting(args.alias, args.file)
    repository.create(setting)
