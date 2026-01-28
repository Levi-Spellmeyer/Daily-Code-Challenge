# Challenge Overview and Instrucitons:
#=====================================#=====================================
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. 
# When starting with 0 and 1, the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

# Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, 
# return an array containing the sequence of the given length.
#   - Your function should handle sequences of any length greater than or equal to zero.
#   - If the length is zero, return an empty array.
#   - Note that the starting numbers are part of the sequence.
#=====================================#=====================================
import unittest

def fibonacci_sequence(start_sequence: list, length: int) -> list:
    '''Given the parameters of an array containing the first two numbers of a Fibonacci sequence 
    and an integer representing the length of the sequence, this function returns an array
    containing the sequence of given length.'''


    if not isinstance(start_sequence, list):
        raise TypeError(f"start_sequence must be a list, got {type(start_sequence).__name__}")
    if not isinstance(length, int):
        raise TypeError(f"length must be an int, got {type(length).__name__}") 

    if(length == 0): return []                      # Edge case of if requested length is 0 or 1
    if(length == 1): return [start_sequence[0]]

    for i in range(length-2):                       # For each number in range of requested length
        start_sequence += [start_sequence[i]+start_sequence[i+1]] 
        # Append a new number to the sequence that is the sum of number i and i+1

    return start_sequence

#=====================================#=====================================
# Test cases:
#=====================================#=====================================
class TestFibonaccieSequence(unittest.TestCase):
    def test_case_1(self):
        result = fibonacci_sequence([0, 1], 20)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])

    def test_case_2(self):
        result = fibonacci_sequence([21, 32], 1)
        self.assertEqual(result, [21])

    def test_case_3(self):
        result = fibonacci_sequence([123456789, 987654321], 5)
        self.assertEqual(result, [123456789, 987654321, 1111111110, 2098765431, 3209876541])

    def test_case_4(self):
        result = fibonacci_sequence([0, 1], 0)
        self.assertEqual(result, [])

    def test_case_5(self):
        result = fibonacci_sequence([10, 20], 2)
        self.assertEqual(result, [10, 20])

    def fail_test_case_6(self):
        result = fibonacci_sequence(10, 2)
        self.assertEqual(result, [10, 20])

    def fail_test_case_5(self):
        result = fibonacci_sequence([10, 20], '2')
        self.assertEqual(result, [10, 20])

if __name__ == "__main__":
    unittest.main()

#=====================================#=====================================