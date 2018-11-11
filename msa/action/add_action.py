from msa import repository, file_manager
from msa.util import log


def execute(args):
    log.set_config(args)
    file = file_manager.add_setting(args.alias, args.file)
    repository.create(args.alias, file)
    log.restore_config()
