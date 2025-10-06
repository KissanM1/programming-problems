/* 
There is a new conveyor belt sushi restaurant in town. Plates of sushi travel around the 
restaurant on a raised conveyor belt and customers choose what to eat by removing plates.
Each red plate of sushi costs $3, each green plate of sushi costs $4, and each blue plate of 
sushi costs $5.
*/

#include <iostream>
using namespace std;

int main() {
    int red;
    int green;
    int blue;
    int cost;

    cin >> red;
    cin >> green;
    cin >> blue;

    cost = (red * 3) + (green * 4) + (blue * 5);
    cout << cost;
}