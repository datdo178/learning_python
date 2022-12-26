"""
## Bài 07:
Python có nhiều hàm được tích hợp sẵn, nếu không biết cách sử dụng nó, bạn có thể đọc tài liệu trực tuyến hoặc tìm vài cuốn sách. Nhưng Python cũng có sẵn tài liệu về hàm cho mọi hàm tích hợp trong Python. Yêu cầu của bài tập này là viết một chương trình để in tài liệu về một số hàm Python được tích hợp sẵn như abs(), int(), input() và thêm tài liệu cho hàm bạn tự định nghĩa.
Gợi ý: Sử dụng __doc__
"""


def print_method_doc() -> None:
    """Print some __doc__ methods"""
    print('1. print_method_doc.__doc__:', print_method_doc.__doc__)
    print('2. abs.__doc__:', abs.__doc__)
    print('3. int.__doc__:', int.__doc__ )


print_method_doc()
