
import urllib.request

APIKey = "c0b6f1f5-126a-11ea-9fa5-0200cd936042"
Sender = "TFCTOR"
To = "{8919297732,9790297893}"
message = "\'Sample%20Auto%20Send%20Message%20Based%20on%20unusual%20stuff%20seen%20near%20by\'"
url = "https://2factor.in/API/R1/?module=PROMO_SMS&apikey="+APIKey+"&to="+To+"&from="+Sender+"&msg="+message+""

r = urllib.request.urlopen(url)
print(r.read())

'''
conn = http.client.HTTPConnection("2factor.in")

payload = "{\"From\": \"TFCTOR\",\"To\": \"{8919297732, 8919297732}\", \"Msg\": \"Hellow\"}"

conn.request("POST", "/API/V1/c0b6f1f5-126a-11ea-9fa5-0200cd936042/ADDON_SERVICES/SEND/TSMS", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))'''