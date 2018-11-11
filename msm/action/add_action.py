from msm import repository
from msm.util import log


def execute(args):
    log.set_config(args)
    repository.create(args.alias, args.file)
    log.restore_config()
