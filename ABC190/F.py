# Binary Indexed Tree (BIT)を利用する
# BITのindexが0始まりなことに工夫が必要

import copy

N = int(input())
A = list(map(int, input().split()))

BIT = [0]*(N+1)

def get(x):
    ans = 0
    while x > 0:
        ans += BIT[x]
        x -= x & -x
    return ans

def add(x, val):
    x += 1
    while x <= N:
        BIT[x] += val
        x += x & -x
    
ans = 0
for x in reversed(A):
    ans += get(x)
    add(x, 1)

for x in A:
    print(ans)
    ans += N - 1 - 2*x