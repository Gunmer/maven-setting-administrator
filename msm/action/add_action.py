from msm import repository, file_manager
from msm.util import log


def execute(args):
    log.set_config(args)
    file = file_manager.add_setting(args.file)
    repository.create(args.alias, file)
    log.restore_config()
