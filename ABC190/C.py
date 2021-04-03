import itertools 

N, M = map(int, input().split())
rule = []
for m in range(1, M+1):
    a, b = map(int, input().split())
    rule.append((a, b))
K = int(input())
dish = []
for k in range(1, K+1):
    c, d = map(int, input().split())
    dish.append((c, d))
ans = 0
for balls in itertools.product(*dish):
    balls = set(balls)
    count = 0
    for a, b in rule:
        if a in balls and b in balls:
            count +=1
    if ans < count:
        ans = count
print(ans)
            

