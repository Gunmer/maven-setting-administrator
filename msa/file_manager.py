import os
from shutil import copyfile

from msa import config
from msa.setting import Setting


class FileManager(object):

    def __init__(self, logger):
        self.log = logger

    def directory_exist(self):
        exist = os.path.exists(config.msa_path)
        self.log.debug('Detected msa directory: {}'.format(exist))
        return exist

    def create_directory(self):
        self.log.debug('Creating msa directory in {}'.format(config.m2_path))
        os.mkdir(config.msa_path)

    def create_setting(self, alias, file_path):

        file_name = alias + os.path.split(file_path)[1]
        dst_path = config.msa_path + file_name

        self.log.debug('Create {F} to {D}'.format(F=file_path, D=dst_path))
        copyfile(file_path, dst_path)

        return Setting(alias, file_name)

    def activate_setting(self, setting):
        if not str(setting.file):
            return

        src_path = config.msa_path + setting.file
        dst_path = config.m2_path + 'settings.xml'

        self.log.debug('Activate {}'.format(setting))
        copyfile(src_path, dst_path)

    def deactivate_setting(self, setting):
        src_path = config.m2_path + 'settings.xml'
        if not os.path.exists(src_path):
            return

        self.log.debug('Deactivate {}'.format(setting))
        os.remove(src_path)

    def remove_setting(self, setting):
        if not str(setting.file):
            return

        setting_path = config.msa_path + setting.file

        self.log.debug('Remove {}'.format(setting))
        os.remove(setting_path)
