number = "0"
number = list(number)
summ = 0
if number.count('0') == len(number):
    print(number.count('0'))
else:
    for i in number:
        if i == '0':
            summ += 1
        elif i in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            print(summ)
            exit()

