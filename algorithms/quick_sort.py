def quick_sort(lst, left_pivot, right_pivot, direct):
    if left_pivot < right_pivot:
        p = partition(lst, left_pivot, right_pivot, direct)
        quick_sort(lst, left_pivot, p, direct)
        quick_sort(lst, p + 1, right_pivot, direct)


def partition(lst, left_pivot, right_pivot, direct):
    pivot = lst[left_pivot]
    j = left_pivot
    for i in range(left_pivot + 1, right_pivot + 1):
        if direct == "asc":
            if lst[i] < pivot:
                lst[j + 1], lst[i] = lst[i], lst[j + 1]
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                j += 1
        elif direct == "desc":
            if lst[i] > pivot:
                lst[j + 1], lst[i] = lst[i], lst[j + 1]
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                j += 1
    return j


def quick_sort_top_down(lst, left_pivot, right_pivot, direct):
    if left_pivot < right_pivot:
        p = partition(lst, left_pivot, right_pivot, direct)
        quick_sort_top_down(lst, left_pivot, p - 1, direct)
        quick_sort_top_down(lst, p + 1, right_pivot, direct)


def partition_top_down(lst, left_pivot, right_pivot, direct):
    pivot = lst[right_pivot]
    j = right_pivot
    for i in reversed(range(left_pivot, right_pivot)):
        if direct == "asc":
            if lst[i] > pivot:
                lst[j - 1], lst[i] = lst[i], lst[j - 1]
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
                j -= 1
        elif direct == "desc":
            if lst[i] < pivot:
                lst[j - 1], lst[i] = lst[i], lst[j - 1]
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
                j -= 1

    return j
