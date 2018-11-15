class Setting(object):

    def __init__(self, alias, file, selected=0):
        self.alias = alias
        self.file = file
        self.selected = selected

    def __str__(self):
        return 'Setting({A}, {F}, {S})'.format(A=self.alias, F=self.file, S=self.selected)

    def is_selected(self):
        return bool(self.selected)

    def select(self):
        self.selected = 1

    def deselect(self):
        self.selected = 0
