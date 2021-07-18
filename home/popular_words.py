def popular_words(text: str, words: list):
    '''
Возвращает словарь с частотой заданных элементов
    :param text: строка в которой нужно найти и т. д.
    :param words: слова которые ищем
    '''
    text = text.lower().split()
    dict_one = {}
    for i in words:
        dict_one[i] = text.count(i)
    return dict_one


print(popular_words('''
    When I was One
    I had just begun
    When I was Two
    I was nearly new
    ''', ['i', 'was', 'three', 'near']))