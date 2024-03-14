# age = 27
# print(type(age))

#int
# -infinity to +infinity all the whole numbers know as integer number
'''
ex:- 57, 89, 999, 12345678, -5678, -567, -12, 90, 0
'''

#float
'''
-infinity to +infinity all the decimal numbers know as flot number
'''
# num = 90.0
# print(type(num))

'''
ex:- -90.8, -456789.56789, 0.0 , 45.789,78.5678,234567890.6789
'''

#Complex
'''
complex is combination real number and imaginary number
real number :- int number(whole) or float number(decimal) know as real number 
imaginary :- realnumber but addition with j
'''

# c1 = 5+9j
# print(type(c1))
'''
-5+(-9j) , -5+9.6j, 6.8+4j, 0+0j
real part add with only real part and imaginary part add with imag =inary part.
'''
# c2 = 7+5j
# print(c1+c2)

#boolean :- bool(True, False)
'''if we ask something it's coorect or not, if it correct then boolean retuens True, if not returns False'''
# print(10<20)
# print(20==20)
# print(90<56)

'''if some object is present or not, if it is present then True, if not then False'''
#
# li = [10,20,30,40]
# print(40 in li)
# print(56 in li)

# print(True+True)
# print(True+False)
# print(False+False)

'''Hence, Proved True is always 1 and False is always 0.'''

# a = 10+20j
# b = 10.5+20.5j
# print(a+b)


#Garbage Collection
#
# a = 10
# print('a',id(a))
# a = 20
# print(a)
#
# print(id(10))
# print(id(20))

#5 String
#
# single cot, double cot, and threeple cot
#
# '', "" , ''' ''', """ """

# var = 'qwertyWERDFGH4356789#$%^&*'
# print(type(var))

# var = '' # empty str
# print(type(var))

# single cot and double cot only use when we will declare a data in variable

# var1 = 'qwerty'
# var2 = "qwerty"

#triple cot know as doc string.

# def addition:
#     '''this function written for addition two number'''


#string slicing
s = 'qwerty'

#indexing :- position of each element in a string
#there are two types indexing , +ve(Left to right) , -ve index)(right to left)
#python is zero base indexing

'''
-6  -5    -4      -3     -2    -1
Q    W      E      R     T      Y
0    1      2      3     4      5

'''

'''
variable_name[start_po:end_po+1:steps]
'''
s = 'qwerty'
# s_slice = s[0:4:1]
# print(s_slice)
# print(s[2:5])
# print(s[-4:-1])
# print(s[-4:-1])
# print(s[2:])

# name = 'Suryakanta'
# dob = '12/12/1912'
# print(name[0:4]+dob[-4:])

s = 'qweRtY'
# print(dir(s))
'''
('capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 
 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 
 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill')
'''

# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.startswith('q'))
# print(s.endswith('Y'))

# s = '    qedfgh    '
# print(s.strip())

#count
# s = 'i love india'
# # print(len(s))
# print(s.count('i'))

#find and index
# s = 'i love india'
# print(s.find('ia'))
# print(s.index('ia'))
# print(s.find('z'))
# print(s.index('z'))

#split,join

#format
# a = 10
# b = 20
# c = a+b
# print(f'addition data is :- {c}')

#-------------------------------------------------
# List :- []
'''1.Hetrogeous object 
2.Every element separate with another element with help comma(,)
3. it's growable in nature
4.list is accepting the index concept.
var = single_data
'''
# var = [1,78.89,6+9j,True,'ertyui',[56,89]]
# print(type(var))
#
# li = [1,2,3,4,5]
# # print(li[-1])
# li[2] = 30
# print(li)
#
# mutable and immutable

# li = [1,2,3]
# print(dir(li))

# append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# li.append('qwertyu')
# print(li)

# li.insert(1,45)
# print(li)

# li.clear()
# print(li)

# li_dup = li.copy()
# print(li_dup)

# li = [1,2,3,1,1,2,1,2,3,4,5]
# print(li.count(4))
# print(li.index(1))

# li_1 = [1,2,3]
# li_2 = [4,5,6]
# li_1.extend(li_2)
# print(li_1)
# print(li_2)

# li= [1,2,3]
# print(li.pop())
# print(li)

#remove
# li = [1,1,2,3,1,2,4]
# li.remove(1)
# li.remove(1)
# print(li)

#sort

# li = [78,67,90,98,76,45,43,54,23,11,67,34,41]
# li.sort(reverse=True)
# print(li)
#
# #reverse
# li = [78,67,90,98,76,45,43,54,23,11,67,34,41]
# li.reverse()
# print(li)

#string -- split and join

# str_name = 'Rabi Sankar Gupta Janee Subha Khitish Utkal'
# var = str_name.split(' ')
# print(var)

# l = ['Rabi', 'Sankar', 'Gupta', 'Janee', 'Subha', 'Khitish', 'Utkal']
# st = '-'.join(l)
# print(st)

#tuple :- () tuple is immutable data type
# same as list hetrogeneous, seprate with comma and do indexing

# t = (1,2,3)
# print(type(t))
# print(dir(t))

#Range :- it's generating sequence of number
# formual :- (start, end+1, step)
# range(10) :- 0,1,2,3,4,5,6,7,8,9
# range(10,21)
# range(10,21,2)
# print(range(10))

# for i in range(10):
#     print(i)


#set, frozenset,bytes, bytearray :- 10mints

# imp data type:- str, list, range, dict

# class:- 6

# se = {1,5.8,9+9j,'dfghj',True,{1,2,1}}
# print(type(se))

# set is partial allow hetrogeneous objects
#set is not allowed duplicate value

# li = [1,1,2,3,4,1,1,2,2]
# print(li)
# se = {1,1,2,3,4,1,1,2,2,45,87,123,89,345,'567m'}
# print(se)
# print(dir(se))

#Type casting
# convert one data type to another data type know as type casting

# int,float,complex,boolean ---
#
# string
#
# list,tuple,set,frozenset,bytes,bytearray,dictionary


# a = 10
# b = float(a)
# print(b)
# print(type(b))


# fronzenset
# li = [1,2,3,1,2,3,1,2,3]
# fz = frozenset(li)
# print(fz)

# #bytes(im) and bytearray(m) :- 0-255
# li = [10,29,34,254,255]
# b = bytearray(li)
# print(b)

#Dictionary :-
'''
Name   Age   Salary 
A      25     56k
B      27     67k
C      28     45k
'''

# di = {key:value} # key is always unique like columns and it's accept only immutable data type
# and vales may be duplicate and it's accept both mutable and immutable data type

# di = {'Name':'A','Age':25,'Salary':56000}
# print(di)
# print(type(di))

# di = {'Name':'A','Age':25,'Salary':56000}
#Values
# variable_name['Key_name']
# print(di['Age'])
# di['Salary']= 72000
# print(di)

# method of dictionary
# di = {'Name':'A','Age':25,'Salary':56000}
# print(dir(di))
# clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

#clear
# di.clear()
# print(di)

#copy
# b = di.copy()
# print(b)

#get
# print(di.get('Name'))

#items
# print(di.items())

# #keys
# print(di.keys())

#values
# print(di.values())

#setdefault
# di.setdefault('department','QA')
# print(di)

#update
# di.update({'dept':'QA','id':'101','HR':'SWADHA'})
# print(di)

#popitem
# di.popitem()
# print(di)

#pop
# di.pop('Name')
# print(di)


#None :-

# def f1():
#     a = 10
#
# print(f1())








