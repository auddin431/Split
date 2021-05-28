import requests
prefix = "http://0.0.0.0:5000/split_api/"
#test image
my_img = {
    "image": open("rec.png", "rb"),
}
p = {
    "payer_id": 0
}
split = requests.get(prefix + "split", files=my_img, params=p)
print(split.text)