class NameTest:
    total = 0

print(dir())
print("before: ", NameTest.__dict__)
NameTest.total = 1
print("after: ", NameTest.__dict__)


n1 = NameTest()
n2 = NameTest()
# 네임스페이스 찾는 순서 - 인스턴스의 네임스페이스 -> 클래스의 네임스페이스
print(id(n1), 'vs', id(n2))
print(n1.__dict__)
print(n2.__dict__)

n1.total = 77
print(n1.__dict__)
print(n2.__dict__)

print(n1.total)
print(n2.total)