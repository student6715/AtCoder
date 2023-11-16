# ABC_002_A 正直者
# https://atcoder.jp/contests/abc002/tasks/abc002_1

import io
import sys

_INPUT = """\
10 11
"""

sys.stdin = io.StringIO(_INPUT)

X, Y = map(int, input().split())
print(max(X, Y))