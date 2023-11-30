# 008 Brute Force 1
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_h

import io
import sys

_INPUT = """\
869 120
"""

sys.stdin = io.StringIO(_INPUT)

N, S = map(int, input().split())
count = 0
for red in range(1, N+1):
    for blue in range(1, N+1):
        if red + blue <= S:
            count += 1
print(count)