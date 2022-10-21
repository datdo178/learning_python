"""
Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.
"""

try:
    num = int(input('Nhập số: '))
except:
    num = int(input('Chỉ được nhập số nguyên >=1. Mời nhập lại:'))

while num < 1:
    num = int(input('Chỉ được nhập số nguyên >=1. Mời nhập lại:'))

thisDict = {}
for i in range(1, num + 1):
    thisDict[i] = i * i

print(dict)


"""
Đáp án:
    - Khởi tạo:
        thisDict = dict()
"""