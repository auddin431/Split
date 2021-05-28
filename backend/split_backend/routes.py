from .models import db, User, Purchase, Item, Group
from flask import Blueprint, g, session, request
import json
from .config import client_id, client_secret, username, api_key
from veryfi import Client

api_bp = Blueprint(
    "api_bp", __name__
)

#create group and returns the group id
#also creates an empty purchase object
@api_bp.route("/split_api/create_group", methods=["POST", "GET"])
def create_group():
    #need to pass in group name and purchase name
    #group_name, purchase_name
    new_group = Group(name=request.args.get("group_name"))
    db.session.add(new_group)

    new_purchase = Purchase(name=request.args.get("purchase_name"))
    new_purchase.group_id = new_group.id
    new_purchase.group = new_group
    db.session.add(new_purchase)

    db.session.commit()
    return str(new_group.id)


#add user to group
@api_bp.route("/split_api/add_user_to_group", methods=["POST", "GET"])
def add_user_to_group():
    """
    Need to pass in user_id, and group_id
    :return: group id is success, or -1
    """
    params = request.args
    user_id = params.get("user_id")
    group_id = params.get("group_id")

    user = User.query.filter_by(id=user_id).first()
    user.group_id = group_id

    group = Group.query.filter_by(id=group_id).first()
    user.group = group
    db.session.commit()
    return str(group_id)


#add item reuqest for a user
@api_bp.route("/split_api/add_item", methods=["POST", "GET"])
def req_item():
    #takes in item_id, user_id, amount
    params = request.args
    item_name = params.get("item_name")
    user_id = params.get("user_id")
    amount = int(params.get("amount"))

    final_item = None
    items = db.session.query(Item)
    for item in items:
        if item.name == item_name and int(item.user_id) == int(user_id):
            item.count = amount
            db.session.commit()
            return str(item.id)

    if final_item is None:
        user = User.query.filter_by(id=user_id).first()
        new_item = Item(name=item_name, user_id=user_id, user=user, count=0)
        final_item = new_item

    final_item.count = amount
    db.session.add(final_item)
    db.session.commit()
    return str(final_item.id)

#get money other people oe a user
@api_bp.route("/split_api/get_owed_money", methods=["POST", "GET"])
def get_money_owed():
    params = request.args
    user_id = params.get("user_id")

    user = User.query.filter_by(id=user_id).first()
    return str(user.owed)

#get money user owes another
@api_bp.route("/split_api/get_money_owes_others", methods=["POST", "GET"])
def get_money_owes_others():
    params = request.args
    user_id = params.get("user_id")

    user = User.query.filter_by(id=user_id).first()
    return str(user.need_to_pay)

#return dict of items {item: {user: count, user2: count2}}
@api_bp.route("/split_api/item_list", methods=["GET", "POST"])
def item_list():
    """
    Main method to display the item list along with the amount each user
    reuqests. This is in the format {item: {user: count, user2: count2}}
    amount each user
    :param: group id
    :return: the JSON dict descirbed above
    """
    d = {}
    items = db.session.query(Item)
    for item in items:
        if item.name in d.keys():
            d[item.name][item.user.name] = item.count
        else:
            d[item.name] = {}
            d[item.name][item.user.name] = item.count
    return json.dumps(d)

#return the total amount request for an item
#1 param: item_name
@api_bp.route("/split_api/item_total", methods=["GET", "POST"])
def item_total():
    item_name = request.args.get("item_name")
    items = db.session.query(Item)
    total = 0
    for item in items:
        if item.name == item_name:
            total += item.count
    return str(total)

def parse_recipt(img_path):
    """Uses the VeryFi API to parse
    a recipt. Returns a dict of item, price"""
    veryfi_client = Client(client_id, client_secret, username, api_key)
    categories = ['Grocery', 'Utilities', 'Travel']
    # This submits document for processing (takes 3-5 seconds to get response)

    response = veryfi_client.process_document(img_path, categories=categories)

    ret = {}
    for line in response["line_items"]:
        ret[line["description"]] = line["total"]
    return ret

def item_list_helper():
    """
    Identical to orginal method but used for backend, and
    return just the dictionary
    """
    d = {}
    items = db.session.query(Item)
    for item in items:
        if item.name in d.keys():
            d[item.name][item.user.name] = item.count
        else:
            d[item.name] = {}
            d[item.name][item.user.name] = item.count
    return d

def get_people_who_wanted_item(item_name):
    people = []
    quants = []
    items = db.session.query(Item)
    for item in items:
        if item.name == item_name:
            user = User.query.filter_by(id=item.user_id).first()
            people.append(user.id)
            quants.append(item.count)
    return people, quants

#calculate split - scans the reciept, gets items costs, assigns to users
#takes in an image parameter, and user
@api_bp.route("/split_api/split", methods=["GET", "POST"])
def split():
    #Read image and perform OCR and ICR
    file = request.files["image"]
    payer_id = request.args.get("payer_id")
    file.save("image.png")
    line_items = parse_recipt("image.png")

    #Calculate how much each person owes and is owed
    #returns {user: [need to pay, owed]}

    item_requests = item_list_helper()
    sorted_items = sorted(item_requests.keys(), key=lambda x: x.lower())
    people_running_total = {}
    for item in sorted_items:
        total_price_for_item = line_items[item]
        people_who_req_item, quant_req = get_people_who_wanted_item(item)
        total_wanted_among_all_people = sum(quant_req)
        for i, person in enumerate(people_who_req_item):
            inter =total_price_for_item * (quant_req[i] / total_wanted_among_all_people)
            if person in people_running_total.keys():
                people_running_total[person] += inter
            else:
                people_running_total[person] = inter

    buyer = User.query.filter_by(id=payer_id).first()
    all_people = db.session.query(User)
    for person in all_people:
        if int(person.id) != int(payer_id):
            buyer.owed += people_running_total[person.id]
            person.need_to_pay += people_running_total[person.id]
    db.session.commit()

    return json.dumps(line_items)

#get JSON of {people: {need to pay, owed}, ...}
@api_bp.route("/split_api/get_all_people", methods=["GET", "POST"])
def get_people():
    d = {}
    all_people = db.session.query(User)
    for person in all_people:
        d[person.name] = [person.need_to_pay, person.owed]
    return json.dumps(d)


