/*
 * EXPERIMENT 3 : Circular Queue using an Array
 * --------------------------------------------
 * Part A - C++
 *
 * A normal queue wastes space after a few deletions, because the front index
 * keeps moving forward. A CIRCULAR queue solves that: after the last slot it
 * wraps around to slot 0 using the modulus operator  (index + 1) % SIZE.
 *
 *        SIZE = 5
 *        +-----+-----+-----+-----+-----+
 *        | 10  | 20  | 30  |     |     |
 *        +-----+-----+-----+-----+-----+
 *           ^front        ^rear
 *        rear = (rear + 1) % SIZE   -> wraps to 0 after the last slot
 *
 * Operations: Enqueue (insert at rear), Dequeue (delete from front), Display.
 * The queue is FULL when count == SIZE.
 *
 * Compile : g++ circular_queue.cpp -o circular_queue
 * Run     : ./circular_queue
 */

#include <iostream>
using namespace std;

const int SIZE = 5;               // fixed size of the queue

class CircularQueue {
private:
    int data[SIZE];
    int front;                    // index of the first element
    int rear;                     // index of the last element
    int count;                    // how many elements are inside

public:
    CircularQueue() {
        front = 0;
        rear  = -1;
        count = 0;
    }

    bool isEmpty() { return count == 0; }
    bool isFull()  { return count == SIZE; }

    /* ---- a) Insertion (Enqueue) ---- */
    void enqueue(int value) {
        if (isFull()) {
            cout << "Queue is FULL (size " << SIZE << "). Cannot insert " << value << ".\n";
            return;
        }
        rear = (rear + 1) % SIZE;      // move rear forward, wrap to 0 if needed
        data[rear] = value;
        count++;
        cout << value << " inserted at position " << rear << ".\n";
    }

    /* ---- b) Deletion (Dequeue) ---- */
    int dequeue() {
        if (isEmpty()) {
            cout << "Queue is EMPTY. Nothing to delete.\n";
            return -1;
        }
        int removed = data[front];
        front = (front + 1) % SIZE;    // move front forward, wrap to 0 if needed
        count--;
        cout << removed << " deleted.\n";
        return removed;
    }

    /* ---- c) Display ---- */
    void display() {
        if (isEmpty()) {
            cout << "Queue is EMPTY.\n";
            return;
        }
        cout << "Queue (front -> rear): ";
        for (int i = 0; i < count; i++) {
            int index = (front + i) % SIZE;   // walk circularly
            cout << data[index] << " ";
        }
        cout << "\nfront index = " << front
             << ", rear index = " << rear
             << ", elements = " << count << "/" << SIZE << "\n";

        /* picture of the array so the "circular" part is visible */
        cout << "Array : ";
        for (int i = 0; i < SIZE; i++) {
            bool used = false;
            for (int k = 0; k < count; k++)
                if ((front + k) % SIZE == i) used = true;

            if (used) cout << "[" << data[i] << "] ";
            else      cout << "[ -- ] ";
        }
        cout << "\n";
    }

    /* bonus: look at the front element without deleting it */
    void peek() {
        if (isEmpty()) cout << "Queue is EMPTY.\n";
        else           cout << "Front element = " << data[front] << "\n";
    }
};

int main() {
    CircularQueue q;
    int choice, value;

    do {
        cout << "\n========== CIRCULAR QUEUE (size " << SIZE << ") ==========\n";
        cout << "1. Enqueue (insert)\n";
        cout << "2. Dequeue (delete)\n";
        cout << "3. Display\n";
        cout << "4. Peek front\n";
        cout << "0. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Value to insert: ";
            cin >> value;
            q.enqueue(value);
            q.display();
        }
        else if (choice == 2) {
            q.dequeue();
            q.display();
        }
        else if (choice == 3) {
            q.display();
        }
        else if (choice == 4) {
            q.peek();
        }
        else if (choice != 0) {
            cout << "Invalid choice.\n";
        }

    } while (choice != 0);

    cout << "Bye!\n";
    return 0;
}
