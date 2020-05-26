class UserInfo:
    # def set_info(self, name, phone):
    #     self.name = name
    #     self.phone = phone
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("--------------------")
        print("name : ", self.name)
        print("phone : ", self.phone)
        print("--------------------")

    def __del__(self):
        # 메모리에서 삭제될 때 콜 될 메서드
        print("delete")
#
# user1 = UserInfo()
# user2 = UserInfo()
#
# print(id(user1))
# print(id(user2))
#
# user1.set_info('kim', '0104957280')
# user2.set_info('park', '34526340')
#
# user1.print_info()
# user2.print_info()
#
# # namespace
# print(user1.__dict__)
# print(user2.__dict__)
# print(user1.name)
# print(user1.phone)

user1 = UserInfo("kim", "01054894512")
user2 = UserInfo("park", "01054894512")