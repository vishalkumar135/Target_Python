
#The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)
#The casefold() method returns a string where all the characters are lower case.
x = txt.casefold()
print(x)
#The center() method will center align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.center(25,"o")
print(x)
#The endswith() method returns True if the string ends with the specified value, otherwise False.
#string.endswith(value, start, end)
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)
x = txt.endswith("my world.", 5, 11)
print(x)

# The find() method finds the first occurrence of the specified value.

# The find() method returns -1 if the value is not found.

# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)
x = txt.find("welcome")
print(x)
x = txt.find("e",5,10)
print(x)
print(txt.find('q'))
print(txt.index("w"))#it will raise the error if it is not found
# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
txt = "Company12"
x = txt.isalnum()
print(x)
txt = "Company 12"
x =(txt.isalnum())
print(x)

# The rfind() method finds the last occurrence of the specified value.

# The rfind() method returns -1 if the value is not found.

# The rfind() method is almost the same as the rindex() method. See example below.

# string.rfind(value, start, end)
txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)
# The startswith() method returns True if the string starts with the specified value, otherwise False.
x = txt.startswith("Hello")
print(x)
# string.startswith(value, start, end)
x = txt.startswith("wel", 7, 20)
print(x)