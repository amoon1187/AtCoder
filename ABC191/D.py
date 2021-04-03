# 解答は得られるが、タイムアウトする。

import math

X, Y, R = map(float, input().split())
r_2 = R**2
x_ls = [x-X for x in range(int(X-R), int(X+R)+1)]
count = 0
for x in x_ls:
    h = int(math.sqrt(r_2-x**2))
    for y in range(int(-h+Y), int(h+Y+1)):
        count += 1
print(count)
