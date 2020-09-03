import download_top_podcast, upload_top_podcast

def runTopPodcast():
    download_top_podcast.downloadTopPodcast() #downlaods data from podbean API and puts into Spreadsheet
    upload_top_podcast.uploadData() #handles uploading data to Google Spreadsheets and file cleanup

runTopPodcast()