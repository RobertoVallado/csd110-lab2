# WARNING! WARNING! WARNING!
# Feel free to look, but do not touch!

import pytest
import sys
import util

def test_that_output_is_correct(capsys):
    if 'src.lab2_question3' in sys.modules.keys():
        sys.modules.pop('src.lab2_question3')
    import src.lab2_question3
    out, err = capsys.readouterr()
    expected = "Feeling...HotHotHot!\n"
    assert out == expected, util.format_message("Your code does not produce the correct output. (Have you carefully checked for problems with case sensitivity, spaces, and newlines?)", expected, out)