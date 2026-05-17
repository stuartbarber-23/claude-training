def greeting():
    print("Hi there")


def calculate_pi():
    """
    Calculate pi to the 5th decimal place using the Leibniz formula.
    The Leibniz formula: π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
    
    Returns:
        float: Value of pi rounded to 5 decimal places (3.14159)
    """
    pi_over_4 = 0
    # We need many iterations for the Leibniz formula to converge to 5 decimal places
    for i in range(1000000):
        pi_over_4 += ((-1) ** i) / (2 * i + 1)
    
    pi = 4 * pi_over_4
    return round(pi, 5)