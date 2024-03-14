''''
def catAndMouse(x, y, z):
    dist_cat_a = abs(z - x)
    dist_cat_b = abs(z - y)
    if dist_cat_a == dist_cat_b:
        return "Mouse C"
    elif dist_cat_a < dist_cat_b:
        return "Cat A"
    else:
        return "Cat B"
    
# Example usage
print(catAndMouse(1, 2, 3))  # Output: Cat B
num = 8
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)

sum_even = 0
sum_odd = 0
for num in range(12, 38):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
n1 = 123
total = 0

while n1 > 0:
    digit = n1 % 10
    total += digit
    n1 //= 10
print("Sum of digits of the number:", total)

n1 = 234
reverse = 0
while n1 > 0:
    digit = n1 % 10
    reverse = reverse * 10 + digit
    n1 //= 10
print("Reverse of the given number:", reverse)


# ----> while loop
# ----> brake using while loop

# eg:1
# 1.> iterate from 20 to 30 and break the loopin 27

# i = 20
# while i<31:
#    if i ==27:
#      break
 #   print(1)
  #  i+=1
#   if i==27:
 #      break
  #  i+=1
  

  # ! ------> continue
# ----> eg:1
i = 20
while i<31:
    if 1==27:
        continue
    print(i)
    i=i+1

# ! Eg:5
# while to iterate from 12 to 22
# find the sum of all numbers

i = 12
while i<22+1:
    print(i)
    i+=1
    

  # ! Eg:6
i =12
sum=0
while i<23:
    sum=sum+i
print(sum)


# ! Eg:6
# find the average of value from 20 to 25

# 1 = 20
# sum = 0
# count = 0
# while i<=30:
#   sum=sum+i
#   count+=1
#   1+=1
# print(sum/count)


 # ! -----> nestead for loop
 # Eg:1
for i in range(1, 3+1):
    for j in range(1, 4+1):
       print(i, j)

       
# eg 22
# * * * * 
# * * * * 
# * * * * 
# * * * * 
for row in range (4):
    for col in range(4):
print("*",end="")
 print()


for row in range(5):
    for col in range(5):
        print(row, end = " ")
    print()


# | to print stars in right angled triangle


#for row in range(0,6):
#     for col in range(0, row):
  #        print("*", end=" ")
  #  print()

  # * * * * * * 
  # *         *
  # *         *
  # *         *
  # * * * * * *


# for row in range(5):
  #     for col in ranges(5):
   #       if col==0 or col==5-1 or row ==0 or row ==5-1:
    #       print("*", end=" ")
     #       else:
      #         print(" ",end=" ")
       #     print()
        


    
for row in range(5):
    for col in range(5):
        if col==0 or col==5 or row==0 or row==5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



    
#      *
#    * * *
#   * * * *
#  * * * * *


# for row in range(0,5):
#  for coi in range(0, 6):
      if((row==0 and col==3) or (row==1 and col>=2 and col<=4) or
                                 (row==2 and (col>=1 and col<=5))):
                    print("*", end=" ")
                    else:
                      print(" ", end=" ")


                      
for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()                      


for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
 


for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



# ? -----> negative indexing
# lst1-[1, 4,7, 89.7,7.5,"PP","1"]
# lst1[start index:end index:step]


# print(lst1[0:4])
# print(lst1[6:8])
# print(lst1[3:6])
# print(lst1[:5])
# print(lst1[3:])
# print(lst1[:])

# print(lst1[0:7:1]) #lst[0,7] ---> both are same
# print(lst1[0:7:2])

    
# ? ----> slicing
# lst1[start_index:end_index:step]
lst1 = [1,2,3,4,56,34,"p","g",]
print(lst1[0:8])


# eg : 1
# 1.) iterate from 20 to 30 and break the loop in 27

i = 20
while i<31:
    print(i)
    i+=1



# 2.)
i = 20
while i<31:
    print(i)
    i+=1

    if i==27:
        break


    # i = 12
#sum=0
 #while i<23:
     #sum=sum+i
     #print(sum)
     #i+=1
'''''''
lst = [1, 4, 1,89.7,7.5,"P","i"]
# print(lst[-4:-1])
# print(lst[-1:-4])--->[]
# print(lst[-7:-1])
# print(lst[-7:-1:2])

def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[0], reverse=True)


    
