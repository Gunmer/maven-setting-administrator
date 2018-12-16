import os
from shutil import copyfile

from msa.model.setting import Setting


class FileService(object):

    def __init__(self, logger, config):
        self.config = config
        self.log = logger

    def directory_exist(self):
        exist = os.path.exists(self.config.msa_path)
        self.log.debug('Detected msa directory: {}'.format(exist))
        return exist

    def create_directory(self):
        self.log.debug('Creating msa directory in {}'.format(self.config.m2_path))
        os.mkdir(self.config.msa_path)

    def create_setting(self, alias, file_path):
        self.log.debug('Create with alias: {A} from {P}'.format(A=alias, P=file_path))

        file_name = alias + '.xml'
        dst_path = self.config.msa_path + file_name

        self.log.debug('Copy {F} to {D}'.format(F=file_path, D=dst_path))
        copyfile(file_path, dst_path)

        return Setting(alias, file_name)

    def activate_setting(self, setting):
        self.log.debug('Activate {}'.format(setting))

        if not str(setting.file):
            return

        src_path = self.config.msa_path + setting.file
        dst_path = self.config.m2_settings_path

        self.log.debug('Copy {S} to {D}'.format(S=src_path, D=dst_path))
        copyfile(src_path, dst_path)

    def deactivate_setting(self):
        src_path = self.config.m2_settings_path
        self.log.debug('Deactivate {}'.format(src_path))
        if not os.path.exists(src_path):
            return

        self.log.debug('Delete {S}'.format(S=src_path))
        os.remove(src_path)

    def remove_setting(self, setting):
        setting_path = self.config.msa_path + setting.file

        self.log.debug('Remove {}'.format(setting))

        if not str(setting.file):
            return

        self.log.debug('Delete {S}'.format(S=setting_path))
        os.remove(setting_path)

    def list_all(self):
        all_settings = [setting for setting in os.listdir(self.config.msa_path) if setting != self.config.database_name]

        self.log.debug('Return all setting: {}'.format(all_settings))

        return all_settings
