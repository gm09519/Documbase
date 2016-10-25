import requests
import urlfetch
import time
reader=open("docurl.txt","r")
out=open("originalurl.txt","w")
for docurl in reader.read().split('\n'):
    response = urlfetch.fetch(docurl, follow_redirects=False)
    location1 = response.headers['location']
    print (response.headers['location'])
    time.sleep(1)
    out.write(location1)
    out.write("\n")
out.close()
reader.close()