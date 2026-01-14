"""
Mục tiêu:
- Hiểu class là gì
- Hiểu object / instance là gì
- Biết attribute (thuộc tính) và method (hành vi)
- Biết cách truy cập biến và hàm thông qua class và instance
"""

# =========================
# 1. ĐỊNH NGHĨA CLASS
# =========================
# class dùng để tạo ra một "kiểu dữ liệu mới"
# ban đầu class chưa có gì thì dùng pass làm placeholder

class MyClass:
    pass


# =========================
# 2. TẠO INSTANCE (KHỞI TẠO ĐỐI TƯỢNG)
# =========================
# MyClass() -> tạo một instance (đối tượng) từ class MyClass

myc = MyClass()   # instance object


# =========================
# 3. THUỘC TÍNH (ATTRIBUTE)
# =========================
# attribute là biến thuộc về class

MyClass.a = 5     # gán biến a cho class


# Truy cập attribute thông qua class
print("Truy cập qua class:", MyClass.a)

# Truy cập attribute thông qua instance
print("Truy cập qua instance:", myc.a)

# Kết luận:
# - instance có thể truy cập attribute của class
# - nếu không có class đứng trước -> Python sẽ báo lỗi


# =========================
# 4. METHOD (HÀNH VI)
# =========================
# method là hàm nằm trong class
# method luôn phải có tham số self

class MyClass2:
    
    def hello(self):
        """
        Method hello
        self: đại diện cho instance đang gọi method
        """
        print("Hello, world!")


# Tạo instance từ class MyClass2
obj = MyClass2()

# Gọi method thông qua instance
obj.hello()

# Lưu ý:
# - Không gọi method trực tiếp bằng class nếu không truyền self
# - obj.hello() tương đương MyClass2.hello(obj)


# =========================
# 5. GIẢI THÍCH SELF
# =========================
# self KHÔNG PHẢI là từ khóa đặc biệt
# self chỉ là quy ước, đại diện cho instance hiện tại

class Counter:
    
    def set_value(self, value):
        self.value = value   # value là attribute của instance
    
    def show_value(self):
        print("Giá trị hiện tại:", self.value)


# Tạo instance
c = Counter()

# Gọi method
c.set_value(10)
c.show_value()


# =========================
# 6. TỔNG KẾT KIẾN THỨC
# =========================
"""
- class: khuôn mẫu (template)
- instance/object: đối tượng được tạo từ class
- attribute: biến trong class
- method: hàm trong class
- self: đại diện cho instance đang làm việc
- mọi thứ trong Python đều là object hoặc kế thừa từ object
"""
