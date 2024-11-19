# Explain list, dictionary, and tuple comprehension with an example.

list = [i for i in range(0,10)]
print(list)

# dictionary Comprehension
dict = {i: i*i for i in range(1,11)}
print(dict)

print(dict.get(11, 12))



# What is the difference between shallow copy and deep copy in Python, and when would you use each?
# In Python, shallow and deep copies are used to duplicate objects, but they handle nested structures differently.

# Shallow Copy: A shallow copy creates a new object but inserts references to the objects found in the original. So, if the original object contains other mutable objects (like lists within lists), the shallow copy will reference the same inner objects. This can lead to unexpected changes if you modify one of those inner objects in either the original or copied structure. You can create a shallow copy using the copy() method or the copy module’s copy() function.

# Deep Copy: A deep copy creates a new object and recursively copies all objects found within the original. This means that even nested structures get duplicated, so changes in one copy don’t affect the other. To create a deep copy, you can use the copy module’s deepcopy() function.