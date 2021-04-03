N = int(input())
AB_sum = []
s = 10**6
a_min, a_pre_min = (s, s), (s, s)
b_min, b_pre_min = (s, s), (s, s)
for n in range(N):
    a, b = map(int, input().split())
    if a_min[1] >= a:
        a_pre_min = a_min
        a_min = (n, a)
    if b_min[1] >= b:
        b_pre_min = b_min
        b_min = (n, b)
    AB_sum.append(a+b)
AB_min = min(AB_sum)
if a_min[0] == b_min[0]:
    print(min([max([a_min[1], b_pre_min[1]]), max(a_pre_min[1], b_min[1]), AB_min]))
else:
    print(min([max([a_min[1], b_min[1]]), AB_min]))
