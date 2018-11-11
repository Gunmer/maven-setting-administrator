from msm import repository
from msm.util import log


def execute(args):
    log.set_config(args)
    repository.delete(args.setting)
    log.restore_config()
