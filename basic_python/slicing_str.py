s='Gate Smashers'

#print indexwise 5<10
print(s[5:10])

# print all char from starting up to 10.......
print(s[:10])

#print from 5 to all char up to end........ 
print(s[5:])

#print all from starting to end
print(s[:])

#print (count from upper side)   
print(s[-8:-3])

#print reverse from ending to starting.....
print(s[::-1])

#print char, those start from 5 (index) & left one char then again print char...... 
print(s[5::2])

#print all char from 5 to 12 ,but in upper case
print(s[5:12].upper())

#print all char from 5 to 12 ,but in lower case
print(s[5:12].lower())

#print lentgh of string.......
print(len(s))

#print 1st letter capital & then rest of char small letter of every word .........
print (s.title())

#count()
#print count the Hello word in the string.....
st='Hello World! Hello Hello'
print(st.count('Hello'))

#& count()
#print count the Hello word in the string given the length (3 to 30)....
print(st.count('Hello',3,30))

#find()
#print find the indexing of that word , those user  give ('Hello')
print(st.find('Hello',15,25))

#index()
#print find the indexing of that word , those user  give ('Hello') if word not find then print('substring not found)
print(st.index('Hello'))
#print(st.index('Hee')) #print (substring not found)

#endswith()
st1='Hello World!'
print(st1.endswith('ld!'))  #print (true) because end of string same char 
print(st1.endswith('lde'))  #print (false) because end of string not same char 

#startswith()
print(st1.startswith('Hee'))  #print (true) because start of string same char 
print(st1.startswith('He'))  #print (false) because start of string not same char 

#isalnum()
print(st1.isalnum()) #there shouldn't special char... 

# & isalnum()
q='Rutu123'
print(q.isalnum()) # there is no special char.......

#isspace
w=' \n \t '
print(w.isspace())  #there shouldn't char / num

e='Hello  \n'
print(e.isspace())  # it's wrong

#islower()
r='hello world!'
print(r.islower()) # check lowercase alphabet

#isupper()
t='HELLO WORLD!'
print(t.isupper())  # check uppercase alphabet

#istitle()
print(st1.istitle()) #check 1st letter of every word is capital or not....

#lstrip()
y=' Hello World! ' 
print(y.lstrip())  # if in left side, there is space, then remove that space then print

#rstrip()
print(y.rstrip())  # if in right side, there is space, then remove that space then print

#strip()
print(y.strip())  # if in left side, there is space, then remove that space then print

#replace()
print(st1.replace('o','*')) #replace old string/word/num/char/special char into new string

# &replace()
i='poonam is very beautiful'
print(i.replace('beautiful','pretty')) 

#join()
k='-'
print(k.join(st1))  # join the 2 string by seperator...

#partition()
print(i.partition('is'))  #divide in 3 parts if find that word, those given by user , then 
    #  printlike this ---   ('poonam ', 'is', ' very beautiful')
 
# split()   
print(i.split()) # without use char in split bracket,,,, print like this---['poonam', 'is', 'very', 'beautiful'] 

# & split()
d='India is a Great Country'
print(d.split('a')) # without use char in split bracket,,,, print like this---['Indi', ' is ', ' Gre', 't Country']

# & split()
print(i.split('a'))
#['poon', 'm is very be', 'utiful']----output