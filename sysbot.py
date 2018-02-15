#!/usr/bin/python
from app import bot
import sys
import os
try:
    url = os.environ["SLACK_WEBHOOK_URL"]
    print sys.argv
    message = bot.create_message(sys.argv)
    response = bot.post_to_slack(message,url)
    print response

except KeyError :
    print "No WebHook URL Provided : \n" \
          "$ export SLACK_WEBHOOK_URL='https://SecretSite.Shh/SecretURL'"
