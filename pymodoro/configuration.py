# encoding: utf-8

import os

import pymodoro.logger
import pymodoro.utils


class Paths:
    MAIN_FOLDER = os.path.expanduser('~/.pymodoro.d/')
    LOG = os.path.join(MAIN_FOLDER, 'main.log')


@pymodoro.utils.memoize
def logfile():
    if not os.path.exists(Paths.MAIN_FOLDER):
        _create_folder(Paths.MAIN_FOLDER)

    return dict(path=Paths.LOG)


def _create_folder(path):
    os.mkdir(path, 0o700)
    pymodoro.logger.info(__name__, 'created folder "%s"', path)
