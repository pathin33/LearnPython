"""
CHỦ ĐỀ: INPUT & OUTPUT TRONG PYTHON

Mục tiêu:
- Hiểu cách Python nhận dữ liệu đầu vào (input)
- Hiểu cách Python xuất dữ liệu (print)
- Biết input() luôn trả về string
- Biết dùng typecasting để tính toán
- Biết định dạng output với print
"""

# ======================================
# 1. HÀM INPUT() CƠ BẢN
# ======================================
# input() dùng để lấy dữ liệu từ người dùng
# Dữ liệu nhập vào từ bàn phím luôn là STRING

user_input = input("Please enter something: ")
print(user_input)


# ======================================
# 2. INPUT + GÁN VÀO BIẾN
# ======================================

email = input("Please enter your email: ")
print("Your email is:", email)


# ======================================
# 3. NHẬN INPUT NHƯNG KHÔNG XỬ LÝ
# ======================================
# Nếu không gán vào biến thì input chỉ chờ nhập,
# nhưng không có output

# input("Enter a value:")  # thử bỏ comment để test


# ======================================
# 4. NHẬN HAI INPUT LIÊN TIẾP
# ======================================

num1 = input("Please enter a number: ")
num2 = input("Please enter a second number: ")

print(num1, num2)  # in ra theo thứ tự


# ======================================
# 5. INPUT LUÔN LÀ STRING
# ======================================
# Khi cộng string → nối chuỗi

print(num1 + num2)  # ví dụ: 5 + 4 → 54


# ======================================
# 6. TYPECASTING ĐỂ TÍNH TOÁN
# ======================================
# Chuyển string → int

num1_int = int(num1)
num2_int = int(num2)

print(num1_int + num2_int)  # 5 + 4 → 9


# ======================================
# 7. KIỂM TRA KIỂU DỮ LIỆU
# ======================================

print(type(num1))  # <class 'str'>
print(type(num1_int))  # <class 'int'>


# ======================================
# 8. PRINT() VỚI NHIỀU THAM SỐ
# ======================================
# print có thể nhận nhiều giá trị

print("Hello", "you")
print("Hello", "you", sep=", ")
print("Hello", "you", end="!!!\n")


# ======================================
# 9. CONCATENATION TRONG PRINT
# ======================================

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

print("Hello " + first_name + " " + last_name)


# ======================================
# 10. FORMAT STRING (FORMAT METHOD)
# ======================================
# Dùng format() để thay thế biến vào chuỗi

print("Hello {} {}".format(first_name, last_name))


# ======================================
# 11. FORMAT VỚI THỨ TỰ
# ======================================

print("Hello {1} {0}".format(first_name, last_name))


# ======================================
# 12. TỔNG KẾT
# ======================================
"""
- input() dùng để nhận dữ liệu từ người dùng
- input() LUÔN trả về string
- Muốn tính toán → phải typecast (int, float)
- print() có thể:
  + in nhiều giá trị
  + nối chuỗi
  + định dạng output
"""
