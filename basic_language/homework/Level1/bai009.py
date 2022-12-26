"""
Tính tuổi dựa trên ngày tháng năm sinh nhập vào.
Ví dụ: Nhập vào ngày tháng năm sinh dạng y/m/d, hãy tính tuổi của người này.
Gợi ý: Sử dụng module datetime. Sử dụng datetime, chúng ta có thể tìm tuổi bằng cách trừ năm sinh cho năm hiện tại.
"""
from _datetime import date

def check_age():
    while True:
        try:
            inputTxt = input('Nhập ngày sinh (iso: yyyy-mm-dd):')
            birthday = date.fromisoformat(inputTxt)
        except ValueError as error:
            print(error)
            continue
        else:
            break

    today = date.today()
    print('%d tuổi' % (today.year - birthday.year))


check_age()

"""
Đáp án:
    - Làm theo kiểu nhập vs tính tuổi chi tiết: (cảm thấy phần tính tháng vs ngày không ổn cho lắm)
    import datetime

    print("Mời bạn vui lòng nhập ngày tháng năm sinh để tính tuổi")
    birth_day = int(input("Ngày sinh:"))
    birth_month = int(input("Tháng sinh:"))
    birth_year = int(input("Năm sinh:"))
    
    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    current_day = datetime.date.today().day
    
    age_year = current_year - birth_year
    age_month = abs(current_month-birth_month)
    age_day = abs(current_day-birth_day)
    
    print("### Tuổi của bạn chính xác là:### \n", age_year, " tuổi ", age_month, " tháng và ", age_day, " ngày")
"""
