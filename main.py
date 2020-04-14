class Account:
    username=["Kobe","Cedrick","Van"]
    password=["123","456","789"]
    
    def __init__(self, userx, passx):
        self.userx=userx
        self.passx=passx
        
    def verifyName(self):
        if self.userx in self.username:
            return True
        else:
            return False
        
    def verifyPass(self):
        if self.passx in self.password:
            return True
        else:
            return False
    
    def accountMatch(self):
        if (self.verifyName() and self.verifyPass() == True):
            if (self.username.index(self.userx) == self.password.index(self.passx)):
                return True
            else:
                return False
        else:
            return False
        
    def loginAcc(self):
        if (self.accountMatch() == True):
            return True
        else:
            return False

def main():
    print("----- Welcome! -----")
    fail=0
    
    while (fail!=3 and fail!=99):
        inputUser=input("Enter username: ")
        inputPin=input("Enter PIN: ")
        verify=Account(inputUser,inputPin)
        
        if (verify.loginAcc()==True):
            fail = 99
            break
        else:
            fail = fail + 1
            print("\nPlease enter a valid username and PIN. ", (3-fail), "attempts left.\n")
            if (fail==3):
                break
        
    if (fail == 3):
        print("\nLog-in failed. The police were alerted.\n")
    elif (fail == 99):
        print("\nLog-in successful.\n")

main()
        
        
        