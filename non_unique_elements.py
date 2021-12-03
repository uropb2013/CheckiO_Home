def checkio(data: list) -> list:
    for i in range(len(data)-1, -1, -1):
        if data.count(data[i]) == 1:
            data.pop(i)
    return data


if __name__ == "__main__":
    print(list(checkio([1, 2, 3, 1, 3])))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")