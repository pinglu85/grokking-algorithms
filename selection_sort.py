def find_largest(arr):
    largest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        largest = find_largest(arr)
        sorted_arr.append(arr.pop(largest))
    return sorted_arr


print(selection_sort([5, 3, 6, 2, 10]))
