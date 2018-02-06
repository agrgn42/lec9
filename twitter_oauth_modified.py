
# STEP 3: Now we have verification from the user. It's a special code that
# will let us get an access token that we can use to get the actual data that
# we have been trying to hard to get.
# Wait, what? We still don't have access to the user's data? Nope.
# What we have now is an "opaque" token that will give us access to their data
# (remember, that we could only get this token after the user logged in and
# retreived it).
#
# Aside: when we created our API key, we asked for specific permissions.
#        For Twitter they're not that interesting--either Read or Read/Write.
#        Point is, those permissions matter--they're going to be encoded in
#        the access token we get next. We can only access the stuff our
#        application specifically asked for
#
# OK, back to work: now we need the access token so we can get some actual
# data. There is yet another URL we need to hit to get this.
access_token_url = 'https://api.twitter.com/oauth/access_token'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret,
                          verifier=verifier)
oauth_tokens = oauth.fetch_access_token(access_token_url)

resource_owner_key = oauth_tokens.get('oauth_token')
resource_owner_secret = oauth_tokens.get('oauth_token_secret')

print(resource_owner_key, resource_owner_secret)