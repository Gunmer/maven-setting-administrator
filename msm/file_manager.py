import os

from msm.util import log


def add_setting(file_path):
    home = '/tmp/'
    file_name = os.path.split(file_path)[1]
    dst_path = home + file_name

    log.debug('Add {F} to {D}'.format(F=file_path, D=dst_path))
    os.rename(file_path, dst_path)

    return file_name


def activate_setting(file):
    src_path = '/tmp/' + file
    dst_path = '/tmp/settings.xml'

    log.debug('Activate {}'.format(file))
    os.rename(src_path, dst_path)


def deactivate_setting(file):
    src_path = '/tmp/settings.xml'
    dst_path = '/tmp/' + file

    log.debug('Deactivate {}'.format(file))
    os.rename(src_path, dst_path)


def remove_setting(file):
    setting_path = '/tmp/' + file

    log.debug('Remove {}'.format(setting_path))
    os.remove(setting_path)
