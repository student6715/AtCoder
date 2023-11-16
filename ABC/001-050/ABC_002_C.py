# ABC_002_C 直訴
# https://atcoder.jp/contests/abc002/tasks/abc002_3

import io
import sys

_INPUT = """\
298 520 903 520 4 663
"""

sys.stdin = io.StringIO(_INPUT)

x1, y1, x2, y2, x3, y3 = map(int, input().split())
area = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
print(area)