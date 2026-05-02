#######################
from time import sleep

count = 1
width = 100

for i in range(10):
    print(("*" * count).center(width))
    count+=2
    sleep(0.5)
print("| |".center(width))
print("Happy New Year".center(width))
print("2022".center(width))
print("***** Welcome to the online shopping system of Pino Fastfood *****".center(width))
print("  ")
print("  ")
print("  ")
print("  ")
#######################

customers=open('D:\\CustomerList.txt','a')
FoodList=open('D:\\ّFood.txt','a')
foodList=[]
ClerckList=[]
CustomerList=[]

class Food:

    def __init__(self,index,name,price):
        self.name=name
        self.price=price
        self.index=index

    def __str__(self):
        s=f'{self.index:3d}|{self.name:10s}|{self.price:5d}'
        return s

    def Toostr(self):
        s=f'{self.index:3d}|{self.name:10s}|{self.price:5d}'
        return s

    def Bought(self,index,number):
        foodList[index].price *= number


class User:

    def __init__(self,username,password):
        self.UserName = username
        self.Password = password

    def __setattr__(self, key, value):

        if key == 'UserName':
            self.__dict__[key] = value

        elif key == 'Password':
            flag = True
            while flag:
                if isinstance(value, str):
                    raise ValueError
                else:
                    self.__dict__[key] = value
                    flag = False
        else:
            self.__dict__[key]=value

class Clerck(User):

    def __init__(self,username,password,foodlist):
        super().__init__(username,password)
        self.FoodList=foodlist

    def changePriceFood(self, index, newprice):
        self.FoodList[index].price = newprice

    def GetReportFood(self):
        for p in self.FoodList:
            print(p)

    def login(self,newu,newp):
        correct=False
        if(self.UserName==newu and self.Password==newp):
            correct=True
        return correct

    def Menu(self):
        print("You are clerck")
        Flag = True
        while Flag :
            print("what do you want to do?")
            print("1.see list of foods")
            print("2.change price of foods")
            print("3.add a new food")
            print("4.exit")
            v = int(input())
            if v == 4:
                Flag = False
            elif v == 3:
                st = input("Please enter the index,name of food and price and seprate with |")
                stsplit=st.split('|')
                indexfood=int(stsplit[0])
                namefood=stsplit[1]
                pricefood=int(stsplit[2])
                foodList.append(Food(indexfood,namefood,pricefood))
                for fo in foodList:
                    FoodList.write(fo.Toostr())


            elif v == 2:
                index = int(input('Please enter the index of food to change the price of : '))
                newprice = int(input('please enter new price : '))
                self.changePriceFood(index, newprice)

            elif v == 1:
                self.GetReportFood()

    def __str__(self):
        return f'clerck info : {self.UserName:<15s}|{self.Password:<15d}'



