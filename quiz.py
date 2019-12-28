def increment(num):
    return num + 1
 
def square(num):
    return num * num
 
nine = square(increment(2))
five = increment(square(2))
 
class NumHooker:
    def __init__(self):
        self.funclist = list()
        self.add(lambda x: x)
    def __call__(self, num):
        result = num
        for each_func in self.funclist:
            result = each_func(result)
        return result
    def add(self, func):
        self.funclist.append(func)
 
incsquare = NumHooker()
incsquare.add(increment)
incsquare.add(square)
 
five = incsquare(2)

