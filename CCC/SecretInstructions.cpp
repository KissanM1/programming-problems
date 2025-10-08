/*
Professor Santos has decided to hide a secret formula for a new type of biofuel. She has, however, left a sequence
of coded instructions for her assistant.

Each instruction is a sequence of five digits which represents a direction to turn and the number of steps to take.

The first two digits represent the direction to turn:

If their sum is odd, then the direction to turn is left.
If their sum is even and not zero, then the direction to turn is right.
If their sum is zero, then the direction to turn is the same as the previous instruction.
The remaining three digits represent the number of steps to take which will always be at least 
100
.
Your job is to decode the instructions so the assistant can use them to find the secret formula.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    int input;
    string direction;
    cin >> input;
    while (input != 99999) {
        int firstDigit = input / 10000;
        int secondDigit = (input / 1000) % 10;
        int beginningSum = firstDigit + secondDigit;
        int turns = input % 1000;

        if (beginningSum != 0) {
            direction = (beginningSum % 2 == 0) ? "right" : "left";
        }

        cout << direction << " " << turns << endl;
        cin >> input;
    }
}