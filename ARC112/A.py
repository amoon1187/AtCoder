from itertools import product

T = int(input())
L_R = []

for t in range(T):
    l, r = map(int, input().split())
    L_R.append(list(range(l, r+1)))

for t in range(T):
    count = 0
    for (a, b, c) in product(L_R[t], repeat=3):
        if a - b - c == 0:
            count += 1
    print(count)
