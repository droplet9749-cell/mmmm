n = int(input())
if n % 4 == 0:
    n = n // 4
    a = "long " * n + "int"
    print(a)