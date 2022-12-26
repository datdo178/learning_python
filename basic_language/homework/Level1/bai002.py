"""
Viết một chương trình có thể tính giai thừa của một số cho trước.
Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
"""
while True:
    try:
        num = int(input('Nhập số tính giai thừa (>= 1): '))
    except Exception as Ex:
        print(Ex)
        continue
    else:
        if num < 1:
            continue
        else:
            break

result = 1
while num > 1:
    result *= num
    num -= 1

print('Kết quả:', result)

"""
Đáp án:
    - Sử dụng đệ qui để tính giai thừa
        x=int(input("Nhập số cần tính giai thừa:"))
        def fact(x):
            if x == 0:
                return 1
            return x * fact(x - 1)
        print (fact(x))
"""