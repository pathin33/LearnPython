#Su dung args de nhan nhieu tham so khi ko biet truoc dau vao la bao nhieu
#Ben trong ham args la 1 tuple
def tong(*args):
        return (sum(args))

print((tong(2,3,4,5,6,7)))

#Su dung kwargs de nhan nhieu tham so dang key = value
#Ben trong ham kwargs la 1 dictionary
def Info (**kwargs):
    print((kwargs))
#Vi du
Info(name = 'Thien',age = 21)

def sumAge(**kwargs):
    sum = 0
    for val in kwargs.values():
        sum += val
    return sum
print(sumAge(age1 = 20,age2 = 21))

