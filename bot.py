import markovify
import twitter
import randint
import time

auth_token = '687DF53JDNVDSAQ4542H3J67813JDANQ'

username = 'TheSXSWPlug'
password = 'adamabot'

twitter.authenticate(username=username, password=password, authentication_token=auth_token)
second = 1000
while(1):
  if time.clock()/second % 3600 == 0:
    tweets = markovify(twitter.feed.raw())

    for tweet in tweets:
      rand_num = randint(1, 999)
      if rand_num >= 50 and rand_num <= 100:
        twitter.tweet(tweet)

  
 
