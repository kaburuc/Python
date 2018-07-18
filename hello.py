#!/usr/bin/env python
print ("Hello, World!")
print ("Good Morning Cephas\n")
msg = "python is Easy!"

print (msg)

for i in range(0,1):
    print(msg.capitalize())

#the subtype are int, long, float and complex
mystring = "Hi, I'm a string!"

print ("Hello World, \n")
print ("Python is so cool!")

mylist = [42, 'apple', u'unicode apple', 5234656]
print (mylist)
mylist[2] = 'banana'
print (mylist)
mylist[3] = [['item1', 'item2']]
print (mylist.pop())

mylist = ["spam", "eggs", "toast"] #list of strings
status = "eggs" in mylist
lenth = len(mylist)
print(status)
print(lenth)

mynewlist = ["coffee", "tea"]
print(mylist + mynewlist)

mytuple = tuple(mynewlist)
print(mytuple)

print(mytuple.index("tea"))
mylonglist = ['spam', 'eggs', 'toast', 'coffee', 'tea']
print(mylonglist[2:1])
