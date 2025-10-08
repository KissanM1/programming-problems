#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    int people;
    int mx = 0;
    string output = "";
    string user_availability;
    int days[5] = {0,0,0,0,0};

    cin >> people;

    for (int i = 0; i < people; i++) {
        cin >> user_availability;
        for (int j = 0; j < 5; j++) {
            if( user_availability[j] == 'Y') {
                days[j]++;
            }
        }
    }
    for (int i = 0; i < 5; i++) {
        if (days[i] > mx) {
            mx = days[i];
            output = to_string(i + 1);
        } else if (days[i] == mx) {
            output +=  "," + to_string(i + 1);
        } 
    }
    
    cout << output;
}
