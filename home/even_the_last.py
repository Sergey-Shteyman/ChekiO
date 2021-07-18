array = []
summ = 0
if len(array) == 0:
    print(array)
else:
    for i in array[::2]:
        summ += i
    print(summ * array[-1])
