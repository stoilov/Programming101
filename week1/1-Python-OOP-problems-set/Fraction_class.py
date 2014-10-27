from fractions import gcd


class Fraction:

    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    # least common multiple
    @staticmethod
    def lcm(a, b):
        absolute_value = abs(a * b)
        greatest_common_divisor = gcd(a, b)
        return absolute_value // greatest_common_divisor

    @staticmethod
    def new_nominator_fractions(a, b):
        least_cm = a.lcm(a.denominator, b.denominator)
        new_self_nominator = (least_cm // a.denominator) * a.nominator
        new_other_nominator = (least_cm // b.denominator) * b.nominator
        return (new_self_nominator, new_other_nominator)

    def __add__(self, other):
        least_cm = self.lcm(self.denominator, other.denominator)
        to_sum = self.new_nominator_fractions(self, other)
        new_nominator = to_sum[0] + to_sum[1]

        return Fraction(new_nominator, least_cm)

    def __sub__(self, other):
        least_cm = self.lcm(self.denominator, other.denominator)
        to_sub = self.new_nominator_fractions(self, other)
        new_nominator = to_sub[0] - to_sub[1]

        return Fraction(new_nominator, least_cm)

    def __lt__(self, other):
        to_sub = self.new_nominator_fractions(self, other)
        if to_sub[0] < to_sub[1]:
            return True
        return False

    def __gt__(self, other):
        to_sub = self.new_nominator_fractions(self, other)
        if to_sub[0] > to_sub[1]:
            return True
        return False

    def __eq__(self, other):
        to_sub = self.new_nominator_fractions(self, other)
        if to_sub[0] == to_sub[1]:
            return True
        return False

    def __str__(self):
        return "{} / {}".format(self.nominator, self.denominator)


a = Fraction(2, 3)
b = Fraction(4, 6)

print(a == b)
