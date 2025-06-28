import datetime as dt

import pandas as pd

from epic._cicd_dev import function


def test_function():
    assert function() == 101


def test_fail():
    assert False, "intentional failure"
