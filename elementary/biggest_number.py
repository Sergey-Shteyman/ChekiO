def f(num):
    m = 0
    for n in str(num):
        if int(n) > m:
            m = int(n)
    return m

num = int(input())
print(f(num))