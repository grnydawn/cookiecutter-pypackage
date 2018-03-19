# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import sys
import click

from .{{cookiecutter.project_slug}} import hello

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def main(count, name, args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    for x in range(count):
        print(hello(name))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
