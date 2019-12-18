def insertion_sort(lst, direct):
    for i in range(len(lst) - 1):
        j = i + 1
        key = lst[j]
        if direct == "asc":
            while lst[j - 1] > key and j > 0:
                lst[j] = lst[j - 1]
                j = j - 1
            lst[j] = key

        elif direct == "desc":
            while lst[j - 1] < key and j > 0:
                lst[j] = lst[j - 1]
                j = j - 1
            lst[j] = key


def recursive_insertion_sort(lst, n, direct):
    if n == 1:
        return

    recursive_insertion_sort(lst, n - 1, direct)

    key = lst[n - 1]
    j = n - 2
    if direct == "asc":
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = key

    elif direct == "desc":
        while j >= 0 and lst[j] < key:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = key
