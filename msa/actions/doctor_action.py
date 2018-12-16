from msa.model.setting import Setting
from msa.repositories.setting_repository import SettingRepository
from msa.services.file_service import FileService


def execute(args):
    doctor_action = DoctorAction(logger=args.log, config=args.config)

    if args.fix:
        doctor_action.fix()
    else:
        doctor_action.diagnostic()


class DoctorAction:

    def __init__(self, logger, config):
        self.setting_repository = SettingRepository(logger=logger, config=config)
        self.file_service = FileService(logger=logger, config=config)

    def fix(self):
        self.setting_repository.clear_setting_table()
        self.__print_output('- Clear data base')
        setting_files = self.file_service.list_all()

        for setting_file in setting_files:
            alias = setting_file[:-4]
            setting = Setting(alias=alias, file=setting_file)
            self.__print_output('- Insert in data base {}'.format(setting))
            self.setting_repository.create(setting)

        self.setting_repository.create(Setting(alias='default', file='', selected=1))
        self.__print_output('- Insert default setting')
        self.file_service.deactivate_setting()

    def diagnostic(self):
        pass

    # noinspection PyMethodMayBeStatic
    def __print_output(self, message):
        print(message)
