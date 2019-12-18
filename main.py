from random import random
import time
import math
from copy import deepcopy
from algorithms.selection_sort import selection_sort
from algorithms.bubble_sort import bubble_sort_recurse, bubble_sort
from algorithms.insertion_sort import insertion_sort, recursive_insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort, quick_sort_top_down


def sort(lst, direct="asc"):
    quick_sort_top_down(lst, 0, len(lst) - 1, direct)
    # merge_sort(lst, direct)


def make_lst():
    return [math.floor(random() * 1000000) for i in range(1000000)]


def check_sorted(lst, direct="asc"):
    is_sorted = True
    for i in range(len(lst) - 1):
        if direct == "asc":
            if lst[i] > lst[i + 1]:
                is_sorted = False
                break
        elif direct == "desc":
            if lst[i] < lst[i + 1]:
                is_sorted = False
                break

    return is_sorted


def test_asc(lst):
    print("============ASC================")
    start_time = time.time()
    sort(lst, "asc")
    end_time = time.time()
    is_sorted = check_sorted(lst, "asc")
    print(lst)
    print(is_sorted)
    print(f"Sort execution time {end_time - start_time}")


def test_desc(lst):
    print("===========DESC===============")
    start_time = time.time()
    sort(lst, "desc")
    end_time = time.time()
    is_sorted = check_sorted(lst, "desc")
    print(lst)
    print(is_sorted)
    print(f"Sort execution time {end_time - start_time}")


def main():
    test_asc(make_lst())
    test_desc(make_lst())


if __name__ == "__main__":
    main()
