import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from common.Average import AdvancedAverage


# Initialize an instance of AdvancedMath with 4 decimal precision for testing
test_instance = AdvancedAverage(precision=4)


def test_simple_average():
    # Test simple_average method with a list of floats
    assert test_instance.simple_average([1.0, 2.0, 3.0, 4.0, 5.0]) == 3.0000
    # Test with negative numbers
    assert test_instance.simple_average([-10, -20, -30]) == -20.0000
    # Test with an empty list
    assert test_instance.simple_average([]) == 0.0


def test_quantile_average():
    # Test quantile_average method with a list of floats
    assert test_instance.quantile_average([1.0, 2.0, 3.0, 4.0, 5.0]) == 3.0000
    # Test with a larger range and negative numbers
    data = list(range(-100, 101))  # -100 to 100
    assert test_instance.quantile_average(data) == 0.0000
    # Test with an empty list
    assert test_instance.quantile_average([]) == 0.0


def test_geometric_mean():
    # Test geometric_mean method with a list of positive floats
    assert test_instance.geometric_mean([1.0, 2.0, 3.0, 4.0, 5.0]) == 2.6052
    # Test with numbers that include a growth factor (e.g., interest rates)
    assert test_instance.geometric_mean([1.1, 0.9, 1.05]) == pytest.approx(1.013, 0.0001)
    # Test with an empty list
    assert test_instance.geometric_mean([]) == 0.0