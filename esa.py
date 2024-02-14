class welcome():
        while True:
          print("Welcome to our expense sharing app")
          break
        personList=[]
        n=int(input("enter number of roommates or friends:"))
        if n<=1:
             print("user should greater than 1")
        else:     
          for i in range(1,n+1):
            names=input(f"enter {i} name(name only):")
            personList.append(names)
        print(personList)
                           
class totalamount(welcome):
        if welcome.n<=1:
          print("user should greater than 1")
        else:
          n1=welcome.n
          amount=int(input("enter total amount to shared: "))
          ta=amount/n1
          originalList=welcome.personList
          for i in originalList:
            print(f"{i} to pay:{ta}")
def payment(personList,n,ta):
 
 for person in range(len(personList)):
         n=input(f"enter your name[1-{len(welcome.personList)}]:")
         if n=="":
          print("please enter your name")
         else:
          for i in range(len(personList)):
           if i==personList.index(n):
            amt=float(input("enter amount:"))
            bal=ta-amt
            print("You owes",bal)
            if(bal==0.0):
              print("You don't have to pay.Your balance is",bal)
 
totalamount()
payment(welcome.personList,welcome.n,totalamount.ta)

 
