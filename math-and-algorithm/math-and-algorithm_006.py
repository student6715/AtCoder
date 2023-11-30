# 006 Print 2N+3
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_f

import io
import sys

_INPUT = """\
2 8 8
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
print(2*N+3)