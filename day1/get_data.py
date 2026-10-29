import requests

# it will hit this fake api and then it will generate the resopse

url = "https://fake-json-api.mock.beeceptor.com/users"
respose = requests.get(url=url)
print(respose.json())