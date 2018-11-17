from msa.repository.setting_repository import SettingRepository


def execute(args):
    repository = SettingRepository()

    for setting in repository.list_all():
        output = '   {}'.format(setting.alias)
        if setting.selected:
            output = ' > {}'.format(setting.alias)

        print(output)

