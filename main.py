
print('Hello world')
first_name="Teth"
last_name= " Menghuy"
full_name = first_name+last_name
print ("TMH IDUSTRY OWNER NAME : "+full_name)

age = 23
print( "His age : " +str(age))
name = " Puma"


#string method
print(len(name))
print(name.find("a"))#enter char u wamt to find
print(name.capitalize())
print (name.upper())
print(name.lower())
print(name.count("")) # number of occurrence of ""
print (name.replace('P','k'))# 'c'->'o' change char
print (name*4)
print(type(name))
#print()

#type casting = convert the data type of a value to another data type.
x = 1   #int
y = 2.0 #float
z = "3" #str

x = int(x)
y = int(y)
z = int(z)

x = float(x)
y = float(y)
z = float(z)

x = str(x)
y = str(y)
z = str(z)

print(x)
print(y)
print(z*3)

#user input

#name = input('What is your name? : ')
#age = int (input ('How old are you?: '))
#height = float(input('How tall are you? : '))
#age +=1
#print ("Hello , "+name)
#print('You are '+str(age)+'years old')
#print('You are '+str(height)+'cm')

#math function

import math
pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(420))
print(max(x,y,z))
print(min(x,y,z))


#Slicing = create a subdtring by extracting elements from another string
#indexing[]// use to show string] or slice() use to hide string
# [start:stop:step]
name = "Meng Huy"
f_name= name [0:5] # [0 is the first index:5 is stop at 5 (it's run 0-4)]
print (f_name)

text = 'Hello-,-world'
slice = slice(5,-5) #-5 mean to hide the last index back to front
print (text[slice])

# if else statement
name = input('What is your Name ? :')
age = int (input('How old are you ?: '))
if age >= 18:
    print ('Hello, '+name)
    print ('  You can Vote ')
else:
    print('Hello, ' + name)
    print('You can not Vote ')


#logical operators{and
   #                     or
   #                          not
   #                                }
score = int (input ('Your score in this Mid-term : ' ))
if score >= 90 and score <= 100:
    print ('You got Grade A ')
    print ("You're GOOD!!")
elif score >=75 and score <= 90:
    print ('You got Grade B')
    print("You're GOOD!!")
elif score >=60 and score <= 75:
    print ('You got Grade C ')
    print ('You are good ,Do not give up')
elif score >=50 and score<= 60:
    print ('You got Grade D')
    print('You should try more ')
elif score<=49:
    print ('You Fall!!!')


#Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
elif score<0 or score>100:
    print ('You Can Not Put Score  Hight than 100 ')
    print('Please Try Again .....')


#while loop = unlimited
#while 1==1:
 #   print ('Welcome , b*tch')


#for loop = limited
# syntax
  #  ->     for i in range (start,stop,step):
                    # . . . .

import time
for i in range(10):
    print (i+2)
for i in range (0,100+1,2):
    print (i)
for i in 'Meng Huy':
    print(i)
for seconds in range(15,0,-1):
    print(seconds)
    time.sleep(1)
print ('Welcome To TMH Industry')


# nested loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print("  ")


# loop control
#     break = use to stop loop running
#       continue = use to skip index
#           pass = does nothing on index
while True :
     #name = input ('Enter name : ')
     if name !=" ":
         break
phone_number = "123-321-098"
for i in phone_number:
    if i=="-":
        continue
    print(i,end="- ")

for i in range(0,10):
    if i ==8:
        pass
    else:
        print(i)

#list = use to store multiple items in a single var

drink = ['coca ','pepsi','ize','anchor','ABC','sting']
drink [2]= 'merinda'

#print(drink[2])

#append use to add items
# remove use to remove items
# pop use to remove items at the last
# insert use to add items to  the front
# clear use to remove every thing in the list
# sort use to sort the list items
#food.append("i")
#food.remove("anchor")
#food.pop('')
#food.insert(0,"fanta")
#food.sort('')
#food.clear('')
for x in drink:
    print (x)

# 2d list = a list of list
drinks = ['cofe','tea','soda']
desert = ['ice cream','cake','bread']
dinner = ['pizza','buger','hotdog']

food = [drinks ,desert,dinner]

print (food[1][2])
#food[0][0]
#     |  |
#     |  |
#     |  CHOOSE what we want in the list of FOOD list : drinks = ['cofe','tea','soda']
#     |                                              desert = ['ice cream','cake','bread']
#     |                                              dinner = ['pizza','buger','hotdog']
#     |
#    CHOOSE what we want in the FOOD list : food = [drinks ,desert,dinner]


# tuple = collection which is ordered and unchangeable
#         used to group together related data
student = ('huy',34,'male')
print (student.count('huy'))
print (student. index('male'))
for x in student:
    print(x)
if 'male' in student:
    print('Ah t*th')

# sets = collection which is unordered , unindexed .withuut duplicate value
utensils = {'fork','spoon','knife'}
dishes = {'bowl','plate','cup','knife'}

