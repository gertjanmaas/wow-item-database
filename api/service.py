import json
from flask import jsonify, request

from app import app, db

from entities import Item, ItemQuality

@app.route('/')
def index():
    return open("frontend/index.html").read()

@app.route('/items', methods=['GET'])
def list_items():
    order_by = request.args.get('order_by', "quality")
    order = Item.quality.asc()
    if order_by == "alphabetical":
        order = Item.name.asc()

    print(Item.query.order_by(order))
    return jsonify([i.to_dict() for i in Item.query.order_by(order).all()])

def populate(db):
    items = [
        Item(name="Thunderfury, Blessed Blade of the Windseeker", quality=ItemQuality.LEGENDARY, icon="inv_sword_39"),
        Item(name="Orb of Deception", quality=ItemQuality.RARE, icon="inv_misc_orb_02"),
        Item(name="The Unstoppable Force", quality=ItemQuality.EPIC, icon="inv_hammer_13"),
        Item(name="Noggenfogger Elixir", quality=ItemQuality.COMMON, icon="inv_potion_83"),
        Item(name="Righteous Orb", quality=ItemQuality.UNCOMMON, icon="inv_misc_gem_pearl_03"),
        Item(name="Nat Pagle's Guide to Extreme Anglin'", quality=ItemQuality.JUNK, icon="inv_misc_book_02"),
        Item(name="Savory Deviate Delight", quality=ItemQuality.COMMON, icon="inv_misc_monsterhead_04"),
        Item(name="Carrot on a Stick", quality=ItemQuality.UNCOMMON, icon="inv_misc_food_54"),
        Item(name="Skullflame Shield", quality=ItemQuality.EPIC, icon="inv_shield_01"),
        Item(name="Sulfuras, Hand of Ragnaros", quality=ItemQuality.LEGENDARY, icon="inv_hammer_unique_sulfuras"),
        Item(name="Rusty Warhammer", quality=ItemQuality.JUNK, icon="inv_hammer_16")
    ]

    for i in items:
        if Item.query.filter_by(name=i.name).first() is None:
            db.session.add(i)
    db.session.commit()
    

if __name__ == "__main__":
    db.create_all()
    populate(db)
    app.run(host="0.0.0.0", port=5000)