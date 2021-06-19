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

try:
    api.update_status("New release " + version + " 🎉🎉!" "\n\nhttps://github.com/devisle/advanced-react-cli\n\n#js #react #npm")
    print("New release has been tweeted.")
except tweepy.TweepError as error:
    if error.api_code == 187:
        print('Tweet already exists.')
    else:
        raise error