#utensils.add('napkin')
#utensils.remove ("fork")
#dishes.update(utensils)
#dinner_table = utensils .union(dishes)

#for x in dinner_table:
 #   print (x)
#print(dishes.difference(utensils))
#print(utensils.intersection(dishes))

#dictionary =  A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly
capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

#capitals.update({'Germany':'Berlin'})
#capitals.update({'USA':'Las Vegas'})
#capitals.pop('China')
#capitals.clear()

#print (capitals['Germany'])

print (capitals.get('Germany'))
print (capitals.keys)
print(capitals.values())
print(capitals.items())
for key,value in capitals.items():
    print(key,value)

#Example
# kilo convert to miles
kilometers = float(input('Enter values to convert from Kilo to miles: '))

con_fac = 0.6213

result = kilometers * con_fac

print('The result '+str(kilometers)+' Km is  '+str(result)+' Miles' )
# fahrenheit = celsius * 1.8 + 32
celsius = float (input ('Enter value of degree celsius: '))

fahrenhiet = celsius * 1.8 +32

print ('Values of fahrenhiet = '+str(fahrenhiet)+' F that convert from celsius.')

number = int (input('Enter number to check positive or negative : '))
if number >= 0:
    if number == 0:
        print('Zero.')
    else:
        print('thus the number u input is positive . ')
else:
    print("Thus the number u input is negative")

number = int(input('Enter num to check number is even or odd : '))
if number>=0:
    if (number%2) ==0:
        print ('The number is Even ')
    else :
        print('The number is Odd ')
elif number<0:
    print("Don't input the negative values ")



# index operator = give access to of a sequence's element (str,list,tuple)
name = "meng huy"
#if (name[7 and 0]. islower()):
#    name = name.capitalize()
#name=name[0].upper()
frist_name= name[0:4].lower()
last_name = name[5:].upper()
print(frist_name)
print(last_name)

#function = is a block of code which executed only when it is call.

def greeting ():
    for i in range (1,11):
        print(i,".Hello world !")
        i+=1
print(greeting())

# return = funtion send python values /object to the caller .
#          These values /object are known as the function's reuturn values



#keyword argument = argument preceded by an <identifier> when we pass them to a finction .
def multiplication(b,c):
    a = b+c
    return a
z= multiplication(23,34)
print(z)
#                   The order of the argument doesn't matter ,unlike "positional arguments" .
#                   Python knows the name of the arguments that our function receives

def name (first,last):
    print( " Hello b*tch , "+first)
    print("Your're name "+first+" " +last)
print(name(last="teth",first="huy"))

#scope= The region that a var is recognized
        # A var is only  avaiable from the region it is created.
        # A global and locally scoped versions of a var can be created.

name = " huy " # global scope (available inside & outside fouction )
def display_name ():
    name = " teth" # local scope (available only inside this fouction)
    print (name)
# display_name()
print (name)


# *args = parameter that will pack all arguments into a tuple
        # useful so that a function can accept a varying amount of argument .
def add(*args):
    sum = 0
    for i in args :
        sum+=i
    return sum
print (add(9,8,7,6,55,4,4))

#**kwargs = parameter that will pack all argument into a dictionary
        #   useful so that a function can accept a varying amount of argument .
def print(**kwargs):
    print("Hello mf ." ,end= " " )
    for key, value in kwargs.items():
        print(value ,end=' ')
print(title= " Mr ",first=" meng",last="huy",end="\n")

#str format() = optional method that gives useer more control when display output .

a = "fox"
b= "dog"

print("\tThe quick {} jumps over the lazy {}.".format(a,b)) #or posistional argument inside  {0,1,2,...}
                                                             # e.g print("my first name {0} and last name {1}".format("huy","meng")
                                                             # output
                                                             #  (  my first name huy and last name meng . )
name =" huy "
#type using
print ("my name is {:10}".format(name)) #{:(value u want to give space behind the str)}
print ("his name is{:>10} ".format(name ))
print("His name is {:<10} ".format(name))
print("His name is {:^10}".format(name))

number = 9000

print("The number of char is: {:.2f}".format(number)) #{:0.2f} is float .
print("the number is : {:,}".format(number))
print("the number convert to binary code : {:b}".format(number))
print ("the number is : {:x}".format(number ))
print( "the  octal number is :{:o}".format(number))

#random section
print('\n\t========>random method<=======')
import random

a = random .randint(1,100)
print( "\n\tYour random number is ",a)
b = random.random()
print( "random :",b)
root =['apple ', ' carry','porie']
c = random.choice(root)
print(c)


#exception = event detected during exexuted that interrupt the flow of a program
try :
    print("Enter number for divide")
    a = int(input("Enter The Number : "))
    b = int(input("Enter second number : "))
    c = a/b
    print("Result = ",c)
except Exception:
    print ("someting wrong !!")
else:
    print("huy")
finally:
    print(" The Execute always work ")

