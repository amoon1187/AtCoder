import itertools

N, X = map(int, input().split())
A  = list(map(int, input().split()))

ans = -1
for k in range(len(A), 0, -1):
    for s in sorted(itertools.combinations(A, k), key=lambda x: sum(x), reverse=True):
        a = X-sum(s)
        if a%k == 0:
            ans = a//k
            break
    else:
        continue
    break
print(ans)