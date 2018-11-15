from msa import repository, file_manager
from msa.util import log


def execute(args):
    log.set_config(args)

    selected_setting = repository.find_selected()
    setting_to_use = repository.find_one(args.setting)

    if setting_to_use is None:
        print('Setting not found!!!')
        return

    if selected_setting is not None:
        selected_setting.selected = False
        repository.update(selected_setting)
        file_manager.deactivate_setting(selected_setting.file)

    setting_to_use.selected = True
    repository.update(setting_to_use)
    file_manager.activate_setting(setting_to_use.file)

    log.restore_config()
