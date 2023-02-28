import requests

my_header = {"x-token": ""}



resp = requests.get("http://127.0.0.1:8000/hitems", headers=my_header)


print(resp.content)
