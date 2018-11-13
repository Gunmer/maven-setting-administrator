import os
from shutil import copyfile

from msa import config
from msa.util import log


def init():
    if os.path.exists(config.msa_path):
        log.debug('Detected msa directory in {}'.format(config.m2_path))
        return False

    os.mkdir(config.msa_path)
    log.debug('Creating msa directory in {}'.format(config.m2_path))
    return True


def add_setting(alias, file_path):
    file_name = alias + os.path.split(file_path)[1]
    dst_path = config.msa_path + file_name

    log.debug('Add {F} to {D}'.format(F=file_path, D=dst_path))
    copyfile(file_path, dst_path)

    return file_name


def activate_setting(file):
    if not str(file):
        return

    src_path = config.msa_path + file
    dst_path = config.m2_path + 'settings.xml'

    log.debug('Activate {}'.format(file))
    copyfile(src_path, dst_path)


def deactivate_setting(file):
    src_path = config.m2_path + 'settings.xml'
    if not os.path.exists(src_path):
        return

    log.debug('Deactivate {}'.format(file))
    os.remove(src_path)


def remove_setting(file):
    setting_path = config.msa_path + file

    log.debug('Remove {}'.format(setting_path))
    os.remove(setting_path)
