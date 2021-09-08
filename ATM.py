class ATM (object):
    def init(self,cardNumber,pinNumber, amount):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.amount = amount
        
    def cashWithdrawl(self):
        print('Please give your card and pin number and the amount to be taken out.')

    def transactionSuccessfull(self):
        print('An email will be send regarding the transaction')

Bank = ATM('123', '0000', '1,000,000 $')
print(Bank.amount)