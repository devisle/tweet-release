import tweepy
from github import Github
import config

g = Github()

repo = g.get_repo("devisle/advanced-react-cli")
release = repo.get_releases()[0]
# Replaces GitRelease(title=" ") and only outputs version number.
version = str(release).replace('GitRelease(title="', '').replace('")', '')

auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET_KEY)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
screen_name = "devisle"

user = api.get_user(screen_name)
tweets = api.user_timeline(screen_name = screen_name, tweet_mode="extended", include_retweets=False)
full_tweet = [[tweet.full_text] for tweet in tweets]

try:
    api.update_status("New release " + version + " 🎉🎉!" "\n\nhttps://github.com/devisle/advanced-react-cli\n\n#js #react #npm")
except tweepy.TweepError as error:
    if error.api_code == 187:
        print('Tweet already exists.')
    else:
        raise error
