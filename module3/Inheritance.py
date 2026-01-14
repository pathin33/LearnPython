class NhanSu:
    def  __init__(self,ten,ma_nhan_su):
        self.ten = ten
        self.ma_nhan_su = ma_nhan_su

class QuanLy(NhanSu):
    def __init__(self, ten, ma_nhan_su,mat_khau):
        super().__init__(ten, ma_nhan_su)
        self.mat_khau = mat_khau
class KyThuatVien(NhanSu):
    def xin_nghi_phep(self,so_ngay):
        return f"{self.ten} xin nghi {str(so_ngay)} ngay"
    
quanly = QuanLy("Nguyen Ba Thien","3399","bath005")
print(quanly.mat_khau)
kithuatvien = KyThuatVien("Thien Nguyen Ba","0931")
print(kithuatvien.xin_nghi_phep(3))

