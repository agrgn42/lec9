
from requests_oauthlib import OAuth1Session
from secrets2 import client_key, client_secret, access_token, access_token_secret

#Code for OAuth starts
oauth = OAuth1Session(client_key, client_secret, access_token, access_token_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
print (r.text)
