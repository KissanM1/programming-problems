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
