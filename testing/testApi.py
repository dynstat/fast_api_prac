import requests

my_header = {"x-token": ""}
my_cookie = {"meri_cookie2": "hohohoho"}

resp = requests.get("http://127.0.0.1:8000/test3", headers=my_header, cookies=my_cookie)

print(resp.content)
