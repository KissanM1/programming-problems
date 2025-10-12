/*
The CCC harp is a stringed instrument with strings labelled A, B, …, T. Like other instruments, it can be out of 
tune.

A musically inclined computer science student has written a clever computer program to help tune the harp. The 
program analyzes the sounds produced by the harp and provides instructions to fix each string that is out of tune.
Each instruction includes a group of strings, whether they should be tightened or loosened, and by how many turns.

Unfortunately, the output of the program is not very user friendly. It outputs all the tuning instructions on a 
single line. For example, the single line AFB+8HC-4 actually contains two tuning instructions: AFB+8 and HC-4. 
The first instruction indicates that harp strings A, F, and B should be tightened 
8 turns, and the second instruction indicates that harp strings H and C should be loosened 4 turns.

Your job is to take a single line of tuning instructions and make them easier to read.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {    
    string notes;
    string num;
    string code;
    cin >> code;

    for (int i = 0; i < code.length() + 1; i++) {
        if (isdigit(code[i])) {
            num += code[i];
        } else if (code[i] == '-') {
            cout << notes << " loosen ";
        } else if (code[i] == '+') {
            cout << notes << " tighten ";
        } else {
            if(num != "") {
                cout << num << endl;
                num = "";
                notes = "";
            }
            notes += code[i];
        }
    }
}