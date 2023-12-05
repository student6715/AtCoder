# ABC_003_B AtCoderトランプ
# https://atcoder.jp/contests/abc003/tasks/abc003_2

import io
import sys

_INPUT = """\
arc
abc
"""

sys.stdin = io.StringIO(_INPUT)

S = input()
T = input()

flag = True

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    elif S[i] == '@' and T[i] in 'atcoder':
        continue
    elif S[i] in 'atcoder' and T[i] == '@':
        continue
    else:
        flag = False
        break

if flag: print('You can win')
else: print('You will lose')
