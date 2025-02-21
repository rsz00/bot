class Account:
    def __init__(self,usrnm,psswd):
        self.username = usrnm
        self.password = psswd

#
def generateAccountArray(names,psswords):
    i = 0
    ret = []
    while i < len(names):
        ret.append(Account(names[i],psswords[i]))
    return ret