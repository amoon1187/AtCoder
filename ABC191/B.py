N, X = map(int, input().split())
A_list = list(map(int, input().split()))
for a in A_list:
    if a != X:
        print(a, end=" ")
else:
    print("")