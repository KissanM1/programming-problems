/* 
After completing a competition, you are struck with curiosity. How many participants were awarded bronze level?

Gold level is awarded to all participants who achieve the highest score. Silver level is awarded to all 
participants who achieve the second highest score. Bronze level is awarded to all participants who achieve the 
third highest score.

Given a list of all the scores, your job is to determine the score required for bronze level and how many 
participants achieved this score.
*/

#include <iostream>
#include <set>
using namespace std;

int main() {
    int scoreCount;
    int score;
    int count = 0;
    set<int> scores;

    cin >> scoreCount;
    int allScores[scoreCount];

    for (int i = 0; i < scoreCount; i++) {
        cin >> score;
        allScores[i] = score;
        scores.insert(score); 
    }

    auto target = prev(scores.end(), 3);

    for (int i = 0; i < scoreCount; i++){
        if (allScores[i] == *target) {
            count++;
        }
    }

    cout << *target << " " << count;
}