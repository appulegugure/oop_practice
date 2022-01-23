"""
データ型の宣言：Username
    属性:
        実際にユーザー名
    ルール:
        ユーザー名は4文字以上20文字いない
    できること:
        ユーザー名を大文字に変換する。
"""


class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError('{0}はルール違反です。'.format(name))
        self.name = name

    def screen_name(self):
        return self.name.upper()


bob = UserName(name='bobsmith')
tom = UserName(name='tommaron')


print(bob.name)
print(bob.screen_name())
print(bob.name)
print(tom.name)
print(tom.screen_name())
print(tom.name)
