"""
Python script to test if the backend is working
"""
import requests

user1_params = {
    "username": "sam",
    "password": "abhi"
}

user2_params = {
    "username": "bill",
    "password": "abhi"
}

# test user creation and login
prefix = "http://0.0.0.0:5000/split_api/"
user1_reg = requests.get(prefix + "user/create", params=user1_params)
print(user1_reg.text)
user1_id = user1_reg.text
user2_reg = requests.get(prefix + "user/create", params=user2_params)
print(user2_reg.text)
user2_id = user2_reg.text

#create group and add the two users
group_params = {
    "group_name": "roommates",
    "purchase_name": "jan_groceries"
}

create_group = requests.get(prefix + "create_group", params=group_params)
group_id = int(create_group.text)
print(group_id)

add1 = {
    "group_id": int(group_id),
    "user_id": int(user1_id)
}

add2 = {
    "group_id": int(group_id),
    "user_id": int(user2_id)
}

add_user1 = requests.get(prefix + "add_user_to_group", params=add1)
add_user2 = requests.get(prefix + "add_user_to_group", params=add2)


#test adding and subtracting items, as well as viewing an item list
create_item1 = {
    "user_id": int(user1_id),
    "item_name": "apple"
}

create_item2 = {
    "user_id": int(user1_id),
    "item_name": "bannana"
}
add_item1 = requests.get(prefix + "create_item", params=create_item1)
add_item2 = requests.get(prefix + "create_item", params=create_item2)

req_item1 = {
    "user_id": int(user1_id),
    "item_id": int(add_item1.text),
    "amount": 3
}

req_item2 = {
    "user_id": int(user2_id),
    "item_id": int(add_item2.text),
    "amount": 2
}




