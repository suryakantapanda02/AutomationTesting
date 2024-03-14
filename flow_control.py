#consditional statement:- if,elif,else
#itertional statement
#transfer statement

# if :-
'''
if condtion:
    statement   :- 4 space is known as indentation

if condition is True then excute the if statement

else:
    else is a statement who depends upon if condition, if condition is false then else will execute.
'''

# num = 21
#
# if num%2==0:
#     print('True')
# else:
#     print('False')
# print('Ok')

# num = int(input('Enter your number'))
#
# if num%2==0:
#     print('Even')
# else:
#     print('Odd')

# check a number, number is divisible by both 3 and 5 return True, or False

# num = int(input('Enter your number'))
#
# if num%3==0 or num%5==0:
#     print('True')
# else:
#     print('False')

#check a string , string pallindrom or not.

# str = 'drgjhkl'
# if str == str[::-1]:
#     print('Pallindrom')
# else:
#     print('Not a Pallindrom')

#elif :- if we want a multiple conditional statement then go to elif

# num = int(input('Enter a number:-'))

# if num%2==0:
#     print(num,'is divisiable by 2')
#
# elif num%3==0:
#     print((num,'is divisiable by 3'))
# else:
#     print(num,'is not divisiable by 2 and 3')

# if
# if -else
# if-elif
# if-elif-else

# check if the number divisiable 2 then print number is div by 2 or num is div by 3 the print num is div  by 3
# if num is not div by 2 and 3 print same, if the number div by both 2 and 3 the print same.

# if num%2==0 and num%3==0:
#     print('2 and 3')
#
# elif num%2==0:
#     print('2')
#
# elif num%3==0:
#     print('3')
# else:
#     print('None')

#
# name = input('Enter a city name:-')
# if name == 'BBSR':
#     print('32 degree c')


'''
Interation Statement :- for , while

For :- 

for var in variable_name:
    statement
'''
# st = 'Utkal Keshari'
#
# for i in st:
#     print(i)


# st = 'wertyui'
#
# for i in st:
#     print(i)


# li = [10,20,30,40,50,60]
#
# for i in li:
#     print(i+2)

# li = [10,32,35,65,31,98,78,67,56,55,45,44,38]
#
# even_li = []
# odd_li = []
# for i in li:
#     if i%2==0:
#         even_li.append(i)
#     else:
#         odd_li.append(i)
#
# print(even_li)
# print(odd_li)

# st = 'qwert'
# print(type(st))
#
# li = [10,20,'78','qwertyu',5+9j,[78,89],'dfgh']
#
# for i in li:
#     if type(i)==str:
#         print(i)

# li = [
#     [10,20],
#     [30,40],
#     [50,60]
# ]
#
# for i in li:
#     for j in i:
#         print(j)


# di = {'Name':'Utkala','Age':24,'Salary':67000}
# # print(di.items())
# for k,v in di.items():
#     print(k,v)

#While loop:-
#Conditional Loop
'''
syntax:-

while condition:
    statement
'''

# print(1 to 10)

# num = 1 # 11
#
# while num<=10:
#     print(num)#1,2,3...9,10
#     num = num+1

# while True:
#     print(1)

#add 1 to 10 all number

# num = 1#
# total = 0 # 15
# while num<=10: #
#     total = total+num
#     num = num+1
# print(total)


#nul 1 to 5 all number

# num = 1
# total = 1
# while num<=5:
#     total = total*num
#     num = num+1
# print(total)

#10 to 20 addition and multiplication

# start = 10
# end = 20
# add = 0
# mul = 1
#
# while start <=end:
#     start = start+1
#     add = add+start
#     mul = mul*start
# print('addition',add)
# print('multiplication',mul)

#Transfer Statement :- break, continue and pass

#break :- based on the condition it's breake the loop

# li = ['Ramesh','Suresh','Utkala','Gupta','Rabi','Sahil','Sankar']
#
# for i in li:
#     if i =='Sahil':
#         break
#     print(i)


#continue :- skip
#Based upon the condition it's skip the iteration

# range(1,21)

# for i in range(1,21):
#     if i%2==0:
#         continue
#     print(i)

#pass

# for i in range(1,11):
#     pass
#
# while False:
#     pass
#
# if True:
#     pass


# while , break, continue, pass


# start = 10#20
# end = 20
# mul = 1#10*11*12...*20
#
# while start<=end:
#     mul = mul*start
#     start = start+1
# print(mul)
