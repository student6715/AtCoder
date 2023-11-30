# 005 Modulo 100
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_e

import io
import sys

_INPUT = """\
10
1 2 3 4 5 6 7 8 9 10
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
print(sum(A)%100)