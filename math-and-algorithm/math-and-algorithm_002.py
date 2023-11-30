# 002 Sum of 3 Integers
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_b

import io
import sys

_INPUT = """\

"""

sys.stdin = io.StringIO(_INPUT)

A1, A2, A3 = map(int, input().split())
print(A1+A2+A3)