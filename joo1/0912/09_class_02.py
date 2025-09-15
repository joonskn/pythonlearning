# 클래스 안에 있는 매소드는 ()안데 self를 필수로 넣어야 한다(내부에서 받는 용도)
class people():
    def make_instance(self):
        self.name = None
        self.age = None
        self.addr = None

h1 = people()
h1.make_instance()      #여기서 self에 h1이 들어간다 self = 가.~ .앞에 있는거(가)
print(h1.__dict__)
h2 = people()
print(h2.addr)