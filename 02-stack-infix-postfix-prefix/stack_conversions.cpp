#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>
using namespace std;

struct Node {
    char data;
    Node *next;
};

class Stack {
    Node *top;
public:
    Stack() { top = NULL; }
    ~Stack() { while (!isEmpty()) pop(); }

    bool isEmpty() { return top == NULL; }

    void push(char x) {
        Node *nn = new Node;
        nn->data = x;
        nn->next = top;
        top = nn;
    }

    char pop() {
        if (isEmpty()) return '\0';
        Node *temp = top;
        char val = temp->data;
        top = top->next;
        delete temp;
        return val;
    }

    char peek() {
        if (isEmpty()) return '\0';
        return top->data;
    }

    void display() {
        if (isEmpty()) {
            cout << "Empty\n";
            return;
        }
        for (Node *p = top; p != NULL; p = p->next)
            cout << p->data << " ";
        cout << "\n";
    }
};

int prec(char c) {
    if (c == '^') return 3;
    if (c == '*' || c == '/') return 2;
    if (c == '+' || c == '-') return 1;
    return 0;
}

string convert(string exp, bool revMode) {
    Stack s;
    string res = "";
    for (int i = 0; i < (int)exp.length(); i++) {
        char c = exp[i];
        if (isalnum(c)) {
            res += c;
        } else if (c == '(') {
            s.push(c);
        } else if (c == ')') {
            while (!s.isEmpty() && s.peek() != '(')
                res += s.pop();
            s.pop();
        } else {
            while (!s.isEmpty() && s.peek() != '(' &&
                   (prec(s.peek()) > prec(c) ||
                    (prec(s.peek()) == prec(c) && (revMode ? c == '^' : c != '^'))))
                res += s.pop();
            s.push(c);
        }
    }
    while (!s.isEmpty())
        res += s.pop();
    return res;
}

string infixToPostfix(string exp) {
    return convert(exp, false);
}

string infixToPrefix(string exp) {
    reverse(exp.begin(), exp.end());
    for (int i = 0; i < (int)exp.length(); i++) {
        if (exp[i] == '(') exp[i] = ')';
        else if (exp[i] == ')') exp[i] = '(';
    }
    string res = convert(exp, true);
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    Stack st;
    int ch;
    char val;
    string exp;

    do {
        cout << "\n1.Push  2.Pop  3.Display  4.Convert Infix  0.Exit\nChoice: ";
        cin >> ch;
        if (ch == 1) {
            cout << "Enter char: ";
            cin >> val;
            st.push(val);
        } else if (ch == 2) {
            char r = st.pop();
            if (r == '\0') cout << "Stack Empty\n";
            else cout << "Popped: " << r << "\n";
        } else if (ch == 3) {
            st.display();
        } else if (ch == 4) {
            cout << "Enter infix: ";
            cin >> exp;
            cout << "Postfix: " << infixToPostfix(exp) << "\n";
            cout << "Prefix: " << infixToPrefix(exp) << "\n";
        }
    } while (ch != 0);

    return 0;
}
