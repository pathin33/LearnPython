"""
r   : đọc file (text - mặc định)
rb  : đọc file (binary)
r+  : đọc + ghi
w   : ghi file (ghi đè nội dung cũ)
a   : append (ghi thêm vào cuối file)
b   : dùng kèm với r/w/a để xử lý binary
"""
try:
    with open("module2/test1.txt",mode = "w") as file:
        #file.write("Hello everyone")
        #dung chi ghi 1 dong
        file.writelines(["Xin chao moi nguoi","\nMinh ten la Nguyen Ba Thien"])

except Exception as err:
    print(err)