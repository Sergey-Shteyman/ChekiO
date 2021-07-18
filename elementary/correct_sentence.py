text = "greetings, friends"
if '.' not in text:
    text = text + '.'
b = text[0]
char_upper = b.upper()
text = list(text)
del text[0]
text.insert(0, char_upper)
print(''.join(text))


