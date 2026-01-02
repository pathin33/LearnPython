"""

Mục tiêu:
- Hiểu map và filter dùng để làm gì
- Phân biệt sự khác nhau giữa map và filter
- Hiểu vì sao filter không trả về None
- Ghi nhớ cú pháp chuẩn khi dùng map / filter

-------------------------------------------
1. BÀI TOÁN
-------------------------------------------
- Có một danh sách menu các loại cà phê
- Muốn lấy ra những cà phê bắt đầu bằng chữ 'C'
"""

# ------------------------------------------
# 2. DỮ LIỆU BAN ĐẦU
# ------------------------------------------

menu = [
    "espresso",
    "latte",
    "cappuccino",
    "mocha",
    "cortado",
    "americano"
]


# ------------------------------------------
# 3. HÀM KIỂM TRA (DÙNG CHO MAP & FILTER)
# ------------------------------------------

def find_coffee(coffee):
    """
    Hàm kiểm tra:
    - Nếu tên cà phê bắt đầu bằng 'C' -> trả về coffee
    - Ngược lại -> không trả gì (None)
    """
    if coffee[0] == "c" or coffee[0] == "C":
        return coffee


"""
Lưu ý:
- Hàm này KHÔNG phải pure function chuẩn,
  nhưng dùng tốt cho việc minh họa map và filter
"""


# ------------------------------------------
# 4. MAP FUNCTION
# ------------------------------------------

"""
MAP:
- Áp dụng hàm cho TẤT CẢ phần tử trong list
- Trả về kết quả cho MỖI phần tử
- Nếu hàm không return -> kết quả là None
"""

map_coffee = map(find_coffee, menu)

print("Kết quả map (chưa iterate):", map_coffee)

print("\nKết quả map sau khi iterate:")
for x in map_coffee:
    print(x)


"""
Kết quả sẽ là:
None
None
cappuccino
None
cortado
None

Giải thích:
- map chạy qua TẤT CẢ phần tử
- Phần tử không thỏa điều kiện -> return None
"""


# ------------------------------------------
# 5. FILTER FUNCTION
# ------------------------------------------

"""
FILTER:
- Áp dụng hàm cho TẤT CẢ phần tử
- CHỈ GIỮ LẠI phần tử mà hàm trả về True / giá trị hợp lệ
- Không có None trong kết quả
"""

filter_coffee = filter(find_coffee, menu)

print("\nKết quả filter (chưa iterate):", filter_coffee)

print("\nKết quả filter sau khi iterate:")
for x in filter_coffee:
    print(x)


"""
Kết quả:
cappuccino
cortado

Giải thích:
- filter chỉ giữ lại giá trị mà hàm trả về là True
- None bị loại bỏ hoàn toàn
"""


# ------------------------------------------
# 6. SO SÁNH MAP vs FILTER (RẤT QUAN TRỌNG)
# ------------------------------------------

"""
MAP:
- Biến đổi dữ liệu
- Giữ nguyên số lượng phần tử
- Có thể sinh ra None

FILTER:
- LỌC dữ liệu
- Giảm số lượng phần tử
- Không có None
"""


# ------------------------------------------
# 7. CÁCH VIẾT NGẮN GỌN HƠN (HAY DÙNG)
# ------------------------------------------

"""
Trong thực tế, filter thường dùng với hàm trả về True / False
"""

def starts_with_c(coffee):
    return coffee.lower().startswith("c")

filtered_menu = list(filter(starts_with_c, menu))

print("\nFilter viết gọn hơn:", filtered_menu)


"""
-------------------------------------------
8. TÓM TẮT ĐỂ NHỚ
-------------------------------------------

- map(function, list):
  + Dùng khi muốn BIẾN ĐỔI dữ liệu
  + Mỗi phần tử -> 1 kết quả

- filter(function, list):
  + Dùng khi muốn LỌC dữ liệu
  + Chỉ giữ phần tử thỏa điều kiện

- Cả map và filter:
  + Không cần viết for-loop
  + Đúng tinh thần functional programming
"""
