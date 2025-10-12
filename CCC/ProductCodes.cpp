/*
A store has hired the Code Cleaning Crew to help it update all of its product codes.

The original product codes are sequences of letters, positive integers, and negative integers. For example, 
cG23mH-9s is a product code that contains two uppercase letters, three lowercase letters, one positive integer, 
and one negative integer.

The new product codes are made by removing all lowercase letters, keeping all uppercase letters in order, and 
adding all the integers to form one new integer which is placed at the end of the code. For example, the new 
product code for cG23mH-9s is GH14.

Your job is to take a list of original product codes and determine the new product codes.
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {

    string code;
    string num;
    string output;
    vector<int> nums;
    int repeat;
    int sum;
    cin >> repeat;
    
    for (int j = 0; j < repeat; j++) {
        output = "";
        cin >> code;
        num = "";
        nums.clear();
        sum = 0;

        for (int i = 0; i < code.length() + 1; i++) {
            if (isdigit(code[i])) {
                num += code[i];
            } else if (code[i] == '-'){
                if (num != "") {
                    nums.push_back(stoi(num));
                }
                num = "-";
            } else {
                if (num != "") {
                    nums.push_back(stoi(num));
                    num = "";
                }
                if (isupper(code[i])) {
                    output += code[i];
                }
            } 
        }
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
        }
        cout << output << sum << endl;
    }
}