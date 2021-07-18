def universal(fakam):
    temp = []
    for i in fakam:
        if fakam.count(i) > 1:
            temp.append(i)
    return temp

print(universal([5, 5, 5, 5]))
