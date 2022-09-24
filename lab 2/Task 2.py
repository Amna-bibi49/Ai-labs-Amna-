# write a python program to find the smallest and largest element of the list. 

lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("largest number in the list is :", max(lst))
print("smallest number in the list is :", min(lst))
