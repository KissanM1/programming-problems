/*
A regular box of cupcakes holds 8 cupcakes, while a small box holds 3 cupcakes. There are 28
students in a class and a total of at least 28 cupcakes. Your job is to determine how many 
cupcakes will be left over if each student gets one cupcake.
*/

#include <iostream>
using namespace std;

int main() {
    int largeBox;
    int smallBox;
    int leftOver;

    cin >> largeBox;
    cin >> smallBox;

    leftOver = (largeBox * 8) + (smallBox * 3) - 28;

    cout << leftOver;
}
