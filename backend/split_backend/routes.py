from .models import db, User, Purchase, Item, Group
from flask import Blueprint, g, session, request

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

#create and item and get its id
@api_bp.route("/split_api/create_item", methods=["POST", "GET"])
def create_item():
    params = request.args
    item_name = params.get("item_name")
    user_id = params.get("user_id")
    user = User.query.filter_by(id=user_id).first()

    item = Item(name=item_name, user_id=user_id, user=user, count=0)
    db.session.add(item)
    db.session.commit()
    return str(item.id)


#add item reuqest for a user
@api_bp.route("/split_api/add_item", methods=["POST", "GET"])
def req_item():
    #takes in item_id, amount
    params = request.args
    item_id = params.get("item_id")
    amount = int(params.get("amount"))

    item = Item.query.filter_by(id=item_id).first()
    item.count += amount
    db.session.commit()
    return str(item.id)

#subtract item reuqest for user
@api_bp.route("/split_api/add_item", methods=["POST"])
def sub_item():
    #takes in item_id, amount
    params = request.args
    item_id = params.get("item_id")
    amount = params.get("amount")

    item = Item.query.filter_by(id=item_id).first()
    item.count -= amount
    db.session.commit()

    return str(item.id)

#get money other people oe a user
@api_bp.route("/split_api/get_owed_money", methods=["POST"])
def get_money_owed():
    params = request.args
    user_id = params.get("user_id")

    user = User.query.filter_by(id=user_id).first()
    return str(user.owed)

#get money user owes another
@api_bp.route("/split_api/get_money_owes_others", methods=["POST"])
def get_money_owes_others():
    params = request.args
    user_id = params.get("user_id")

    user = User.query.filter_by(id=user_id).first()
    return str(user.need_to_pay)

#return dict of items {item: {user: count, user2: count2}}
@api_bp.route("/split_api/item_list")
def item_list():
    """
    Main method to display the item list along with the amount each user
    reuqests. This is in the format {item: {user: count, user2: count2}}
    amount each user
    :param: group id
    :return: the JSON dict descirbed above
    """
    d = {}
    items = Item.name
    for item in session.Query(Item):
        if item.name in d.keys():
            d[item.name][item.user.name] = item.count
        else:
            d[item.name] = {}
            d[item.name][item.user.name] = item.count
    return d

#return the total amount request for an item
#1 param: item_name
@api_bp.route("/split_api/item_total")
def item_total():
    item_name = request.args.get("item_name")
    total = 0
    for item in session.Query(Item):
        if item.name == item_name:
            total += item.count
    return total


#calculate split - scans the reciept, gets items costs, assigns to users
#takes in an image parameter, and user
