#MRO kieu nhu la ban do chi duong cho ta biet cac lop ke thua nhu nao
class A:
    def hien_thi(self):
        print("Hàm từ lớp A")

class B(A):
    def hien_thi(self):
        print("Hàm từ lớp B")

class C(A):
    def hien_thi(self):
        print("Hàm từ lớp C")

class D(B, C):
    pass

class E(D):
    pass
e = E()
e.hien_thi()
#do B và C là 2 class đều có phương thức giống tên nhau và để là lớp cha của E 
#thì python sẽ tuân theo MRO để thực thi xem cái nào sẽ được gọi 


#Ta se dung ham nay de hien ra so do cac lop ke thua theo thu tu
print(E.mro())
#[<class '__main__.E'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#=> Ta thay la class B truoc class C len phuong thuc cua lop B se duoc in ra truoc