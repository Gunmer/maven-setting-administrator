import datetime


class Log(object):

    def __init__(self, args):
        self.is_enable = args.debug

    def debug(self, message):
        if self.is_enable:
            print('DEBUG::MSM::{D}::{M}'.format(D=datetime.datetime.now(), M=message))

    def info(self, message):
        if self.is_enable:
            print('INFO::MSM::{D}::{M}'.format(D=datetime.datetime.now(), M=message))

    def error(self, message):
        if self.is_enable:
            print('ERROR::MSM::{D}::{M}'.format(D=datetime.datetime.now(), M=message))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_enable = False
