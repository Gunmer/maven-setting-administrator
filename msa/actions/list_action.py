from msa.repositories.setting_repository import SettingRepository


def execute(args):
    action = ListAction(logger=args.log, config=args.config)
    action.execute()


class ListAction(object):

    def __init__(self, logger, config):
        self.logger = logger
        self.settingRepository = SettingRepository(logger=logger, config=config)

    def execute(self):
        for setting in self.settingRepository.list_all():
            self._print_setting(setting)

    # noinspection PyMethodMayBeStatic
    def _print_setting(self, setting):
        if setting.is_selected():
            print(' > {}'.format(setting.alias))
        else:
            print('   {}'.format(setting.alias))
