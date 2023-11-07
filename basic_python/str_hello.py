str="Hello, World!"
print(str)  #print string

print(len(str)) #lentgh of str

print(str[0])   #print any char.....

# this is wrong because here we can't replace any diff char into string
# print(str[1])='o'  #wrong

# 1<4 tak hi char print ex(e,l,l)........
print(str[1:4])

# in list (num change/replace)............
list=[1,3,10]
list[1]=50
print(list)

#string concatnation
str="Hello"
str2="World"
str3=str+' '+str2
print(str3)

#concat the string with number.... 
str="Hello"
str2="20"
str3=str+str2
print(str3)

#one way print the whole sentence 
f_name='Poonam'
l_name='Chaudhary'
age='20'
print(f'My first Name is {f_name} & My Last Name is {l_name} & My age is {age}')
