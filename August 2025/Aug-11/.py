'''
Challenge Description:
---------------------
Given a string, determine whether the number of vowels in the first half of 
the string is equal to the number of vowels in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character.
'''
import unittest

def is_balanced(s:str) -> bool:
    """
    Description:
    ------------
    Given a string, determine whether the number of vowels in the first half of 
    the string is equal to the number of vowels in the second half.
    
    Parameters:
    -----------
    - s: input string in which number of vowels in the 1st and 2nd halves are counted/compared

    Returns:
    --------
    - True if number of vowels in each half are eqaul
    - False if number of vowels in each half are NOT equal
    """
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    first_half = 0
    sec_half = 0
    len_of_s = len(s)//2

    for char in range(len(s)): # For each character of the input string
        if s[char] in vowels:#   Check if that character is a vowel
            if char == len_of_s and len(s)%2 != 0:# If string is odd length and char is middle char, ignore
                continue
            if char < len_of_s:# If char is vowel and is in first half of string +1 to first half count
                first_half += 1
            elif char > len_of_s//2:# Else if char is vowel in 2nd half, +1 to second half count
                sec_half += 1

    return first_half == sec_half# return boolean answer to if vowels in 1st and 2nd half are equal

#================================ My thoughts on solution/improvement ================================
# Other possible solutions could include using RE library and using a regex
# to check if the character under review is a vowel
# could just uppercase the input  string and remove half the list of vowels
# This function runs in O(4n) time


#==================================== Solution from generative ai ====================================
def is_balanced(s: str) -> bool:
    vowels = set('aeiouAEIOU')
    mid = len(s) // 2

    first_half = sum(1 for c in s[:mid] if c in vowels)
    sec_half   = sum(1 for c in s[mid + (len(s) % 2):] if c in vowels)
    return first_half == sec_half


#==================================== Unit Tests ======================================================

class TestIsBalanced(unittest.TestCase):
    def test_racecar(self):
        self.assertEqual(is_balanced("racecar") , True)

    def test_latin(self):
        self.assertEqual(is_balanced("Lorem Ipsum") , True)
    
    def test_KittyIpsum(self):
        self.assertEqual(is_balanced("Kitty Ipsum") , False)

    def test_string(self):
        self.assertEqual(is_balanced("string") , False)

    def test_empty_string(self):
        self.assertEqual(is_balanced(" ") , True)

    def test_alphabet(self):
        self.assertEqual(is_balanced("abcdefghijklmnopqrstuvwxyz") , False)

    def test_special_char(self):
        self.assertEqual(is_balanced("123A#b!E&*456-0.U") , False)




if __name__ == "__main__":
    unittest.main(verbosity=2)




