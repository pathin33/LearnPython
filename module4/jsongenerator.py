''' 
Các câu lệnh Import: 
    1. Import gói json có sẵn của python
    2. Từ employee.py, import hàm details và các biến employee_name, age, title
'''
### VIẾT CÁC CÂU LỆNH IMPORT TẠI ĐÂY
import json
from employee import details, employee_name, age, title

def create_dict(name, age, title):
    """ Tạo một dictionary lưu trữ thông tin của nhân viên

    [THỰC HIỆN TẠI ĐÂY]
        1. Trả về một dictionary ánh xạ "first_name" thành name, "age" thành age, và "title" thành title

    Đối số (Args):
        name: Tên của nhân viên
        age: Tuổi của nhân viên
        title: Chức danh của nhân viên

    Trả về (Returns):
        dict - Một dictionary ánh xạ "first_name", "age", và "title" lần lượt tới các 
               đối số name, age, và title. Đảm bảo rằng các giá trị được ép kiểu 
               chính xác (name - string, age - int, title - string)
    """
    ### VIẾT LỜI GIẢI TẠI ĐÂY
    dict = {
        "first_name" : str(name),
        "age" : int(age),
        "title": str(title)
    }
    return dict

def write_json_to_file(json_obj, output_file):
    """ Ghi chuỗi json vào file

    [THỰC HIỆN TẠI ĐÂY]
        1. Mở file employee.json
        2. Ghi json_obj vào file mới

    Đối số (Args):
        json_obj: chuỗi json chứa thông tin nhân viên
    """
    ### VIẾT LỜI GIẢI TẠI ĐÂY
    with open (output_file,mode= "w") as file:
        file.writelines(json_obj)


def main():
    # In nội dung của hàm details() -- Dòng này sẽ in chi tiết của một nhân viên
    details()

    # Tạo dictionary nhân viên
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    ''' 
    Sử dụng một hàm gọi là dumps từ module json để chuyển đổi employee_dict
    thành một chuỗi json và lưu trữ nó vào một biến gọi là json_object.
    '''
    ### VIẾT CODE CỦA BẠN BẰNG CÁCH CHỈNH SỬA DÒNG DƯỚI ĐÂY
    # Ở dòng dưới đây, hãy thay thế từ khóa None bằng mã của bạn. 
    # Định dạng nên là: variable = json.dumps(dict)
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Ghi đối tượng json ra file
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()