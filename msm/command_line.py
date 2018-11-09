import argparse

from msm.action import add_action, delete_action, use_action, list_action


def main():
    parser = argparse.ArgumentParser(prog='msm', usage='msm [-h] action')
    subparsers = parser.add_subparsers(title='actions', metavar='')

    use_parser = subparsers.add_parser('use', help='Select the setting to use')
    use_parser.set_defaults(func=use_action.execute)

    list_parser = subparsers.add_parser('ls', help='Show a list setting')
    list_parser.set_defaults(func=list_action.execute)

    add_parser = subparsers.add_parser('add', help='Add a new setting')
    add_parser.set_defaults(func=add_action.execute)

    delete_parser = subparsers.add_parser('del', help='Delete a setting')
    delete_parser.set_defaults(func=delete_action.execute)

    args = parser.parse_args()
    args.func(args)
