# this is for usiing the favicon for recon :)))))))
import requests
import mmh3
import codecs
target_url = input (' hey alio :) enter the target url :) ')
response = requests.get( target_url+'/favicon.ico')
favicon = codecs.encode(response.content , "base64")
print(favicon) # if have -fa tag print the base 64 of the favicon
hash = mmh3.hash(favicon)

print(hash )


