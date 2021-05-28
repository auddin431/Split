#test image
my_img = {
    "image": open("rec.png", "rb"),
}
p = {
    "payer_id": int(user1_id)
}
split = requests.get(prefix + "split", files=my_img, params=p)
print(split.text)