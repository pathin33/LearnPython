"""
Mục đích:
- Giải thích List trong Python
- Cách khai báo list
- Truy cập phần tử theo index
- List lồng nhau (nested list)
- Thêm, xóa, sửa phần tử trong list
- Duyệt list bằng vòng lặp
"""

# =========================
# 1. LIST LÀ GÌ?
# =========================
# List là một SEQUENCE (chuỗi có thứ tự)
# - Có thể chứa nhiều kiểu dữ liệu khác nhau
# - Là mảng động (dynamic array)
# - Index bắt đầu từ 0


# =========================
# 2. KHAI BÁO LIST
# =========================

# List số
list1 = [1, 2, 3, 4, 5]

# List chuỗi
list2 = ["A", "B", "C"]

# List nhiều kiểu dữ liệu
list3 = ["Hello", 10, True, 3.14]

print(list1)
print(list2)
print(list3)


# =========================
# 3. TRUY CẬP PHẦN TỬ THEO INDEX
# =========================
# Index trong list bắt đầu từ 0

print(list1[0])  # Phần tử đầu tiên → 1
print(list1[2])  # Phần tử thứ 3 → 3


# =========================
# 4. LIST LỒNG NHAU (NESTED LIST)
# =========================

list4 = [1, [2, 3, 4], 5, 6]

print(list4)
print(list4[1])  # [2, 3, 4]
print(list4[1][0])  # 2


# =========================
# 5. IN TOÀN BỘ LIST
# =========================

# In dạng list
print(list1)

# In từng phần tử (unpacking)
print(*list1)


# =========================
# 6. THÊM PHẦN TỬ VÀO LIST
# =========================

# --- insert(index, value) ---
# Chèn phần tử vào vị trí chỉ định

list1.insert(len(list1), 6)
print("After insert:", list1)

# --- append(value) ---
# Thêm phần tử vào cuối list

list1.append(7)
print("After append:", list1)

# --- extend(list) ---
# Nối thêm nhiều phần tử

list1.extend([8, 9])
print("After extend:", list1)


# =========================
# 7. XÓA PHẦN TỬ KHỎI LIST
# =========================

# --- pop(index) ---
# Xóa theo index (nếu không truyền index → xóa cuối)

list1.pop(4)  # Xóa phần tử tại index 4
print("After pop:", list1)

# --- del ---
# Xóa phần tử theo index

del list1[2]
print("After del:", list1)


# =========================
# 8. DUYỆT LIST (ITERATE)
# =========================

for x in list1:
    print("Value:", x)


# =========================
# 9. TÓM TẮT KIẾN THỨC
# =========================
"""
- List là mảng động
- Có thể chứa nhiều kiểu dữ liệu
- Index bắt đầu từ 0
- Có thể lồng list trong list
- Thêm phần tử: insert, append, extend
- Xóa phần tử: pop, del
- Có thể duyệt list bằng for loop
"""
