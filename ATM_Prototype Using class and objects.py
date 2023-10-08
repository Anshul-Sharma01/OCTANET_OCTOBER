class ATM:
    _lst=[]
    _uname="Anshul Sharma"
    _pin=1234
    _amount=0
    _fund_transferred=0
    def __init__(self):
        print("Welcome to the ATM Interface")
        uname = input("Please enter your username:")
        pin = int(input("Please enter your pin:"))
        if self._uname==uname and self._pin==pin:
            print("Authentication Completed!!")
        else:
            print("!!Authentication Failed!!")
            print("!!Exiting the ATM!!")
            exit()

    def Transaction_history(self):
        print("-----Transaction History-----")
        for hist in self._lst:
            print(hist)
            print("----------")
    def Withdraw(self,am):
        if am>0 and am<=self._amount:
            self._amount-=am
            self._lst.append(f"Amount Withdrawn : {am}\nAmount Left : {self._amount}")
        else:
            print("Please Enter the Valid Amount!!")

    def Deposit(self,am):
        self._amount+=am
        self._lst.append(f"Amount Deposited : {am}\nTotal Amount Now: {self._amount}")

    def Transfer(self):

        acc=int(input("Please enter the Beneficiary account number : "))
        fund=int(input("Please enter the fund to be transferred to beneficiary account : "))
        if fund>0 and fund<=self._amount :
            self._amount-=fund
            self._fund_transferred=fund
            self._lst.append(f"Amount Transferred : {fund}\nAmount Left : {self._amount} \nTotal Funds Transferred : {self._fund_transferred}")
        else:
            print("Please Enter the Valid Amount!!")

    def Quit(self):
        print("--------Thanks For using ATM--------")
        print("--------Have a Good Day--------")
        exit()



p1=ATM()
while True:
    print("-------Services------")
    print("1.Transaction History")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.Transfer")
    print("5.Quit")
    print("---------------------")
    ch=int(input("Please enter your choice:-"))
    if ch==1:
        p1.Transaction_history()
    elif ch==2:
        am=int(input("Please enter the amount you want to withdraw:"))
        p1.Withdraw(am)
    elif ch==3:
        am=int(input("Please enter the amount to be deposited:"))
        p1.Deposit(am)
    elif ch==4:
        p1.Transfer()
    elif ch==5:
        p1.Quit()
    else:
        print("Please enter valid choice!!!!\n")


