url='http://api.open-notify.org/astros.json"
response=urllib.request.urlopen(url)
result=json.loads(response.read())
print(result)
