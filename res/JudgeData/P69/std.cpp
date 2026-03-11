#include <iostream>
#include <string>
using namespace std;

struct student {
    string name;
    int grade;
    int class_evaluation;
    char student_leader;
    char west;
    int thesis;
    int money;
};

int main() {
    int n;
    cin >> n;
    student stu[105];
    int maxn = -1;
    string maxname;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> stu[i].name >> stu[i].grade >> stu[i].class_evaluation >> stu[i].student_leader >> stu[i].west >> stu[i].thesis;
        stu[i].money = 0;
        if (stu[i].grade > 80 && stu[i].thesis > 0) stu[i].money += 8000;
        if (stu[i].grade > 85 && stu[i].class_evaluation > 80) stu[i].money += 4000;
        if (stu[i].grade > 90) stu[i].money += 2000;
        if (stu[i].grade > 85 && stu[i].west == 'Y') stu[i].money += 1000;
        if (stu[i].class_evaluation > 80 && stu[i].student_leader == 'Y') stu[i].money += 850;
        if (stu[i].money > maxn) {
            maxn = stu[i].money;
            maxname = stu[i].name;
        }
        sum += stu[i].money;
    }
    cout << maxname << endl;
    cout << maxn << endl;
    cout << sum << endl;
    return 0;
}