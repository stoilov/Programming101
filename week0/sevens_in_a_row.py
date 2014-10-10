def sevens_in_a_row(arr, n):
    str_from_arr = "".join(map(str, arr))
    sevens = ""
    for i in range(n):
        sevens += "7"
        
    if sevens in str_from_arr:
        return True
    else:
        return False

print(sevens_in_a_row([7,2,1,6,2], 1))
