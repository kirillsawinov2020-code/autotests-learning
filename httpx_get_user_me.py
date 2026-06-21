import httpx

data = {
    "email": "kirill.savin0v@yandex.ru",
    "password": "qwerty123"
}

response_login = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=data)
response = response_login.json()
print(response_login.status_code)
print(response)

token = response['token']['accessToken']

headers = {
    "Authorization": f"Bearer {token}"
}


getme = {
  "user": {
    "id": "string",
    "email": "user@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
  }
}

response_me = httpx.get("http://127.0.0.1:8000/api/v1/users/me",headers=headers)
response2 = response_me.json()

print(response_me.status_code)
print(response2)


