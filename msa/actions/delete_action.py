from msa.repositories.setting_repository import SettingRepository
from msa.services.file_service import FileService


def execute(args):
    action = DeleteAction(logger=args.log, config=args.config)
    action.execute(args.setting)


class DeleteAction(object):

    def __init__(self, logger, config):
        self.setting_repository = SettingRepository(logger=logger, config=config)
        self.file_service = FileService(logger=logger, config=config)

    def execute(self, alias):
        setting = self.setting_repository.find_one_by(alias)

        if setting is None:
            self._print_output('Setting not found!!!')
            return

        self.setting_repository.delete(setting)
        self.file_service.remove_setting(setting)
        self._print_output('The {} setting was deleted'.format(setting.alias))

    # noinspection PyMethodMayBeStatic
    def _print_output(self, message):
        print(message)
