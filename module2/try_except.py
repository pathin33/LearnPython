"""
Mục đích:
- Minh họa cách xử lý exception (lỗi) trong Python
- Sử dụng try / except
- Tùy chỉnh thông báo lỗi cho thân thiện với người dùng
"""

# ==============================
# 1. Ví dụ hàm chia số (chưa xử lý lỗi)
# ==============================

def divide_by(a, b):
    """
    Hàm chia hai số a và b
    Nếu b = 0 → sẽ phát sinh lỗi ZeroDivisionError
    """
    return a / b


# ==============================
# 2. Ví dụ gây lỗi (chia cho 0)
# ==============================

# print(divide_by(40, 4))   # Kết quả: 10.0 (hợp lệ)
# print(divide_by(40, 0))   # Lỗi: ZeroDivisionError


# ==============================
# 3. Xử lý lỗi bằng try / except (cơ bản)
# ==============================

try:
    # Python sẽ "thử" chạy đoạn code này
    result = divide_by(40, 0)
    print(result)
except:
    # Nếu có bất kỳ lỗi nào xảy ra
    print("Something went wrong")


# ==============================
# 4. Bắt exception cụ thể bằng Exception as e
# ==============================

try:
    result = divide_by(40, 0)
    print(result)
except Exception as e:
    # e là đối tượng đại diện cho lỗi
    print("Something went wrong:", e)


# ==============================
# 5. Xem loại (class) của exception
# ==============================

try:
    result = divide_by(40, 0)
    print(result)
except Exception as e:
    print("Error message:", e)
    print("Error type:", e.__class__)


# ==============================
# 6. Bắt lỗi cụ thể: ZeroDivisionError
# ==============================

try:
    result = divide_by(40, 0)
    print(result)
except ZeroDivisionError as e:
    # Thông báo thân thiện hơn cho người dùng
    print(e, "- We cannot divide by zero")


# ==============================
# 7. Xử lý nhiều exception (chaining except)
# ==============================

try:
    # Thử thay đổi dữ liệu để test các lỗi khác
    result = divide_by(40, 0)
    print(result)

except ZeroDivisionError as e:
    # Ưu tiên bắt lỗi cụ thể trước
    print(e, "- We cannot divide by zero")

except Exception as e:
    # Bắt các lỗi còn lại (lỗi chung)
    print("Unexpected error:", e)


# ==============================
# 8. Kết luận (ghi nhớ)
# ==============================

"""
- try: đặt code có khả năng gây lỗi
- except: xử lý khi lỗi xảy ra
- Exception: lớp cha của mọi exception trong Python
- as e: lấy thông tin chi tiết của lỗi
- Nên bắt lỗi cụ thể trước, lỗi chung sau
"""
