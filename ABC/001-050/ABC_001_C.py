# ABC_001_C 風力観測
# https://atcoder.jp/contests/abc001/tasks/abc001_3

import io
import sys

_INPUT = """\
2750 628
"""

sys.stdin = io.StringIO(_INPUT)

def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p

Deg, Dis = map(int, input().split())

DIR = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
       'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']

if Deg < 112.5 or Deg >= 3487.5:
    Dir = 'N'
else:
    Dir = DIR[int((Deg - 112.5) // 225)+1]

Dis = my_round(Dis/60, 1)
if Dis <= 0.2:
    W = 0
    Dir = 'C'
elif Dis <=  1.5: W = 1
elif Dis <=  3.3: W = 2
elif Dis <=  5.4: W = 3
elif Dis <=  7.9: W = 4
elif Dis <= 10.7: W = 5
elif Dis <= 13.8: W = 6
elif Dis <= 17.1: W = 7
elif Dis <= 20.7: W = 8
elif Dis <= 24.4: W = 9
elif Dis <= 28.4: W = 10
elif Dis <= 32.6: W = 11
else: W = 12

print(Dir, W)