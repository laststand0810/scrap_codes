def partition(sort_list, low, high):
    pivot_pos = low
    for i in range(low, high-1):
        if sort_list[i] < sort_list[high-1]:
            sort_list[pivot_pos], sort_list[i] = sort_list[i], sort_list[pivot_pos]
            pivot_pos += 1
    sort_list[pivot_pos], sort_list[high-1] = sort_list[high-1], sort_list[pivot_pos]
    return pivot_pos


def quick_sort(sort_list, low, high):
    if low < high:
        pivot = partition(sort_list, low, high)
        quick_sort(sort_list, low, pivot - 1)
        quick_sort(sort_list, pivot + 1, high)


test_list = ["dafghaer", "argrgargbae", "1111111111", "num", "qq", "w", "erre", "sdfag"]
quick_sort(test_list, 0, len(test_list))
print(test_list)