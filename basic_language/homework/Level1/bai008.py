"""
## Bài 08:
Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
Gợi ý:
Khi định nghĩa tham số instance, cần thêm nó vào __init__
Bạn có thể khởi tạo một đối tượng với tham số bắt đầu hoặc thiết lập giá trị sau đó.

=> Ko hiểu đề bài cho lắm nên xem bài giải luôn
"""


class Person:
    name = "Person"  # tham số lớp

    def __init__(self, name = None):
        self.name = name  # tham số instance


jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print ("%s name is %s" % (Person.name, nico.name))
