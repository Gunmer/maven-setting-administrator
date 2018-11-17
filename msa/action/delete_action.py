from msa import file_manager
from msa.setting_repository import SettingRepository
from msa.util import log


def execute(args):
    log.set_config(args)

    repository = SettingRepository()

    setting = repository.find_one(args.setting)

    if setting is None:
        print('Setting not found!!!')
        return

    repository.delete(setting)
    file_manager.remove_setting(setting)

    log.restore_config()
