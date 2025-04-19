class myClass:
    __privateVar=27
        
    def __privateMeth(self):
        print("I am in the class")
    def hello(self):
        print("Private Variable is: ",myClass.__privateVar)
obj=myClass()
obj.hello()
obj.__privateMeth()
