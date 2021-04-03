import re

S = input()
def c_small(c):
    if re.match(r'[a-z]', c):
        return True
    else:
        return False

def c_big(c):
    if re.match(r'[A-Z]', c):
        return True
    else:
        return False

ans = []
for idx, c in enumerate(S):
    if idx%2 == 1:
        ans.append(c_big(c))
    else:
        ans.append(c_small(c))

if sum(ans)==len(S):
    print("Yes")
else:
    print("No")