# Dữ liệu đầu vào: Danh sách các dictionary
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Hàm sẽ được truyền vào hàm map(). Không được thay đổi hàm này.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   """
   Chuyển đổi danh sách dictionary nhân viên
   thành danh sách chuỗi có dạng: name_department

   [BẠN CẦN CÀI ĐẶT HÀM NÀY]
      1. Sử dụng hàm map() để áp dụng hàm mod()
         cho tất cả phần tử trong employee_list

   Tham số:
      employee_list: danh sách các đối tượng nhân viên (dictionary)

   Giá trị trả về:
      list - Danh sách các chuỗi gồm tên + phòng ban
   """
   ### VIẾT CODE Ở ĐÂY ###
   return list(map(mod,employee_list))

def generate_usernames(mod_list):
   """
   Tạo danh sách username

   [BẠN CẦN CÀI ĐẶT HÀM NÀY]
      1. Sử dụng list comprehension
      2. Thay thế các dấu cách (space) bằng dấu gạch dưới (_)

   Tham số:
      mod_list: danh sách chuỗi name_department

   Giá trị trả về:
      list - Danh sách username với name và department
             được phân cách bằng dấu gạch dưới
   """
   ### VIẾT CODE Ở ĐÂY ###
   return [
      x.replace(" ","_")
      for x in mod_list
   ]

def map_id_to_initial(employee_list):
   """
   Ánh xạ (map) id nhân viên với chữ cái đầu tiên trong tên

   [BẠN CẦN CÀI ĐẶT HÀM NÀY]
      1. Sử dụng dictionary comprehension
      2. Map id của nhân viên (value)
         với chữ cái đầu tiên của tên (key)

   Tham số:
      employee_list: danh sách các đối tượng nhân viên

   Giá trị trả về:
      dict - Dictionary ánh xạ id nhân viên
             với chữ cái đầu trong tên của họ
   """
   ### VIẾT CODE Ở ĐÂY ###
   new_dict = {item['name'][0]: item['id']  for item in employee_list}
   return new_dict
def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Danh sách nhân viên sau khi chỉnh sửa: " + str(mod_emp_list) + "\n")
   print(f"Danh sách username: {generate_usernames(mod_emp_list)}\n")
   print(f"Chữ cái đầu và id: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()
