import browser, upload_top_podcast
import os

def runTopPodcast():
    browser.token_get_data()
    #upload_top_podcast.uploadData() #handles uploading data to Google Spreadsheets and file cleanup

def run_server():
    pass

runTopPodcast()

'''
#File Clean Up
for file in filtered_files:
        path_to_file = os.path.join("./google_sheets_top",file)
        os.remove(path_to_file)

'''