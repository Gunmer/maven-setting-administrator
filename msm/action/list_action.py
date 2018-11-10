from msm import repository


def execute(args):
    for alias, is_selected in repository.list_all():
        output = '   {}'.format(alias)
        if is_selected == 1:
            output = ' > {}'.format(alias)

        print(output)
