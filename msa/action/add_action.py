from msa import repository, file_manager
from msa.util import log


def execute(args):
    log.set_config(args)

    if repository.find_one(args.alias):
        print('Setting already added')
        return

    setting = file_manager.add_setting(args.alias, args.file)
    repository.create(setting)

    log.restore_config()
