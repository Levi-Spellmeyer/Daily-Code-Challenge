/* 
 * Author: Levi Spellmeyer
 * Date: 9/25/2025
 * Purpose: Program to determine if string has equal number of vowels in first and second half
*/

// Function is called with 1 string parameter
function isBalanced(s) {
    // Converts parameter string to upperCase and removes spaces
    let string = s.toUpperCase();
    string = string.replace(/\s/g, "");
    
    // Count variabes for vowels counted in string
    let beginCount = 0;
    let endCount = 0;

    // List of vowels that characters of string will be compared to
    const vowels = ['A','E','I','O','U'];
    
    // Length of parameter string used in below for loop
    let strLength = string.length;

    // For each character in the input string:
    //  - Check if character is in first/second half of string/ if it is a vowel
    //  - Increment appropriate counter if char in vowels array
    for (let i=0; i<strLength; i++){
        if( i < Math.floor((strLength/2 )) &&  vowels.includes(string[i])){
            beginCount++;
        } else if (i > Math.ceil((strLength/2)-1) && vowels.includes(string[i])){
            endCount++;
        }
    }

    // If counters are equal return true else false
    beginCount === endCount ? true : false;
}

let bool = isBalanced("racecar");
console.log(bool);
