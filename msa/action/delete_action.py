from msa import repository, file_manager
from msa.util import log


def execute(args):
    log.set_config(args)

    setting_to_remove = repository.find_one(args.setting)

    if setting_to_remove is None:
        print('Setting not found!!!')
        return

    repository.delete(setting_to_remove[0])
    file_manager.remove_setting(setting_to_remove[1])

    log.restore_config()
