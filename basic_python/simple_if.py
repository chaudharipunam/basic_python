# 'is' &  '==' are different in 'is' there value same & list ,tupple like this datatype output will be false (because in list , etc there is collection of data )  that's why their address different  
# 'is' use only for single datatype 
x=10
y=10
print(x is y)
z=x
print (z is x)
print(id(x))
print(id(y))
print(id(z))

