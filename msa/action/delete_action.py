from msa import repository, file_manager
from msa.util import log


def execute(args):
    log.set_config(args)

    setting = repository.find_one(args.setting)

    if setting is None:
        print('Setting not found!!!')
        return

    repository.delete(setting)
    file_manager.remove_setting(setting.file)

    log.restore_config()
