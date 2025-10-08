/*
Ron is cooking chili using an assortment of peppers.
The spiciness of a pepper is measured in Scoville Heat Units (SHU). Ron's chili is currently not spicy at all, 
but each time Ron adds a pepper, the total spiciness of the chili increases by the SHU value of that pepper.

The SHU values of the peppers available to Ron are shown in the following table:

Pepper Name	Scoville Heat Units
Poblano	1500
Mirasol	6000
Serrano	15500
Cayenne	40000
Thai	75000
Habanero	125000
Your job is to determine the total spiciness of Ron's chili after he has finished adding peppers.
*/

#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    int pepperCount;
    int heatCount = 0;
    string pepper;
    unordered_map<string, int> peppers;

    peppers["Poblano"] = 1500;
    peppers["Mirasol"] = 6000;
    peppers["Serrano"] = 15500;
    peppers["Cayenne"] = 40000;
    peppers["Thai"] = 75000;
    peppers["Habanero"] = 125000;

    cin >> pepperCount;

    for (int i = 0; i < pepperCount; i++) {
        cin >> pepper;
        heatCount += peppers[pepper];
    }

    cout << heatCount;
}