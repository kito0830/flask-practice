#inner関数
def outer():
    def inner():
        print('inner')

    inner()

outer()
