#include <stdio.h>      // Standard input and output library for terminal printing
#include <stdbool.h>    // Standard bool library to be abe to use boolean vallues
#include <string.h>     // Library that gives me ability to use strlen()

bool is_balanced(char s[]); // Function declaration (or prototype)

int main(){ // No comparable library to pythons unit-test, created my own tests
    printf("Test1 %s\n", is_balanced("racecar")     == true ? "Pass":"Fail");
    printf("Test2 %s\n", is_balanced("Lorem Ipsum") == true ? "Pass":"Fail");
    printf("Test3 %s\n", is_balanced("Kitty Ipsum") == false ? "Pass":"Fail");
    printf("Test4 %s\n", is_balanced("string")      == false ? "Pass":"Fail");
    printf("Test5 %s\n", is_balanced(" ")           == true ? "Pass":"Fail");
    printf("Test6 %s\n", is_balanced("abcdefghijklmnopqrstuvwxyz") == false ? "Pass":"Fail");
    printf("Test7 %s\n", is_balanced("123A#b!E&*456-0.U")           == false ? "Pass":"Fail");
    return 0;
}


bool is_balanced(char s[]){
    //Description:
    // ------------
    // Given a string, determine whether the number of vowels in the first half of 
    // the string is equal to the number of vowels in the second half.
    
    // Parameters:
    // -----------
    // - s: input string in which number of vowels in the 1st and 2nd halves are counted/compared

    // Returns:
    // --------
    // - True if number of vowels in each half are eqaul
    // - False if number of vowels in each half are NOT equal

    char vowels[] = "aeiouAEIOU";
    int first_half = 0;
    int sec_half = 0;
    int middle = strlen(s)/2;

    for(int i=0; i<strlen(s); i++){             // For each character in the input string
        for(int j=0; j<strlen(vowels); j++){    // for each character in the string of vowels
            if(vowels[j] == s[i]){              // If character from input is in string of vowels check the following
                if(i == middle && strlen(s)%2 != 0){ // if it is the middle character of an odd length input, ignore
                    continue;
                }
                if(i<middle){                   // If it is before the middle character increment first half count
                    first_half++;
                }
                else if(i > middle-1){          // If after middle character, increment 2nd half count
                    sec_half++;
                }
            }
        }
    }
    return first_half == sec_half; // Return boolean value
}

// My thoughts/ realizations
// 1. I could use int values of 0 and 1 instead of importing bool header file
// 2. Time complexity is O(n^2)
// 3. I could have used "if (strchr(vowels, s[i])) { ... }" to check if s[i] is in vowels (becomes O(n) complexity)
// 4. I am calling strlen() every iteration of the loop at that point make it a variable
// 5. I could have used Upper() string function to reduce the number of vowels in comparrison string
// 6. since input string is never changed making it a const could just help catch mistakes 







//   AI solution
#include <stdio.h>
#include <string.h>
#include <ctype.h>


int is_vowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int is_balanced(const char *s) {
    int len        = strlen(s);
    int half       = len / 2;
    int is_odd     = len % 2;
    int first_half = 0;
    int sec_half   = 0;

    for (int i = 0; i < len; i++) {
        if (!is_vowel(s[i])) continue;

        if (i == half && is_odd) continue;  // Skip middle char if odd length

        if (i < half)
            first_half++;
        else
            sec_half++;
    }

    return first_half == sec_half;
}

/*================================ Unit Tests ================================*/

typedef struct {
    const char *input;
    int         expected;
    const char *name;
} TestCase;

int run_tests() {
    TestCase tests[] = {
        { "racecar",                    1, "test_racecar"      },
        { "Lorem Ipsum",                1, "test_latin"        },
        { "Kitty Ipsum",                0, "test_KittyIpsum"   },
        { "string",                     0, "test_string"       },
        { " ",                          1, "test_empty_string" },
        { "abcdefghijklmnopqrstuvwxyz", 0, "test_alphabet"     },
        { "123A#b!E&*456-0.U",          0, "test_special_char" },
    };

    int num_tests = sizeof(tests) / sizeof(tests[0]);
    int passed    = 0;

    for (int i = 0; i < num_tests; i++) {
        int result = is_balanced(tests[i].input);
        int ok     = result == tests[i].expected;
        printf("%s (%s) ... %s\n",
               tests[i].name,
               tests[i].input,
               ok ? "OK" : "FAIL");
        if (ok) passed++;
    }

    printf("\n%d/%d tests passed.\n", passed, num_tests);
    return passed == num_tests ? 0 : 1;
}

int main() {
    return run_tests();
}