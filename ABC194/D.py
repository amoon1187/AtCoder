N = int(input())
total = 0
for i in range(1, 10000):
    total += i*((N-1)/N)**i * ((N-2)/N)**i
print(total)