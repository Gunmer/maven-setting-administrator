import argparse

from msa.action import add_action, delete_action, use_action, list_action


def main():
    parser = argparse.ArgumentParser(prog='msa', usage='msa [-h] action')
    subparsers = parser.add_subparsers(title='actions', metavar='')

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
    args.func(args)
