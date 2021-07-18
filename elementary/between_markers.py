text = input()
begin = input()
end = input()
print(text[text.find(begin) + 1:text.rfind(end)])
