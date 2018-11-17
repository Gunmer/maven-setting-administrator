from msa import file_manager
from msa.repository.setting_repository import SettingRepository
from msa.util import log


def execute(args):
    log.set_config(args)

    repository = SettingRepository()

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

    log.restore_config()
