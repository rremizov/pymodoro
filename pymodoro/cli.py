# encoding: utf-8

import argparse

import pymodoro.logger
import pymodoro.utils


@pymodoro.utils.memoize
def parameters():
    parser = argparse.ArgumentParser(description='pymodoro')

    return parser.parse_args()

parameters()
