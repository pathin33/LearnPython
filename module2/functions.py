"""
Mục đích:
- Giải thích hàm (function) trong Python
- Cách khai báo hàm bằng def
- Truyền tham số (arguments) vào hàm
- Trả dữ liệu ra khỏi hàm bằng return
- Ví dụ thực tế: tính thuế (tax) cho hóa đơn
"""

# =========================
# 1. FUNCTION LÀ GÌ?
# =========================
# Function (hàm) là một khối code có thể tái sử dụng
# Hàm:
# - Nhận dữ liệu đầu vào (input / arguments)
# - Thực hiện một công việc
# - Trả về kết quả (output / return)

# Ví dụ: print() là một hàm
print("Hello World")  # "Hello World" là argument truyền vào hàm print


# =========================
# 2. CÁCH KHAI BÁO HÀM
# =========================
# Cú pháp:
# def ten_ham(tham_so1, tham_so2, ...):
#     code xử lý
#     return kết_quả


# Ví dụ: hàm cộng 2 số
def sum(x, y):
    return x + y


# =========================
# 3. VÍ DỤ KHÔNG DÙNG FUNCTION
# =========================
# Tính thuế cho một hóa đơn (cách làm KHÔNG tối ưu)

bill = 175.00  # Tổng hóa đơn
tax_rate = 15  # Thuế suất (%)

total_tax = bill * tax_rate / 100
print("Total tax:", total_tax)  # 26.25

# Nhược điểm:
# - Muốn tính hóa đơn khác phải sửa biến
# - Không tái sử dụng được


# =========================
# 4. TẠO FUNCTION TÍNH THUẾ
# =========================
# Giải pháp: đưa logic vào function để tái sử dụng


def calculate_tax(bill, tax_rate):
    """
    Hàm tính tiền thuế
    bill: tổng hóa đơn
    tax_rate: phần trăm thuế
    """
    return bill * tax_rate / 100


# =========================
# 5. GỌI FUNCTION
# =========================
# Function chỉ chạy khi được GỌI

print("Total tax:", calculate_tax(175, 15))  # 26.25


# =========================
# 6. TÁI SỬ DỤNG FUNCTION
# =========================

print("Total tax:", calculate_tax(164.33, 22))
# Kết quả: 36.1526


# =========================
# 7. LÀM ĐẸP KẾT QUẢ VỚI round()
# =========================
# round(number, số_chữ_số_thập_phân)

print("Total tax:", round(calculate_tax(164.33, 22), 2))
# Kết quả: 36.15


# =========================
# 8. TÓM TẮT KIẾN THỨC
# =========================
"""
- def dùng để khai báo hàm
- Hàm có thể nhận tham số (arguments)
- return dùng để trả kết quả
- Hàm giúp code:
  + Gọn hơn
  + Dễ bảo trì
  + Tái sử dụng nhiều lần
- Sửa logic 1 lần → mọi nơi gọi hàm đều được cập nhật
"""
