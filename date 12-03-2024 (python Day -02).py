a, b=c=7, 8
print(a)
print(b)
print(c)

 # a=b, c =4, 2
 # print(a, b, c)

 #----> swapping of variables
a= 7
b= 5
 #eg:1
# temp=a #temp=7
# a=b    #a=5
# b=temp #b=7 

  # # a=5, b=7
  #  print(a,b)

   # Eg:2
   # a=a+b #a=12
   # b=a-b #b=12-7=5
   # a=a-b #a=12-5=7

   # print(a, b)

   # a, b=b, a # only in python
   # print(a,b)

  # a=a*b #a=35
  # b=a/b #b=35/7 =5.0
  # a=a/b #a=35/5 =7.0
  # print(int(a), int(b))

  # id() --> used to find the memory address of the variable
  # a = 7
  # b = 8
  # print(id(a))
  # print(id(b))

  # ----> keywords
  # keywords are reserved words which provides special meaning to
  # compiler or interpretor

import keyword
 # print(keyword.kwlist)
 # print(len(keyword.kwlist))
 # print(type(keyword.kwlist))


 # To check if the string is keyword or not
 # print(keyword.iskeyword("sid")) # false

 # if = 8
 # print(if) # error coz if is a keyword

  # !----> literals
  # literal is the considers to be constant when  it is defines
  # in caps

  # a= 78 # a is variable
  # A=78 # A is constant

  # hash()--. it creates a hash value for constant datatypes and
  # provides error for non constant datatypes
n1 = 89+7j
print(hash(n1))

f1 =[7, 8, 9]
print(hash(f1)) # error ---> list is non-constant or mutable datatype

 # a = 9
 # b = 9
 # b = 90
 # print(id(a))
 # print(id(b))

 #!----> operators
 # ? operators are symbols which is used to perform various operations
 # ? between 2 or  more operands


 # arithmatic
 # assignment
 # logical
 # relation orcomparison
 # bitwise
 # identify
 # membership


 # fodo ----> arithmatic ---> +, -, *,/,%,//,**
# a = 8
# b = 6
# c = 9
# print(a+b+c)

# input() ---> used to get the runtime input
n1 = input("Enter the value:")
pri(type(n1))
      
a = 4
b = 2
print(a/b) # is used to get the quotient value print(a%b) # is used to get the remainder value

#! ## --> used for power of a number
# print(2**4) # --> 16

# ! assignment --> +-=, -=, /=, *=, //=, **=, &=,|=

# a= 8
# a+=2
# print(a)

# a=30
# a-=5
# print(a)

# a = 9
# b = 5
# print(a==b)

# ! bitwise operator --> &, |,^,~,<<,>>
a = 7
b = 4
print(a&b)

# 2^4 2^3 2^2 2^0
# 8   4    2   1

# 0    1   1    1   #--> 7
# 0    1    0    0   # --> 4 &
#-----------------------
# 0    1    0    0

# 256 128 64 32 16 8 4 2 1
# 0 0 0 0 0 0 0 0 1 0 0


 # AND
 # A B A/B
 # 0 0 0
 # 0 1 0
 # 1 1 1

 # ~ --->
 # a = 6876
 # print

 # a = 9
 # 128 64 32 16 8 4 2 1
 #0     0  0  0  1 0 0 1 #--->  9


 # 1  1  1  1  1  0  1  1 0 # ---> -10

 # 0 0  0   0   1  0  1  1  0 ---> 10

 # 1 1  1  1 0  1 0 1 -> 1s  compliment of 10
                  # 1 -> 2s  compliment
 # --------------------
 # 1 1 1 1 0 1 1 0 --> -10

 # 256 128 64 32 16 8 4 2 1
 #  0   0   0  0  0 0 0 0 0  3<
 #  0   0   0  1  0 1 0 0 0 ---> 40
 #  107

 # <<, >>
 # print(5>>1)

 # 16>4
 # ! logical
 # and, or , not
a = 6
# print(a>3 and  a<10)
# print(a>7 or   a<30)
# print(not(a>8 and a<10)

#! identity operator
# is, is not
a = 8
b = 8
# print(a is b)
# print(a==b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)

# ! menbership operator
#  in , no
 # num = 55
 # print(num in 11)
 # print(num not in 11)

 # num  = 678
 # print(8 in num) # error

 # ! conditional statement
 #  if, elif, else
 # Eg:1
 # a = 6
 # if a>3:
 #      print("yes")
# else:
#     print("no")
# Eg:3
# if 7>8

# a nmber is even or odd

  
name = input (" Enter the name:")
age = int(input(" enter the  age:"))
nationality=input(" enter the ntion:")

if age>=18 and nationality== "india":
   print("eligible for vote")
else:
    print("not eligible")












   
   
