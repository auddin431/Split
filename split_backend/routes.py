from .models import db, User, Purchase, Item, Group
from flask import Blueprint, g, session, request
import json
from .config import client_id, client_secret, username, api_key
from veryfi import Client

api_bp = Blueprint(
    "api_bp", __name__
)

"""
NOTE: in order to register users, the api_reg_user
method in auth.py is needed.

"""

"""
NOTE ON TESTING: In order to have some data to test
without a front end, first run the flask server with
'python wsgi.py". Then, in a seperate terminal run
python test.py. Now, some data is populated in
the database. Then, test_split_image can be run
with the appropriate image.'

Make sure to delete test_cat.db and image.png
before restarting the flask server
"""


#create group and returns the group id
#also creates an empty purchase object
@api_bp.route("/split_api/create_group", methods=["POST", "GET"])
def create_group():
    """
    Create a new group. Need to pass in a group_name
    and a purchase_name
    ex. group_name = "roomates", purchase_name = "january_groceries"
    :return: the new group's id
    """
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
    Need to pass in user_id and group_id. Adds the user to the group. This
    is needed for future functions
    :return: group id the user was added to
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
    """
    Takes in a user_id, item_name, and amount. The item name
    needs to be an exact match to what is on the recipt image.
    The amount will overwrite any previous amount present.
    ex. item_name = "apple", amount=3
    :return: the id of the item requested
    """
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
    """
    Needs a user_id
    :return: the amount the user is owed by others
    """
    params = request.args
    user_id = params.get("user_id")

    user = User.query.filter_by(id=user_id).first()
    return str(user.owed)

#get money user owes another
@api_bp.route("/split_api/get_money_owes_others", methods=["POST", "GET"])
def get_money_owes_others():
    """
    Needs a user_id
    :return: Returns the amount the user needs to pay others
    """
    params = request.args
    user_id = params.get("user_id")

    user = User.query.filter_by(id=user_id).first()
    return str(user.need_to_pay)

#return dict of items {item: {user: count, user2: count2}}
@api_bp.route("/split_api/item_list", methods=["GET", "POST"])
def item_list():
    """
    Main method to display the item list along with the amount each user
    reuqests. This is in the format {item: {user: count, user2: count2},
    item2: {user: count}}. Users with no items DO NOT appear with a count of 0
    amount each user
    :param: no input necessary
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
    """
    Gives the specific amount that was reuqested
    for an item.
    :param: item_name (exact match)
    :return: the total number requested among all people
    """
    item_name = request.args.get("item_name")
    items = db.session.query(Item)
    total = 0
    for item in items:
        if item.name == item_name:
            total += item.count
    return str(total)

def parse_recipt(img_path):
    """
    HELPER_METHOD

    Uses the VeryFi API to parse
    a recipt. Returns a dict of item, price. This
    is a helper method not called by the frontend"""
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
    HELPER_METHOD

    Identical to orginal method but used for backend, and
    return just the dictionary. HELPER METHOD
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
    """
    HELPER_METHOD
    """
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
    """
    Takes in an image and the user_id of the person
    who paid. This only returns a json of what the
    OCR managed to read, but the real work is done my modifying
    the backend database.

    This can be called by putting the file bytes in the
    files section of the request with title image. The payer_id can be
    passed in regularly. NOTE: this method uses payer_id, not user_id

    If the recipt image should not come from the frontend and instead
    be hard coded, insert the image in the directory above
    this one. Then, comment out lines 245 and 247. Change the file
    name in like 248 to the image to be read.

    To get a list of all the people and the amount
    they owe others/are owed themselves, use the method below
    called get_people()
    :return:
    """
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
    """
    Takes in nothing, but returns useful info after a split.
    It returns all the users and the amount of money they 1)
    need to pay others and 2) the amount others need to pay them, in that order.

    ex. {person_name: [need to pay, owed], person2_name: [need to pay, owed], ...}
    :return: JSON data
    """
    d = {}
    all_people = db.session.query(User)
    for person in all_people:
        d[person.name] = [person.need_to_pay, person.owed]
    return json.dumps(d)