class Team:
    def __init__(self):
        self.member=[]

    def setMember(self, name):
        self.member.append(name)
    
    def showMember(self):
        print("The members are: ")
        for name in self.member:
            print(name,end=', ')

t1=Team()
t1.setMember('Soumen')
t1.setMember('Bijen')
t1.showMember()