from flask import Flask, render_template, request, redirect
import gspread
import os
import json
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Google Sheets setup
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.readonly"
]

# Authentication using service account credentials from environment variable
if "GOOGLE_CREDENTIALS" in os.environ:
    creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])
    creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
else:
    # fallback for local development
    creds = Credentials.from_service_account_file("credentials.json", scopes=scope)

# Authorize gspread with the credentials
client = gspread.authorize(creds)

# Spreadsheet setup
SPREADSHEET_ID = "1vb_dh0SrwmKU8ZmXs0xNod1GJlvcMu-XqbyymeAkdyg"
try:
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet("Sheet1")
    print("✅ Successfully connected to Google Sheet.")
except Exception as e:
    print(f"❌ ERROR connecting to Google Sheet: {e}")
    sheet = None  # Prevent crashing if connection fails

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_form():
    if request.method == "POST":
        # Capture form data exactly in the order of Google Sheet headers
        data = [
            request.form.get("session", ""),
            request.form.get("form_number", ""),
            request.form.get("date", ""),
            request.form.get("name", ""),               # corrected (not student_name)
            request.form.get("admission_class", ""),
            request.form.get("father_name", ""),
            request.form.get("father_occupation", ""),
            request.form.get("address", ""),
            request.form.get("referred_by", ""),
            request.form.get("last_school", ""),
            request.form.get("phone", ""),              # corrected (not phone_number)
            request.form.get("school_visited", ""),
            request.form.get("proposed_fees", ""),      # corrected (was proposed_fee)
            request.form.get("discount_given", ""),
            request.form.get("fee_agreement", ""),      # corrected (was parent_agrees)
            request.form.get("comments", ""),
            request.form.get("counseled_by", ""),
            request.form.get("principals_comments", "") # corrected (was principal_comments)
        ]

        if sheet:
            try:
                sheet.append_row(data)
                print("✅ Data successfully saved to Google Sheet.")
            except Exception as e:
                print(f"❌ ERROR saving data to Google Sheet: {e}")
        else:
            print("❌ No sheet connection available.")
        return redirect("/")
    
    return render_template("add.html")

@app.route("/search")
def search():
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)
