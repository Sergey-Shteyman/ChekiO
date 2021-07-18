def second_index(text: str, symbol: str):
    if text.count(symbol) < 2:
        return None
    first_symbol = text.find(symbol)
    return text.find(symbol, first_symbol + 1)


print(second_index("find the river", "e"))