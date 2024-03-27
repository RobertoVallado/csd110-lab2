# WARNING! WARNING! WARNING!
# Feel free to look, but do not touch!

import pytest
import sys

def test_that_the_file_run_without_error():
    if 'src.lab2_question2' in sys.modules.keys():
        sys.modules.pop('src.lab2_question2')
    import src.lab2_question2