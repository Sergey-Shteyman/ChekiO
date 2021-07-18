from pprint import pprint


def bigger_price(limit: int, data: list) -> list:
    return sorted(data, key=lambda x: x["price"], reverse=True)[:limit]


print(pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ])))