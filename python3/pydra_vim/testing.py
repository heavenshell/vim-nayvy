import sys

import vim  # noqa
from pydra.testing.autogen import AutoGenerator


def pydra_auto_touch_test(filepath: str) -> None:
    test_path = AutoGenerator.touch_test_file(filepath)
    if test_path is None:
        print(
            'Please check if your python project is created correcty',
            file=sys.stderr,
        )
        return
    vim.command(f'vs {test_path}')
    return