from msa import repository, file_manager
from msa.setting import Setting
from msa.util import log


def execute(args):
    log.set_config(args)
    file = file_manager.add_setting(args.alias, args.file)
    setting = Setting(args.alias, file)
    repository.create(setting)
    log.restore_config()
