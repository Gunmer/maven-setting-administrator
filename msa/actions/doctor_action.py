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
        pass

    def diagnostic(self):
        pass
