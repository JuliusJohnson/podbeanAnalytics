import requests, json, os, pprint, csv
from datetime import datetime
import api_info #local imports

#Get Current Date and Time
now = datetime.today().strftime("%Y-%m-%d")

#Header Information
headers = api_info.headers #A seperate file that contains header information

#API Parameters
params = api_info.params #A seperate file that contains header information

#Call the API
response = requests.get('https://api-v2.podbean.com/admin/stats/top-download-episodes', headers=headers, params=params)
jsonResponse = response.json()['data']

#opens file for writing
top_podcast_file = open(f'top_podcast_{now}.csv', 'w')
#create the csv writer object
csv_writier = csv.writer(top_podcast_file)

#edit the json outpus as a list of dictionaries 
print(type(jsonResponse))
for podcast in jsonResponse:
    podcast.update({'datePulled' : str(now)}) #adds datetime the data was pulled from the API
    podcast.update({'publishTimeConverted' : datetime.fromtimestamp(int(podcast['publishTime'])).strftime('%Y-%m-%d %H:%M:%S')}) #converts unixtime stamp from the 'publishTime' field

pprint.pprint(jsonResponse)

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