# ABC_002_B 罠
# https://atcoder.jp/contests/abc002/tasks/abc002_2

import io
import sys

_INPUT = """\
mazushii
"""

sys.stdin = io.StringIO(_INPUT)

W = input()
N = ''
vowels = ['a', 'e', 'i', 'o', 'u']
for c in W:
    if c in vowels:
        continue
    else:
        N += c
print(N)
