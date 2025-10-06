/*
Fergusonball players are given a star rating based on the number of points that they score and 
the number of fouls that they commit. Specifically, they are awarded 5 stars for each point 
scored, and 3 stars are taken away for each foul committed. For every player, the number of 
points that they score is greater than the number of fouls that they commit. Your job is to 
determine how many players on a team have a star rating greater than 40. You also need to 
determine if the team is considered a gold team which means that all the players have a 
star rating greater than 40.
*/

#include <iostream>
using namespace std;

int main() {
    int repeat;
    int points;
    int fouls;
    int rating;
    int count = 0; 
    bool star = true;

    cin >> repeat;
    for (int i = 0; i < repeat; i++) {
        cin >> points;
        cin >> fouls;
        rating = (points * 5) - (fouls * 3);

        if (rating > 40) {
            count++;
        } else {
            star = false;
        }
    }

    cout << count;
    if (star) {
        cout << '+';
    } 
}