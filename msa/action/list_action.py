from msa.setting_repository import SettingRepository
from msa.util import log


def execute(args):
    log.set_config(args)

    repository = SettingRepository()

    for setting in repository.list_all():
        output = '   {}'.format(setting.alias)
        if setting.selected:
            output = ' > {}'.format(setting.alias)

        print(output)

    log.restore_config()
