#include <iostream>
using namespace std;
int main() {
    int a[5], key;
    cout << "Enter 5 elements: ";
    for (int i = 0; i < 5; i++) cin >> a[i];
    cout << "Enter value to search: "; cin >> key;
    for (int i = 0; i < 5; i++) {
        if (a[i] == key) { cout << "Found at position " << i + 1; return 0; }
    }
    cout << "Not Found";
    return 0;
}
