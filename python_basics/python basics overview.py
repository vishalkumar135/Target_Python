# name  = input("what is your\n")
# print(name)
x = str(3)
y = int(3)
z = float(3)
print(x,y,z)
#Slicing
b = "hello World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
#upper case
print(b.upper())
print(b.lower())
a = " Hello, World! "
print(a.strip())#returns "hello World"
# replace string
print(a.replace("H","V"))
#Split String
aa =(a.split(","))
print(aa)
print(type(aa))

#String Concatenation
a = "hello"
b = "World"
c = a+b
print(c)
c = a+ " " + b
print(c)

#String Format
age  = 36
txt = "MY name is john , i am  {}"
print(txt.format(age))

quantity = 3
itemno = 56
price  = 49.95
myorder = "I want {} pieces of item {} for {} dollars. "
print(myorder.format(quantity,itemno,price))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))

#Escape Character

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
txt = 'It\'s alright'
print(txt)
txt = "this will insert one \\ (backslash)"
print(txt)
# carriage Return
txt = "hello\rWorld!"
print(txt)
