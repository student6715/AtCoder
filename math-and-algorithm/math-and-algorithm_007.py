# 007 Number of Multiples 1
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_g

import io
import sys

_INPUT = """\
1000000 11 13
"""

sys.stdin = io.StringIO(_INPUT)

N, X, Y = map(int, input().split())
ans = 0
for i in range(1, N+1):
    if i % X == 0 or i % Y == 0:
        ans += 1
print(ans)
