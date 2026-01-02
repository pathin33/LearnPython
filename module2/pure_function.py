"""

Mục tiêu của file này:
- Nhắc lại kiến thức về pure function
- Hiểu vì sao pure function giúp code sạch, dễ debug
- Phân biệt hàm thường và hàm thuần
- Ví dụ minh họa rõ ràng

-------------------------------------------
1. HÀM (FUNCTION) LÀ GÌ?
-------------------------------------------
Hàm là một khối code:
- Nhận input
- Xử lý
- Trả output

Mô hình chung:
input -> function -> output
"""


# ------------------------------------------
# 2. HÀM KHÔNG THUẦN (NON-PURE FUNCTION)
# ------------------------------------------

# Biến toàn cục (global scope)
my_list = [1, 2, 3]

def add_to_list_not_pure(item):
    """
    Hàm này KHÔNG phải pure function
    Vì:
    - Nó sửa trực tiếp biến my_list bên ngoài hàm
    """
    my_list.append(item)

# Gọi hàm
add_to_list_not_pure(4)

# Kết quả: my_list bị thay đổi
print("Non-pure function result:", my_list)
# [1, 2, 3, 4]


"""
Vấn đề:
- Hàm làm thay đổi dữ liệu global
- Gọi hàm ở 1 chỗ có thể gây lỗi ở chỗ khác
- Rất khó debug khi chương trình lớn
"""


# ------------------------------------------
# 3. PURE FUNCTION LÀ GÌ?
# ------------------------------------------

"""
PURE FUNCTION có 2 đặc điểm quan trọng:

1. KHÔNG thay đổi dữ liệu bên ngoài hàm
2. Cùng input -> luôn cho cùng output

=> Hàm chỉ làm việc với dữ liệu được truyền vào
=> Không đụng tới global scope
"""


# ------------------------------------------
# 4. CHUYỂN HÀM THƯỜNG -> PURE FUNCTION
# ------------------------------------------

def add_to_list_pure(lst, item):
    """
    Đây là PURE FUNCTION

    Cách làm:
    - Không sửa list gốc
    - Tạo bản sao (copy)
    - Thêm phần tử vào bản sao
    - Trả về list mới
    """
    new_list = lst.copy()   # tạo bản sao
    new_list.append(item)  # thao tác trên bản sao
    return new_list        # trả về list mới


# Dữ liệu ban đầu
original_list = [1, 2, 3]

# Gọi pure function
new_list = add_to_list_pure(original_list, 4)

# Kiểm tra kết quả
print("Original list:", original_list)  # [1, 2, 3]
print("New list:", new_list)            # [1, 2, 3, 4]


"""
Nhận xét:
- original_list KHÔNG bị thay đổi
- new_list là dữ liệu mới
- Hàm an toàn, dễ debug
"""


# ------------------------------------------
# 5. VÌ SAO PURE FUNCTION TỐT?
# ------------------------------------------

"""
Ưu điểm của pure function:

1. Dễ đoán kết quả
   - Nhìn input là biết output

2. Dễ debug
   - Lỗi nằm trong hàm, không lan ra ngoài

3. Dễ test
   - Không cần setup global state

4. An toàn khi chạy song song (multi-thread)
   - Không tranh chấp dữ liệu

5. Code sạch, dễ mở rộng
"""


# ------------------------------------------
# 6. PURE FUNCTION TRONG FUNCTIONAL PROGRAMMING
# ------------------------------------------

"""
Lập trình hàm (Functional Programming):
- Ưu tiên dùng pure function
- Không sửa dữ liệu cũ
- Tạo dữ liệu mới từ dữ liệu cũ
- Hay dùng các hàm như: map, filter, sorted
"""


# Ví dụ pure function đơn giản
def reverse_string(s):
    """
    Pure function:
    - Không sửa dữ liệu ngoài
    - Chỉ trả kết quả mới
    """
    return s[::-1]


# Ví dụ dùng map (phong cách functional)
coffees = ["latte", "espresso", "mocha"]

reversed_coffees = list(map(reverse_string, coffees))

print("Original coffees:", coffees)
print("Reversed coffees:", reversed_coffees)


"""
-------------------------------------------
7. TÓM TẮT NGẮN GỌN (ĐỂ NHỚ)
-------------------------------------------

- Pure function:
  + Không sửa dữ liệu bên ngoài
  + Input giống -> output giống

- Khi xử lý list / dict:
  + Đừng sửa trực tiếp
  + Hãy copy rồi xử lý

- Pure function giúp:
  + Code sạch
  + Ít bug
  + Dễ bảo trì
"""
