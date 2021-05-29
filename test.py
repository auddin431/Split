"""
Python script to test if the backend is working.
Puts in needed data
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

user3_params = {
    "username": "sarah",
    "password": "abhi"
}

# test user creation and login
prefix = "http://localhost:5000/split_api/"
user1_reg = requests.get(prefix + "user/create", params=user1_params)
user1_id = user1_reg.text

user2_reg = requests.get(prefix + "user/create", params=user2_params)
user2_id = user2_reg.text

user3_reg = requests.get(prefix + "user/create", params=user3_params)
user3_id = user3_reg.text

#create group and add the two users
group_params = {
    "group_name": "roommates",
    "purchase_name": "jan_groceries"
}

create_group = requests.get(prefix + "create_group", params=group_params)
group_id = int(create_group.text)

add1 = {
    "group_id": int(group_id),
    "user_id": int(user1_id)
}

add2 = {
    "group_id": int(group_id),
    "user_id": int(user2_id)
}

add3 = {
    "group_id": int(group_id),
    "user_id": int(user3_id)
}

add_user1 = requests.get(prefix + "add_user_to_group", params=add1)
add_user2 = requests.get(prefix + "add_user_to_group", params=add2)
add_user3 = requests.get(prefix + "add_user_to_group", params=add3)


#test adding and subtracting items, as well as viewing an item list

req_item1 = {
    "item_name": "Bananas",
    "user_id": int(user1_id),
    "amount": 2
}

req_item2 = {
    "item_name": "Cherrios",
    "user_id": int(user2_id),
    "amount": 2
}

req_item3 = {
    "item_name": "Milk",
    "user_id": int(user2_id),
    "amount": 3
}

req_item4 = {
    "item_name": "Lunchables",
    "user_id": int(user3_id),
    "amount": 1
}

req_item5 = {
    "item_name": "Hershey",
    "user_id": int(user2_id),
    "amount": 4
}

req_item6 = {
    "item_name": "Hershey",
    "user_id": int(user3_id),
    "amount": 3
}

add_item1_ = requests.get(prefix + "add_item", params=req_item1)
add_item2_ = requests.get(prefix + "add_item", params=req_item2)
add_item3_ = requests.get(prefix + "add_item", params=req_item3)
add_item4_ = requests.get(prefix + "add_item", params=req_item4)
add_item5_ = requests.get(prefix + "add_item", params=req_item5)
add_item6_ = requests.get(prefix + "add_item", params=req_item6)

#test item dict
item_dict = requests.get(prefix + "item_list")
print(item_dict.text)

it_name = {
    "item_name": "Hershey"
}

item_total = requests.get(prefix + "item_total", params=it_name)




