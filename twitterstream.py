import requests
from requests_oauthlib import OAuth1
import jsonlines

api_key = "JmbILNfM04OVBP8Exst6so0p6"
api_secret = "uW9SCinVXeXVbpkbkM0m3Wj28GmKR2bEEjAbWwEonHC3MvvbrQ"
access_token_key = "1056888916945653760-UjxoEboKigdUW6uzhDcetJqXAklQVy"
access_token_secret = "muXCUmwD0b127kual3lhGgtMw1jNzQYcgzsN2y4J1VLi5"

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url, auth=auth)
print(r.status_code)

url = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = requests.get(url, auth=auth, stream=True)
if r.encoding is None:
    r.encoding = 'utf-8'

with jsonlines.open('output.json', mode='w') as writer:    
    try:
        for line in r.iter_lines(decode_unicode=True):
            if line:
                writer.write(line)
    except KeyboardInterrupt:
        pass
    
    
    


