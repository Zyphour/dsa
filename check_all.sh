#!/usr/bin/env bash

set -u
ok=0
fail=0

echo "== Part A (C++) =="
for src in part_a_cpp/*/*.cpp; do
    name=$(basename "$src" .cpp)
    if g++ -Wall -O2 "$src" -o "/tmp/$name" 2>/tmp/build.log; then
        echo "  OK   $src"
        ok=$((ok + 1))
    else
        echo "  FAIL $src"
        cat /tmp/build.log
        fail=$((fail + 1))
    fi
done

echo "== Part B (Python) =="
for src in part_b_python/*/*.py; do
    if python3 -m py_compile "$src" 2>/tmp/build.log; then
        echo "  OK   $src"
        ok=$((ok + 1))
    else
        echo "  FAIL $src"
        cat /tmp/build.log
        fail=$((fail + 1))
    fi
done

find . -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null

echo
echo "passed: $ok   failed: $fail"
