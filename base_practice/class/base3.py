# コンストラクタ

class SampleClass:
    def __init__(self, msg, name="None"):
        print("コンストラクタが呼ばれました")
        self.msg = msg # インスタンス変数
        self.name = name # インスタンス変数

    def print_msg(self):
        print(self.msg)
    
    def print_name(self):
        print(self.name)


var_1 = SampleClass("Hello", "Taro")
print(var_1.msg)
print(var_1.name)
var_1.print_msg()
var_1.print_name()
