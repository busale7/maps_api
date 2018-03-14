from django.shortcuts import render
from urllib.parse import quote
import oauth2
# Create your views here.
CONSUMER_KEY ="JOp5t7DapP5HijinscAVul7kB"
CONSUMER_SECRET ="MK7UWGuDt8qnub94SE9jlJ1v1wCC0T7Ucqz7cHzECVbfVXRFth"

def oauth_req(url, key, secret, http_method="GET", post_body='', http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content


def tweetsearch(request):
	query="@busale7"
	enc_q=quote(query)
	url="https://api.twitter.com/1.1/search/tweets.json?q=%s"%(enc_q)
	token ="some_token"
	token_secert ="some_token_secret"

	response=oauth_req(url,token,token_secert, "GET")
	print(response)
	pass
