import pytest
from tp_marcelo.main import mean, mean_distance

def test_mean():
    values = [1, 5, 7, 10, 15, 20, 22]

    mean_expected = 11.428571428571

    assert mean(values) == mean_expected
