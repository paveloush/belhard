class Accounts:
    _accounts = {}

    def add_card(self, card_id, password, _bill):
        self.card_id = card_id
        self.password = password
        self._bill = _bill
        if self.card_id not in self._accounts:
            self._accounts[self.card_id] = {'pass':self.password, 'money': self._bill}
            print ('New card added!')
        else:
            print('Card #',card_id, 'already exists in DB')

class Atm(Accounts):
    def __init__(self, card_id, password):
        self.card_id = card_id
        self.password = password
        if self.card_id in self._accounts:
            if self._accounts[self.card_id]['pass'] == self.password:
                print('You are logged in')
            else:
                raise NameError ('Wrong password, please, try again')
        else:
            raise NameError('Sorry, your card #'+ str(self.card_id) + ' is not recognized')

    def cash(self, summ):
        self.summ = summ
        if summ <= self._accounts[self.card_id]['money']:
            self._accounts[self.card_id]['money'] -= self.summ
            print('please, take your ' + str(summ) + '$')
        else:
            print('You don\'t have money enough to make this operation.')

    def check(self):
        print('Your balance is '+ str(self._accounts[self.card_id]['money']) + '$')



while True:
    message = input('print \'add card\' or \'atm\' to start')
    if message == 'add card':
        id = input('enter card id')
        pas = int(input('enter password'))
        money = int(input('enter amount of money'))
        a = Accounts()
        a.add_card(id, pas, money)
    elif message == 'atm':
        id = input('enter card id')
        pas = int(input('enter password'))
        atm = Atm(id, pas)
        while True:
            operation = input('print \'cashout\' or \'balance\' ')
            if operation == 'cashout':
                s = int(input('choose a summ'))
                atm.cash(s)
            elif operation == 'balance':
                atm.check()
            exit = input('print \'exit\' to exit or press Enter to continue working with your card')
            if exit == 'exit':
                break
    exit = input('print \'exit\' to exit or press Enter to continue')
    if exit == 'exit':
        break