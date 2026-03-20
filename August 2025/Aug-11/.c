#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool is_balanced(char s[]);


int main(){
    printf("Test1 %s\n", is_balanced("racecar")     == true ? "Pass":"Fail");
    printf("Test2 %s\n", is_balanced("Lorem Ipsum") == true ? "Pass":"Fail");
    printf("Test3 %s\n", is_balanced("Kitty Ipsum") == false ? "Pass":"Fail");
    printf("Test4 %s\n", is_balanced("string")      == false ? "Pass":"Fail");
    printf("Test5 %s\n", is_balanced(" ")           == true ? "Pass":"Fail");
    printf("Test6 %s\n", is_balanced("abcdefghijklmnnopqrstuvwxyz") == false ? "Pass":"Fail");
    printf("Test7 %s\n", is_balanced("123A#b!E&*456-0.U")           == false ? "Pass":"Fail");
    return 0;
}


bool is_balanced(char s[]){
    char vowels[] = "aeiouAEIOU";
    int first_half = 0;
    int sec_half = 0;
    int middle = strlen(s)/2;

    // printf("%d\n", middle);
    for(int i=0; i<strlen(s); i++){
        //printf("%d\n", i);
        for(int j=0; j<strlen(vowels); j++){
            //printf("%d\n",j);
            if(vowels[j] == s[i]){
                if(i == middle && strlen(s)%2 != 0){
                    // printf("skipped");
                    continue;
                }
                if(i<middle){
                    first_half++;
                    // printf("%d\n", first_half);
                }
                else if(i > middle-1){
                    sec_half++;
                    // printf("%d\n",sec_half);
                }
            }
        }
    }

    return first_half == sec_half;
}