"""
Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.

Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Gợi ý:
Viết lệnh để nhận giá trị X, Y từ giao diện điều khiển do người dùng nhập vào.
"""


def nhap_du_lieu():
    """
    Lẽ ra hàm cho nhập 1 số vs gọi lại sử dụng nhiều lần thì hay hơn.
    Nhưng mình muốn check thử return List và Destructuring
    """
    while True:
        try:
            num_row = int(input('Nhập số nguyên X (row): '))
        except:
            print('Giá trị nhập không hợp lệ. Xin nhập lại!')
            continue
        else:
            break

    while True:
        try:
            num_col = int(input('Nhập số nguyên Y (col): '))
        except:
            print('Giá trị nhập không hợp lệ. Xin nhập lại!')
            continue
        else:
            break
    return [num_row, num_col]


def main():
    [num_row, num_col] = nhap_du_lieu()
    table = []

    for x in range(num_row):
        row = []
        for y in range(num_col):
            row.append(x*y)
        table.append(row)

    print('Kết quả:')
    for row in table:
        print(row)


main()
