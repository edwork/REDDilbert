#!/usr/bin/env python3

"""REDDilbert.py: Fetches the daily Dilbert Strip and posts to Reddit"""

__author__    = "Edward Boal"
__email__     = "ed.boal@edwork.org"
__version__   = "1.0"
__licence__   = "GPL"

import time
from urllib.request import urlopen
import yaml
from bs4 import BeautifulSoup
import praw

print ('Generating Post')
## Date in 'yyyy-mm-dd' format
currentDate = (time.strftime("%Y-%m-%d"))
## Create today's URL
dilbertURL = 'http://dilbert.com/strip/' + currentDate
## Fetch today's URL, parse for title
soup = BeautifulSoup(urlopen(dilbertURL), "html.parser")
## Trim the title
postTitle = soup.title.string[:-24]
## Output to Console
print ('Post URL: ' + dilbertURL)
print ('Post Title: ' + postTitle)
## Create Settings Dict from yaml config
REDDilbertSettings = yaml.load(open('config.yaml'))
## Create a Reddit Instance
reddit = praw.Reddit(client_id=(REDDilbertSettings["client_id"]), client_secret=(REDDilbertSettings["client_secret"]),
                     password=(REDDilbertSettings["password"]), user_agent=(REDDilbertSettings["user_agent"]),
                     username=(REDDilbertSettings["username"]))
## Post to Reddit
## Check for existing post with the same title we are about to submit, post if all is clear
subreddit = reddit.subreddit(REDDilbertSettings["subreddit"])
for submission in subreddit.hot(limit=10):
    if (submission.url) == dilbertURL:
        print ("Post Exists, Skipping")
    else:
        print ("Posting Today's Strip")
        reddit.subreddit(REDDilbertSettings["subreddit"]).submit(postTitle, url=dilbertURL)