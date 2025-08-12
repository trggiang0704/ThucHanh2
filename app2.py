from flask import Flask, render_template, request
from datetime import datetime, timedelta
import firebase_admin
from firebase_admin import credentials, firestore

# 1. Kết nối Firebase
cred = credentials.Certificate("env-management-31772-firebase-adminsdk-fbsvc-31189783eb.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

# Hàm lấy toàn bộ dữ liệu từ Firestore
def get_all_records():
    docs = db.collection("weather_data").stream()
    all_records = []
    for doc in docs:
        data = doc.to_dict().get("records", [])
        all_records.extend(data)
    return all_records

# Hàm cố gắng parse giá trị Time thành datetime (hỗ trợ nhiều định dạng)
def parse_time_value(time_value):
    if not time_value:
        return None

    # Nếu đã là datetime (ví dụ Firestore Timestamp đã được chuyển thành datetime)
    if isinstance(time_value, datetime):
        return time_value

    s = str(time_value).strip()

    # Thử một số format phổ biến (có/không có giây, có chữ 'T' giữa ngày-giờ)
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%d"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue

    # Thử ISO parse (Python 3.7+)
    try:
        return datetime.fromisoformat(s)
    except Exception:
        pass

    # Không parse được
    return None

# 2. Trang xem dữ liệu (có lọc theo khoảng thời gian)
@app.route("/data", methods=["GET"])
def view_all():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    records = get_all_records()

    if start_date and end_date:
        try:
            # Parse ngày bắt đầu/kết thúc từ input (format YYYY-MM-DD)
            start = datetime.strptime(start_date, "%Y-%m-%d")
            # Bao trọn ngày kết thúc: +1 ngày và dùng điều kiện < end_next_day
            end_next = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)

            filtered_records = []
            for r in records:
                time_value = r.get("Time")
                record_time = parse_time_value(time_value)

                # Nếu không parse được, bỏ qua bản ghi (hoặc bạn có thể include tuỳ ý)
                if record_time is None:
                    continue

                # Lọc: bao gồm start ngày và mọi thời điểm trước end_next (== bao trọn end_date)
                if start <= record_time < end_next:
                    filtered_records.append(r)

            records = filtered_records

        except Exception as e:
            # In log để debug nếu cần
            print("Lỗi khi lọc thời gian:", e)

    # Optionally sort records by Time desc
    try:
        records.sort(key=lambda x: parse_time_value(x.get("Time")) or datetime.min, reverse=True)
    except Exception:
        pass

    return render_template("list.html", records=records, start_date=start_date, end_date=end_date)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
