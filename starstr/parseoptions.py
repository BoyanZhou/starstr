#!/usr/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser, OptionGroup, SUPPRESS_HELP
import os
import sys
from starstr.version import __version__


def file_exist(filename):
    if os.path.exists(filename) and not os.path.isdir(filename):
        return True
    elif filename == "-":
        return True
    else:
        sys.stderr.write("Error: '%s' is not a valid file\n" % filename)
        return None


def where_is(program):
    # check if Python/R executable is present on the system
    for path in os.environ.get('PATH', '').split(':'):
        if os.path.exists(os.path.join(path, program)) and not os.path.isdir(os.path.join(path, program)):
            return os.path.join(path, program)
    return None


def options_parsed():
    parser = OptionParser("%prog [options] -i str_file -o output_suffix\n\nUse option -h or --help for help",
                          version=__version__, epilog="report bugs to boyanzhou1992@gmail.com")

    args = OptionGroup(parser, "Input files")
    args.add_option("-i", "--input", help="STR file",
                    action="store", type="string", dest="filename")
    args.add_option("-o", "--output", help="Suffix of the input file",
                    action="store", type="string", dest="output_suffix")
    args.add_option("-t", "--thread", help="Thread of distance calculation",
                    action="store", type="int", dest="thread", default=10)
    args.add_option("-r", "--rate", help="Mutation rate of each locus",
                    action="store", type="str", dest="rate")
    args.add_option("-s", "--star", help="Threshold number of individuals of star_cluster",
                    action="store", type="int", dest="star", default=100)
    args.add_option("-e", "--step", help="Threshold number of step distance",
                    action="store", type="int", dest="step", default=1)
    args.add_option("-y", "--years", help="Whether use normalized years as additional threshold",
                    action="store_true",  dest="years", default=False)

    parser.add_option_group(args)
    group = OptionGroup(parser, "General options")
    group.add_option("--no-plot", dest="no_r", help=SUPPRESS_HELP, default=False, action="store_true")
    group.add_option("-f", "--folder", help="folder name to store results [results_FILENAME]",
                     action="store", type="string", dest="folder")
    parser.add_option_group(group)

    # Parse the arguments
    (options, args) = parser.parse_args()

    # check folder
    if not options.folder:
        options.folder = os.getcwd()

    # check if the Rscript executable is present on the system
    if not where_is('Rscript'):
        print("Warning, Rscript is not in your PATH, plotting is disabled")
        options.no_r = True

    # get mutation rate
    if options.rate:
        rate_pergeneration = options.rate
        rate_pergeneration = rate_pergeneration.split(",")
        options.rate = [float(i) for i in rate_pergeneration]

    return options
