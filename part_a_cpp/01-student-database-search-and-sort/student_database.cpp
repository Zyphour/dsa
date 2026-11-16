/*
 * EXPERIMENT 1 : Student Database (Searching and Sorting)
 * -------------------------------------------------------
 * Part A - C++
 *
 * What this program does:
 *   1. Stores student details (ID, Name, CGPA) in memory that we allocate at run time
 *      using malloc() and grow using realloc().
 *   2. Linear Search  - works on any order of records.
 *   3. Binary Search  - works only when records are sorted by ID.
 *   4. Bubble Sort    - sorts by Name (A-Z) and by ID.
 *      Selection Sort - sorts by CGPA (ascending or descending).
 *   5. Counts comparisons of Linear Search vs Binary Search so we can compare them.
 *
 * Compile : g++ student_database.cpp -o student_database
 * Run     : ./student_database
 */

#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>
#include <cstdlib>
using namespace std;

struct Student {
    int   id;
    char  name[50];
    float cgpa;
};

/* ---- global "database" ---- */
Student* students = NULL;   // points to memory we get from malloc / realloc
int count    = 0;           // how many students are stored
int capacity = 0;           // how many students we have space for

/* ---------------------------------------------------------------
 * Make room for one more student.
 * If the array is already full, ask realloc() for a bigger block.
 * --------------------------------------------------------------- */
void makeRoom() {
    if (count < capacity) return;                    // still some space left

    int newCapacity = (capacity == 0) ? 2 : capacity * 2;   // double the size
    Student* temp = (Student*)realloc(students, newCapacity * sizeof(Student));

    if (temp == NULL) {                              // realloc failed
        cout << "Error: not enough memory!\n";
        exit(1);
    }
    students = temp;
    capacity = newCapacity;
    cout << "   [realloc: memory expanded to " << capacity << " slots]\n";
}

/* ---------------- 1. Add a student ---------------- */
void addStudent() {
    makeRoom();

    cout << "Enter ID    : ";
    cin >> students[count].id;
    cout << "Enter Name  : ";
    cin >> students[count].name;
    cout << "Enter CGPA  : ";
    cin >> students[count].cgpa;

    count++;
    cout << "Student added. Total students = " << count << "\n";
}

/* ---------------- Display the table ---------------- */
void displayStudents() {
    if (count == 0) {
        cout << "No records yet.\n";
        return;
    }
    cout << "\n" << left << setw(8) << "ID" << setw(20) << "NAME" << setw(8) << "CGPA" << "\n";
    cout << "--------------------------------------\n";
    for (int i = 0; i < count; i++) {
        cout << left << setw(8) << students[i].id
             << setw(20) << students[i].name
             << setw(8) << fixed << setprecision(2) << students[i].cgpa << "\n";
    }
    cout << "--------------------------------------\n";
}

/* ---------------- 2. Linear Search by ID ----------------
 * Look at every record one by one until we find the ID.
 * Best case : 1 comparison      Worst case : n comparisons
 * -------------------------------------------------------- */
int linearSearch(int id, long long &comparisons) {
    comparisons = 0;
    for (int i = 0; i < count; i++) {
        comparisons++;
        if (students[i].id == id) return i;
    }
    return -1;                       // not found
}

/* ---------------- 3. Binary Search by ID ----------------
 * Only correct if the array is sorted by ID (ascending).
 * Each step throws away half of the remaining records.
 * Worst case : about log2(n) comparisons
 * -------------------------------------------------------- */
int binarySearch(Student arr[], int n, int id, long long &comparisons) {
    int low = 0, high = n - 1;
    comparisons = 0;

    while (low <= high) {
        int mid = (low + high) / 2;
        comparisons++;

        if (arr[mid].id == id)      return mid;
        else if (arr[mid].id < id)  low  = mid + 1;   // go right
        else                        high = mid - 1;   // go left
    }
    return -1;
}

/* ---------------- 4a. Bubble Sort (by Name / by ID) ----------------
 * Compare neighbours and swap them if they are in the wrong order.
 * After every pass the biggest value "bubbles" to the end.
 * ------------------------------------------------------------------ */
void bubbleSort(bool byName) {
    for (int pass = 0; pass < count - 1; pass++) {
        bool swapped = false;
        for (int i = 0; i < count - 1 - pass; i++) {
            bool wrongOrder;

            if (byName)
                wrongOrder = strcmp(students[i].name, students[i + 1].name) > 0;
            else
                wrongOrder = students[i].id > students[i + 1].id;

            if (wrongOrder) {
                Student temp      = students[i];
                students[i]       = students[i + 1];
                students[i + 1]   = temp;
                swapped = true;
            }
        }
        if (!swapped) break;        // array already sorted -> stop early
    }
}

/* ---------------- 4b. Selection Sort (by CGPA) ----------------
 * Find the smallest (or largest) CGPA and put it at the front,
 * then repeat for the rest of the array.
 * ------------------------------------------------------------- */
void selectionSortCGPA(bool ascending) {
    for (int i = 0; i < count - 1; i++) {
        int best = i;                                   // index of best record

        for (int j = i + 1; j < count; j++) {
            bool better = ascending ? (students[j].cgpa < students[best].cgpa)
                                    : (students[j].cgpa > students[best].cgpa);
            if (better) best = j;
        }

        if (best != i) {                                // swap
            Student temp    = students[i];
            students[i]     = students[best];
            students[best]  = temp;
        }
    }
}

