# 4.1 Sum all the numbers in a list with recursion
def sum_list(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_list(list[1:])


print(sum_list([2, 4, 6]))


# 4.2 Count the number of items in a list with recursion
def count_list(list):
    if len(list) == 0:
        return 0
    else:
        return 1 + count_list(list[1:])


print(count_list([2, 4, 6, 8, 7]))


# 4.3 Find the maximum number in a list with recursion
def find_max(list, max=0):
    if len(list) == 0:
        return max
    else:
        if list[0] > max:
            max = list[0]
        return find_max(list[1:], max)


print(find_max([2, 6, 4]))


# 4.4 Recursive binary search
def binary_search(list, target, offset=0):
    mid = (0 + len(list) - 1) // 2
    if list[mid] == target:
        return mid + offset
    else:
        start = 0
        end = len(list)
        if list[mid] < target:
            start = mid + 1
            offset = offset + mid + 1
        elif list[mid] > target:
            end = mid
        return binary_search(list[start:end], target, offset)


print(binary_search([1, 4, 8, 10, 99, 100, 110], 99))  # 4
print(binary_search([1, 4, 8, 10, 99, 100, 110], 1))  # 0
print(binary_search([1, 4, 8, 10, 99, 100, 110], 100))  # 5
print(binary_search([1, 4, 8, 10, 99, 100, 110], 110))  # 6
print(binary_search([1, 4, 8, 10, 99, 100, 110], 4))  # 1
print(binary_search([1, 4, 8, 10, 99, 100, 110], 8))  # 2
print(binary_search([1, 4, 8, 10, 99, 100, 110], 10))  # 3
