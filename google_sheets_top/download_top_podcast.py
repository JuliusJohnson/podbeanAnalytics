#Gets Top "X" Podcast
import requests, json, os, pprint, csv
from datetime import datetime
import headers #local import

def downloadTopPodcast(accesstoken):
    #get podbean credentials:
    #with open("accesstoken2.json", "r") as f:
    #    accessToken = json.load(f)['podbean_cred']['accesstoken']#accessToken stored in seperate file

    #Get Current Date and Time
    now = datetime.today().strftime("%Y-%m-%d")

    #Header Information
    head = headers.headers #A seperate file that contains header information

    #API Parameters
    params = [
    ['slug', 'thepathchurch'],
    ['access-token', str(accesstoken)],
    ['start', '2016-12-01'], 
    ['end', now], 
    ['period', 'd'],
    ['limit', '50'],
    ['t', '5f83c0af'],
    ['s', 'WJkBFKR/M2QkSQJkTJCB1eWfND4=']
    ]

    #Call the API
    response = requests.get('https://api-v2.podbean.com/admin/stats/top-download-episodes', headers=head, params=params)
    jsonResponse = response.json()['data']

    #opens file for writing
    top_podcast_file = open(f'google_sheets_top/top_podcast_{now}.csv', 'w')
    #create the csv writer object
    csv_writier = csv.writer(top_podcast_file)

    #edit the json outpus as a list of dictionaries 
    #print(type(jsonResponse)) -- for debugging
    for podcast in jsonResponse:
        podcast.update({'datePulled' : str(now)}) #adds datetime the data was pulled from the API
        podcast.update({'publishTimeConverted' : datetime.fromtimestamp(int(podcast['publishTime'])).strftime('%Y-%m-%d %H:%M:%S')}) #converts unixtime stamp from the 'publishTime' field

    #3 Counter variable used for writing headers to the CSV file
    count = 0

    for podcast in jsonResponse:
        if count == 0:

            #Wrirting headers of CSV File
            header = podcast.keys()
            csv_writier.writerow(header)
            count +=1
        
        #Writing data of CSV file
        csv_writier.writerow(podcast.values())
    top_podcast_file.close()