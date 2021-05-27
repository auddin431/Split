from .models import db, User, Purchase, Item, Group
from flask import Blueprint, g, session, request

api_bp = Blueprint(
    "api_bp", __name__
)

#create group and returns the group id
#also creates an empty purchase object
@api_bp.route("/split_api/create_group", methods=["POST"])
def create_group():
    #need to pass in group name and purchase name
    #group_name, purchase_name
    new_group = Group(name=request.args.get("group_name"))
    new_purchase = Purchase(name=request.args.get("purchase_name"))
    new_purchase.group_id = new_group.id
    new_purchase.group = new_group
    db.session.add(new_purchase)
    db.session.add(new_group)
    db.session.commit()
    return new_group.id


#add user to group
@api_bp.route("/split_api/add_user_to_group", methods=["POST"])
def add_user_to_group():
    """
    Need to pass in user_id, and group_id
    :return: group id is success, or -1
    """
    params = request.args
    user_id = params.get("user_id")
    group_id = params.get("group_id")
    user = User.query.filter_by(name=user_id).first()
    group = Group.query.filter_by(id=group_id)
    user.group_id = group_id
    user.group = group
    db.session.commit()
    return group_id


#add item reuqest for a user
@api_bp.route("/split_api/add_item", methods=["POST"])
def req_item():
    #takes in user id, item name, and amount to add for user
    #will create item if doesn't exist yet
    #user_id, item_name, amount
    #returns item id
    params = request.args
    user_id = params.get("user_id")
    item_name = params.get("item_name")
    amount = params.get("amount")

    item = Item.query.filter_by(name=item_name).first()
    if item is None:
        item = Item(name=item_name, count=0)
    item.count += amount

    user = User.query.filter_by(id=user_id).first()
    item.user_id = user_id
    item.user = user
    return item.id

#subtract item reuqest for user
@api_bp.route("/split_api/add_item", methods=["POST"])
def sub_item():
    #takes in user id, item name, and amount to subtract for user
    #user_id, item_name, amount
    #returns item id
    #does nothing if item does not exist
    params = request.args
    user_id = params.get("user_id")
    item_name = params.get("item_name")
    amount = params.get("amount")

    item = Item.query.filter_by(name=item_name).first()
    if item is None:
        return -1
    item.count -= amount

    user = User.query.filter_by(id=user_id).first()
    item.user_id = user_id
    item.user = user
    return item.id

#get money other people oe a user
@api_bp.route("/split_api/get_owed_money", methods=["POST"])
def get_money_owed():
    params = request.args
    user_id = params.get("user_id")

    user = User.query.filter_by(id=user_id).first()
    return user.owed

#get money user owes another
@api_bp.route("/split_api/get_money_owes_others", methods=["POST"])
def get_money_owes_others():
    params = request.args
    user_id = params.get("user_id")

    user = User.query.filter_by(id=user_id).first()
    return user.need_to_pay

#return dict of items {item: {user: count, user2: count2}}
@api_bp.route("/split_api/item_list"):
def item_list():
    """
    Main method to display the item list along with the amount each user
    reuqests. This is in the format {item: {user: count, user2: count2}}
    amount each user
    :param: group id
    :return: the JSON dict descirbed above
    """
    pass


#calculate split - scans the reciept, gets items costs, assigns to users
#takes in an image parameter, and user
