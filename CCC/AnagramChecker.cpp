/*
An anagram is a word or a phrase formed by rearranging the letters of another phrase such as ITEM and TIME. 
Anagrams may be several words long such as CS AT WATERLOO and COOL AS WET ART. Note that two phrases may be 
anagrams of each other even if each phrase has a different number of words (as in the previous example). Write 
a program to determine if two phrases are anagrams of each other.
*/

#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    string phrase1;
    string phrase2;
    unordered_map<char, int> count1;
    unordered_map<char, int> count2;

    getline(cin, phrase1);
    getline(cin, phrase2);


    for (int i = 0; i < phrase1.length(); i++) {
        if (isalpha(phrase1[i])){
            count1[phrase1[i]] += 1;
        }
    }

    for (int i = 0; i < phrase2.length(); i++) {
        if (isalpha(phrase2[i])){
            count2[phrase2[i]] += 1;
        }
    }

    if (count1 == count2) {
        cout << "Is an anagram.";
    } else {
        cout << "Is not an anagram.";
    }
}