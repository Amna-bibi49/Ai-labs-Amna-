#Accept two lists from user and display their join.

myList1=[]
print("enter the object of first list")
for i in range (5):
    val=input("enter the value:")
    n=int (val)
    myList1.append(n)
myList2=[]
print("enter the element of second list")
for i in range (5):
    val=input("enter the value:")
    n=int (val)
    myList2.append(n)
    
List3=myList1+myList2;
print(List3)
