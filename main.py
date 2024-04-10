from common.Average import AdvancedAverage


data = [
    4.40,
    5.20,
    3.10,
    1.90,
    6.40,
    3.88,
    3.18,
    2.66,
    5.00,
    1500.0,  # Out-liner
    3000.0]  # Out-liner

math_operations = AdvancedAverage(precision=4)

print("Simple Average:", math_operations.simple_average(data))
print("Quantile Average:", math_operations.quantile_average(data))
print("Geometric Mean:", math_operations.geometric_mean(data))