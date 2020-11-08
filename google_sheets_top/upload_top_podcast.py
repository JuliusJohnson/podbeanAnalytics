import gspread, csv, os
from oauth2client.service_account import ServiceAccountCredentials

def uploadData():
    #GOOGLE AUTH STUFF
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/julius/Documents/programming/python/projects/Podbean_Analytics/client_secret.json', scope)
    client = gspread.authorize(credentials)

    files = os.listdir('google_sheets_top')
    filtered_files = [file for file in files if file.endswith(".csv")]

    #OPENS TARGET GOOGLE SHEET
    spreadsheet = client.open('Copy of PodBean Stats')
    sheet = spreadsheet.sheet1

    #APPENDS LATEST DATA
    with open(f'google_sheets_top/{filtered_files[0]}', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        sheet.append_rows(data[1:], value_input_option='USER_ENTERED', insert_data_option='INSERT_ROWS')