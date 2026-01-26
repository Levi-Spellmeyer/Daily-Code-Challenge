# Challenge Overview and Instrucitons:
#=====================================#=====================================
# Given a string representing a number, and an integer base from 2 to 36, 
# determine whether the number is valid in that base.

#   - The string may contain integers, and uppercase or lowercase characters.
#   - The check should be case-insensitive.
#   - The base can be any number 2-36.
#   - A number is valid if every character is a valid digit in the given base.
#   - Example of valid digits for bases:
#       - Base 2: 0-1
#       - Base 8: 0-7
#       - Base 10: 0-9
#       - Base 16: 0-9 and A-F
#       - Base 36: 0-9 and A-Z
#=====================================#=====================================
import unittest

def is_valid_number(str_Number:str, base:int) -> bool:
    """ Given a string representing a number, and an integer base from 2 to 36, 
    determine whether the number is valid in that base. """

    str_Number = str_Number.upper()                     # Ensures the function is case-insensitive
    strChars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"   # Letters associated with their numerical index (hex values)
    intLenN = len(str_Number)

    if not (2 <= base <= 36):
        raise ValueError("Base must be between 2 and 36")

    for char in range(0, intLenN):                      # For each character of str_num
        if strChars.index(str_Number[char]) >= base:    # Check if its numerical value surpasses parameter base
            return False                                # If so, flag as invalid number of that base


    return True                                         # Else if parameter base not surpassed, return valid

#=====================================#=====================================
# Test cases:
#=====================================#=====================================
class TestIsValidNumber(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(is_valid_number("10101", 2))

    def test_case_2(self):
        self.assertFalse(is_valid_number("10201", 2))

    def test_case_3(self):
        self.assertTrue(is_valid_number("76543210", 8))

    def test_case_4(self):
        self.assertFalse(is_valid_number("9876543210", 8))

    def test_case_5(self):
        self.assertTrue(is_valid_number("9876543210", 10))

    def test_case_6(self):
        self.assertFalse(is_valid_number("ABC", 10))

    def test_case_7(self):
        self.assertTrue(is_valid_number("ABC", 16))

    def test_case_8(self):
        self.assertTrue(is_valid_number("Z", 36))

    def test_case_9(self):
        self.assertTrue(is_valid_number("ABC", 20))

    def test_case_10(self):
        self.assertTrue(is_valid_number("4B4BA9", 16))

    def test_case_11(self):
        self.assertFalse(is_valid_number("5G3F8F", 16))

    def test_case_12(self):
        self.assertTrue(is_valid_number("5G3F8F", 17))

    def test_case_13(self):
        self.assertFalse(is_valid_number("abc", 10))

    def test_case_14(self):
        self.assertTrue(is_valid_number("abc", 16))

    def test_case_15(self):
        self.assertTrue(is_valid_number("AbC", 16))

    def test_case_16(self):
        self.assertTrue(is_valid_number("z", 36))


if __name__ == "__main__":
    unittest.main()

#=====================================#=====================================
