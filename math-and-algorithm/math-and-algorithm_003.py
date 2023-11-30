# 003 Sum of N Integers
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_c

import io
import sys

_INPUT = """\
5
3 1 4 1 5
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
print(sum(A))