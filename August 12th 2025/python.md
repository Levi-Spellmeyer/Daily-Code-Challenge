# Generative AI solution to the is_valid_number problem

## ChatGPT

``` Python
#========================================================
# is_valid_number.py
#========================================================
"""
Module: is_valid_number

Functionality:
- Validate whether a string represents a number in a given base (2-36).
- Fully case-insensitive.
- Optimized for performance using a character-to-value mapping.
- Robust error handling for incorrect types or invalid bases.
"""

from typing import Dict


#--------------------------------------------------------
# Precomputed character-to-value map for bases 2-36
#--------------------------------------------------------
CHAR_VALUES: Dict[str, int] = {char: i for i, char in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}


#--------------------------------------------------------
# Core Function
#--------------------------------------------------------
def is_valid_number(str_number: str, base: int) -> bool:
    """
    Validate if a string is a correct representation of a number in the given base.

    Args:
        str_number (str): The number string to validate.
        base (int): Numeric base to validate against (2-36).

    Returns:
        bool: True if the string is a valid number in the base, False otherwise.

    Raises:
        TypeError: If str_number is not a string or base is not an integer.
        ValueError: If base is outside the allowed range (2-36).
    """

    #-----------------------------
    # Input type validation
    #-----------------------------
    if not isinstance(str_number, str):
        raise TypeError(f"str_number must be a string, got {type(str_number).__name__}")
    if not isinstance(base, int):
        raise TypeError(f"base must be an integer, got {type(base).__name__}")
    if not (2 <= base <= 36):
        raise ValueError(f"base must be between 2 and 36, got {base}")

    #-----------------------------
    # Empty string is invalid
    #-----------------------------
    if not str_number:
        return False

    #-----------------------------
    # Normalize to uppercase (case-insensitive)
    #-----------------------------
    str_number = str_number.upper()

    #-----------------------------
    # Validate each character in O(1) time using CHAR_VALUES dict
    #-----------------------------
    for ch in str_number:
        val = CHAR_VALUES.get(ch, -1)  # -1 indicates invalid character
        if val == -1 or val >= base:
            return False

    return True


#========================================================
# Unit Testing
#========================================================
import unittest


class TestIsValidNumber(unittest.TestCase):
    """
    Comprehensive test suite for is_valid_number.

    Covers:
        - Provided test cases (16)
        - Edge cases (empty string, invalid characters)
        - Error handling (invalid base, invalid types)
        - Case insensitivity
        - Extended bases (up to 36)
    """

    #-----------------------------
    # Provided test cases
    #-----------------------------
    def test_provided_cases(self):
        self.assertTrue(is_valid_number("10101", 2))
        self.assertFalse(is_valid_number("10201", 2))
        self.assertTrue(is_valid_number("76543210", 8))
        self.assertFalse(is_valid_number("9876543210", 8))
        self.assertTrue(is_valid_number("9876543210", 10))
        self.assertFalse(is_valid_number("ABC", 10))
        self.assertTrue(is_valid_number("ABC", 16))
        self.assertTrue(is_valid_number("Z", 36))
        self.assertTrue(is_valid_number("ABC", 20))
        self.assertTrue(is_valid_number("4B4BA9", 16))
        self.assertFalse(is_valid_number("5G3F8F", 16))
        self.assertTrue(is_valid_number("5G3F8F", 17))
        self.assertFalse(is_valid_number("abc", 10))
        self.assertTrue(is_valid_number("abc", 16))
        self.assertTrue(is_valid_number("AbC", 16))
        self.assertTrue(is_valid_number("z", 36))

    #-----------------------------
    # Edge cases
    #-----------------------------
    def test_empty_string(self):
        self.assertFalse(is_valid_number("", 2))
        self.assertFalse(is_valid_number("", 36))

    def test_invalid_characters(self):
        # Invalid symbols
        self.assertFalse(is_valid_number("12-3", 10))
        self.assertFalse(is_valid_number("12 3", 10))
        self.assertFalse(is_valid_number("12.3", 10))
        self.assertFalse(is_valid_number("!@#", 36))

    def test_case_insensitivity(self):
        # Should treat lowercase same as uppercase
        self.assertTrue(is_valid_number("abc", 16))
        self.assertTrue(is_valid_number("AbC", 16))
        self.assertTrue(is_valid_number("z", 36))

    #-----------------------------
    # Error handling
    #-----------------------------
    def test_invalid_base(self):
        with self.assertRaises(ValueError):
            is_valid_number("101", 1)
        with self.assertRaises(ValueError):
            is_valid_number("101", 37)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            is_valid_number(101, 10)  # str_number must be string
        with self.assertRaises(TypeError):
            is_valid_number("101", "10")  # base must be int

    #-----------------------------
    # Extended bases
    #-----------------------------
    def test_high_base_36(self):
        self.assertTrue(is_valid_number("123ABCXYZ", 36))
        self.assertFalse(is_valid_number("123abcxyz!", 36))

    #-----------------------------
    # Leading/trailing whitespace not allowed
    #-----------------------------
    def test_whitespace(self):
        self.assertFalse(is_valid_number(" 123", 10))
        self.assertFalse(is_valid_number("123 ", 10))

#--------------------------------------------------------
# Test runner
#--------------------------------------------------------
if __name__ == "__main__":
    unittest.main()
```




## Claude

