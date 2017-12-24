import logging

import pymodoro.configuration
import pymodoro.utils


def critical(name, *args, **kwargs):
    return _logger(name).critical(*args, **kwargs)


def error(name, *args, **kwargs):
    return _logger(name).error(*args, **kwargs)


def info(name, *args, **kwargs):
    return _logger(name).info(*args, **kwargs)


def debug(name, *args, **kwargs):
    return _logger(name).debug(*args, **kwargs)


@pymodoro.utils.memoize
def _logger(name):
    result = logging.getLogger(name)
    result.setLevel(logging.DEBUG)

    handler = logging.FileHandler(pymodoro.configuration.logfile()['path'])
    handler.setFormatter(logging.Formatter(
        '%(asctime)s;%(name)s;%(levelname)s;%(message)s'))
    result.addHandler(handler)

    return result
