def is_decreasing(seq):
    decreasing = True
    for i in range(len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            decreasing = False

    return decreasing
