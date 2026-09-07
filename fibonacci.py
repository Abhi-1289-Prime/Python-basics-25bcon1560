n = 10
a = 0
b = 1

for _ in range(n):
    print(a, end=" ")
    next_val = a + b
    a = b
    b = next_val