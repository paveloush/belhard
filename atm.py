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



a = Accounts()
a.add_card(12345678, 1111, 500)
a.add_card(54321000, 2222, 100)
b = Accounts()
b.add_card(54321000, 2222, 100)
c = Atm(54321000, 2222)
c.cash(50)
c.check()
