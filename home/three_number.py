def three_number(line):
    counter = 0
    if len(line) > 4:
        for i in range(len(line) - 4):
            if line[i].isdigit() and line[i + 1] == ' ' and line[i + 3] == ' ' and line[i + 2].isdigit() and line[i + 4].isdigit():
                return True
            else:
                return False
    else:
        return False

print(three_number("123 apple 2 2 3"))
