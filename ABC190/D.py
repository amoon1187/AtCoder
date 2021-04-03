N = int(input())
def div(n):
    lower_div, upper_div = [] , []
    i = 1
    while i*i <= n:
        if n%i == 0:
            lower_div.append(i)
            if i != n//i:
                upper_div.append(n//i)
        i += 1
    return lower_div + upper_div[::-1]

def even(n):
    if n%2 == 0:
        return True
    else:
        return False

N2 = N*2
count = 0
for n in div(N2):
    if even(n) != even(N2/n):
        count += 1
print(count)