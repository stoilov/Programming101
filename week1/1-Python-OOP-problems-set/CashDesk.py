class CashDesk:

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, notes):
        self.notes = notes
        for note, quantity in notes.items():
            self.money[note] += quantity

    def total(self):
        total_sum = 0
        for note, quantity in self.notes.items():
            if quantity > 0:
                total_sum += quantity * note

        print(total_sum)

    def can_withdraw_money(self, amount_of_money):
        permutation = []
        for note, quantity in self.notes.items():
            permutation.append(note)

my_cash_desk = CashDesk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
my_cash_desk.total()
