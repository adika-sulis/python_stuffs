import aTools as t
import os # not necessary
os.system("cls") # not necessary

x = t.pinput("Enter a number: ", "kg")
# for instance input is 10 kg
print(x) # 10
print(type(x)) # <class 'int'>
y = t.pinput("Enter a list: ", "list")
# for instance input is list[1, 2, 3]
print(y) # [1, 2, 3]
print(type(y)) # <class 'list'>
y = t.pinput("What is 1.01 + 2.13: ")
# for instance input is 3.14
print(y) # 3.14
print(type(y)) # <class 'float'>