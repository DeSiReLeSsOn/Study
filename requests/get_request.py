import requests


"""get"""

# 200-300 - ok
# 404 - not found
# 500 - internal server error


responce = requests.get(
    "https://yandex.ru/search", params={"text": "Ronaldo"}
)  # what data is being requested?
# print(responce.headers) #service information
# print(responce.text)  # gets html

if responce.status_code == 200:
    print("ok")
else:
    print("some error", responce.status_code)


page = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = page.json()  # read json
print(data)
