"""
Mục đích:
- Giải thích Set trong Python
- Cách khai báo set
- Đặc điểm quan trọng của set (không trùng lặp, không có index)
- Thêm / xóa phần tử
- Các phép toán tập hợp: union, intersection, difference, symmetric difference
"""

# =========================
# 1. SET LÀ GÌ?
# =========================
# Set là một collection:
# - KHÔNG cho phép giá trị trùng lặp
# - KHÔNG có thứ tự (unordered)
# - KHÔNG có index
# - Thường dùng cho các phép toán tập hợp


# =========================
# 2. KHAI BÁO SET
# =========================

set_a = {1, 2, 3, 4, 5}
print(set_a)

# Set KHÔNG cho phép phần tử trùng
set_a = {1, 2, 3, 4, 5, 5}
print(set_a)  # 5 chỉ xuất hiện 1 lần


# =========================
# 3. THÊM PHẦN TỬ VÀO SET
# =========================

set_a.add(6)
print("After add:", set_a)


# =========================
# 4. XÓA PHẦN TỬ TRONG SET
# =========================

# remove(): xóa phần tử (báo lỗi nếu không tồn tại)
set_a.remove(2)
print("After remove:", set_a)

# discard(): xóa phần tử (KHÔNG báo lỗi nếu không tồn tại)
set_a.discard(10)
print("After discard:", set_a)


# =========================
# 5. TẠO SET THỨ HAI
# =========================

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}


# =========================
# 6. UNION (HỢP)
# =========================
# Lấy tất cả phần tử của cả 2 set (không trùng)

print(set_a.union(set_b))
print(set_a | set_b)  # Ký hiệu | tương đương union


# =========================
# 7. INTERSECTION (GIAO)
# =========================
# Lấy phần tử chung của cả 2 set

print(set_a.intersection(set_b))
print(set_a & set_b)  # Ký hiệu & tương đương intersection


# =========================
# 8. DIFFERENCE (HIỆU)
# =========================
# Phần tử có trong set_a nhưng KHÔNG có trong set_b

print(set_a.difference(set_b))
print(set_a - set_b)  # Ký hiệu - tương đương difference


# =========================
# 9. SYMMETRIC DIFFERENCE
# =========================
# Phần tử chỉ có trong 1 trong 2 set (không có chung)

print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)  # Ký hiệu ^ tương đương symmetric difference


# =========================
# 10. SET KHÔNG CÓ INDEX
# =========================
# Set không phải là sequence → không truy cập bằng index

# DÒNG CODE DƯỚI ĐÂY SẼ BÁO LỖI
# print(set_a[0])

"""
Lỗi:
TypeError: 'set' object is not subscriptable

→ Set không có thứ tự, không có index
"""


# =========================
# 11. TÓM TẮT KIẾN THỨC
# =========================
"""
SET:
- Không trùng lặp
- Không có index
- Không đảm bảo thứ tự
- Rất mạnh cho các phép toán tập hợp

Phép toán quan trọng:
- union        |
- intersection &
- difference   -
- symmetric    ^
"""
