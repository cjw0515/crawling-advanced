class SelfTest:
    @staticmethod
    def fn1():
        print("func 1 called")
    def fn2(self):
        print("func 2 called")


f = SelfTest()
print(dir(f))
f.fn1()
f.fn2()