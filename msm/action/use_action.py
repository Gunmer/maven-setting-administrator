from msm import repository


def execute(args):
    alias, file = repository.find_selected()
    if alias is not None:
        repository.update(alias, 0)

    repository.update(args.setting, 1)
