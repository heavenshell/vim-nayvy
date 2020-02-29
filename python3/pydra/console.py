import argparse
import os
import sys

from .importing.fixer import Fixer
from .importing.import_config import ImportConfig
from .importing.pyflakes import PyflakesEngine


def run() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('file_path', type=str)
    args = parser.parse_args()
    # load config
    config = ImportConfig.of_jsonfile(
        os.environ['HOME'] +
        '/.config/pydra/config.json'
    )
    if config is None:
        print('cannot load pydra config file', file=sys.stderr)
        sys.exit(1)
    fixer = Fixer(config, PyflakesEngine())
    fixer.print_fixed_content(args.file_path)
    return