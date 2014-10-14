def number_to_list(n):
    n = list(str(n))
    for i in range(len(n)):
       n[i] = int(n[i])

    return n
