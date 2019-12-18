import math


def merge_sort(lst, direct):
    if len(lst) == 1:
        return lst

    middle = len(lst) // 2
    left = merge_sort(lst[:middle], direct)
    right = merge_sort(lst[middle:], direct)

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if direct == "asc":
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
                k += 1
            else:
                lst[k] = right[j]
                j = j + 1
                k += 1
        elif direct == "desc":
            if left[i] > right[j]:
                lst[k] = left[i]
                i += 1
                k += 1
            else:
                lst[k] = right[j]
                j = j + 1
                k += 1

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1

    return lst