``` Python

"""
Module for validating numbers in different numeral systems (bases 2-36).

This module provides functionality to determine whether a string represents
a valid number in a given base, supporting bases from binary (2) to base-36.
"""

import unittest
from typing import Final


def is_valid_number(number: str, base: int) -> bool:
    """
    Validate whether a string represents a valid number in the specified base.
    
    A number is valid in a given base if all its digits are within the valid
    range for that base. For example, in base 10, valid digits are 0-9; in
    base 16, valid digits are 0-9 and A-F.
    
    Args:
        number: String representation of the number to validate.
                May contain digits (0-9) and letters (A-Z, case-insensitive).
        base: The numeral system base (must be between 2 and 36, inclusive).
    
    Returns:
        True if the number is valid in the specified base, False otherwise.
    
    Raises:
        ValueError: If base is not between 2 and 36, or if number is empty.
        ValueError: If number contains characters outside the valid digit set.
    
    Examples:
        >>> is_valid_number("10101", 2)
        True
        >>> is_valid_number("10201", 2)
        False
        >>> is_valid_number("ABC", 16)
        True
        >>> is_valid_number("Z", 36)
        True
    """
    # Input validation
    if not 2 <= base <= 36:
        raise ValueError(f"Base must be between 2 and 36, got {base}")
    
    if not number:
        raise ValueError("Number string cannot be empty")
    
    # Valid digits for bases 2-36: 0-9 represent values 0-9, A-Z represent 10-35
    VALID_DIGITS: Final[str] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Normalize to uppercase for case-insensitive comparison
    normalized_number = number.upper()
    
    # Check each character
    for char in normalized_number:
        # Find the numeric value this character represents
        try:
            digit_value = VALID_DIGITS.index(char)
        except ValueError:
            raise ValueError(
                f"Invalid character '{char}' in number. "
                f"Valid characters are 0-9 and A-Z."
            )
        
        # Verify the digit value is valid for this base
        if digit_value >= base:
            return False
    
    return True


class TestIsValidNumber(unittest.TestCase):
    """Comprehensive test suite for the is_valid_number function."""
    
    # Binary (base 2) tests
    def test_valid_binary(self):
        """Test valid binary numbers."""
        self.assertTrue(is_valid_number("10101", 2))
    
    def test_invalid_binary(self):
        """Test invalid binary number (contains digit 2)."""
        self.assertFalse(is_valid_number("10201", 2))
    
    # Octal (base 8) tests
    def test_valid_octal(self):
        """Test valid octal number."""
        self.assertTrue(is_valid_number("76543210", 8))
    
    def test_invalid_octal(self):
        """Test invalid octal number (contains digit 9)."""
        self.assertFalse(is_valid_number("9876543210", 8))
    
    # Decimal (base 10) tests
    def test_valid_decimal(self):
        """Test valid decimal number."""
        self.assertTrue(is_valid_number("9876543210", 10))
    
    def test_invalid_decimal_with_letters(self):
        """Test invalid decimal number (contains letters)."""
        self.assertFalse(is_valid_number("ABC", 10))
    
    def test_invalid_decimal_lowercase(self):
        """Test invalid decimal number with lowercase letters."""
        self.assertFalse(is_valid_number("abc", 10))
    
    # Hexadecimal (base 16) tests
    def test_valid_hexadecimal_uppercase(self):
        """Test valid hexadecimal with uppercase letters."""
        self.assertTrue(is_valid_number("ABC", 16))
    
    def test_valid_hexadecimal_lowercase(self):
        """Test valid hexadecimal with lowercase letters."""
        self.assertTrue(is_valid_number("abc", 16))
    
    def test_valid_hexadecimal_mixed_case(self):
        """Test valid hexadecimal with mixed case."""
        self.assertTrue(is_valid_number("AbC", 16))
    
    def test_valid_hexadecimal_alphanumeric(self):
        """Test valid hexadecimal with numbers and letters."""
        self.assertTrue(is_valid_number("4B4BA9", 16))
    
    def test_invalid_hexadecimal(self):
        """Test invalid hexadecimal (contains 'G')."""
        self.assertFalse(is_valid_number("5G3F8F", 16))
    
    # Base 17 tests
    def test_valid_base_17(self):
        """Test valid base-17 number (includes 'G')."""
        self.assertTrue(is_valid_number("5G3F8F", 17))
    
    # Base 20 tests
    def test_valid_base_20(self):
        """Test valid base-20 number."""
        self.assertTrue(is_valid_number("ABC", 20))
    
    # Base 36 tests
    def test_valid_base_36_uppercase(self):
        """Test valid base-36 with uppercase 'Z'."""
        self.assertTrue(is_valid_number("Z", 36))
    
    def test_valid_base_36_lowercase(self):
        """Test valid base-36 with lowercase 'z'."""
        self.assertTrue(is_valid_number("z", 36))
    
    # Edge cases and error handling
    def test_invalid_base_too_low(self):
        """Test that base < 2 raises ValueError."""
        with self.assertRaises(ValueError):
            is_valid_number("10", 1)
    
    def test_invalid_base_too_high(self):
        """Test that base > 36 raises ValueError."""
        with self.assertRaises(ValueError):
            is_valid_number("10", 37)
    
    def test_empty_string(self):
        """Test that empty string raises ValueError."""
        with self.assertRaises(ValueError):
            is_valid_number("", 10)
    
    def test_invalid_character(self):
        """Test that invalid characters raise ValueError."""
        with self.assertRaises(ValueError):
            is_valid_number("12@34", 10)


if __name__ == "__main__":
    unittest.main()

```