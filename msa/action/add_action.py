from msa import file_manager
from msa.setting_repository import SettingRepository
from msa.util import log


def execute(args):
    log.set_config(args)

    repository = SettingRepository()

    if repository.find_one(args.alias):
        print('Setting already added')
        return

    setting = file_manager.add_setting(args.alias, args.file)
    repository.create(setting)

    log.restore_config()
