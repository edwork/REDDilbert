# REDDilbert
Fetches the daily Dilbert Strip and posts to Reddit

### Why?
I wanted to post the daily Dilbert comic strip to Reddit automatically without using a third party service.

### How does it work?
It generates a date based URL that corresponds to the Daily Dilbert comic strip on dilbert.com. The URL is fetched and the HTML Title tag is parsed, which is used to generate a Reddit post title. The URL to the comic and post title are then submitted to Reddit. A check is done prior to posting to ensure we don't repost. The check is done on the URL in case somebody posts with a different title.

### This is useless to anyone else, right?
No. There's a YAML based config file. All you need to do is change some of the config options and you can start posting to X subreddit with Y site. It could take a little tweaking but it can be done. This is more of an example than anything else.

## Requirements:
* Python3
* PIP3
  * urllib
  * pyyaml
  * bs4
  * praw

## Installation:
Running it via cron is easy. Just create a new cron job that runs daily, like so:
<code>0 1 * * * /usr/bin/python3 /path/to/script/REDDilbert.py</code>

The above example runs daily at 01:00.

## Want to contribute?
I plan on trying to make this more extensible and able to snag more URLs and parse them into post titles for all of that sweet sweet Karma. Feel free to send me a PR.
