H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(list(input().split())[0])

def check(i, j):
    count = 0
    if S[i][j] == '#':
        count += 1
    if S[i][j-1] == '#':
        count += 1
    if S[i-1][j] == '#':
        count += 1
    if S[i-1][j-1] == '#':
        count += 1
    return count

tyoten = 0
for i in range(1, H):
    for j in range(1, W):
        p = check(i, j)
        if p%2 == 1:
            tyoten += 1
print(tyoten)
