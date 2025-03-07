###################################################
# header_factions.py
# This file contains declarations for factions
# DO NOT EDIT THIS FILE!!!! 
###################################################

from header_common import *

ff_always_hide_label = 0x00000001
ff_max_rating_bits = 8
ff_max_rating_mask = 0x0000ff00

def max_player_rating(rating):
  r = 100 - rating
  return (r << ff_max_rating_bits) & ff_max_rating_mask

def find_faction(factions,faction_id):
  result = -1
  num_factions = len(factions)
  i_faction = 0
  while (i_faction < num_factions) and (result == -1):
    faction = factions[i_faction]
    if (faction[0] == faction_id):
      result = i_faction
    i_faction += 1
  return result
