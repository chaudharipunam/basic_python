#print list.....
list1=[20,5.5,'Hello']
print(list1)

#print list in list(Nested list)......
list2=[['Punu',2003],['Rutu',2004],['Gitu',2005]]
print(list2)

#print list index.....
print(list1[0])

#print index out of list .........then print error
'''print(list1[5])'''

print(list1[-1]) # print (hello) because hello element is on -1 indexing

print(list1[3-1]) #print last element (n-1)

print(list1[-3]) # print (20) because counting of negative indexing from  last 

#print(list1[2])='Good'

'''list operation'''
#concatnation.......join two list using '+' operator  
list3=[2,4,6,8]
print(list1+list3) 

#repetition.........repeat the element in the list using '*' operator
list4=['Hello']
print(list4*5)

#membership........ element is or not in the list given by user.....
list5=['punu','rutu','sonu','minu','monu']
print('purva' in list5) #false....

# & membership............
print('punu' in list5) #true....

# & membership............
print('kajal'not in list5) #true......

# slicing..... indexing 2<4 (element)......
print(list5[2:4])

# & slicing........
print(list5[0:5])   #print up to (n-1)indexing

# & slicing........
print(list5[0:])  #it means print from indexing 0 up to all

# & slicing........
print(list5[:(5)]) #it means print up to (N) from starting.......

# & slicing........
print(list5[:])  #print all elements of list..........

# & slicing........
print(list5[-1])   # print last element... because last element is on -1 indexing

# & slicing........
list5=['punu','rutu','sonu','minu','monu']
print(list5[-2:])  # print (-2) se last tk ke elements 

# & slicing........
print(list5[::-1]) #print all elements form last to start (reverse)

# & slicing........
print(list5[1::-1]) #print elements from indexing 1 to -1 (1,0,-1)  

# & slicing........
print(list5[:-3:-1]) #print elements -2 indexing se last tk

# & slicing........
print(list5[-3::-1])  # -1 se -2 tk ki indexing ko chodke baki ke pure elements print

