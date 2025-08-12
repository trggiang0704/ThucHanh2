from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore

# 1. Kết nối Firebase
cred = credentials.Certificate("env-management-31772-firebase-adminsdk-fbsvc-31189783eb.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

# 2. Trang nhập dữ liệu môi trường
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        record_id = request.form["id"]
        name = request.form["name"]
        temperature = request.form["temperature"]
        humidity = request.form["humidity"]
        wind = request.form["wind"]
        pressure = request.form["pressure"]
        time_input = request.form["time"]

        doc_ref = db.collection("weather_data").document(record_id)
        doc = doc_ref.get()

        if doc.exists:
            old_data = doc.to_dict().get("records", [])
            old_data.append({
                "ID": record_id,
                "Name": name,
                "Temperature": temperature,
                "Humidity": humidity,
                "Wind": wind,
                "Pressure": pressure,
                "Time": time_input
            })
            doc_ref.set({"records": old_data})
        else:
            doc_ref.set({
                "records": [{
                    "ID": record_id,
                    "Name": name,
                    "Temperature": temperature,
                    "Humidity": humidity,
                    "Wind": wind,
                    "Pressure": pressure,
                    "Time": time_input
                }]
            })

        # Redirect sang GET kèm query param success=1
        return redirect(url_for("index", success=1))

    # Lấy query param success (nếu có)
    success = request.args.get("success") == "1"
    return render_template("index.html", success=success)


if __name__ == "__main__":
    app.run(debug=True, port=5000)