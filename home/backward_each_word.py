def backward_string_by_word(text: str) -> str:
    if len(text) == 0:
        return text
    else:
        string = list(i[::-1] for i in text.split(' '))
        return ' '.join(string)


print(backward_string_by_word('hello world'))