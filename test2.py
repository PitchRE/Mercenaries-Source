
import MySQLdb
import MySQLdb.cursors
import glob
import os
from module_items import *
from header_items import *

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


db = MySQLdb.connect(host="localhost", user="root", passwd="Mania211##", db="Mercenaries", connect_timeout=10,
                     cursorclass=MySQLdb.cursors.DictCursor)

cursor = db.cursor()    
cursor.execute("SELECT * FROM items")
numrows = cursor.rowcount

for x in xrange(0,numrows):
  row = cursor.fetchone()
  for index, item in enumerate(items):
      if item[2][0][0] == row["code_name"] or item[0] == row["code_name"] or item[2][0][1] == row["code_name"]:
        code_name = row["id"]
        if item_type(item[3]) == "itp_type_body_armor":
            armor = get_body_armor(item[6])
        elif item_type(item[3]) == "itp_type_head_armor":
            armor = get_head_armor(item[6])
        elif item_type(item[3]) == "itp_type_foot_armor":
            armor = get_leg_armor(item[6])   
        elif item_type(item[3]) == "itp_type_hand_armor":
            armor = get_body_armor(item[6]) 
        else:
            continue       

        cursor2 = db.cursor()            
        cursor2.execute("UPDATE items SET defence=%s where id=%s", (armor,row["id"]))
        db.commit()
        print row["id"], row["code_name"], armor
        print("     affected rows = {}".format(cursor2.rowcount))
      