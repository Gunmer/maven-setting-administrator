class Setting(object):

    def __init__(self, alias, file, selected=False):
        self.alias = alias
        self.file = file
        self.selected = selected

    def __str__(self):
        return 'Setting({A}, {F}, {S})'.format(A=self.alias, F=self.file, S=self.selected)
