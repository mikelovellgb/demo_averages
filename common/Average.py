from typing import List
import numpy as np


class AdvancedAverage:
    """
    A class to perform various mathematical operations on a list of floats,
    including calculating averages and quantile averages with specified precision.
    """

    def __init__(self, precision: int = 2) -> None:
        """
        Initializes the AdvancedMath object with the desired precision for calculation results.

        :param precision: The number of decimal places to round the results to.
        """
        self.precision = precision

    def simple_average(self, data: List[float]) -> float:
        """
        Calculates the arithmetic mean of a list of floats.

        :param data: A list of floating-point numbers.
        :return: The arithmetic mean, rounded to the specified number of decimal places.
        """
        if not data:  # Return 0 if the list is empty
            return 0.0
        average = sum(data) / len(data)

        return round(average, self.precision)

    def quantile_average(self, data: List[float]) -> float:
        """
        Calculates the average of the 25th and 75th percentiles (Q1 and Q3) of a list of floats.

        This can be useful for understanding the central tendency of the data while excluding outliers.

        :param data: A list of floating-point numbers.
        :return: The average of the 25th and 75th percentiles, rounded to the specified number of decimal places.
        """
        if not data:  # Return 0 if the list is empty
            return 0.0
        q25, q75 = np.percentile(data, [25, 75])  # Calculate the 25th and 75th percentiles
        quantile_avg = (q25 + q75) / 2  # Calculate the average of the two quantiles

        return round(quantile_avg, self.precision)

    def geometric_mean(self, data: List[float]) -> float:
        """
        Calculates the geometric mean of a list of floats.

        The geometric mean is more appropriate than the arithmetic mean for data that are products or exponential in nature.

        :param data: A list of floating-point numbers.
        :return: The geometric mean, rounded to the specified number of decimal places.
        """
        if not data:  # Return 0 if the list is empty
            return 0.0
        product = np.prod(data)  # Calculate the product of all numbers in the list
        geom_mean = product**(1/len(data))  # Calculate the nth root of the product

        return round(geom_mean, self.precision)
