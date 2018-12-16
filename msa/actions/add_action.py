from msa.repositories.setting_repository import SettingRepository
from msa.services.file_service import FileService


def execute(args):
    action = AddAction(logger=args.log, config=args.config)
    action.execute(args.alias, args.file)


class AddAction(object):

    def __init__(self, logger, config):
        self.setting_repository = SettingRepository(logger=logger, config=config)
        self.file_service = FileService(logger=logger, config=config)

    def execute(self, alias, file_path):
        if self.setting_repository.find_one_by(alias):
            self._print_output('Setting already added')
            return

        setting = self.file_service.create_setting(alias, file_path)
        self.setting_repository.create(setting)

        self._print_output('The {} setting was created'.format(setting.alias))

    # noinspection PyMethodMayBeStatic
    def _print_output(self, message):
        print(message)
