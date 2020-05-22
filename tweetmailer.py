# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:04:04 2020

@author: Austin Lesh
"""

import GetOldTweets3 as got
import re
from datetime import date, timedelta
import smtplib, ssl

sending_email = input('Enter an email to send from: ')
sender_password = input('Enter password for the sender\'s email: ')
receiving_email = input('Enter an email to send to:')

username = 'jimmyfallon'
count = 20

today = str(date.today())
yesterday = str(date.today() - timedelta(days = 1))

tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                           .setMaxTweets(count)\
                                           .setSince(yesterday)\
                                           .setUntil(today)

tweets = got.manager.TweetManager.getTweets(tweetCriteria)

lst = []
    
for i in range(len(tweets)):
    text = tweets[i].text
    exps = ['Tonight']
    
    for exp in exps:
        match = re.search(exp, text)
        if match:
            lst.append(text)    
    
######

def send_email():
    port = 465  # For SSL
    
    password = sender_password
    sender_email = sending_email
    receiver_email = receiving_email

    context = ssl.create_default_context()

    message = """\
    New tweet from {}!

    Tweets of interest: {}""".format(username, lst)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
######        
            
if len(lst) != 0:
    send_email()