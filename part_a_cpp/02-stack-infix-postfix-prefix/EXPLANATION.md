# Code explanation — `stack_conversions.cpp`

Two halves: the stack ADT (linked nodes) and the expression converter that uses it.

## Stack ADT

```cpp
struct Node { char data; Node* next; };

class Stack {
    Node* top;              // first node, or NULL when empty
public:
    void push(char value);  // add on top
    char pop();             // remove the top
    char peek();            // read the top
    bool isEmpty();
    void display();
    ~Stack();               // frees all remaining nodes
};
```

`push` (three lines that matter):

```cpp
Node* newNode = new Node;
newNode->data = value;
newNode->next = top;        // new node points at the old top
top = newNode;              // and becomes the new top
```

`pop`:

```cpp
Node* temp = top;  char value = temp->data;
top = temp->next;  delete temp;  return value;
```

The destructor repeats that unlink-and-delete until `top == NULL`, so nothing is
leaked when a `Stack` goes out of scope.

## Conversion functions

| Function | Job |
|---|---|
| `priority(op)` | `^` = 3, `* /` = 2, `+ -` = 1, everything else 0 |
| `isOperator(c)` | true for `+ - * / ^` |
| `bracketsOk(exp)` | pushes `(` and pops on `)` — a bracket check using the stack |
| `infixToPostfix(exp, reversedMode)` | the shunting-yard engine |
| `infixToPrefix(exp)` | reverse + swap brackets → postfix → reverse |

The only tricky condition in `infixToPostfix`:

```cpp
if (priority(top) > priority(c))                  mustPop = true;
else if (priority(top) == priority(c))
    mustPop = reversedMode ? (c == '^') : (c != '^');
```

Normal mode pops an equal-precedence operator except `^` (right associative).
Reversed mode does the exact opposite, because the reversal flips associativity.

`infixToPrefix` therefore calls `infixToPostfix(reversed, true)`.

## Dry run — `A*(B+C)-D`

| Read | Stack | Output |
|---|---|---|
| A | | A |
| * | * | A |
| ( | * ( | A |
| B | * ( | A B |
| + | * ( + | A B |
| C | * ( + | A B C |
| ) | * | A B C + |
| - | - | A B C + * |
| D | - | A B C + * D |
| end | | A B C + * D - |

Postfix `ABC+*D-`. Prefix: reverse with brackets swapped → `D-(C+B)*A` → postfix
`DCB+A*-` → reverse → `-*A+BCD`.

## Common mistakes

- Writing `top = newNode;` before `newNode->next = top;` — the rest of the stack is lost.
- Forgetting `delete` in `pop`.
- Popping on equal precedence for `^`, so `A^B^C` becomes `AB^C^` instead of `ABC^^`.
- Converting prefix without swapping the brackets while reversing.
- Not testing bracket balance first, so `(A+B` silently produces nonsense.

## Viva — short answers

| Question | Answer |
|---|---|
| Why a linked-list stack? | No size limit and no shifting; push/pop stay O(1). |
| Convert `A+B*C` to postfix. | `ABC*+`. |
| Convert `(A-B)/C` to prefix. | `/-ABC`. |
| Why is postfix easier to evaluate? | One left-to-right pass with a stack; no precedence or brackets. |
| Complexity of the conversion? | O(n) time, O(n) extra stack space. |
