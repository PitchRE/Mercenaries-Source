import glob
import os
from module_items import items
from header_items import *
import json
from blacklisted_items import blacklist


worth_items = ["itp_type_horse", "itp_type_one_handed_wpn", "itp_type_two_handed_wpn", "itp_type_polearm", "itp_type_arrows", "itp_type_bolts", "itp_type_shield", "itp_type_bow", "itp_type_crossbow", "itp_type_thrown", "itp_type_head_armor", "itp_type_body_armor", "itp_type_foot_armor", "itp_type_hand_armor", "itp_type_bullets", "itp_type_pistol", "itp_type_musket"]
weapons = ["itp_type_one_handed_wpn", "itp_type_two_handed_wpn", "itp_type_polearm", "itp_type_arrows", "itp_type_bolts", "itp_type_bow", "itp_type_crossbow", "itp_type_musket", "itp_type_thrown", "itp_type_bullets"]
armors = {"itp_type_head_armor", "itp_type_body_armor", "itp_type_foot_armor", "itp_type_hand_armor"}
ranged = {"itp_type_bow", "itp_type_crossbow", "itp_type_musket"}
item_list = {}
def item_types(x):
    itm = x
    if itm == -1:

        itm = 'itp_type_horse'

    if itm == -2:

        itm = 'itp_type_one_handed_wpn'

    if itm == -3:

        itm = 'itp_type_two_handed_wpn'

    if itm == -4:

        itm = 'itp_type_polearm'

    if itm == -5:

        itm = 'itp_type_arrows'

    if itm == -6:

        itm = 'itp_type_bolts'

    if itm == -7:

        itm = 'itp_type_shield'

    if itm == -8:

        itm = 'itp_type_bow'

    if itm == -9:

        itm = 'itp_type_crossbow'

    if itm == -10:

        itm = 'itp_type_thrown'

    if itm == -11:

        itm = 'itp_type_goods'

    if itm == -12:

        itm = 'itp_type_head_armor'

    if itm == -13:

        itm = 'itp_type_body_armor'

    if itm == -14:

        itm = 'itp_type_foot_armor'

    if itm == -15:

        itm = 'itp_type_hand_armor'

    if itm == -16:

        itm = 'itp_type_pistol'

    if itm == -17:

        itm = 'itp_type_musket'

    if itm == -18:

        itm = 'itp_type_bullets'

    if itm == -19:

        itm = 'itp_type_animal'

    if itm == -20:

        itm = 'itp_type_book'
    return itm   

def get_valid_damage(x):
    if x < 256:
        return x
    elif x < 512:
        x = x - 256
        return x
    elif x > 511:
       x = x - 513
       return x
def get_damage_type(x):
    if x < 256:
        return "cut"
    elif x < 512:
        x = x - 256
        return "pierce"
    elif x > 511:
       x = x - 513
       return "blunt"       




def loop_items():
    for index, item in enumerate(items):
        item_type = item_types(item[3])
        if item_type in worth_items:
            if item[0] in blacklist:
                buyable = 0
            if item[2][0][0] in blacklist:
                buyable = 0    
            else:
                buyable = 1    
            if "_melee" in item[0]:    
                continue
            if item_type in armors:
                head_armor = get_head_armor(item[6])
                body_armor = get_body_armor(item[6])
                leg_armor = get_leg_armor(item[6])
            else:
                head_armor = None
                body_armor = None
                leg_armor = None    
            if item_type in weapons:
                thrust_damage = get_thrust_damage(item[6])
                thrust_damage = get_valid_damage(thrust_damage)
                swing_damage = get_swing_damage(item[6])
                swing_damage = get_valid_damage(swing_damage)
                swing_damage_type = get_damage_type(swing_damage)
                thrust_damage_type = get_damage_type(thrust_damage)
            else:
                thrust_damage = None
                swing_damage = None 
                swing_damage_type = None
                thrust_damage_type = None
            if item_type == "itp_type_horse":
                thrust_damage = get_thrust_damage(item[6])
                thrust_damage = get_valid_damage(thrust_damage)
                thrust_damage_type = get_damage_type(thrust_damage)   
                horse_maneuver = get_speed_rating(item[6])
            else:
                horse_speed = None  
                horse_maneuver = None  
            if item_type in ranged:
                missile_speed = get_missile_speed(item[6])
            else:
                missile_speed = None     
            speed_rating = get_speed_rating(item[6])




            item_list[item[0]] = {
                "code_name": item[0],
                "name": item[1],
                "type": item_type,
                "game_id": index,
                "image": None,
                "head_armor": head_armor,
                "body_armor": body_armor,
                "leg_armor": leg_armor,
                "weight": get_weight(item[6]),
                "thrust_damage": thrust_damage,
                "swing_damage": swing_damage,
                "price": item[5],
                "speed_rating": speed_rating,
                "thrust_damage_type": thrust_damage_type,
                "swing_damage_type": swing_damage_type,
                "horse_speed": horse_speed,
                "missile_speed": missile_speed,
                "horse_maneuver": horse_maneuver,
                "buyable": buyable,
                "model_name": item[2][0][0],
            }
    return item_list        

    
json = json.dumps(loop_items(), sort_keys=True, indent=4)

if os.path.exists("./data/item_list.json"):
  os.remove("./data/item_list.json")

file1 = open("./data/item_list.json","a") 
file1.write(json)  




