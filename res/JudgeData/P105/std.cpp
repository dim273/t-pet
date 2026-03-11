#include <iostream>
#include <queue>
using namespace std;

class RecentCounter {
    queue<int> q;
public:
    RecentCounter() {}

    int ping(int t) {
        q.push(t);
        while (q.front() < t - 3000) {
            q.pop();
        }
        return q.size();
    }
};

int main() {
    int n;
    cin >> n;
    RecentCounter* obj = new RecentCounter();
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        cout << obj->ping(t) << " ";
    }
    cout << endl;
    return 0;
}