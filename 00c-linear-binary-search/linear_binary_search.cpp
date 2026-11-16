#include <iostream>
using namespace std;
int main() {
    int arr[10], n, key, choice;
    cout << "Enter the number of elements: "; cin >> n;
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << "\n----- MENU -----\n1. Linear Search\n2. Binary Search\nEnter your choice: "; cin >> choice;
    cout << "Enter the element to search: "; cin >> key;
    switch (choice) {
        case 1:
            for (int i = 0; i < n; i++)
                if (arr[i] == key) { cout << "Element found at position " << i + 1; return 0; }
            cout << "Element not found."; break;
        case 2: {
            int low = 0, high = n - 1, mid;
            while (low <= high) {
                mid = (low + high) / 2;
                if (arr[mid] == key) { cout << "Element found at position " << mid + 1; return 0; }
                else if (arr[mid] < key) low = mid + 1;
                else high = mid - 1;
            }
            cout << "Element not found.";
            break;
        }
        default: cout << "Invalid Choice!";
    }
    return 0;
}
