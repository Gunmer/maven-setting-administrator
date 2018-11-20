from msa.file_manager import FileManager
from msa.repositories.setting_repository import SettingRepository


def execute(args):
    repository = SettingRepository(logger=args.log, config=args.config)
    file_manager = FileManager(logger=args.log, config=args.config)

    old_setting = repository.find_selected()
    new_setting = repository.find_one(args.setting)

    if new_setting is None:
        print('Setting not found!!!')
        return

    if old_setting is not None:
        old_setting.deselect()
        repository.update(old_setting)
        file_manager.deactivate_setting(old_setting)

    new_setting.select()
    repository.update(new_setting)
    file_manager.activate_setting(new_setting)
