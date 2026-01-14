from abc import ABC,abstractmethod
class ThanhToan(ABC):
    @abstractmethod
    def thanh_toan(so_tien):
        pass    

class ThanhToanTienMat(ThanhToan):
    def thanh_toan(self,so_tien):
        return f"Da thanh toan {so_tien} bang tien mat"
    
class ThanhToanChuyenKhoan(ThanhToan):
    def thanh_toan(self,so_tien):
        return f"Da thanh toan {so_tien} bang tien chuyen khoan"

tienmat= ThanhToanTienMat()
tienchuyenkhoan = ThanhToanChuyenKhoan()
print(tienchuyenkhoan.thanh_toan(4000))
print(tienmat.thanh_toan(36000))