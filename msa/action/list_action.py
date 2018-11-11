from msa import repository
from msa.util import log


def execute(args):
    log.set_config(args)
    for alias, file, is_selected in repository.list_all():
        output = '   {}'.format(alias)
        if is_selected == 1:
            output = ' > {}'.format(alias)

        print(output)
    log.restore_config()
