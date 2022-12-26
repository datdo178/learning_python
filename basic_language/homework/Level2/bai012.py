"""
Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này thành chữ in hoa và in ra màn hình. Giả sử đầu vào là:

Hello world
Practice makes perfect

Thì đầu ra sẽ là:
HELLO WORLD
PRACTICE MAKES PERFECT

Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
"""


def input_value():
    contents = []
    print("Nhập nội dung. Việc nhập sẽ kết thúc khi gõ Enter trên một empty line: ")

    while True:
        line = input(">>")
        if line:
            contents.append(line)
        else:
            break

    return contents


def toUpperCase():
    input_arr = input_value()
    output_arr = [x.upper() for x in input_arr]
    print('\n'.join(output_arr))


toUpperCase()


"""
Đáp án:
    - Bài này phải xem đáp án mới biết cách lấy dữ liệu multiple line
"""
