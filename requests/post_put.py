import requests

# post - create
website = "https://jsonplaceholder.typicode.com/posts"


responce_post = requests.post(
    website,
    data={
        "userId": 1,
        "title": "creating a new post",
        "body": "some text,it does not matter",
        "photo": {"1.png", "2.jpg", "3.png"},
    },
)  # creating a new post


print(responce_post.text)


# Update


website_for_put = "https://jsonplaceholder.typicode.com/posts/5"

responce_put = requests.put(
    website_for_put,
    data={
        "userId": 1,
        "title": "updating post",
        "body": "some text,it does not matter",
        "photo": {"1.png", "2.jpg", "3.png"},
    },
)
print(responce_put.text)
