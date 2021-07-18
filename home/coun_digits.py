def count_digits(text: str):
    counter = 0
    for i in text:
        if i.isdigit():
            counter += 1
    return counter


print(count_digits(''))