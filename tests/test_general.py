import datetime as dt

import pandas as pd

from epic._cicd_dev import function


def test_function():
    assert function() == 100
