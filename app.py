from flask import Flask, render_template, request, redirect
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Google Sheets setup
scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
client = gspread.authorize(creds)
sheet = client.open("Counseling Form Submissions").sheet1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_form():
    if request.method == "POST":
        data = [
            request.form["session"],
            request.form["form_number"],
            request.form["date"],
            request.form["student_name"],
            request.form["admission_class"],
            request.form["father_name"],
            request.form.get("father_occupation", ""),
            request.form.get("address", ""),
            request.form.get("referred_by", ""),
            request.form.get("last_school", ""),
            request.form["phone_number"],
            request.form["school_visited"],
            request.form.get("comments", ""),
            request.form.get("counseled_by", ""),
            request.form.get("proposed_fee", ""),
            request.form.get("discount_given", ""),
            request.form.get("parent_agrees", ""),
            request.form.get("principal_comments", "")
        ]
        sheet.append_row(data)
        return redirect("/")
    return render_template("add.html")

@app.route("/search")
def search():
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)