/* ---------------- 5. Compare searching before and after sorting ----------------
 * We make a sorted copy of the database (sorted by ID), then search the SAME
 * target IDs with Linear Search and with Binary Search and count comparisons.
 * ------------------------------------------------------------------------------ */
void compareSearchPerformance() {
    if (count == 0) {
        cout << "Add some students first.\n";
        return;
    }

    // make a copy so the user's current order is not changed
    Student* sorted = (Student*)malloc(count * sizeof(Student));
    for (int i = 0; i < count; i++) sorted[i] = students[i];

    // sort the copy by ID with bubble sort
    for (int pass = 0; pass < count - 1; pass++) {
        for (int i = 0; i < count - 1 - pass; i++) {
            if (sorted[i].id > sorted[i + 1].id) {
                Student temp = sorted[i];
                sorted[i]     = sorted[i + 1];
                sorted[i + 1] = temp;
            }
        }
    }

    cout << "\n---- Search performance comparison ----\n";
    cout << "Targets searched : every ID stored once + one ID that does not exist\n\n";
    cout << left << setw(8) << "ID" << setw(22) << "Linear (unsorted)"
         << setw(22) << "Binary (sorted)" << "\n";
    cout << "--------------------------------------------------\n";

    long long totalLinear = 0, totalBinary = 0;
    int targets = count + 1;

    for (int t = 0; t <= count; t++) {
        // last t == count is a "not present" ID on purpose
        int target = (t < count) ? students[t].id : -999;

        long long linComp, binComp;
        int linPos = linearSearch(target, linComp);          // on the ORIGINAL array
        int binPos = binarySearch(sorted, count, target, binComp);

        totalLinear += linComp;
        totalBinary += binComp;

        cout << left << setw(8) << target
             << setw(22) << (to_string(linComp) + (linPos == -1 ? " (miss)" : " (hit)"))
             << setw(22) << (to_string(binComp) + (binPos == -1 ? " (miss)" : " (hit)"))
             << "\n";
    }

    cout << "--------------------------------------------------\n";
    cout << "Total comparisons   Linear = " << totalLinear
         << "   Binary = " << totalBinary << "\n";
    cout << fixed << setprecision(2);
    cout << "Average comparisons Linear = " << (double)totalLinear / targets
         << "   Binary = " << (double)totalBinary / targets << "\n";

    if (totalBinary > 0)
        cout << "Binary Search needed about "
             << (double)totalLinear / totalBinary << " times fewer comparisons.\n";

    cout << "\nNote: Binary Search gave correct answers only because the copy was\n";
    cout << "      sorted by ID. On an unsorted array it can miss a record.\n";

    free(sorted);
}

/* ---------------- main menu ---------------- */
int main() {
    int choice;

    do {
        cout << "\n========= STUDENT DATABASE =========\n";
        cout << "1. Add student\n";
        cout << "2. Display all students\n";
        cout << "3. Linear search by ID\n";
        cout << "4. Binary search by ID (sorts by ID first)\n";
        cout << "5. Sort by Name (Bubble Sort)\n";
        cout << "6. Sort by CGPA (Selection Sort)\n";
        cout << "7. Compare Linear vs Binary search performance\n";
        cout << "0. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 1) {
            addStudent();
        }
        else if (choice == 2) {
            displayStudents();
        }
        else if (choice == 3) {
            int id; long long comp;
            cout << "Enter ID to search: ";
            cin >> id;
            int pos = linearSearch(id, comp);
            if (pos == -1) cout << "Student not found. Comparisons = " << comp << "\n";
            else           cout << "Found at position " << pos + 1 << ": "
                                << students[pos].name << ", CGPA " << students[pos].cgpa
                                << ". Comparisons = " << comp << "\n";
        }
        else if (choice == 4) {
            if (count == 0) { cout << "No records yet.\n"; continue; }

            bubbleSort(false);                       // binary search needs sorted data
            cout << "Records sorted by ID.\n";

            int id; long long comp;
            cout << "Enter ID to search: ";
            cin >> id;
            int pos = binarySearch(students, count, id, comp);
            if (pos == -1) cout << "Student not found. Comparisons = " << comp << "\n";
            else           cout << "Found at position " << pos + 1 << ": "
                                << students[pos].name << ", CGPA " << students[pos].cgpa
                                << ". Comparisons = " << comp << "\n";
        }
        else if (choice == 5) {
            bubbleSort(true);
            cout << "Sorted by Name (A-Z).\n";
            displayStudents();
        }
        else if (choice == 6) {
            int order;
            cout << "1. Ascending CGPA   2. Descending CGPA : ";
            cin >> order;
            selectionSortCGPA(order == 1);
            cout << "Sorted by CGPA " << (order == 1 ? "(ascending)" : "(descending)") << ".\n";
            displayStudents();
        }
        else if (choice == 7) {
            compareSearchPerformance();
        }
        else if (choice != 0) {
            cout << "Invalid choice.\n";
        }

    } while (choice != 0);

    free(students);          // always give the memory back
    cout << "Memory freed. Bye!\n";
    return 0;
}
