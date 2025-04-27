import oauthlib
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Define the scope of the API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets"]

# Replace this with the path to your credentials JSON file
creds = ServiceAccountCredentials.from_json_keyfile_name("path_to_your_credentials.json", scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet by name (replace "Your Google Sheet Name" with the actual sheet name)
sheet = client.open("Your Google Sheet Name").sheet1

# Fetch and print all records from the sheet
print(sheet.get_all_records())
