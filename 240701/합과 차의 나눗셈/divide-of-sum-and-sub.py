a, b = map(int, input().split())

c = (a+b) / (a-b)
c = round(c, 2)

print(f"{c:.2f}")