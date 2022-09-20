#Write a program that prompts the user to input an integer and then outputs the number with the digits 
#reversed. For example, if the input is 12345, the output should be 54321.

Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\n Reverse of entered number is = %d" %Reverse) 
