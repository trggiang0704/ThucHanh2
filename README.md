Ứng dụng Quản Lý Thông Tin Môi Trường
(Flask + Firebase Firestore)

📌 Giới thiệu
Ứng dụng web giúp thu thập và quản lý thông tin môi trường (nhiệt độ, độ ẩm, áp suất...) và lưu trữ dữ liệu trên Firebase Firestore.

Các chức năng chính:

📝 Nhập dữ liệu môi trường từ form web

☁ Lưu trữ dữ liệu vào Firebase Firestore

📄 Xem toàn bộ lịch sử dữ liệu đã lưu

✅ Hiển thị thông báo khi lưu dữ liệu thành công

Ứng dụng phù hợp để thực hành Flask kết nối Firebase.

🛠 Công nghệ sử dụng
Thành phần	Công nghệ
Ngôn ngữ	Python 3
Web Framework	Flask
CSDL	Firebase Firestore
Thư viện Firebase	firebase-admin
Frontend	HTML, CSS, Bootstrap 5
Template Engine	Jinja2

🧠 Cách hoạt động
Người dùng nhập thông tin môi trường qua form web

Flask nhận dữ liệu, lưu vào collection weather_data trên Firestore

Sau khi lưu, hệ thống hiển thị thông báo "Thêm thành công"

Người dùng có thể truy cập /data để xem toàn bộ dữ liệu đã lưu

🖼 Giao diện mẫu
🔹 Form nhập dữ liệu
(Chèn ảnh minh họa ở đây)

🔹 Danh sách dữ liệu môi trường
(Chèn ảnh minh họa ở đây)

🚀 Cài đặt & Chạy ứng dụng
1️⃣ Cài đặt thư viện
bash
Sao chép
Chỉnh sửa
pip install flask firebase-admin
2️⃣ Cấu hình Firebase
Tạo Project trên Firebase Console

Tải file serviceAccountKey.json (Firebase Admin SDK)

Đặt file vào thư mục dự án và đổi tên theo cấu hình trong code
(ví dụ: env-management-31772-firebase-adminsdk.json)

3️⃣ Chạy ứng dụng
bash
Sao chép
Chỉnh sửa
python app.py
Mặc định:

Form nhập dữ liệu: http://127.0.0.1:5000

Xem dữ liệu: http://127.0.0.1:5001/data

📂 Cấu trúc thư mục
plaintext
Sao chép
Chỉnh sửa
📦 env-management
 ┣ 📜 app.py                # File Flask chính
 ┣ 📜 env-management-31772-firebase-adminsdk.json  # Key Firebase
 ┣ 📂 templates
 ┃ ┣ 📜 index.html          # Form nhập dữ liệu
 ┃ ┣ 📜 list.html           # Trang hiển thị danh sách dữ liệu
 ┣ 📂 static                # CSS, JS, hình ảnh
📌 Ghi chú
Có thể thay đổi port bằng:

python
Sao chép
Chỉnh sửa
app.run(debug=True, port=5001)
Nếu chạy nhiều cổng, hãy sử dụng đường dẫn tuyệt đối trong HTML để điều hướng đúng port.

