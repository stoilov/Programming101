def is_increasing(seq):
    increasing = True
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            increasing = False

    return increasing
