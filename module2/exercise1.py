def read_file(file_name):
    """ Đọc và trả về TOÀN BỘ nội dung của một file dưới dạng một chuỗi (string).

    [CẦN TRIỂN KHAI]
        1. Mở file được truyền vào và đọc toàn bộ nội dung bằng hàm read().
        2. In (print) nội dung của file ra màn hình.
        3. Trả về nội dung của file.

    Tham số:
        file_name (str): Tên file cần đọc.

    Giá trị trả về:
        str: Toàn bộ nội dung của file.
    """
    ### VIẾT LỜI GIẢI Ở ĐÂY
    try:
        with open(file_name,mode= "r") as file:
            data = file.read()
            print(data)
            return data
    except Exception as err:
        print(err)
        return ""


def read_file_into_list(file_name):
    """ Đọc file và trả về một danh sách (list),
        trong đó mỗi phần tử là một dòng trong file.

    [CẦN TRIỂN KHAI]
        1. Mở file được truyền vào.
        2. Đọc file theo từng dòng và thêm mỗi dòng vào một list.
        3. Trả về list đó.

    Tham số:
        file_name (str): Tên file cần đọc.

    Giá trị trả về:
        list: Danh sách, mỗi phần tử là một dòng trong file.
    """
    ### VIẾT LỜI GIẢI Ở ĐÂY
    try:
        with open(file_name,mode= "r") as file:
            listData = []
            for line in file:
                listData.append(line)
            return listData
    except Exception as err:
        print(err)
        return []


def write_first_line_to_file(file_contents, output_filename):
    """ Ghi dòng đầu tiên của một chuỗi vào một file mới.

    [CẦN TRIỂN KHAI]
        1. Lấy dòng đầu tiên từ chuỗi file_contents.
        2. Dùng hàm write() để ghi dòng đầu tiên đó vào file
           có tên là output_filename.

        Dòng đầu tiên được hiểu là toàn bộ nội dung
        đứng trước ký tự xuống dòng ('\\n') đầu tiên.

    Tham số:
        file_contents (str): Chuỗi chứa nhiều dòng văn bản.
        output_filename (str): Tên file dùng để ghi dòng đầu tiên.
    """
    ### VIẾT LỜI GIẢI Ở ĐÂY
    try:
        data = file_contents.split("\n")[0]
        with open(output_filename,mode='w') as file1:
            file1.write(data)
    except Exception as err:
        print(err)
    


def read_even_numbered_lines(file_name):
    """ Đọc các dòng CHẴN trong file và trả về chúng dưới dạng list.

    [CẦN TRIỂN KHAI]
        1. Mở và đọc file được truyền vào.
        2. Đọc file theo từng dòng và chỉ thêm các dòng CHẴN
           (dòng 2, 4, 6, ...) vào list.
        3. Trả về list đó.

    Tham số:
        file_name (str): Tên file cần đọc.

    Giá trị trả về:
        list: Danh sách các dòng chẵn trong file.
    """
    ### VIẾT LỜI GIẢI Ở ĐÂY
    
    try:
        with open(file_name,mode= "r") as file:
            listData = []
            for index , line in enumerate(file):
                if index%2==0:
                    listData.append(line)
            return listData
    except Exception as err:
        print(err)
        return []

def read_file_in_reverse(file_name):
    """ Đọc file và trả về danh sách các dòng theo thứ tự NGƯỢC LẠI.

    [CẦN TRIỂN KHAI]
        1. Mở và đọc file được truyền vào.
        2. Đọc file theo từng dòng và lưu các dòng vào list theo thứ tự đảo ngược.
        3. In (print) list đó ra màn hình.
        4. Trả về list.

    Tham số:
        file_name (str): Tên file_
    """
    ### VIẾT LỜI GIẢI Ở ĐÂY
    try:
        with open(file_name,mode= "r") as file:
            listData = file.read()
            newlist = listData.split('\n')
            newlist.reverse()
            print(newlist)
            return newlist
    except Exception as err:
        print(err)

# Các lệnh mẫu để chạy / kiểm tra các hàm bạn đã cài đặt
def main():
    file_contents = read_file("module2/sampletext.txt")
    # print("Nội dung file:\n", file_contents)
    
    # print(read_file_into_list("sampletext.txt"))
    #write_first_line_to_file(file_contents, "output.txt")
    print(read_even_numbered_lines("module2/sampletext.txt"))
    #read_file_in_reverse("module2/sampletext.txt")

if __name__ == "__main__":
    main()