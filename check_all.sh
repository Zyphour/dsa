#!/usr/bin/env bash

set -u
ok=0
fail=0
log=$(mktemp)
trap 'rm -f "$log"' EXIT

echo "== C++ =="
for src in [0-9][0-9]-*/*.cpp; do
    name=$(basename "$src" .cpp)
    if g++ -Wall -O2 "$src" -o "/tmp/$name" 2>"$log"; then
        echo "  OK   $src"
        ok=$((ok + 1))
    else
        echo "  FAIL $src"
        cat "$log"
        fail=$((fail + 1))
    fi
done

echo "== Python =="
for src in [0-9][0-9]-*/*.py; do
    if python3 -m py_compile "$src" 2>"$log"; then
        echo "  OK   $src"
        ok=$((ok + 1))
    else
        echo "  FAIL $src"
        cat "$log"
        fail=$((fail + 1))
    fi
done

find . -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null

echo
echo "passed: $ok   failed: $fail"
exit $((fail > 0 ? 1 : 0))
