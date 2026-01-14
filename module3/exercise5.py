# Import ABC và abstractmethod từ module abc (abc là viết tắt của abstract base classes)
from abc import ABC, abstractmethod

# Lớp Bank
class Bank(ABC):
    """ Một lớp ngân hàng trừu tượng (abstract)

    [CẦN CÀI ĐẶT]
        1. Lớp này phải kế thừa từ lớp ABC
        2. Viết hàm basicinfo() để in ra "This is a generic bank" và
           trả về chuỗi "Generic bank: 0"
        3. Định nghĩa thêm một hàm thứ hai tên là withdraw và để trống
           bằng cách dùng từ khóa `pass`.
           Đánh dấu hàm này là abstract bằng cách thêm `@abstractmethod`
           ngay phía trên khai báo hàm.
    """
    ### WRITE YOUR CODE HERE
    def basicinfo():
        print("This is a generic bank")
        return "Generic bank: 0"
    @abstractmethod
    def withdraw():
        pass

# Lớp Swiss
class Swiss(Bank):
    """ Một loại ngân hàng cụ thể kế thừa từ lớp Bank

    [CẦN CÀI ĐẶT]
        1. Lớp này phải kế thừa từ lớp Bank
        2. Tạo constructor cho lớp này để khởi tạo
           biến `bal` (số dư) với giá trị ban đầu là 1000
        3. Cài đặt lại hàm basicinfo() sao cho in ra
           "This is the Swiss Bank" và trả về chuỗi
           "Swiss Bank: " (chú ý có khoảng trắng sau dấu hai chấm)
           theo sau là số dư hiện tại của ngân hàng.

           Ví dụ: nếu self.bal = 80 thì trả về "Swiss Bank: 80"

        4. Cài đặt hàm withdraw nhận thêm một tham số
           (ngoài self) là một số nguyên, đại diện cho số tiền rút.
           Trừ số tiền rút khỏi biến bal, in ra:
           "Withdrawn amount: {amount}"
           và in ra:
           "New Balance: {self.bal}", sau đó trả về số dư mới.

           Lưu ý: Phải kiểm tra xem có đủ tiền để rút hay không!
                 Nếu số tiền rút lớn hơn số dư hiện tại thì
                 KHÔNG trừ tiền.
                 Thay vào đó, in ra dòng:
                 "Insufficient funds"
                 và trả về số dư ban đầu.
    """
    ### WRITE YOUR CODE HERE
    def __init__(self):
        super().__init__()
        self.bal = 1000
    def basicinfo(self):
        print("This is the Swiss Bank")
        return f"Swiss Bank: {self.bal}"
    def withdraw(self,amount):
        if(self.bal<amount):
            print("Insufficient funds")
            return self.bal
        print(f"Withdrawn amount: {amount}\n"+f"New Balance: {self.bal-amount}")
        
        



# Code chạy chính
def main():
    assert issubclass(Bank, ABC)
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()
