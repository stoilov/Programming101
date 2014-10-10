def calculate_coins(sum):
    hundreds, fifties, twenties, tens, fives, twos, ones = 0, 0, 0, 0, 0, 0, 0
    my_sum = 0
    coins = [100, 50, 20, 10, 5, 2, 1]
    sum *= 100
    difference = sum - my_sum
    while difference > 0:
        if difference >= 100:
            while difference >= 100:
                my_sum += 100
                hundreds += 1
                difference = sum - my_sum
        elif difference >= 50:
            while difference >= 50:
                my_sum += 50
                fifties += 1
                difference = sum - my_sum
        elif difference >= 20:
            while difference >= 20:
                my_sum += 20
                twenties += 1
                difference = sum - my_sum
        elif difference >= 10:
            while difference >= 10:
                my_sum += 10
                tens += 1
                difference = sum - my_sum
        elif difference >= 5:
            while difference >= 5:
                my_sum += 5
                fives += 1
                difference = sum - my_sum
        elif difference >= 2:
            while difference >= 2:
                my_sum += 2
                twos += 1
                difference = sum - my_sum
        else:
            while difference >= 1:
                my_sum += 1
                ones += 1
                difference = sum - my_sum

    result = {
    1: ones,
    2: twos,
    100: hundreds,
    5: fives,
    10: tens,
    50: fifties,
    20: twenties
    }

    return result
