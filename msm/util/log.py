import datetime

from msm import config


def debug(message):
    if config.log_debug_enable:
        print('DEBUG::MSM::{D}::{M}'.format(D=datetime.datetime.now(), M=message))


def info(message):
    print('INFO::MSM::{D}::{M}'.format(D=datetime.datetime.now(), M=message))


def error(message):
    print('ERROR::MSM::{D}::{M}'.format(D=datetime.datetime.now(), M=message))
