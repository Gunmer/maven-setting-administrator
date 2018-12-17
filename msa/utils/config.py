from os.path import expanduser


class Config(object):
    version = '1.1.2'

    def __init__(self):
        self.user_home_path = expanduser("~") + '/'
        self.m2_path = self.user_home_path + '.m2/'
        self.m2_settings_path = self.m2_path + 'settings.xml'
        self.msa_path = self.m2_path + 'msa/'
        self.database_name = 'msa.db'
        self.database_path = self.msa_path + self.database_name
