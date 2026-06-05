class TestAccount:

    testString = "Hello World"

    def __init__(self,testVar1:"Var1", testVar2:1.0):
        self.var1=testVar1
        self.var2=testVar2

    def displayVar1(self):
        return "Var 1:" + self.var1
    def displayVar2(self):
        return "Var2: " +str(self.var2)
    def incrementVar2(self,increment:0.0):
            self.var2 += increment
            return "Var2 is now: " + str(self.var2)

