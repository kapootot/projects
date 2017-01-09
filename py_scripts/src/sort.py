
a = [7, 1, 3, 5, 2, 8]

# a = [1, 7, 3, 5, 2, 8]

def my_sort(arr):
    min_val = arr[0]
    max_val = [arr[len(arr)]-1]
    i = 0

    while i < len(a):
        if a[i] < min_val:
            a[a.index(min_val)] = a[i]
            a[i]