##Classes
print("-------------Classes-------------")
class Cookie:
    def __init__(self,color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self,color):
        self.color = color


cookie_one = Cookie("brown")

cookie_two = Cookie("black")

print(cookie_one.get_color())

print(cookie_two.get_color())

cookie_one.set_color("green")

print(cookie_one.get_color())
print(cookie_two.get_color())

##Pointers
print("-------------Pointers-------------")
num1 = 11

num2 = num1

print("Before num2 change:")
print("num1:",num1)
print("num2:",num2)

print("\nnum1 pointer:",id(num1))
print("num2 pointer:",id(num2))

num2 = 22

print("\nAfter num2 change:")
print("num1:",num1)
print("num2:",num2)
print("num1 pointer:",id(num1))
print("num2 pointer:",id(num2))


dict1 = {"value":11}

dict2 = dict1

print("\nBefore dict2 change:")
print("dict1:",dict1)
print("dict2:",dict2)   
print("\ndict1 pointer:",id(dict1))
print("dict2 pointer:",id(dict2))

dict2["value"] = 22
print("\nAfter dict2 change:")
print("dict1:",dict1)
print("dict2:",dict2)
print("dict1 pointer:",id(dict1))
print("dict2 pointer:",id(dict2))

dict3 = {"value":33}
dict1 = dict3
print("\nAfter dict1 reassignment:")
print("dict2:",dict2)
print("dict2 pointer:",id(dict2))

print("\nAfter dict2 reassignment:")
dict2 = dict1


print("dict1:",dict1)
print("dict2:",dict2)
print("dict1 pointer:",id(dict1))
print("dict2 pointer:",id(dict2))