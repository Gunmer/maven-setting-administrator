from msa.repositories.setting_repository import SettingRepository
from msa.services.file_service import FileService


def execute(args):
    action = UseAction(logger=args.log, config=args.config)
    action.execute(args.setting)


class UseAction(object):

    def __init__(self, logger, config):
        self.setting_repository = SettingRepository(logger=logger, config=config)
        self.file_service = FileService(logger=logger, config=config)

    def execute(self, alias):
        old_setting = self.setting_repository.find_selected()
        new_setting = self.setting_repository.find_one_by(alias)

        if new_setting is None:
            self._print_output('Setting not found!!!')
            return

        if old_setting is not None:
            old_setting.deselect()
            self.setting_repository.update(old_setting)
            self.file_service.deactivate_setting()

        new_setting.select()
        self.setting_repository.update(new_setting)
        self.file_service.activate_setting(new_setting)

        self._print_output('The {} setting is selected'.format(new_setting.alias))

    # noinspection PyMethodMayBeStatic
    def _print_output(self, message):
        print(message)
