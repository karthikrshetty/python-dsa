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