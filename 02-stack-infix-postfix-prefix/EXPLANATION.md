# Code explanation — `stack_conversions.cpp`

Two parts: the linked-list `Stack` ADT and the infix converter that uses it.

## Stack ADT

```cpp
struct Node { char data; Node *next; };

class Stack {
    Node *top;
public:
    Stack() { top = NULL; }
    ~Stack() { while (!isEmpty()) pop(); }
    bool isEmpty();
    void push(char x);
    char pop();
    char peek();
    void display();
};
```

`push`:

```cpp
Node *nn = new Node;
nn->data = x;
nn->next = top;
top = nn;
```

`pop`:

```cpp
Node *temp = top;
char val = temp->data;
top = top->next;
delete temp;
return val;
```

## Conversion functions

| Function | Job |
|---|---|
| `prec(c)` | `^` = 3, `* /` = 2, `+ -` = 1, else 0 |
| `convert(exp, revMode)` | shunting-yard engine (`revMode = false` normal, `true` for reversed string) |
| `infixToPostfix(exp)` | calls `convert(exp, false)` |
| `infixToPrefix(exp)` | `reverse`, swap `(` and `)`, call `convert(exp, true)`, `reverse` result |

Key operator precedence check inside `convert`:

```cpp
while (!s.isEmpty() && s.peek() != '(' &&
       (prec(s.peek()) > prec(c) ||
        (prec(s.peek()) == prec(c) && (revMode ? c == '^' : c != '^'))))
    res += s.pop();
```

Normal mode pops equal-precedence operators except right-associative `^`.
Reversed mode flips that rule because reversing the string flips associativity.

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

Postfix: `ABC+*D-`. Prefix: reverse + swap brackets → `D-(C+B)*A` → `DCB+A*-` → `-*A+BCD`.

## Common mistakes

- Setting `top = nn` before `nn->next = top` — loses the rest of the list.
- Forgetting `delete temp` in `pop`.
- Popping equal-precedence `^` in normal mode (`A^B^C` must be `ABC^^`).
- Reversing for prefix without swapping `(` and `)`.

## Viva — short answers

| Question | Answer |
|---|---|
| Why a linked-list stack? | Dynamic size with O(1) push and pop at the head. |
| Convert `A+B*C` to postfix. | `ABC*+`. |
| Convert `(A-B)/C` to prefix. | `/-ABC`. |
| Why is postfix easier to evaluate? | Single left-to-right pass with a stack; no brackets or precedence needed. |
| Time & space of conversion? | O(n) time, O(n) stack space. |
