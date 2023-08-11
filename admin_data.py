import requests
from pprint import pprint

url = "https://sit.backend.vriti.ai/api/v2/get-db-details/"

payload = {}
headers = {
  'vriti': 'vinashak-ai',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyNDQ3NzQ0LCJqdGkiOiJiMDNhYTkyZTAxODk0MDlkYWE3OGE4NzNkMzkyY2MzMCIsImFjY291bnRfaWQiOjc0N30.I9IELhwCW2fkVc_Vpo8m7yo6PRqqnn4inXtioA9UcSQ',
  'Cookie': 'sessionid=va5h13v76g9w9arvk9dx8p7nvcj8bjhi'
}

response = requests.request("GET", url, headers=headers, data=payload)

# pprint(response.json())

with open('admin.txt','a') as file:
    print(response.json(),file=file)
