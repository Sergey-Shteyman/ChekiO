line = input()
n = 2
new_list = []
for i in range(0, len(line), n):
    element = line[i:i + n]
    if len(element) == 1:
        new_list.append(element + '_')
    else:
        new_list.append(element)

print(new_list)


