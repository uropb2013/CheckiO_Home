def split_list(items: list) -> list:
    # your code here
    list_1 = []
    list_2 = []
    if len(items) % 2:
        for i in range((len(items) // 2) + 1):
            list_1.append(items[i])
        for i in range((len(items) // 2) + 1, len(items)):
            list_2.append(items[i])
    else:
        for i in range(len(items) // 2):
            list_1.append(items[i])
        for i in range(len(items) // 2, len(items)):
            list_2.append(items[i])
    return [list_1, list_2]



if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
