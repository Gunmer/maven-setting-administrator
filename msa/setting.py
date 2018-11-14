class Setting(object):

    def __init__(self, alias, file, selected = False):
        self.alias = alias
        self.file = file
        self.selected = setting

    def get_tuple(self):
        return self.alias, self.file, int(self.selected)

    def __str__(self):
        print('Setting: {A}, {F}, {S}'.format(A=self.alias, F=self.file, S=self.selected))
