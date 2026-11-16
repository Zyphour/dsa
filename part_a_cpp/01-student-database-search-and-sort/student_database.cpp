#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

struct Student {
    int id;
    char name[50];
    float cgpa;
};

Student *arr = NULL;
int n = 0;

void addStudent() {
    if (n == 0)
        arr = (Student*)malloc(sizeof(Student));
    else
        arr = (Student*)realloc(arr, (n + 1) * sizeof(Student));

    cout << "Enter ID, Name, CGPA: ";
    cin >> arr[n].id >> arr[n].name >> arr[n].cgpa;
    n++;
}

void display() {
    if (n == 0) {
        cout << "No records\n";
        return;
    }
    cout << "ID\tName\tCGPA\n";
    for (int i = 0; i < n; i++)
        cout << arr[i].id << "\t" << arr[i].name << "\t" << arr[i].cgpa << "\n";
}

int linearSearch(int key, int &comp) {
    comp = 0;
    for (int i = 0; i < n; i++) {
        comp++;
        if (arr[i].id == key)
            return i;
    }
    return -1;
}

int binarySearch(int key, int &comp) {
    int low = 0, high = n - 1;
    comp = 0;
    while (low <= high) {
        int mid = (low + high) / 2;
        comp++;
        if (arr[mid].id == key)
            return mid;
        else if (arr[mid].id < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

void sortById() {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (arr[j].id > arr[j + 1].id)
                swap(arr[j], arr[j + 1]);
}

void sortByName() {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (strcmp(arr[j].name, arr[j + 1].name) > 0)
                swap(arr[j], arr[j + 1]);
}

void sortByCGPA(int asc) {
    for (int i = 0; i < n - 1; i++) {
        int idx = i;
        for (int j = i + 1; j < n; j++) {
            if (asc == 1 && arr[j].cgpa < arr[idx].cgpa)
                idx = j;
            else if (asc != 1 && arr[j].cgpa > arr[idx].cgpa)
                idx = j;
        }
        swap(arr[i], arr[idx]);
    }
}

int main() {
    int ch, id, comp, pos, ord;
    do {
        cout << "\n1.Add  2.Display  3.Linear Search  4.Binary Search\n";
        cout << "5.Sort Name  6.Sort CGPA  7.Compare Search  0.Exit\nChoice: ";
        cin >> ch;

        if (ch == 1) {
            addStudent();
        } else if (ch == 2) {
            display();
        } else if (ch == 3) {
            cout << "Enter ID: ";
            cin >> id;
            pos = linearSearch(id, comp);
            if (pos == -1) cout << "Not found (" << comp << " comparisons)\n";
            else cout << "Found: " << arr[pos].name << " (" << comp << " comparisons)\n";
        } else if (ch == 4) {
            sortById();
            cout << "Enter ID: ";
            cin >> id;
            pos = binarySearch(id, comp);
            if (pos == -1) cout << "Not found (" << comp << " comparisons)\n";
            else cout << "Found: " << arr[pos].name << " (" << comp << " comparisons)\n";
        } else if (ch == 5) {
            sortByName();
            display();
        } else if (ch == 6) {
            cout << "1.Ascending  2.Descending: ";
            cin >> ord;
            sortByCGPA(ord);
            display();
        } else if (ch == 7) {
            int c1, c2;
            cout << "Enter ID to compare: ";
            cin >> id;
            linearSearch(id, c1);
            sortById();
            binarySearch(id, c2);
            cout << "Linear Search Comparisons: " << c1 << "\n";
            cout << "Binary Search Comparisons: " << c2 << "\n";
        }
    } while (ch != 0);

    free(arr);
    return 0;
}
