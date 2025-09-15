# 클래스 안에 있는 매소드는 ()안데 self를 필수로 넣어야 한다(내부에서 받는 용도)
class Product():
    serial_num = 0
    def __init__(self):
        Product.serial_num += 1
        self.serial_num = Product.serial_num
        self.name = None

tv1 = Product()
tv2 = Product()
tv3 = Product()

print(tv3)

# __~__ 콜백(이벤트)함수 어떤 상황이 되면 호출 됨

