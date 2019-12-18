def selection_sort(lst, direct):
    for i in range(len(lst) - 1):
        index = i
        for j in range(i + 1, len(lst)):
            if direct == "desc":
                if lst[index] < lst[j]:
                    index = j
            elif direct == "asc":
                if lst[index] > lst[j]:
                    index = j
        lst[i], lst[index] = lst[index], lst[i]
