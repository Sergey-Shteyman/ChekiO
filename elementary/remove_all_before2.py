def remove_all_before(items: list, border: int):
    if border not in items:
        return items
    else:
        return items[items.index(border):]


print(list(remove_all_before([1, 2, 3, 4, 5], 3)))