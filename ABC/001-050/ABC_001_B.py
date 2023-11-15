# ABC_001_B 視程の通報
# https://atcoder.jp/contests/abc001/tasks/abc001_2

import io
import sys

_INPUT = """\
200
"""

sys.stdin = io.StringIO(_INPUT)

m = int(input()) / 1000
if m < 0.1:
    print('{0:02d}'.format(0))
elif m >= 0.1 and m <= 5:
    print('{0:02d}'.format(int(m * 10)))
elif m >= 0.6 and m <= 30:
    print('{0:02d}'.format(int(m + 50)))
elif m >= 35 and m <= 70:
    print(int((m - 30)/5 + 80))
else:
    print(89)