from flask import Flask, render_template, request, redirect
import gspread
import os
import json
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Google Sheets setup using environment variable
scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds_dict = json.loads(os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"])
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)
sheet = client.open("Counseling Form Submissions").worksheet("Sheet1")

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

        # Try to append data to Google Sheets
        try:
            sheet.append_row(data)
            print("✅ Data successfully written to Google Sheet.")
        except Exception as e:
            print("❌ ERROR while writing to sheet:", e)

        return redirect("/")
    return render_template("add.html")

@app.route("/search")
def search():
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)
