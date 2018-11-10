from msm import repository


def execute(args):
    repository.delete(args.setting)
