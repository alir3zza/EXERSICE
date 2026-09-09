#2026/9/8
#Problem 1: Weird or Not Weird

#n = int (input())




#if n % 2 != 0:
    #print("Weird")
#elif 2<= n <= 5 :
    #print ("Not Weird")
#elif 6<= n <= 20 :
    #print ("Weird")
#elif n >= 20 :
    #print ("Not Weird")







#---------------------------------------------
#2026/9/8
#Problem 2: Sum, Difference, and Product

'''
a = int(input())
b = int(input())
    
def ab (a, b):
    d = a + b
    c = a - b
    h = a * b
    
    return d, c, h 
d, c, h = ab(a, b)
#print(ab(a, b))
print (d)
print (c)
print (h) 

'''

#------------

#2026/9/8
#Problem 3: Floor Division and Float Division
'''
a = int(input())
b = int (input())


def division (a, b):
    floor = a // b
    float = a / b
    return floor, float 

floor, float = division(a, b)
print(floor)# this floor division and its change answer to down
print(float)



'''






#-----------------------
#2026/9/8
#Problem 4: List of Squares



'''
n = int (input())


d = []
for i in range(n):

    if i < n :
        x = i * i
        d.append(x)


print(d)



'''



#-------------------
#2026/9/8
#Problem 5: Leap Year Check
'''
def is_leap(year):
    leap = False
    if year % 4 == 0 :
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

year = int(input())
print(is_leap(year))

'''



#-----------------
#2026/9/9
#Problem 6: List of Numbers

n = int (input())

for i in range (1,n+1):
    print(i, end = "")





        








    



