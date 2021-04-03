V, T, S, D = map(int, input().split())
if T <= D/V and D/V <= S:
    print("No")
else:
    print("Yes")