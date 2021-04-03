N, K = map(int, input().split())
def f(x):
    x_ls = [int(c) for c in str(x)]
    x_ls_down = int(''.join([str(c) for c in sorted(x_ls, reverse=True)]))
    x_ls_up = int(''.join([str(c) for c in sorted(x_ls)]))
    return x_ls_down - x_ls_up

a = N
for k in range(K):
    a = f(a)

print(a)