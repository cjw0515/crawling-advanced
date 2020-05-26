# 클래스변수, 인스턴스 변수


class WareHouse:
    # 클래스변수는 인스턴스 전역적으로 공유됨
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수는 공유되지 않음.
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse('kim')
user2 = WareHouse('park')

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(WareHouse.__dict__)

