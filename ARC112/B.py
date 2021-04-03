B, C = map(int, input().split())
ans = 0
if C <= abs(B*2):
    ans = C+1
if abs(4*B+1) < C:
    ans = B*2+1 + C-(4*B+1)
print(ans)