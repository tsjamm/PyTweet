from sys import argv
import twitter

script, twitter_name = argv

api = twitter.Api()

last5_msgs = api.GetUserTimeline(twitter_name)

print "Last 5 Tweets from Channel %r : " % twitter_name

for i in range(0, 6):
    print "Tweet - %s\n\n" % last5_msgs[i].text

