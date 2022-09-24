#Write a function in python that receives a string and returns True if that string is a palindrome and False otherwise.


def ispalindrome(word):
    temp=word[::-1]
    if temp.capitalize()==word.capitalize():
        return True
    else:
        return False

print(ispalindrome("deed"))
