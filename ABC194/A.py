A, B = map(int, input().split())
AB = A + B
if AB >= 15 and B >= 8:
    print(1)
elif AB >= 10 and B >= 3:
    print(2)
elif AB >= 3:
    print(3)
else:
    print(4)