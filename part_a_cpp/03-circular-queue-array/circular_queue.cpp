#include <iostream>
using namespace std;

#define SIZE 5

class CircularQueue {
    int arr[SIZE];
    int front, rear, count;

public:
    CircularQueue() {
        front = 0;
        rear = -1;
        count = 0;
    }

    void enqueue(int x) {
        if (count == SIZE) {
            cout << "Queue Full\n";
            return;
        }
        rear = (rear + 1) % SIZE;
        arr[rear] = x;
        count++;
    }

    void dequeue() {
        if (count == 0) {
            cout << "Queue Empty\n";
            return;
        }
        cout << "Deleted: " << arr[front] << "\n";
        front = (front + 1) % SIZE;
        count--;
    }

    void display() {
        if (count == 0) {
            cout << "Queue Empty\n";
            return;
        }
        for (int i = 0; i < count; i++)
            cout << arr[(front + i) % SIZE] << " ";
        cout << "\n";
    }
};

int main() {
    CircularQueue q;
    int ch, val;

    do {
        cout << "\n1.Enqueue  2.Dequeue  3.Display  0.Exit\nChoice: ";
        cin >> ch;
        if (ch == 1) {
            cout << "Value: ";
            cin >> val;
            q.enqueue(val);
        } else if (ch == 2) {
            q.dequeue();
        } else if (ch == 3) {
            q.display();
        }
    } while (ch != 0);

    return 0;
}
