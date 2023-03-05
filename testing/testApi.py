import requests

my_header = {"x-token": ""}
my_cookie = {
    "encoded_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjc3ODY0NjQ1fQ.faMjJP0SWsfhiWK5tdS4kKwdteKJ7aIcwiQtSj4WAoI"
}

resp = requests.get("http://127.0.0.1:8000/users/all2", cookies=my_cookie)

print(resp.content)
