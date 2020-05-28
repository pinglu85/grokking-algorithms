my_list = [1, 4, 8, 9, 10, 23, 40]


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


result = binary_search(my_list, 4)
print(result)
