#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
 pearce [options]

Options:
  -h --help                         Show this screen.
  --version                         Show version.
  -c, --colored                     Colored output if provided.
                                    [default: False]
  -i <n>, --iterations <n>          Iterations for the for-loop.
                                    [default: 10]
  -v <level>, --verbosity <level>   Logging verbosity. Choices are debug, info, warning, error, and critical.
                                    [default: debug]
"""

from docopt import docopt
from termcolor import colored
import logging
import os
import random
import sys
import time


# Constants ..................................................................

ITERATIONS_DEFAULT = 10


# Classes ..................................................................

class CustomLogFormatter(logging.Formatter):
    '''
    Custom log formatter, if desired, when using colored output.
    '''
    log_datefmt = '%d/%b/%Y:%H:%M:%S %z'
    log_format_default = '[%(asctime)s] [%(levelname)s] %(message)s'

    # Colored overides.
    log_colorized = False
    log_format_debug_colored = '[%(asctime)s] [' + colored('%(levelname)s', 'blue') + '] %(message)s'
    log_format_info_colored = '[%(asctime)s] [' + colored('%(levelname)s', 'green') + '] %(message)s'
    log_format_warn_colored = '[%(asctime)s] [' + colored('%(levelname)s', 'yellow') + '] %(message)s'
    log_format_error_colored = '[%(asctime)s] [' + colored('%(levelname)s', 'red') + '] %(message)s'
    log_format_crit_colored = '[%(asctime)s] [' + colored('%(levelname)s', 'magenta') + '] %(message)s'

    def __init__(self, colorized=False):
        super().__init__(
            fmt=CustomLogFormatter.log_format_default,
            datefmt=CustomLogFormatter.log_datefmt,
            style='%'
        )
        self.log_colorized = colorized

    def format(self, record):
        # Save the original format configured by the user when the logger
        # formatter was instantiated.
        format_orig = self._style._fmt

        # Override logging format based on level.
        if self.log_colorized:
            if record.levelno == logging.DEBUG:
                self._style._fmt = CustomLogFormatter.log_format_debug_colored
            elif record.levelno == logging.INFO:
                self._style._fmt = CustomLogFormatter.log_format_info_colored
            elif record.levelno == logging.WARN:
                self._style._fmt = CustomLogFormatter.log_format_warn_colored
            elif record.levelno == logging.ERROR:
                self._style._fmt = CustomLogFormatter.log_format_error_colored
            elif record.levelno == logging.CRITICAL:
                self._style._fmt = CustomLogFormatter.log_format_crit_colored
            else:
                self._style._fmt = CustomLogFormatter.log_format_default
        else:
            self._style._fmt = CustomLogFormatter.log_format_default

        # Call the original formatter class.
        result = logging.Formatter.format(self, record)

        # Restore the original format configured by the user.
        self._style._fmt = format_orig

        return result


# Functions ..................................................................


def getNameAndBuild():
    '''
    Constructs the name and build number of this CLI script. Returns the name
    and build number as a tuple.
    '''
    filename = os.path.basename(__file__)
    name = os.path.splitext(filename)[0].upper()

    try:
        file_path = os.path.dirname(os.path.realpath(__file__))
        f = open('{}/build_number'.format(file_path), 'r')
        build = f.read().strip()
    except Exception:
        build = 0

    return name, build


def configureLogging(log_level='INFO', color_output=False):
    '''
    Configures logging for this CLI. Returns nothing.
    '''
    log_level = log_level.upper()
    log_level_value = getattr(logging, log_level.upper(), logging.DEBUG)

    log_formatter = CustomLogFormatter(color_output)
    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setFormatter(log_formatter)
    logging.root.addHandler(log_handler)
    logging.root.setLevel(log_level_value)
    return


# Main .......................................................................


def main():
    '''
    Convenient main method.
    '''

    # Sets the name and build number of the script.
    cli_name, cli_build = getNameAndBuild()
    arguments = docopt(__doc__, version='{} v{}'.format(cli_name, cli_build))

    # Configures logging.
    color_output = arguments['--colored']
    log_level = arguments['--verbosity']
    configureLogging(log_level, color_output)
    logging.debug('Starting main().')

    # Configures the number of iterations we'll run.
    iterations_param = arguments['--iterations']
    if not iterations_param.isnumeric():
        message = 'Supplied value for iterations was not a number. '
        message += 'Using default of {}.'.format(ITERATIONS_DEFAULT)
        logging.warning(message)
        iterations = ITERATIONS_DEFAULT
    else:
        iterations = int(iterations_param)

    # Seed the random generator, write its value to logs very second.
    random.seed()
    for i in range(iterations):
        value = random.randint(0, 100)
        if value > 90:
            logging.critical('Iteration {} with value {}'.format(i, value))
        elif value > 80:
            logging.error('Iteration {} with value {}'.format(i, value))
        elif value > 70:
            logging.warning('Iteration {} with value {}'.format(i, value))
        else:
            logging.info('Iteration {} with value {}'.format(i, value))
        time.sleep(1)

    # Aaaand we're done.
    logging.debug('Exiting main().')
    sys.exit(0)


if __name__ == '__main__':
    sys.exit(main())
