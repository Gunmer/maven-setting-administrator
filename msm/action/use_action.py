from msm import repository
from msm.util import log


def execute(args):
    log.set_config(args)
    alias, file = repository.find_selected()
    if alias is not None:
        repository.update(alias, 0)

    repository.update(args.setting, 1)
    log.restore_config()
