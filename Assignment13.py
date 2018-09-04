import requests
response=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=text&key=98765")
print(response.content)
