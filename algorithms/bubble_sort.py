def bubble_sort(lst, direct):
    for i in range(len(lst) - 1):
        is_sorted = True
        for j in range(len(lst) - 1 - i):
            if direct == "asc":
                if lst[j] > lst[j + 1]:
                    is_sorted = False
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
            if direct == "desc":
                if lst[j] < lst[j + 1]:
                    is_sorted = False
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if is_sorted:
            break


def bubble_sort_recurse(lst, n, direct):
    if n == 1:
        return

    is_sorted = True
    for j in range(n - 1):
        if direct == "asc":
            if lst[j] > lst[j + 1]:
                is_sorted = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if direct == "desc":
            if lst[j] < lst[j + 1]:
                is_sorted = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    if is_sorted:
        return

    bubble_sort_recurse(lst, n - 1, direct)
