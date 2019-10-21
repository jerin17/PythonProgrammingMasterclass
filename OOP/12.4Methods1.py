import datetime
import pytz


class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print('Account created for', self.name)
        self.show_transaction()


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount < 0:
            print('Amount must be greater than zero !')
        elif amount > self.balance:
            print('Sorry, Insufficient Funds !')
        else:
            self.balance -= amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))

    def show_balance(self):
        print("Balance : {}".format(self.balance))

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print('{:6} {} on {} (local time - {})'.format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    jerin = Account('Jerin', 0)
    jerin.show_balance()

    jerin.deposit(100)
    jerin.withdraw(10)
    jerin.show_transaction()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transaction()
