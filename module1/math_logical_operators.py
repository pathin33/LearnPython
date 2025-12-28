"""
Mục đích:
- Minh họa các toán tử (operators) trong Python
- Bao gồm: Toán tử toán học (Math operators) và toán tử logic (Logical operators)
- Có ví dụ + giải thích bằng comment
"""

# =========================
# 1. TOÁN TỬ TOÁN HỌC (Math Operators)
# =========================

# Toán tử cộng (+)
# Dùng để cộng hai số
print(2 + 2)  # Kết quả mong đợi: 4

# Toán tử trừ (-)
# Dùng để trừ hai số
print(2 - 2)  # Kết quả mong đợi: 0

# Toán tử chia (/)
# Dùng để chia hai số
# Lưu ý: Kết quả luôn là số thực (float)
print(35 / 5)  # Kết quả: 7.0

# Toán tử nhân (*)
# Dùng để nhân hai số
print(25 * 7)  # Kết quả: 175


# =========================
# 2. TOÁN TỬ LOGIC (Logical Operators)
# =========================

# Toán tử logic thường dùng trong câu điều kiện (if)
# Kết quả trả về luôn là True hoặc False

# -------------------------
# AND (và)
# -------------------------
# Điều kiện chỉ đúng khi TẤT CẢ đều đúng

a = True
b = True

if a and b:
    print("AND: All true")  # Chỉ in ra khi cả a và b đều True

# Đổi b thành False
b = False

if a and b:
    print("AND: All true")  # Không in ra vì b = False


# -------------------------
# OR (hoặc)
# -------------------------
# Điều kiện đúng khi CHỈ CẦN 1 trong các điều kiện đúng

a = True
b = False

if a or b:
    print("OR: At least one is true")  # In ra vì a = True

# Nếu cả hai đều False
a = False
b = False

if a or b:
    print("OR: At least one is true")  # Không in ra


# -------------------------
# NOT (phủ định)
# -------------------------
# Đảo ngược giá trị True <-> False

a = False
b = False

if (not a) or (not b):
    print("NOT: Condition is true")
    # not a = True, not b = True → True OR True → True

# Nếu a và b đều True
a = True
b = True

if (not a) or (not b):
    print("NOT: Condition is true")
    # not a = False, not b = False → False OR False → False
    # → Không in ra


# =========================
# 3. VÍ DỤ THỰC TẾ (Giống video)
# =========================

# Ví dụ: Nhà hàng giảm giá nếu
# - Khách là thành viên thân thiết
# - VÀ chi tiêu trên 100$

is_loyal_customer = True
total_spent = 120

if is_loyal_customer and total_spent > 100:
    print("Customer gets a discount!")
else:
    print("No discount")


"""
TÓM TẮT:
- Math operators: +, -, *, /
- Logical operators: and, or, not
- Toán tử logic thường dùng trong if để kiểm soát luồng chương trình
"""
