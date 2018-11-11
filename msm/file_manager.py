import os

from msm import config
from msm.util import log


def init():
    if os.path.exists(config.msm_path):
        log.debug('Detected msm directory in {}'.format(config.m2_path))
        return False

    print('Initialize msm')
    os.mkdir(config.msm_path)
    log.debug('Creating msm directory in {}'.format(config.m2_path))
    return True


def add_setting(alias, file_path):
    file_name = alias + os.path.split(file_path)[1]
    dst_path = config.msm_path + file_name

    log.debug('Add {F} to {D}'.format(F=file_path, D=dst_path))
    os.rename(file_path, dst_path)

    return file_name


def activate_setting(file):
    src_path = config.msm_path + file
    dst_path = config.m2_path + 'settings.xml'

    log.debug('Activate {}'.format(file))
    os.rename(src_path, dst_path)


def deactivate_setting(file):
    src_path = config.m2_path + 'settings.xml'
    dst_path = config.msm_path + file

    log.debug('Deactivate {}'.format(file))
    os.rename(src_path, dst_path)


def remove_setting(file):
    setting_path = config.msm_path + file

    log.debug('Remove {}'.format(setting_path))
    os.remove(setting_path)
