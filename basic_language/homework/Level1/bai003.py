"""
Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.
"""
while True:
    try:
        num = int(input('Nhập số nguyên  >= 1: '))
    except Exception as Ex:
        print(Ex)
        continue
    else:
        print(num)
        if num < 1:
            continue
        else:
            break


thisDict = {}
for i in range(1, num + 1):
    thisDict[i] = i * i

print(thisDict)

"""
Đáp án:
    - Khởi tạo:
        thisDict = dict()
"""
