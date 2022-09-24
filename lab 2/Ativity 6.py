#Create a Python program that contains a dictionary of names and phone numbers. Use a tuple of 
#separate first and last name values for the key field. Initialize the dictionary with at least three 
#names and numbers. Ask the user to search for a phone number by entering a first and last name. 
#Display the matching number if found, or a message if not found


sample={("sohaib","ali"):"024655468445",("aib","li"):"024655468445",
        ("sib","ai"):"123456780987654",}
firstname=input("enter the first name")
lastname=input("enter the last name")
searchtuple=(firstname,lastname)
if searchtuple in sample:
    print(sample[searchtuple])
else:
    print("name not found")
