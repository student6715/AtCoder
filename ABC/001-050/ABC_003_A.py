# ABC_003_A AtCoder社の給料
# https://atcoder.jp/contests/abc003/tasks/abc003_1

import io
import sys

_INPUT = """\
91
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
ans = 0
for i in range(1, N+1):
    ans += 10000 * i / N
print(ans)