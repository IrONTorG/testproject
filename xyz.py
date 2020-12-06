n = int(input("задайте N:"))
for i in range(1, n):
    d = 1
    while i >= d:
        d = d * 10
        if (i % d) == i:
            print("число", i, "квадрат", i * i)
