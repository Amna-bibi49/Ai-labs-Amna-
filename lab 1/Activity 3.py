#Write a python code that finds another matrix/2D list that is a product of and b,
#i.e., C=a*b


a=[[1,0,0],[0,1,0],[0,0,1]]
b=[[1,2,3],[4,5,6],[7,8,9]]

for indrow in range (3):
    c.append ([])
    for indcol in range(3):
        c[indrow].append (0)
        for indaux in range (3):
            c[indrow][indol] += a[indrow][indaux] * b[indcol][indaux]

print(c)



            
