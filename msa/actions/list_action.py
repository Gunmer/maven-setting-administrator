from msa.repositories.setting_repository import SettingRepository


def execute(args):
    repository = SettingRepository(logger=args.log, config=args.config)

    for setting in repository.list_all():
        output = '   {}'.format(setting.alias)
        if setting.selected:
            output = ' > {}'.format(setting.alias)

        print(output)

