def bigger_price(limit: int, data: list):
    # your code here
    top_prices = []
    for i in range(0, limit):
        max_price = 0
        val = 0
        m_val = 0
        for b in data:
            if b["price"] > max_price:
                max_price = b["price"]
                m_val = val
            val += 1
        top_prices.append(data[m_val])
        del (data[m_val])
    return top_prices


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')