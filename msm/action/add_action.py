from msm import repository


def execute(args):
    repository.create(args.alias, args.file)
