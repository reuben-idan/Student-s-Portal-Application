import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from database import get_db, init_db

app = Flask(__name__)
app.jinja_env.globals["enumerate"] = enumerate
app.config["UPLOAD_FOLDER"] = os.path.join("static", "uploads")
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Collect form fields
    fields = ["first_name", "last_name", "email", "phone", "address", "dob", "gender", "department", "level", "state", "age"]
    data = {f: request.form.get(f, "").strip() for f in fields}

    # Validate all fields are filled
    if not all(data.values()):
        return render_template("form.html", error="All fields are required.")

    # Handle image upload
    image = request.files.get("image")
    if not image or not allowed_file(image.filename):
        return render_template("form.html", error="A valid image file is required.")

    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    # Save to database
    try:
        with get_db() as conn:
            conn.execute("""
                INSERT INTO students (first_name, last_name, email, phone, address, dob, gender, department, level, state, age, image)
                VALUES (:first_name, :last_name, :email, :phone, :address, :dob, :gender, :department, :level, :state, :age, :image)
            """, {**data, "image": filename})
        return redirect(url_for("students"))
    except Exception as e:
        return render_template("form.html", error=f"Submission failed: {str(e)}")

@app.route("/students")
def students():
    with get_db() as conn:
        rows = conn.execute("SELECT id, first_name, last_name, department, level, admission_status FROM students").fetchall()
    return render_template("students.html", students=rows)

@app.route("/student/<int:student_id>")
def details(student_id):
    with get_db() as conn:
        student = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
    if not student:
        return redirect(url_for("students"))
    return render_template("details.html", student=student)

@app.route("/update_status/<int:student_id>", methods=["POST"])
def update_status(student_id):
    # Async status update endpoint
    status = request.json.get("status")
    valid = ["Pending", "Admitted", "Rejected"]
    if status not in valid:
        return jsonify({"success": False, "message": "Invalid status"}), 400
    with get_db() as conn:
        conn.execute("UPDATE students SET admission_status = ? WHERE id = ?", (status, student_id))
    return jsonify({"success": True, "message": f"Status updated to {status}"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
