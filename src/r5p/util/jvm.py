#!/usr/bin/env python3

"""Set up a JVM and import basic java classes."""

import jpype
import jpype.imports

from .memory_footprint import EIGHTY_PERCENT_OF_RAM
from . import config


__all__ = []


config.argparser.add(
    "-r",
    "--r5-classpath",
    help="R5’s class path, can point to r5-all.jar",
    default="/usr/share/java/r5/r5-all.jar"
)
arguments = config.arguments()


jpype.startJVM(
    "-Xmx{:d}G".format(EIGHTY_PERCENT_OF_RAM),
    classpath=[arguments.r5_classpath]
)
