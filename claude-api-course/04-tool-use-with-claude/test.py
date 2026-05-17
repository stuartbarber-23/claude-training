"""
Test file for main.py functions
"""
import math
from main import calculate_pi


def test_calculate_pi():
    """Test that calculate_pi returns pi to the 5th decimal place"""
    result = calculate_pi()
    expected = 3.14159  # Pi to 5 decimal places
    
    print(f"Calculated pi: {result}")
    print(f"Expected value: {expected}")
    print(f"Actual pi (from math): {math.pi}")
    
    # Check if the result matches expected value
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Verify it's close to the actual value of pi
    assert abs(result - math.pi) < 0.00001, f"Result {result} is not close enough to pi"
    
    print("✓ Test passed! Pi calculated correctly to 5 decimal places.")


if __name__ == "__main__":
    test_calculate_pi()
