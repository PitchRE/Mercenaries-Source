import glob
import os
from module_items import *
from header_items_fake import *
import json


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Mania211##",
  database="Mercenaries"
)


def item_type(x):
    item[3] = x
    if item[3] == -1:

        item[3] = 'itp_type_horse'

    if item[3] == -2:

        item[3] = 'itp_type_one_handed_wpn'

    if item[3] == -3:

        item[3] = 'itp_type_two_handed_wpn'

    if item[3] == -4:

        item[3] = 'itp_type_polearm'

    if item[3] == -5:

        item[3] = 'itp_type_arrows'

    if item[3] == -6:

        item[3] = 'itp_type_bolts'

    if item[3] == -7:

        item[3] = 'itp_type_shield'

    if item[3] == -8:

        item[3] = 'itp_type_bow'

    if item[3] == -9:

        item[3] = 'itp_type_crossbow'

    if item[3] == -10:

        item[3] = 'itp_type_thrown'

    if item[3] == -11:

        item[3] = 'itp_type_goods'

    if item[3] == -12:

        item[3] = 'itp_type_head_armor'

    if item[3] == -13:

        item[3] = 'itp_type_body_armor'

    if item[3] == -14:

        item[3] = 'itp_type_foot_armor'

    if item[3] == -15:

        item[3] = 'itp_type_hand_armor'

    if item[3] == -16:

        item[3] = 'itp_type_pistol'

    if item[3] == -17:

        item[3] = 'itp_type_musket'

    if item[3] == -18:

        item[3] = 'itp_type_bullets'

    if item[3] == -19:

        item[3] = 'itp_type_animal'

    if item[3] == -20:

        item[3] = 'itp_type_book'
    return item[3]    









filenames = glob.glob("/home/pitch/Desktop/openbrf/**/*.*",)
filenames = filenames + glob.glob("/home/pitch/Desktop/openbrf/*.*",)
filenames = filenames + glob.glob("/home/pitch/Desktop/openbrf/**/**/*.*",)

Web_Item = {}
to_add = []
if os.path.exists("test.json"):
  os.remove("test.json")



for item_img in filenames:
    item_img = os.path.basename(item_img)
    item_img = os.path.splitext(item_img)[0]
    exists = 0
    for index, item in enumerate(items):    
     
        if item[2][0][0] == item_img or item[0] == item_img or item[2][0][1] == item_img:
           Web_Item[item[0]] = {
               "name": item[1],
               "type": item_type(item[3]),
               "code_name": item[0],
               "game_id": index,
               "image": item_img + ".png",
               "price": None,
               "head": get_head_armor(item[6]),
               "body": get_body_armor(item[6]),
               "boots": get_leg_armor(item[6]),
               "speed": get_speed_rating(item[6]),
               "weapon_length": get_weapon_length(item[6]),
               "swing_damage": get_swing_damage(item[6]),
               "thrust_damage": get_thrust_damage(item[6]),
               "difficulty": get_difficulty(item[6]),
               "shoot_speed": get_missile_speed(item[6]),
               "weight": get_weight(item[6]),    
           }
           mycursor = mydb.cursor()
           if item_type(item[3]) == "itp_type_body_armor":
               mycursor.execute("UPDATE items SET defence = %s WHERE code_name = %s orWhere code_name = %s orWhere code_name = %s", (get_body_armor(item[6]), item[0], item[2][0][1], item[2][0][0]))
           elif item_type(item[3]) == itp_type_head_armor:
               mycursor.execute("UPDATE items SET defence = %s WHERE code_name = %s", (get_head_armor(item[6]), item[0]))
           mydb.commit()
           exists = 1
    if exists == 0 :
        to_add.append(item_img)

          
   

s = json.dumps(Web_Item, sort_keys=True, indent=4)


file1 = open("test.json","a") 
file1.write(s)  


print  json.dumps(to_add, sort_keys=True, indent=4)
print len(to_add)


