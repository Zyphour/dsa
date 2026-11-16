/*
 * EXPERIMENT 2 : Stack as an ADT (Singly Linked List) + Infix -> Postfix / Prefix
 * -------------------------------------------------------------------------------
 * Part A - C++
 *
 * The stack is built from scratch (no STL) out of nodes, so it can grow and
 * shrink at run time:
 *
 *      top -> [ C | ] -> [ B | ] -> [ A | X ]     (NULL)
 *
 * push() adds a node at the top, pop() removes the top node -> O(1) each.
 *
 * The same stack is then used to convert an infix expression like
 *      A + B * C
 * into postfix  (A B C * +)  and prefix (+ A * B C).
 *
 * Compile : g++ stack_conversions.cpp -o stack_conversions
 * Run     : ./stack_conversions
 */

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

/* ============================================================
 *  PART 1 : STACK ADT USING A SINGLY LINKED LIST
 * ============================================================ */
struct Node {
    char  data;
    Node* next;
};

class Stack {
private:
    Node* top;                       // points to the first (top) node

public:
    Stack()  { top = NULL; }         // constructor

    ~Stack() {                       // destructor: free every node
        while (top != NULL) {
            Node* temp = top;
            top = top->next;
            delete temp;
        }
    }

    bool isEmpty() { return top == NULL; }

    void push(char value) {
        Node* newNode = new Node;    // create node
        newNode->data = value;
        newNode->next = top;         // new node points to old top
        top = newNode;               // new node becomes the top
    }

    char pop() {
        if (isEmpty()) return '\0';  // nothing to remove
        Node* temp = top;
        char  value = temp->data;
        top = temp->next;            // top moves one step down
        delete temp;                 // free the removed node
        return value;
    }

    char peek() {
        if (isEmpty()) return '\0';
        return top->data;
    }

    void display() {
        if (isEmpty()) { cout << "(stack is empty)\n"; return; }
        cout << "top -> ";
        for (Node* p = top; p != NULL; p = p->next) cout << p->data << " ";
        cout << "\n";
    }
};

/* ============================================================
 *  PART 2 : HELPER FUNCTIONS FOR CONVERSION
 * ============================================================ */

/* bigger number = higher priority */
int priority(char op) {
    if (op == '^')                 return 3;
    if (op == '*' || op == '/')    return 2;
    if (op == '+' || op == '-')    return 1;
    return 0;                          // for '(' and anything else
}

bool isOperator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
}

/* check that every '(' has a matching ')' */
bool bracketsOk(const string &exp) {
    Stack s;
    for (int i = 0; i < (int)exp.size(); i++) {
        if (exp[i] == '(') s.push('(');
        if (exp[i] == ')' && s.pop() != '(') return false;
    }
    return s.isEmpty();
}

/* ------------------------------------------------------------
 *  INFIX -> POSTFIX  (Shunting Yard idea)
 *
 *  Rule: operands go straight to the answer.
 *        An operator waits on the stack until a lower priority operator
 *        (or a bracket) arrives. Then it is popped into the answer.
 *
 *  reversedMode = false : normal conversion used for postfix output
 *  reversedMode = true  : used only inside infixToPrefix(), see below
 * ------------------------------------------------------------ */
string infixToPostfix(string exp, bool reversedMode = false) {
    Stack  s;
    string postfix = "";

    for (int i = 0; i < (int)exp.size(); i++) {
        char c = exp[i];

        if (c == ' ') continue;                    // ignore spaces

        if (isalnum(c)) {
            postfix += c;                          // operand -> output
        }
        else if (c == '(') {
            s.push(c);                             // remember the bracket
        }
        else if (c == ')') {
            while (!s.isEmpty() && s.peek() != '(')
                postfix += s.pop();                // pop until '('
            s.pop();                               // remove the '(' itself
        }
        else if (isOperator(c)) {
            /* In reversed mode the associativity of every operator is flipped,
               so we only pop strictly higher priority operators. In normal mode
               we pop equal priority too, except for the right associative '^'. */
            bool mustPop;
            while (!s.isEmpty() && s.peek() != '(') {
                if (priority(s.peek()) > priority(c)) {
                    mustPop = true;
                }
                else if (priority(s.peek()) == priority(c)) {
                    /* normal mode : + - * / are left associative, ^ is right
                       reversed mode: everything is flipped by the reversal  */
                    if (reversedMode) mustPop = (c == '^');
                    else              mustPop = (c != '^');
                }
                else mustPop = false;

                if (!mustPop) break;
                postfix += s.pop();
            }
            s.push(c);
        }
    }

    while (!s.isEmpty()) postfix += s.pop();       // empty the stack at the end
    return postfix;
}

/* ------------------------------------------------------------
 *  INFIX -> PREFIX
 *
 *  Simple trick used in most textbooks:
 *    1. reverse the infix expression and swap ( with )
 *    2. convert that to postfix  (associativity is flipped here, which is
 *       why infixToPostfix() is called with reversedMode = true)
 *    3. reverse the result
 *  Example: A+B*C  ->  C*B+A  ->  CB*A+  ->  +A*BC
 * ------------------------------------------------------------ */
string infixToPrefix(string exp) {
    string reversed = "";

    for (int i = (int)exp.size() - 1; i >= 0; i--) {
        char c = exp[i];
        if (c == '(')      reversed += ')';
        else if (c == ')') reversed += '(';
        else               reversed += c;
    }

    string postfixOfReversed = infixToPostfix(reversed, true);

    string prefix = "";
    for (int i = (int)postfixOfReversed.size() - 1; i >= 0; i--)
        prefix += postfixOfReversed[i];

    return prefix;
}

/* ============================================================
 *  PART 3 : MENU
 * ============================================================ */
int main() {
    int choice;

    do {
        cout << "\n========== STACK : INFIX CONVERSION ==========\n";
        cout << "1. Convert an infix expression\n";
        cout << "2. Try the stack ADT operations directly\n";
        cout << "0. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 1) {
            string exp;
            cout << "Enter infix expression (no spaces, e.g. (A+B)*C-D): ";
            cin >> exp;

            if (!bracketsOk(exp)) {
                cout << "Error: brackets are not balanced.\n";
            } else {
                cout << "\nInfix   : " << exp << "\n";
                cout << "Postfix : " << infixToPostfix(exp) << "\n";
                cout << "Prefix  : " << infixToPrefix(exp) << "\n";
            }
        }
        else if (choice == 2) {
            Stack s;
            int op;
            char value;

            do {
                cout << "\n--- STACK ---\n";
                cout << "1. Push   2. Pop   3. Peek   4. Display   0. Back\n";
                cout << "Enter choice: ";
                cin >> op;

                if (op == 1) {
                    cout << "Character to push: ";
                    cin >> value;
                    s.push(value);
                    s.display();
                }
                else if (op == 2) {
                    char removed = s.pop();
                    if (removed == '\0') cout << "Stack is empty, cannot pop.\n";
                    else                 cout << "Popped: " << removed << "\n";
                    s.display();
                }
                else if (op == 3) {
                    if (s.isEmpty()) cout << "Stack is empty.\n";
                    else             cout << "Top element: " << s.peek() << "\n";
                }
                else if (op == 4) {
                    s.display();
                }
            } while (op != 0);
        }
        else if (choice != 0) {
            cout << "Invalid choice.\n";
        }

    } while (choice != 0);

    cout << "Bye!\n";
    return 0;
}
