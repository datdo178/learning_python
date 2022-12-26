Link bài tập: https://quantrimang.com/hoc/hon-100-bai-tap-python-co-loi-giai-code-mau-142456
======== LEVEL 1 =========
## Bài 01:
Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

## Bài 02:
Viết một chương trình có thể tính giai thừa của một số cho trước. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

## Bài 03:
Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.
Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.

## Bài 04:
Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.

Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

## Bài 05:
Định nghĩa một class có ít nhất 2 method:
getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
printString: in chuỗi vừa nhập sang chữ hoa.
Thêm vào các hàm kiểm tra đơn giản để kiểm tra method của class.
Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM 
Gợi ý:
Sử dụng __init__ để xây dựng các tham số.

## Bài 06:
Viết một method tính giá trị bình phương của một số.
Gợi ý: Sử dụng toán tử **.

## Bài 07:
Python có nhiều hàm được tích hợp sẵn, nếu không biết cách sử dụng nó, bạn có thể đọc tài liệu trực tuyến hoặc tìm vài cuốn sách. Nhưng Python cũng có sẵn tài liệu về hàm cho mọi hàm tích hợp trong Python. Yêu cầu của bài tập này là viết một chương trình để in tài liệu về một số hàm Python được tích hợp sẵn như abs(), int(), input() và thêm tài liệu cho hàm bạn tự định nghĩa.
Gợi ý: Sử dụng __doc__

## Bài 08:
Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
Gợi ý:
Khi định nghĩa tham số instance, cần thêm nó vào __init__
Bạn có thể khởi tạo một đối tượng với tham số bắt đầu hoặc thiết lập giá trị sau đó.

## Bài 09:
Tính tuổi dựa trên ngày tháng năm sinh nhập vào.
Ví dụ: Nhập vào ngày tháng năm sinh dạng y/m/d, hãy tính tuổi của người này.
Gợi ý: Sử dụng module datetime. Sử dụng datetime, chúng ta có thể tìm tuổi bằng cách trừ năm sinh cho năm hiện tại.


======== LEVEL 2 =========
## Bài 09: (cái số trong bài viết cũng nhầm)
(trong bài viết, có 2 bài 9)
Viết chương trình và in giá trị theo công thức cho trước:
    Q = √([(2 * C * D)/H])
    (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]
    + Với giá trị cố định của C là 50, H là 30.
    + D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.

Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.

Gợi ý:
Nếu đầu ra nhận được là một số dạng thập phân, bạn cần làm tròn thành giá trị gần nhất, ví dụ 26.0 sẽ được in là 26.
Trong trường hợp dữ liệu đầu vào được cung cấp cho câu hỏi, nó được giả định là đầu vào do người dùng nhập từ giao diện điều khiển.

## Bài 10:
Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.

Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Gợi ý:
Viết lệnh để nhận giá trị X, Y từ giao diện điều khiển do người dùng nhập vào.


## Bài 11:
Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.
Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.


## Bài 12:
Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này thành chữ in hoa và in ra màn hình. Giả sử đầu vào là:

Hello world
Practice makes perfect

Thì đầu ra sẽ là:
HELLO WORLD
PRACTICE MAKES PERFECT

Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.


## Bài 13:
Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng, loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.

Giả sử đầu vào là: hello world and practice makes perfect and hello world again

Thì đầu ra là: again and hello makes perfect practice world

Gợi ý:
- Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
- Sử dụng set để loại bỏ dữ liệu trùng lặp tự động và dùng sorted() để sắp xếp dữ liệu.
