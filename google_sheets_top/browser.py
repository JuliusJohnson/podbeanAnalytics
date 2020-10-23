#!/usr/bin/env python3

#To run run browsermobproxy server first:
#browsermob-proxy-2.1.4-bin/browsermob-proxy-2.1.4/bin/browsermob-proxy
import download_top_podcast #local Import
from selenium import webdriver
from browsermobproxy import Server
import re, time, json, os

#os.system('browsermob-proxy-2.1.4-bin/browsermob-proxy-2.1.4/bin/browsermob-proxy')
#import psutil

# for proc in psutil.process_iter():
#     # check whether the process name matches
#     if proc.name() == "browsermob-proxy":
#         proc.kill()

#dict = {'port': 8090}

def token_get_data():
    
    with open("/home/julius/Documents/programming/python/projects/Podbean_Analytics/credentials.json", "r") as f: # login credentials stored in seperate file
        credentials = (json.load(f)['podbean_cred'])
    #Starts Server
    server = Server("/home/julius/Documents/programming/python/projects/Podbean_Analytics/browsermob-proxy-2.1.4-bin/browsermob-proxy-2.1.4/bin/browsermob-proxy")
    server.start()
    time.sleep(1)
    proxy = server.create_proxy()
    time.sleep(1)

    #Creates Selenium webdriver
    profile = webdriver.FirefoxProfile()
    selenium_proxy = proxy.selenium_proxy()
    profile.set_proxy(selenium_proxy)
    driver = webdriver.Firefox(firefox_profile=profile)

    #Log in to Podbean 
    proxy.new_har("podbean")
    driver.get("https://www.podbean.com/login")
    driver.find_element_by_id("LoginForm_username").send_keys(credentials['username'])
    driver.find_element_by_id("LoginForm_password").send_keys(credentials['password'])
    driver.find_element_by_name("yt0").click()
    time.sleep(5)#Provides enough time for the page to load the needed elements

    #Captures HAR(HTTP Archive Format) output from loaded content within the first 5 seconds of loading
    credentials_har_raw = proxy.har #returns a HAR JSON blob

    #parse HAR output using regex
    accesstokenRegex = re.compile(r'access-token=([^&]*)')
    matches = accesstokenRegex.search(str(credentials_har_raw))
    #print(mo.groups()[0])
    token = (matches.groups()[0])

    download_top_podcast.downloadTopPodcast(token) #downlaods data from podbean API and puts into Spreadsheet
    #time.sleep(90)#The website must stay loaded for the duration of the python excution. A new Access Token is generated at time of login.
    server.stop()
    driver.quit()