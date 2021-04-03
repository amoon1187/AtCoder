X = input()
M = int(input())

n = max([int(c) for c in X]) + 1
ans = 0
while True:
    try:
        if int(X, n)>M:
            break
        else:
            n += 1
            ans += 1
    except:
        break
print(ans)