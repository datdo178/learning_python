"""
## Bài 11:
Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.
Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
"""


def nhap_du_lieu():
    input_str = input('Nhập chuỗi từ: ')
    input_arr = input_str.split(',')
    input_arr.sort()
    output_str = ','.join(input_arr)
    print(output_str)


nhap_du_lieu()

"""
Đáp án:
    items=[x for x in input("Nhập một chuỗi: ").split(',')] => chưa hiểu được tại sao phải xử lý như này. Có phải cồng kềnh quá ko?
    items.sort()
    print (','.join(items))
"""