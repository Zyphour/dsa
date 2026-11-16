# Practical 2 — Stack as an ADT (Linked List) + Infix → Postfix / Prefix

**Aim:** Implement a stack as an abstract data type using a singly linked list,
and use it to convert an infix expression into postfix and prefix form.

**Language:** C++ · **Program:** [`stack_conversions.cpp`](stack_conversions.cpp)

---

## Concepts

**Stack** – a LIFO list: the last element pushed is the first popped. The ADT is
defined by its operations, not by how it is stored.

| Operation | Work | Time |
|---|---|---|
| `push(x)` | add on top | O(1) |
| `pop()` | remove the top | O(1) |
| `peek()` | read the top | O(1) |
| `isEmpty()` | check | O(1) |

**Why a linked list?** No fixed size and no shifting: `push` adds a node at the
front, `pop` unlinks the front node. An array stack would need a maximum size or
a growing array.

## Expression forms

| Form | Example | Operator position |
|---|---|---|
| Infix | `A + B * C` | between operands (with precedence and brackets) |
| Postfix | `A B C * +` | after the operands |
| Prefix | `+ A * B C` | before the operands |

Postfix and prefix need **no brackets and no precedence rules** — the position of
each operator already decides the order of evaluation. That is why compilers and
calculators convert first.

Precedence: `^` > `* /` > `+ -`. Associativity: `+ - * /` left to right,
`^` right to left (`A^B^C` = `A^(B^C)`).

## Infix → postfix (shunting yard)

Scan left to right:

1. **Operand** → send it straight to the output.
2. **`(`** → push it.
3. **`)`** → pop to the output until `(` is found; discard the `(`.
4. **Operator** → pop operators of higher or equal precedence, then push it
   (an equal `^` is *not* popped, because `^` is right associative).
5. **End** → pop whatever is left.

`(A+B)*C-D` → `AB+C*D-`

## Infix → prefix

1. Reverse the expression and swap `(` with `)`.
2. Convert that to postfix.
3. Reverse the result.

`A+B*C` → `C*B+A` → `CB*A+` → `+A*BC`

**Careful:** reversing flips the associativity of every operator, so when the
reversed string is converted, equal precedence must be handled the opposite way.
Without that, `A*(B+C)/D` gives `*A/+BCD` instead of `/*A+BCD`.

## Complexity

Conversion is one pass over `n` characters → **O(n)** time, **O(n)** stack space.
Every stack operation is `O(1)`.

## Exam points

- `pop` on an empty stack must be checked (otherwise undefined behaviour).
- Every node removed from the list must be `delete`d — otherwise a memory leak.
- `^` is the only right-associative operator here.
- Stack uses: expression conversion and evaluation, function calls, undo,
  bracket matching, DFS, backtracking.
