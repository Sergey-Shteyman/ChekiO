def between_markers(text: str, begin: str, end: str) -> str:
    if (end not in text) and (begin not in text):
        return text
    elif begin not in text:
        return text[:text.find(end)]
    elif end not in text:
        return text[text.find(begin) + len(begin):]
    elif abs(text.index(begin) > text.index(end)):
        return ''
    else:
        return text[text.find(begin) + len(begin):text.find(end)]

print(between_markers('What is >apple<', '>', '<'))