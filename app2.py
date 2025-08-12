from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore

# 1. Kết nối Firebase
cred = credentials.Certificate("env-management-31772-firebase-adminsdk-fbsvc-31189783eb.json")
# Chỉ khởi tạo nếu chưa init
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

# 2. Trang xem toàn bộ dữ liệu
@app.route("/data")
def view_all():
    docs = db.collection("weather_data").stream()
    all_records = []
    for doc in docs:
        data = doc.to_dict().get("records", [])
        all_records.extend(data)

    return render_template("list.html", records=all_records)


if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Chạy trên cổng khác 5001
