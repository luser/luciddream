#!/usr/bin/env python

from __future__ import print_function
import argparse
import sys

from marionette import Marionette
from mozrunner import B2GEmulatorRunner

class CommandLineError(Exception):
    pass


def validate_options(options):
    if not options.b2gPath:
        raise CommandLineError('You must specify --b2gpath')


def parse_args(in_args):
    parser = argparse.ArgumentParser(description='Run Luciddream tests.')
    parser.add_argument('--emulator', dest='emulator', action='store',
                        default='arm',
                        help='Architecture of emulator to use: x86 or arm')
    parser.add_argument('--b2gpath', dest='b2gPath', action='store',
                        help='path to B2G repo or qemu dir')
    parser.add_argument('--adbpath', dest='adbPath', action='store',
                        default='adb',
                        help='path to adb binary')
    args = parser.parse_args(in_args)
    try:
        validate_options(args)
        return args
    except CommandLineError as e:
        print('Error: ', e.args[0], file=sys.stderr)
        parser.print_help()
        raise


def start_emulator(args):
    marionette = Marionette(
        adb_path=args.adbPath,
        emulator=args.emulator,
        homedir=args.b2gPath,
    )
    runner = marionette.runner
    runner.start()
    marionette.wait_for_port()
    marionette.start_session()
    marionette.set_context(self.marionette.CONTEXT_CHROME)
    return marionette


def main(in_args):
    try:
        args = parse_args(in_args)
    except CommandLineError as e:
        return 1

    emulator = start_emulator(args)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
