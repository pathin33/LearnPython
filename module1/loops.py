"""
Mục đích:
- Minh họa khái niệm looping (vòng lặp) trong Python
- Sử dụng for loop và while loop
- Ví dụ với string, range, list (array)
- Giải thích rõ sự khác nhau giữa for và while
"""

# =========================
# 1. LOOPING LÀ GÌ?
# =========================
# Looping (vòng lặp) là việc lặp lại cùng một khối lệnh nhiều lần
# Ví dụ đời thực:
# - Nghe 1 bài nhạc bật chế độ loop
# - Làm việc lặp đi lặp lại cho đến khi xong

# Python có 2 loại vòng lặp chính:
# - for loop
# - while loop


# =========================
# 2. FOR LOOP VỚI STRING
# =========================
# String là một SEQUENCE (chuỗi có thứ tự)
# => có thể duyệt từng ký tự

text = "looping"

for item in text:
    # item lần lượt là từng ký tự trong chuỗi
    print(item)

# Output:
# l
# o
# o
# p
# i
# n
# g


# =========================
# 3. FOR LOOP VỚI RANGE
# =========================
# range(10) tạo ra dãy số từ 0 đến 9

for i in range(10):
    print("Looping", i)

# Lưu ý quan trọng:
# - Vòng lặp for thường bắt đầu từ 0
# - Index trong Python bắt đầu từ 0
# - range(10) KHÔNG bao gồm số 10


# =========================
# 4. FOR LOOP VỚI LIST (ARRAY)
# =========================

favorites = ["Cake", "Ice Cream", "Chocolate", "Donut", "Pudding"]

for item in favorites:
    print("I like this dessert:", item)

# item lần lượt là từng phần tử trong list favorites


# =========================
# 5. WHILE LOOP
# =========================
# While loop chạy khi điều kiện còn đúng (True)

count = 0

while count < len(favorites):
    # Phải dùng index để truy cập phần tử
    print("I like this dessert:", favorites[count])

    # BẮT BUỘC tăng count
    # Nếu không sẽ bị infinite loop (vòng lặp vô hạn)
    count += 1


# =========================
# 6. FOR LOOP + ENUMERATE
# =========================
# enumerate() giúp:
# - Lấy được index
# - Và giá trị của phần tử

for idx, item in enumerate(favorites):
    print(idx, item)

# Output:
# 0 Cake
# 1 Ice Cream
# 2 Chocolate
# 3 Donut
# 4 Pudding


# =========================
# 7. SO SÁNH NHANH
# =========================
"""
FOR LOOP:
- Dùng khi biết trước số lần lặp
- Gọn, dễ đọc
- Ít gây lỗi

WHILE LOOP:
- Dùng khi không biết trước số lần lặp
- Phải tự quản lý biến đếm
- Dễ gây infinite loop nếu quên tăng biến
"""
