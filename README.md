Ứng dụng quản lý thông tin môi trường với Flask & Firebase
📌 Giới thiệu
Ứng dụng web này giúp thu thập và quản lý thông tin môi trường (nhiệt độ, độ ẩm, áp suất...) và lưu trữ dữ liệu trên Firebase Firestore.
Các chức năng chính bao gồm:

Nhập dữ liệu môi trường từ form web

Lưu trữ dữ liệu vào Firebase Firestore

Xem toàn bộ lịch sử dữ liệu đã lưu

Thông báo khi lưu dữ liệu thành công

Ứng dụng phù hợp cho bài tập thực hành Flask kết nối Firebase.

🛠️ Công nghệ sử dụng
Thành phần	Công nghệ
Ngôn ngữ lập trình	Python 3
Web Framework	Flask
Cơ sở dữ liệu	Firebase Firestore
Thư viện Firebase	firebase-admin
Frontend	HTML, CSS, Bootstrap 5
Template Engine	Jinja2

🧠 Cách hoạt động
Người dùng nhập thông tin môi trường qua form web.

Flask nhận dữ liệu, lưu vào collection weather_data trên Firestore.

Sau khi lưu, hệ thống hiển thị thông báo "Thêm thành công".

Người dùng có thể truy cập trang /data để xem toàn bộ dữ liệu đã lưu.

🖼️ Một số giao diện
🔹 Form nhập dữ liệu
(Thêm ảnh minh họa form nhập ở đây)

🔹 Danh sách dữ liệu môi trường
(Thêm ảnh minh họa bảng dữ liệu ở đây)

🚀 Cài đặt và chạy ứng dụng
1️⃣ Cài đặt thư viện
bash
Sao chép
Chỉnh sửa
pip install flask firebase-admin
2️⃣ Cấu hình Firebase
Tạo project Firebase

Tải file serviceAccountKey.json (Firebase Admin SDK)

Đặt file này vào thư mục dự án và đổi tên theo cấu hình trong code (vd: env-management-31772-firebase-adminsdk.json)

3️⃣ Chạy ứng dụng
bash
Sao chép
Chỉnh sửa
python app.py
Ứng dụng mặc định chạy tại:

less
Sao chép
Chỉnh sửa
Form nhập dữ liệu: http://127.0.0.1:5000
Xem dữ liệu: http://127.0.0.1:5001/data
📂 Cấu trúc thư mục
csharp
Sao chép
Chỉnh sửa
📦 env-management
 ┣ 📜 app.py               # File Flask chính
 ┣ 📜 env-management-31772-firebase-adminsdk.json  # Key Firebase
 ┣ 📂 templates
 ┃ ┣ 📜 index.html         # Form nhập dữ liệu
 ┃ ┣ 📜 list.html          # Trang hiển thị danh sách dữ liệu
 ┣ 📂 static               # CSS, JS, hình ảnh
📌 Ghi chú
Có thể tùy chỉnh port Flask bằng app.run(debug=True, port=5001)

Nếu chạy nhiều cổng, cần cấu hình liên kết đường dẫn tuyệt đối trong HTML để điều hướng đúng port.
