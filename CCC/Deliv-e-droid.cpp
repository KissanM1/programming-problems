/*
In the game, Deliv-e-droid, a robot droid has to deliver packages while avoiding obstacles. 
At the end of the game, the final score is calculated based on the following point system:
Gain 50 points for every package delivered.
Lose 10 points for every collision with an obstacle.
Earn a bonus 500 points if the number of packages delivered is greater than the number of 
collisions with obstacles.
Your job is to determine the final score at the end of a game.
*/

#include <iostream>
using namespace std;

int main() {
    int packagesDelivered;
    int numberOfCollisions;
    int points;
    cin >> packagesDelivered;
    cin >> numberOfCollisions;

    points =  (packagesDelivered * 50) - (numberOfCollisions * 10);

    if (packagesDelivered > numberOfCollisions) {
        points += 500;
    }

    cout << points;
}


