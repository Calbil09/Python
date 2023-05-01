class self:
    def insert(self):
        self.year = int(input("Enter Year you study: "))
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.id = input("Enter id: ")
        self.major = input("Your major is: ")
        print("\t>>>Enter score you got<<<")
        self.a = int(input("English: "))
        self.b = int(input("France: "))
        self.c = int(input("Math: "))
        self.d = int(input("Physic: "))
        self.e = int(input("Chemitry: "))
        print("\t\t==============================")

    def display(self):
        print("\t==============================")
        print("\n\t Information self \n")
        print("\t==============================")
        print("\tYou study at year : ", self.year)
        print("\tName : ", self.name)
        print("\tage : ", self.age, " years")
        print("\tID : ", self.id)
        print("\tYour're major is : ", self.major)
        print("\tYou got : ", self.a, " pt")
        print("\tYou got : ", self.b, " pt")
        print("\tYou got : ", self.c, " pt")
        print("\tYou got : ", self.d, " pt")
        print("\tYou got : ", self.e, " pt")
        self.score = self.a + self.b + self.c + self.d + self.e
        print("\tAll score you got : ", self.score, " pt")

    def find(self):
        print("Check Average!")
        self.score = self.a + self.b + self.c + self.d + self.e
        self.average = self.score / 5
        print("\tID: ", self.id)
        print("\tYou got : ", self.score, " pt")
        print("\tAverage : ", self.average, " . ")
        if self.average >= 90 and self.average <= 100:
                print('\tYou got Grade A ')
                print("\tYou're GOOD!!")
        elif self.average >= 75 and self.average <= 90:
                print('\tYou got Grade B')
                print("\tYou're GOOD!!")
        elif self.average >= 60 and self.average <= 75:
                print('\tYou got Grade C ')
                print('\tYou are good ,Try more')
        elif self.average >= 50 and self.average <= 60:
                print('\tYou got Grade D')
        elif self.average <= 49:
                print('\tYou Fall!!!')
    def sort_by_average(self,user):
        self.score = self.a + self.b + self.c + self.d + self.e
        self.average = self.score / 5
        sort_=sorted(self.average,key=float)
        print ("\t\t Sort self : \n")
        for i in range(0,user):
            print("\t==============================")
            print("\tYou study at year : ",self.year)
            print("\tName : " ,self.name)
            print("\tage : ",self.age," years")
            print("\tID :",self.id)
            print("\tYour're major is : ",self.major)
            print("\tYou got : ",self.a , " pt")
            print("\tYou got : ", self.b, " pt")
            print("\tYou got : ", self.c, " pt")
            print("\tYou got : ", self.d, " pt")
            print("\tYou got : ", self.e, " pt")
class S(self):
    pass
s = S()

while True:
    print("\t\t==============================\n")
    print("\t\tChoose option Below")
    print("\t\t1. Insert self inform.")
    print("\t\t2. Display data ")
    print("\t\t3. Find average")
    print("\t\t4. Sort self by average ")
    print("\t\t==============================")
    store = int(input('Enter option : '))
    if store == 1:
       s.insert()
    elif store == 2:
        s.display()
    elif store == 3:
        s.find()
    elif store ==4 :
        s.sort_by_average( )