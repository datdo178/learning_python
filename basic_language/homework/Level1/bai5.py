"""
Định nghĩa một class có ít nhất 2 method:<br>
getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.<br>
printString: in chuỗi vừa nhập sang chữ hoa.<br>
Thêm vào các hàm kiểm tra đơn giản để kiểm tra method của class.<br>
Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM <br>
Gợi ý:<br>
Sử dụng __init__ để xây dựng các tham số.
"""


class bai5():
    def __init__(self):
        self.str = ""

    def getString(self) -> None:
        inputStr = input('Nhap chuoi: ')
        self.str = inputStr

    def printString(self) -> None:
        print(self.str.upper())


doiTuong = bai5()

doiTuong.getString()
doiTuong.printString()


"""
Đáp án:
    - Giá trị khởi tạo của self.str = ""
    --> như vậy sẽ tránh được lỗi khi gọi printString() trước khi có getString()
"""