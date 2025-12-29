"""
1. Dictionary trong Python là gì?
--------------------------------
Dictionary (từ điển) là một kiểu dữ liệu dùng để lưu trữ dữ liệu
dưới dạng CẶP KEY - VALUE (khóa - giá trị).

Cách hoạt động của dictionary giống với từ điển ngoài đời:
- Bạn tra từ theo "từ khóa" (key)
- Python trả về "giá trị" (value)

Khác với list:
- List truy cập bằng chỉ số (index)
- Dictionary truy cập bằng khóa (key)

=> Dictionary nhanh hơn list khi cần tìm kiếm dữ liệu.
"""

# --------------------------------------------------
# 2. Khởi tạo dictionary
# --------------------------------------------------

# Dictionary rỗng
my_d = {}

print(type(my_d))  # <class 'dict'>


"""
3. Thêm dữ liệu vào dictionary
------------------------------
Cú pháp:
dictionary[key] = value
"""

my_d[1] = "test"        # key là số
my_d["name"] = "Jim"    # key là chuỗi

print(my_d)
# {1: 'test', 'name': 'Jim'}


"""
4. Truy cập giá trị trong dictionary
------------------------------------
Cú pháp:
dictionary[key]
"""

print(my_d[1])       # test
print(my_d["name"])  # Jim


"""
5. Thêm mới hoặc cập nhật giá trị
---------------------------------
- Nếu key CHƯA tồn tại → thêm mới
- Nếu key ĐÃ tồn tại → cập nhật giá trị
"""

# Thêm key mới
my_d[2] = "test 2"
print(my_d)

# Cập nhật key cũ
my_d[1] = "not a test"
print(my_d)


"""
6. Lưu ý quan trọng: KHÔNG có key trùng lặp
-------------------------------------------
- Dictionary không cho phép trùng key
- Nếu gán trùng key → giá trị cũ bị ghi đè
"""

my_d[1] = "overwrite value"
print(my_d)
# key 1 chỉ xuất hiện 1 lần


"""
7. Xóa phần tử trong dictionary
-------------------------------
Cú pháp:
del dictionary[key]
"""

del my_d[1]
print(my_d)


"""
8. Duyệt dictionary (Iteration)
--------------------------------
"""

# 8.1 Duyệt key (mặc định)
for x in my_d:
    print(x)
# Chỉ in ra key


"""
8.2 Duyệt cả key và value bằng items()
--------------------------------------
"""

for key, value in my_d.items():
    print(str(key) + " : " + value)


"""
8.3 Duyệt chỉ value bằng values()
---------------------------------
"""

for value in my_d.values():
    print(value)


"""
9. Tổng kết
-----------
✔ Dictionary lưu dữ liệu dưới dạng key - value
✔ Truy cập nhanh hơn list
✔ Key có thể là int, string (hoặc immutable type)
✔ Value có thể thay đổi
✔ Không cho phép trùng key
✔ Rất phổ biến trong thực tế:
  - JSON
  - API response
  - Cấu hình
  - Mapping dữ liệu
"""

