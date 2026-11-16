# Practical 2: Stack ADT (Linked List) & Infix → Postfix / Prefix — Complete Reference & Code Guide (`stack_conversions.cpp`)

> **Aim:** Implement a stack as an abstract data type using a singly linked list, and use it to convert an infix expression into postfix and prefix form.
>
> **Language:** C++ · **Program:** [`stack_conversions.cpp`](stack_conversions.cpp) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`stack_conversions.cpp`](stack_conversions.cpp) implements two components inside an interactive **menu-driven C++ program**:
1. **A Linked-List `Stack` class (ADT):** Supports `push(char)` (insert at head), `pop()` (delete from head and return value), `peek()` (read top without deleting), `isEmpty()`, and `display()`.
2. **Infix Expression Converter:** When the user selects option `4` and enters an **Infix expression** without spaces (such as `(A+B)*C-D` or `A+B*C`), it uses the linked-list `Stack` to compute and print **both** its **Postfix** equivalent and its **Prefix** equivalent, repeating the menu until the user enters `0` to exit.

### Sample Run
```text
1.Push  2.Pop  3.Display  4.Convert Infix  0.Exit
Choice: 4
Enter infix: A*(B+C)-D
Postfix: ABC+*D-
Prefix: -*A+BCD

1.Push  2.Pop  3.Display  4.Convert Infix  0.Exit
Choice: 0
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Abbreviation | Full Form & Definition |
|---|---|
| **ADT** | **Full Form:** *Abstract Data Type* — a mathematical/logical specification of a data structure defined strictly by **what operations it performs** (interface), independent of **how it is implemented** in memory (array vs. linked list). |
| **LIFO** | **Full Form:** *Last In, First Out* (also called **FILO** = *First In, Last Out*) — the last item inserted (`pushed`) onto a Stack is the first item removed (`popped`). |
| **Stack** | A linear LIFO data structure where all insertions (`push`) and deletions (`pop`) occur at **one single end** called **`top`**. |
| **Singly Linked List** | A dynamic chain of heap-allocated `Node` objects where each node contains a `data` field and a single `next` pointer to the next node (`NULL` marks the end). |
| **Stack Underflow** | Attempting to `pop()` or `peek()` when the stack is **empty** (`top == NULL`). |
| **Stack Overflow** | Attempting to `push()` when no more memory is available (common in fixed-size arrays; in linked lists, occurs only if system heap RAM is exhausted). |
| **Infix Notation** | Expression format where each binary operator sits **between** its operands: `A + B * C`. Requires parentheses and precedence rules. |
| **Postfix Notation (RPN)** | **Full Form of RPN:** *Reverse Polish Notation* — expression format where each operator sits **after** its operands: `A B C * +`. Requires **zero brackets** and **zero precedence rules**. |
| **Prefix Notation** | Also called **Polish Notation** — expression format where each operator sits **before** its operands: `+ A * B C`. Also requires **zero brackets**. |
| **Operator Precedence** | Priority order deciding which operator binds first: `^` (`3`, highest) `>` `*`, `/` (`2`) `>` `+`, `-` (`1`, lowest). |
| **Associativity** | Rule breaking ties between operators of **equal precedence**: `+`, `-`, `*`, `/` are **Left-to-Right** (`A - B - C = (A - B) - C`), while exponent `^` is **Right-to-Left** (`A ^ B ^ C = A ^ (B ^ C)`). |

---

## 3. Core Facts, Properties, Advantages & Uses

### Why Implement a Stack Using a Singly Linked List?
- **No fixed size limit:** Grows and shrinks dynamically at runtime (`new` on `push`, `delete` on `pop`).
- **O(1) operations at Head:** Keeping `top` at the **front (head)** of the singly linked list lets `push`, `pop`, `peek`, and `isEmpty` all execute in **O(1)** constant time with zero element shifting.

### Why Compilers & Calculators Convert Infix to Postfix / Prefix
- Infix expressions are ambiguous without parentheses and operator precedence tables.
- Postfix and Prefix expressions are **100% bracket-free and unambiguous**: a computer evaluates a Postfix expression in a **single left-to-right pass** using a stack in `O(n)` time!

### Real-World Uses / Applications of Stack
1. **Infix to Postfix / Prefix conversion** and **Postfix expression evaluation** in compilers and calculators.
2. **Function Call Stack** — managing function calls, local variables, return addresses, and **recursion**.
3. **Undo / Redo** operations in text editors and **Back** button history in web browsers.
4. **Syntax / Balanced Parentheses checking** (`()`, `{}`, `[]`) in compilers.
5. **DFS (Depth-First Search)** traversal and **backtracking** algorithms.

---

## 4. Step-by-Step Conversion Algorithms

### A. Infix → Postfix (Dijkstra's Shunting-Yard Algorithm)
Scan the infix expression **left to right**, character `c` by character:
1. **Operand (`isalnum(c)`):** Append `c` directly to output string `res`.
2. **Left Parenthesis `(`:** Push `(` onto stack `s`.
3. **Right Parenthesis `)`:** Pop from `s` and append to `res` until `(` is at the top of `s`; then pop and **discard** `(`.
4. **Operator (`+`, `-`, `*`, `/`, `^`):** While `s` is non-empty, `s.peek() != '('`, and (`prec(s.peek()) > prec(c)` **OR** (`prec(s.peek()) == prec(c)` and `c != '^'`)):
   - Pop from `s` and append to `res`.
   *(Equal `^` is NOT popped because `^` is right-associative!)*
   - Then push `c` onto `s`.
5. **End of Expression:** Pop all remaining operators from `s` and append to `res`.

### B. Infix → Prefix Algorithm
1. **Reverse** the input infix string (`reverse(exp.begin(), exp.end())`).
2. **Swap brackets:** Change every `'('` to `')'` and every `')'` to `'('`.
3. **Convert to Postfix with reversed associativity (`revMode = true`):** Because reversing the string flips left-vs-right operator order, equal-precedence left-associative operators (`+ - * /`) are **not** popped on ties, while equal right-associative `^` **is** popped (`revMode ? c == '^' : c != '^'`).
4. **Reverse** the resulting string to obtain the final **Prefix** expression.

---

## 5. Line-by-Line Code Explanation

| Code Component | Exact Role in `stack_conversions.cpp` |
|---|---|
| `#include <cctype>` & `<algorithm>` | Provides `isalnum(c)` (checks if `c` is a letter or digit `A-Z`, `a-z`, `0-9`) and `std::reverse(...)`. |
| `struct Node { char data; Node *next; };` | Defines one linked-list node storing character `data` and pointer `next`. |
| `Stack() { top = NULL; }` | Constructor initializing an empty stack (`top` points nowhere). |
| `~Stack() { while (!isEmpty()) pop(); }` | Destructor automatically freeing all remaining heap nodes via `pop()` (`delete`) to prevent memory leaks. |
| `push(char x)` | Allocates `Node *nn = new Node;`, sets `nn->data = x;`, links **`nn->next = top;`**, and updates **`top = nn;`** (`O(1)`). |
| `pop()` | Returns `'\0'` if empty; otherwise saves `temp = top` and `val = temp->data`, advances `top = top->next`, frees RAM with **`delete temp;`**, and returns `val` (`O(1)`). |
| `peek()` | Returns `top->data` without removing the node (`'\0'` if empty) (`O(1)`). |
| `display()` | Walks `Node *p = top` down `p = p->next` until `NULL`, printing stack contents from top to bottom (`O(n)`). |
| `prec(char c)` | Returns integer precedence: `'^' → 3`, `'*'` or `'/' → 2`, `'+'` or `'-' → 1`, anything else `→ 0`. |
| `convert(string exp, bool revMode)` | Core Shunting-Yard loop used by both `infixToPostfix` (`revMode = false`) and `infixToPrefix` (`revMode = true`). |
| `infixToPrefix(string exp)` | Reverses `exp`, swaps `'(' ↔ ')'`, calls `convert(exp, true)`, and reverses the output. |
| `main()` | `do-while` menu offering `1.Push`, `2.Pop`, `3.Display`, `4.Convert Infix`, `0.Exit`. |

---

## 6. Step-by-Step Dry Run — `A*(B+C)-D`

### Infix → Postfix (`convert("A*(B+C)-D", false)`)

| Read `c` | Rule Triggered | Stack (bottom → top) | Output `res` |
|---|---|---|---|
| `A` | Operand → output | *(empty)* | `A` |
| `*` | Operator → push | `*` | `A` |
| `(` | Open bracket → push | `* (` | `A` |
| `B` | Operand → output | `* (` | `AB` |
| `+` | Operator over `(` → push | `* ( +` | `AB` |
| `C` | Operand → output | `* ( +` | `ABC` |
| `)` | Pop until `(`, discard `(` | `*` | `ABC+` |
| `-` | `prec('*') > prec('-')` → pop `*`, push `-` | `-` | `ABC+*` |
| `D` | Operand → output | `-` | `ABC+*D` |
| End | Pop remaining stack | *(empty)* | **`ABC+*D-`** |

### Infix → Prefix on `A*(B+C)-D`
1. Reverse: `D-)C+B(*A`
2. Swap brackets: `D-(C+B)*A`
3. `convert("D-(C+B)*A", true)` → `DCB+A*-`
4. Reverse result → **`-*A+BCD`**

---

## 7. Time & Space Complexity Fact Sheet

| Operation / Function | Time Complexity | Auxiliary Space Complexity | Reason |
|---|---|---|---|
| **`push(x)`** | **O(1)** | O(1) per node | Updates head pointer `top` directly. |
| **`pop()`** | **O(1)** | O(1) | Unlinks and `delete`s head node `top`. |
| **`peek()` / `isEmpty()`** | **O(1)** | O(1) | Reads `top` directly. |
| **`display()`** | **O(n)** | O(1) | Visits all `n` nodes in the stack. |
| **`infixToPostfix(exp)`** | **O(n)** | **O(n)** | Single pass over `n` chars; each char pushed & popped at most once. |
| **`infixToPrefix(exp)`** | **O(n)** | **O(n)** | `O(n)` reverse + `O(n)` `convert` + `O(n)` reverse = **O(n)**. |

---

## 8. Important Exam Points & Common Mistakes

- **Mistake 1 — Writing `top = nn;` BEFORE `nn->next = top;` in `push`:** Loses the pointer to the rest of the linked list!
- **Mistake 2 — Forgetting `delete temp;` in `pop`:** Causes a **memory leak** on the heap.
- **Mistake 3 — Not checking `isEmpty()` in `pop` / `peek`:** Dereferencing `NULL` crashes with a Segmentation Fault.
- **Mistake 4 — Popping equal `^` in Postfix:** `A^B^C` must convert to `ABC^^` (`A^(B^C)`), NOT `AB^C^`.
- **Mistake 5 — Forgetting to swap `(` and `)` after reversing in `infixToPrefix`.**

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | What are the full forms of ADT, LIFO, and RPN? | **ADT:** Abstract Data Type. **LIFO:** Last In, First Out. **RPN:** Reverse Polish Notation (Postfix). |
| 2 | Define a Stack. | A Stack is a linear data structure following **LIFO (Last In, First Out)** where both insertion (`push`) and deletion (`pop`) happen at a single end called `top`. |
| 3 | State the time complexity of `push`, `pop`, and `peek` in a linked-list stack. | All three take **O(1)** constant time. |
| 4 | What is the advantage of a linked-list Stack over an array-based Stack? | Dynamic size — it has no fixed maximum capacity limit and allocates/frees exact memory as needed without wasting space or overflowing prematurely. |
| 5 | What are Stack Overflow and Stack Underflow? | **Overflow:** pushing onto a full stack (out of memory). **Underflow:** popping or peeking from an empty stack (`top == NULL`). |
| 6 | Define Infix, Postfix, and Prefix notations with an example for `A + B`. | **Infix:** operator between operands (`A + B`). **Postfix:** operator after operands (`A B +`). **Prefix:** operator before operands (`+ A B`). |
| 7 | Why do compilers prefer Postfix/Prefix over Infix? | Postfix and Prefix need **no parentheses and no precedence checks**, allowing fast single-pass evaluation with a stack in `O(n)` time. |
| 8 | State the precedence and associativity of `^`, `*`, `/`, `+`, `-`. | Precedence: `^` (highest, 3) > `*`, `/` (2) > `+`, `-` (lowest, 1). Associativity: `^` is **Right-to-Left**; `*`, `/`, `+`, `-` are **Left-to-Right**. |
| 9 | Convert `A + B * C` to Postfix and Prefix. | Postfix: **`ABC*+`**. Prefix: **`+A*BC`**. |
| 10 | State the time and space complexity of Infix-to-Postfix and Infix-to-Prefix conversion. | **O(n)** time complexity and **O(n)** space complexity (for an expression of length `n`). |
| 11 | Why do we call `delete temp;` inside `pop()`? | Because `new Node` allocates memory dynamically on the heap; `delete temp` frees that memory back to the OS to avoid a memory leak. |
| 12 | List four applications/uses of a Stack. | (1) Expression conversion & evaluation, (2) function call / recursion stack, (3) Undo/Redo in editors, and (4) balanced bracket checking. |
