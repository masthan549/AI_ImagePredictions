import http.client

conn = http.client.HTTPConnection("2factor.in")

payload = "{\"From\": \"{8919297732}\",\"To\": \"{8919297732}\", \"Msg\": \"{MessageBody}\"}"

conn.request("POST", "/API/V1/{c0b6f1f5-126a-11ea-9fa5-0200cd936042}/ADDON_SERVICES/SEND/TSMS", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))