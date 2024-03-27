# WARNING! WARNING! WARNING!
# Feel free to look, but do not touch!

import pytest
import math
from src.lab2_question1 import *

def test_that_n_is_42():
    assert n == 42, "n has value 42"

def test_that_tau_is_2pi():
    assert abs(tau - 6.28319) < 0.001, "tau has value 2*pi"

def test_that_school_is_sault_college():
    assert school == "Sault College", "school has value 'Sault College'"