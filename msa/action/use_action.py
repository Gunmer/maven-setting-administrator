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
        repository.update(selected_setting[0], 0)
        file_manager.deactivate_setting(selected_setting[1])

    repository.update(setting_to_use[0], 1)
    file_manager.activate_setting(setting_to_use[1])

    log.restore_config()
