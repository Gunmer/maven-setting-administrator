import argparse

from msa.action import add_action, delete_action, use_action, list_action
from msa.file_manager import FileManager
from msa.repository.setting_repository import SettingRepository
from msa.setting import Setting
from msa.util.config import Config
from msa.util.log import Log


def main():
    parser = argparse.ArgumentParser(prog='msa', usage='msa [-h] action')
    subparsers = parser.add_subparsers(title='actions', metavar='')

    parser.add_argument('-v', '--version', help='Show version', action='store_true')
    parser.add_argument('-d', '--debug', action='store_true')

    use_parser = subparsers.add_parser('use', help='Select the setting to use')
    use_parser.set_defaults(func=use_action.execute)
    use_parser.add_argument('setting', help='Select setting for use')
    use_parser.add_argument('-d', '--debug', action='store_true')

    list_parser = subparsers.add_parser('ls', help='Show a list setting')
    list_parser.set_defaults(func=list_action.execute)
    list_parser.add_argument('-d', '--debug', action='store_true')

    add_parser = subparsers.add_parser('add', help='Add a new setting')
    add_parser.set_defaults(func=add_action.execute)
    add_parser.add_argument('alias', help='Alias of setting')
    add_parser.add_argument('file', help='File name of setting')
    add_parser.add_argument('-d', '--debug', action='store_true')

    delete_parser = subparsers.add_parser('del', help='Delete a setting')
    delete_parser.set_defaults(func=delete_action.execute)
    delete_parser.add_argument('setting', help='Select setting for delete')
    delete_parser.add_argument('-d', '--debug', action='store_true')

    args = parser.parse_args()
    args.config = Config()
    args.log = Log(args.debug)

    _initialize(args)

    if args.version:
        print('msa version: {}'.format(Config.version))
    elif hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


def _initialize(args):
    repository = SettingRepository(logger=args.log, config=args.config)
    file_manager = FileManager(logger=args.log, config=args.config)

    if not file_manager.directory_exist():
        print('... Creating directory ...')
        file_manager.create_directory()
        print('... Creating database ...')
        repository.create_settings_table()

    if repository.find_one('default') is None:
        print('... Adding default settings ...')
        repository.create(Setting('default', ''))
