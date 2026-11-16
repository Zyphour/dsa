#include <iostream>
using namespace std;
int q[5], f = -1, r = -1;
void enqueue(int x) {
    if ((r + 1) % 5 == f) cout << "Full";
    else { if (f == -1) f = 0; r = (r + 1) % 5; q[r] = x; }
}
void dequeue() {
    if (f == -1) cout << "Empty";
    else { cout << "Deleted: " << q[f]; if (f == r) f = r = -1; else f = (f + 1) % 5; }
}
void display() {
    if (f == -1) cout << "Empty";
    else {
        for (int i = f; ; i = (i + 1) % 5) { cout << q[i] << " "; if (i == r) break; }
    }
}
int main() {
    int ch, x;
    do {
        cout << "\n1.Enqueue 2.Dequeue 3.Display 4.Exit\n"; cin >> ch;
        switch (ch) {
            case 1: cin >> x; enqueue(x); break;
            case 2: dequeue(); break;
            case 3: display(); break;
        }
    } while (ch != 4);
    return 0;
}
