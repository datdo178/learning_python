"""
Viết một method tính giá trị bình phương của một số.
Gợi ý: Sử dụng toán tử **.
"""


def square():
    while True:
        try:
            num = int(input('Nhập số: '))
        except Exception as Ex:
            print(Ex)
            continue
        else:
            break

    print('num^2=', num ** 2)


square()
