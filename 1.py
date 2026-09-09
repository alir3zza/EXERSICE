

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


n = int (input())


d = []
for i in range(n):
    d = i 
    d.append(i)

print (d)






    



