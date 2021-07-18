num = int(input())
counter = 0
if num == 0:
    print(1)
if num != 0 and num < 10:
    print(0)

else:
    while num != 0:
        if num % 10 == 0:
            counter += 1
        num //= 10
        if num % 10 != 0:
            break
    print(counter)
