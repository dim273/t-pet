#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        sort(deck.begin(), deck.end());
        deque<int> de;
        int i = deck.size() - 1;
        de.push_back(deck[i]);
        while (i > 0) {
            de.push_front(de.back());
            de.pop_back();
            de.push_front(deck[--i]);
        }
        vector<int> ans(de.begin(), de.end());
        return ans;
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> deck(n);
    for (int i = 0; i < n; i++) {
        cin >> deck[i];
    }
    Solution sol;
    vector<int> result = sol.deckRevealedIncreasing(deck);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}