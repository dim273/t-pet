#include <iostream>
#include <queue>
using namespace std;

class MovingAverage {
public:
    MovingAverage(int size) {
        this->size = size;
        this->sum = 0.0;
    }
    double next(int val) {
        if (qu.size() == size) {
            sum -= qu.front();
            qu.pop();
        }
        qu.emplace(val);
        sum += val;
        return sum / qu.size();
    }
private:
    int size;
    double sum;
    queue<int> qu;
};

int main() {
    int n;
    cin >> n;
    MovingAverage* obj = nullptr;
    for (int i = 0; i < n; i++) {
        string cmd;
        cin >> cmd;
        if (cmd == "MovingAverage") {
            int size;
            cin >> size;
            obj = new MovingAverage(size);
            cout << "null" << endl;
        } else if (cmd == "next") {
            int val;
            cin >> val;
            double res = obj->next(val);
            cout.precision(5);
            cout << fixed << res << endl;
        }
    }
    return 0;
}