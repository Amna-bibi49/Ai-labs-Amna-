#Create a dictionary (in your file) of names and birthdays. When you  run your program it should ask
#the user to enter a name, and return the birthday of that person back to them.

import time
Birthdays ={
    "Albert Einstein": "14/3/1889",
    "Bill Gates": "28/10/1955",
    "Steve Jobs": "24/2/1955",
}
print("Welcome to the Birthday game ! We have the birthdays to:")
time.sleep(1)
for x in Birthdays:
    print(x)
    time.sleep(0.7)
choice= input("\nWho's birthday do you want to look up?")

if choice in Birthdays:
    print("The birthday of {} is on: ".format(choice))
    print(Birthdays[choice])