class Customer(User):
    def __init__(self,username,password,phonenumber,address,foodlist,stock=0):
        super().__init__(username, password)
        self.FoodList = foodlist
        self.PhoneNumber = phonenumber
        self.Address = address
        self.__Stock = stock

    def __str__(self):
        return f'customer info : {self.UserName:<15s}|{self.Password:<15d}|{self.PhoneNumber:<10d}|{self.Address:<20s}'

    def __setattr__(self, key, value):

        if key == 'PhoneNumber':
            flag = True
            while flag:
                if isinstance(value, str):
                    raise ValueError
                else:
                    self.__dict__[key] = value
                    flag = False

        elif key == 'Address':
            self.__dict__[key] = value
        elif key == '_Customer__Stock':
            flag = True
            while flag:
                if isinstance(value, str):
                    raise ValueError
                else:
                    self.__dict__[key] = value
                    flag = False

        #else:
         #   print('No other attribute is allowed')

    def GetReportFood(self):
        for p in self.FoodList:
            print(p)

    def login(self,newu,newp):
        correct=False
        if(self.UserName==newu and self.Password==newp):
            correct=True
        return correct

    def Menu(self):
        Flag = True
        while Flag :
            print("what do you want to do?")
            print("1.Order food")
            print("2.Increse the stock")
            print("3.exit")
            v = int(input())
            if v==3:
                Flag=False

            elif v==2:
                money=int(input("please enter your intended amout : "))
                self.IncreaseStockFunc(money)

            elif v == 1:
                while Flag:
                    print("***** Menu *****")
                    foodList=FoodList.readlines()
                    #FoodList.readlines()
                    flag=True
                    Cost=0
                    while flag:
                        index=int(input("please enter the index of intended food : "))
                        number=int(input("please enter the number of this food : "))
                        cost=Food.Bought(self.FoodList,index,number)
                        Cost +=cost
                        r=input("If you want to continue ordering please enter yes,otherwise no ")
                        if r=="no" or r=="No" :
                            flag=False
                    print("Your Bill is "+str(Cost))
                    pay=input("If you want to use your stock to payment please enter yes,otherwise no")
                    if pay=="no" or pay=="No" :
                        print("Pay your bill at home")
                        print("We will send your foods to your address")
                        print("Thank you for your trust")

                    elif pay=="yes" or pay=="Yes" :
                        self.UseStockFunc(Cost)
                        print("We will send your foods to your address")
                        print("Thank you for your trust")


    def IncreaseStockFunc(self,w):
        self.__Stock +=w

    def UseStockFunc(self,z):
        if (z < self.__Stock):
            self.__Stock -= z
        else:
            print('Your stock is not enough!!!')
            print("Pay your bill at home")


#############
ClerckList.append(Clerck('AliAhmadi',223344,foodList))
ClerckList.append(Clerck('SaraAbedi',987654,foodList))
ClerckList.append(Clerck('MinaTaheri',223344,foodList))
##############
CustomerList.append(Customer('SaharAkbari',990099,2775577,'TehranVanak',foodList))
#CustomerList.append(Customer('AmirSafari',123456,2744337,'TehranNarmak',foodList))
#CustomerList.append(Customer('ZahraNaderi',557755,3344555,'TehranPiroozi',foodList))
##############

u=int(input("If you are clerck,enter 1 and if you are customer,enter 2 : "))

if u==1:

    Clerck.UserName = input("Please enter your username(lowercase English letters) :")

    try:
        Clerck.Password = int(input("Please enter your password(just contains numbers) : "))
    except(ValueError):
        print('Your username must be an integer !!! ')

    haslogined = False
    for line in ClerckList:
        haslogined = line.login(Clerck.UserName,Clerck.Password)
        if (haslogined):
            loginedLine = line
            Clerck.Menu(line)
    if (haslogined == False):
        print('username and password is not correct ')

elif u==2:

    l = input("If you have already registered on the site, enter yes, otherwise, enter the no : ")

    if l=="no" or l=="No":

        Customer.UserName = input("Please enter your intended username(lowercase English letters) :")

        try:
            Customer.Password = int(input("Please enter your intended password(just contains numbers) : "))
        except(ValueError):
            print('Your password must be an integer !!! ')

        try:
            Customer.PhoneNumber = int(input("Please enter your phonenumber : "))
        except(ValueError):
            print('Your phone number must be an integer !!! ')

        Customer.Address = input("Please enter your address : ")

        info = f'{Customer.UserName:<10s}|{Customer.Password:<10d}|{Customer.PhoneNumber:<10d}|{Customer.Address:<20s}'
        print(info)
        TF = input("If these information is true,enter T and otherwise enter F : ")
        if TF == "T":
            c=Customer(Customer.UserName,Customer.Password,Customer.PhoneNumber,Customer.Address,foodList)
            CustomerList.append(c)
            customers.write(str(c)+'\n')
            #print(CustomerList)

    elif l=="yes" or l=="Yes":

        Customer.UserName = input("Please enter your username(lowercase English letters) :")

        try:
            Customer.Password =int( input("Please enter your password(just contains numbers) : "))
        except(ValueError):
            print('Your password must be an integer !!! ')

        haslogined = False
        for line in CustomerList:
            haslogined = line.login(Customer.UserName, Customer.Password)
            if (haslogined):
                loginedLine = line
                Customer.Menu(line)

        if (haslogined == False):
            print('username and password is not correct ')
