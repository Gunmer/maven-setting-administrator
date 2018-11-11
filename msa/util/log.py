import datetime

from msa import config


def debug(message):
    if config.log_debug_enable:
        print('DEBUG::MSM::{D}::{M}'.format(D=datetime.datetime.now(), M=message))


def info(message):
    print('INFO::MSM::{D}::{M}'.format(D=datetime.datetime.now(), M=message))


def error(message):
    print('ERROR::MSM::{D}::{M}'.format(D=datetime.datetime.now(), M=message))


def set_config(args):
    config.log_debug_enable = args.debug


def restore_config():
    config.log_debug_enable = False
