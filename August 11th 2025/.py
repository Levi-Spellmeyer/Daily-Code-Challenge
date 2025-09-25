# Author: Levi Spellmeyer
# Date: 9/25/2025
# Purpose: Program to determine if string has equal number of vowels in first and second half


 # import math library to have acces to flor and ceil functions
import math

# Function is called with 1 string passed as a parameter
def is_balanced(s):
    # List of vowels that char in param string will be compared to
    listOfVowels = ["A","E","I","O","U"]
    countFirstHalf = 0
    countSecHalf = 0

    # Converts string to uppercase and removes spaces
    s = s.upper()
    s = s.replace(" ", "")

    # Used for iterating below for loop
    length = len(s)

    # For each char in string compare char to listOfVowels and location in string
    # If char in listOfVowels appropriate counter incremented based on location within string
    for i in range(0, len(s)):
        if(s[i] in listOfVowels and i<math.floor(length/2)):
            countFirstHalf += 1
        elif(s[i] in listOfVowels and i > math.ceil(length/2)-1):
            countSecHalf += 1

    # If num vowels in first and second half are equal return true else false
    if(countFirstHalf == countSecHalf):
        return True
    else:
        return False

is_balanced("Lorem Ipsum")