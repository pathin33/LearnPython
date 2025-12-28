"""
Mục đích:
- Minh họa Control Flow (luồng điều khiển) trong Python
- Tập trung vào conditional statements: if, elif, else
- Ví dụ thực tế: áp dụng giảm giá cho hóa đơn nhà hàng
"""

# =========================
# 1. CONTROL FLOW LÀ GÌ?
# =========================
# Control Flow (luồng điều khiển) là thứ tự các câu lệnh trong chương trình
# được thực thi dựa trên điều kiện.
#
# Ví dụ đời thực:
# - Mặc đồ đi tiệc: nếu tiệc trang trọng -> mặc vest, nếu không -> mặc thường
# - Công tắc đèn: ON thì sáng, OFF thì tắt


# =========================
# 2. IF STATEMENT (CÂU ĐIỀU KIỆN IF)
# =========================

# Tổng tiền hóa đơn của khách
bill_total = 114

# Mức giảm giá thứ nhất
discount1 = 10

# Nếu hóa đơn > 100 thì áp dụng giảm giá
if bill_total > 100:
    print("Bill is greater than 100")
    bill_total = bill_total - discount1

# Luôn in tổng tiền cuối cùng
print("Total bill is " + str(bill_total))


# =========================
# 3. IF - ELSE
# =========================

bill_total = 95
discount1 = 10

if bill_total > 100:
    print("Bill is greater than 100")
    bill_total = bill_total - discount1
else:
    # Else sẽ chạy khi điều kiện IF không đúng
    print("Bill is less than or equal to 100")

print("Total bill is " + str(bill_total))


# =========================
# 4. IF - ELIF - ELSE
# =========================
# Nhà hàng có 2 mức giảm giá:
# - > 100 và < 200 : giảm 10
# - > 200         : giảm 20

bill_total = 210

discount1 = 10
discount2 = 20

if bill_total > 100 and bill_total < 200:
    print("Bill is greater than 100")
    bill_total = bill_total - discount1

elif bill_total > 200:
    # Elif (else if) chỉ được kiểm tra
    # khi điều kiện IF phía trên là False
    print("Bill is greater than 200")
    bill_total = bill_total - discount2

else:
    # Else chỉ chạy khi TẤT CẢ điều kiện trên đều sai
    print("No discount applied")

print("Total bill is " + str(bill_total))


# =========================
# 5. TÓM TẮT KIẾN THỨC
# =========================
"""
- if: chạy khi điều kiện đúng (True)
- elif: kiểm tra thêm điều kiện khác nếu if sai
- else: chạy khi tất cả điều kiện đều sai

Thứ tự kiểm tra:
IF -> ELIF -> ELSE

Chỉ MỘT khối được thực thi
"""
