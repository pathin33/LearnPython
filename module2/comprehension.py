"""

Mục tiêu của file này:
- Hiểu comprehension là gì
- Biết 4 loại comprehension trong Python
- Hiểu khi nào dùng list / dict / set / generator
- So sánh comprehension với for-loop và map

----------------------------------------------------
1. COMPREHENSION LÀ GÌ?
----------------------------------------------------
Comprehension là cách tạo MỘT sequence mới
từ MỘT sequence có sẵn bằng cú pháp ngắn gọn.

Tư duy chung:
"Lấy từng phần tử -> lọc / biến đổi -> tạo dữ liệu mới"
"""


# ==================================================
# 2. LIST COMPREHENSION
# ==================================================

"""
Cú pháp chuẩn:
[expression for x in sequence if condition]
"""

data = [2, 3, 5, 7, 11, 13, 17, 19]

# --- Ví dụ 1: Biến đổi dữ liệu ---
plus_three = [x + 3 for x in data]
print("Add 3:", plus_three)

# --- Ví dụ 2: Tạo list mới ---
double = [x * 2 for x in data]
print("Double:", double)

# --- Ví dụ 3: Lọc dữ liệu ---
div_by_four = [x for x in double if x % 4 == 0]
print("Divisible by 4:", div_by_four)

# --- Ví dụ 4: Lọc + biến đổi ---
div_by_four_minus_one = [x - 1 for x in double if x % 4 == 0]
print("Divisible by 4 minus 1:", div_by_four_minus_one)

# --- Ví dụ 5: Dùng range ---
nines = [x for x in range(100) if x % 9 == 0]
print("Nines:", nines)


"""
So sánh với for-loop (cùng logic):
"""

result = []
for x in data:
    result.append(x + 3)
print("For-loop add 3:", result)


# ==================================================
# 3. DICTIONARY COMPREHENSION
# ==================================================

"""
Cú pháp:
{key: value for x in sequence if condition}
"""

# --- Ví dụ 1: Từ range ---
square_dict = {x: x * x for x in range(5)}
print("Square dict:", square_dict)

# --- Ví dụ 2: Từ một list ---
numbers = [1, 2, 3, 4, 5]
num_dict = {x: x ** 2 for x in numbers}
print("Number dict:", num_dict)

# --- Ví dụ 3: Từ hai list (dùng zip) ---
months = ["Jan", "Feb", "Mar", "Apr", "May"]
month_dict = {i + 1: month for i, month in enumerate(months)}
print("Month dict:", month_dict)

# Cách khác dùng zip
month_dict_zip = {k: v for k, v in zip(range(1, 6), months)}
print("Month dict (zip):", month_dict_zip)


"""
Lưu ý:
- zip ghép từng cặp
- List ngắn hơn quyết định độ dài dict
"""


# ==================================================
# 4. SET COMPREHENSION
# ==================================================

"""
Set comprehension:
- Giống list comprehension
- Dùng {}
- Không có phần tử trùng
"""

set_data = {x for x in range(10, 20) if x not in [12, 14, 16]}
print("Set comprehension:", set_data)


# ==================================================
# 5. GENERATOR COMPREHENSION
# ==================================================

"""
Generator comprehension:
- Giống list comprehension
- Dùng ()
- Sinh dữ liệu khi cần (tiết kiệm bộ nhớ)
"""

gen_data = (x * 2 for x in data)

print("Generator object:", gen_data)
print("Generator type:", type(gen_data))

print("Iterating generator:")
for item in gen_data:
    print(item, end=" ")

print("\n")


"""
Lưu ý:
- Generator KHÔNG lưu toàn bộ dữ liệu
- Chỉ dùng được MỘT LẦN
"""


# ==================================================
# 6. SO SÁNH MAP vs LIST COMPREHENSION
# ==================================================

def square(num):
    return num * 2

# --- map ---
map_result = map(square, data)
print("Map result:", list(map_result))

# --- list comprehension ---
list_comp_result = [square(x) for x in data]
print("List comprehension result:", list_comp_result)


"""
So sánh:
- map() -> iterator
- list comprehension -> list

map:
- Tốt cho dữ liệu lớn
- Phong cách functional

list comprehension:
- Pythonic
- Dễ đọc, dễ hiểu
"""


# ==================================================
# 7. KHI NÀO DÙNG LOẠI NÀO?
# ==================================================

"""
LIST COMPREHENSION:
- Dùng nhiều nhất
- Khi cần list ngay
- Code rõ ràng

DICT COMPREHENSION:
- Khi cần map key-value

SET COMPREHENSION:
- Khi cần dữ liệu không trùng

GENERATOR COMPREHENSION:
- Khi dữ liệu rất lớn
- Quan tâm đến bộ nhớ

MAP / FILTER:
- Khi xử lý pipeline dữ liệu lớn
"""


# ==================================================
# 8. TÓM TẮT CUỐI FILE
# ==================================================

"""
COMPREHENSION = FOR + IF + BIẾN ĐỔI
viết gọn, rõ, đúng phong cách Python

Đây là kỹ năng RẤT QUAN TRỌNG
khi học functional programming trong Python.
"""

