import browser, upload_top_podcast
import os, time, glob
from datetime import datetime

now = datetime.today().strftime("%Y-%m-%d") 

if __name__=='__main__':
    browser.token_get_data() #pulls data from API, converts to csv, then does some light processing
    upload_top_podcast.uploadData() #handles uploading data to Google Spreadsheets and file cleanup
    os.remove(f'/home/julius/Documents/programming/python/projects/Podbean_Analytics/google_sheets_top/top_podcast_{now}.csv') #deletes the generated csv file