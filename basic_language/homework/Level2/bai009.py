"""
(trong bài viết, có 2 bài 9)
Viết chương trình và in giá trị theo công thức cho trước:
    Q = √([(2 * C * D)/H])
    (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]
    + Với giá trị cố định của C là 50, H là 30.
    + D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.

Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.

Gợi ý:
Nếu đầu ra nhận được là một số dạng thập phân, bạn cần làm tròn thành giá trị gần nhất, ví dụ 26.0 sẽ được in là 26.
Trong trường hợp dữ liệu đầu vào được cung cấp cho câu hỏi, nó được giả định là đầu vào do người dùng nhập từ giao diện điều khiển.
"""
import math


def nhap_du_lieu():
    while True:
        try:
            input_str = input('Nhập dãy số nguyên (cách nhau bởi dấu phẩy):')
            str_list = input_str.split(',')
            num_list = []
            for i in str_list:
                num_list.append(int(i))
        except:
            print('Lỗi dữ liệu nhập. Xin mời nhập lại!')
            continue
        else:
            break
    return num_list


def tinh_toan(num):
    const_c = 50
    const_h = 30
    return math.sqrt((2 * const_c * num)/const_h)


def main():
    day_so = nhap_du_lieu()
    ket_qua = []

    for i in day_so:
        ket_qua.append(int(tinh_toan(i)))

    print('Kết quả: ', ket_qua)


main()
