class ATM(object):
    def __init__(self,atmNumber,pinNumber):
        self.atmNumber=atmNumber
        self.pinNumber=pinNumber
      
    def CashWithdrawl(self):
        print("Cash Withdrawl")
        
    def BalanceEnquiry(self):
        print("Balance Enquiry")

   
obj1=ATM(5689,2345)
print(obj1.atmNumber)
print(obj1.pinNumber)
obj1.CashWithdrawl()
obj1.BalanceEnquiry()


