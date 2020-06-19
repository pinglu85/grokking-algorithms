# 4.1 Sum all the numbers in a list with recursion
def sum_list(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_list(list[1:])


print(sum_list([2, 4, 6]))


# 4.2 Count the number of items in a list with recursion
def count_list(list):
    if list == []:
        return 0
    else:
        return 1 + count_list(list[1:])


print(count_list([2, 4, 6, 8, 7]))


# 4.3 Find the maximum number in a list with recursion
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print(max([2, 5, 4]))


# 4.4 Recursive binary search
def binary_search(list, target, offset=0):
    if len(list) == 1:
        return offset if list[0] == target else None
    else:
        start = 0
        end = len(list)
        mid = (start + end - 1) // 2
        if list[mid] == target:
            return mid + offset
        elif list[mid] < target:
            start = mid + 1
            offset += start
        else:
            end = mid
        return binary_search(list[start:end], target, offset)


print(binary_search([1, 4, 8, 10, 99, 100, 110], 99))  # 4
print(binary_search([1, 4, 8, 10, 99, 100, 110], 1))  # 0
print(binary_search([1, 4, 8, 10, 99, 100, 110], 100))  # 5
print(binary_search([1, 4, 8, 10, 99, 100, 110], 110))  # 6
print(binary_search([1, 4, 8, 10, 99, 100, 110], 4))  # 1
print(binary_search([1, 4, 8, 10, 99, 100, 110], 8))  # 2
print(binary_search([1, 4, 8, 10, 99, 100, 110], 10))  # 3
print(binary_search([1, 4, 8, 10, 99, 100, 110], 11))  # None
print(binary_search([1, 4, 8, 9, 10, 12, 50, 99, 100, 110], 99))  # 7
print(binary_search([1, 4, 8, 9, 10, 12, 50, 99, 100, 110], 8))  # 2
print(binary_search([1, 4, 8, 9, 10, 12, 50, 99, 100, 110], 110))  # 9
