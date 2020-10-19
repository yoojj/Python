# packing 
numbers = 1, 2, 3, 4, 5
print(numbers)
print(type(numbers))


# unpacking 
(n1, n2, n3, n4, n5) = numbers 
print(n1, n2, n3, n4, n5)
print(type(n1))



obj = {'a':1, 'b':2}

key = [*obj] 
print(key)
print(type(key))

keyValue = {**obj}
print(keyValue)

keyValue = {**obj, 'b':20}
print(keyValue)



x = [1, 2, 3, 4, 5]
y = x
z = [*x]

print((x is y) == True)
print((x is z) == False)

