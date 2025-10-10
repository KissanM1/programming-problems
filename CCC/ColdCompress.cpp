/*
Your new cellphone plan charges you for every character you send from your phone. Since you tend to send 
sequences of symbols in your messages, you have come up with the following compression technique: for each 
symbol, write down the number of times it appears consecutively, followed by the symbol itself. This compression 
technique is called run-length encoding.

More formally, a block is a substring of identical symbols that is as long as possible. A block will be 
represented in compressed form as the length of the block followed by the symbol in that block. The encoding of a 
string is the representation of each block in the string in the order in which they appear in the string.

Given a sequence of characters, write a program to encode them in this format.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    string code;
    char prev;
    int count;
    int codes;

    cin >> codes;
    for (int i = 0; i < codes; i++) {
        cin >> code;
        prev = code[0];
        count = 1;
        for (int j = 1; j < code.length() ; j++) {
            if (code[j] != prev) {
                cout << count << " " << prev << " ";
                prev = code[j];
                count = 1;
            } else {
                count++;
            }
        }
        cout << count << " " << prev << endl;
    }
}