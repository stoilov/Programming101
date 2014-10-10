def biggest_difference(arr):
    a = max(arr)
    b = min(arr)
    if arr.index(a) >= arr.index(b):
        return b - a
    else:
        return a - b
