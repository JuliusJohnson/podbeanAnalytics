import browser, upload_top_podcast

def runTopPodcast():
    browser.token_get_data()
    #download_top_podcast.downloadTopPodcast() #downlaods data from podbean API and puts into Spreadsheet
    #upload_top_podcast.uploadData() #handles uploading data to Google Spreadsheets and file cleanup

runTopPodcast()

'''
#File Clean Up
for file in filtered_files:
        path_to_file = os.path.join("./google_sheets_top",file)
        os.remove(path_to_file)

'''