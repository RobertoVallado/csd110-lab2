# WARNING! WARNING! WARNING!
# Feel free to look, but do not touch!

import pytest
import sys
import util

def test_that_the_program_calculates_the_correct_volume(capsys):
    if 'src.lab2_question4' in sys.modules.keys():
        sys.modules.pop('src.lab2_question4')
    
    import src.lab2_question4    
    out, err = capsys.readouterr()
    expected = "The volume of a square pyramid with base 3000cm and height 1000cm is 3000000000.0cm^3"
    assert out.strip() == expected, util.format_message("Your code does not produce the correct output", expected, out)