#include <iostream>
#include <string>
using namespace std;

struct Student { int roll; string name; float cgpa; };

int main() {
    Student s[15], temp;
    for(int i=0; i<15; i++) cin >> s[i].roll >> s[i].name >> s[i].cgpa;
    for(int i=0; i<14; i++)
        for(int j=0; j<14-i; j++)
            if(s[j].roll > s[j+1].roll) { temp = s[j]; s[j] = s[j+1]; s[j+1] = temp; }
    for(int i=0; i<15; i++)
        cout << s[i].roll << " " << s[i].name << " " << s[i].cgpa << endl;
    return 0;
}
