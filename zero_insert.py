from list_to_number import list_to_number

def zero_insert(n):
    n = list(str(n))
    m = []
    for i in range(len(n) - 1):
        m.append(n[i])
        if n[i] == n[i + 1] or (int(n[i]) + int(n[i + 1])) % 10 == 0:
            m.append(0)

    m.append(n[len(n) - 1])
    return list_to_number(m)
