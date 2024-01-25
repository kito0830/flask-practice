# インスタンス変数、クラス変数

class SampleA():
    class_val = 'class val' # クラス変数

    def set_val(self):
        self.instance_val = 'instance val' # インスタンス変数


    def print_val(self):
        print('クラス変数 = {}'.format(self.class_val))
        print('インスタンス変数 = {}'.format(self.instance_val))

isinstance_a = SampleA()
isinstance_a.set_val()
print(isinstance_a.instance_val)
isinstance_a.print_val()
print(SampleA.class_val)
print(isinstance_a.__class__.class_val)

instance_b = SampleA() # インスタンス化
instance_b.set_val()
instance_b.print_val()

# クラス変数を変更すると他のインスタンスにも影響するので注意
isinstance_a.__class__.class_val = 'class val 2' 

print(instance_b.__class__.class_val)
print(isinstance_a.__class__.class_val)
