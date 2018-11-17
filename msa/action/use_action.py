from msa.file_manager import FileManager
from msa.repository.setting_repository import SettingRepository
from msa.util.log import Log


def execute(args):
    log = Log(args)

    repository = SettingRepository()
    file_manager = FileManager(log)

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
