def selection_sort(arr):
    for i in range(len(arr)):
        lowest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j
        # swap
        if i != lowest:
            temp = arr[lowest]
            arr[lowest] = arr[i]
            arr[i] = temp
    return arr


print(selection_sort([5, 3, 6, 2, 10]))
