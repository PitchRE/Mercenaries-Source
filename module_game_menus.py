from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

game_menus = [
  ("start_game_0",menu_text_color(0xFF000000)|mnf_disable_all_keys,"Welcome, adventurer, to Mount and Blade: With Fire and Sword. Before beginning your journey, you must create your character and set the game's difficulty.",
    "none",
    [
		(assign,"$current_string_reg",10),
		(assign, "$g_tutoral_mission_done", 0),
           #(troop_set_type,"trp_player",0),
           #(assign,"$character_gender",tf_male),
           (set_show_messages, 0),
           (troop_raise_skill, "trp_player","skl_power_draw",1),
           (troop_raise_skill, "trp_player","skl_tracking",1),
           (troop_raise_skill, "trp_player","skl_spotting",1),
           (troop_raise_skill, "trp_player","skl_athletics",1),
           (troop_raise_skill, "trp_player","skl_weapon_master",2),
           (troop_raise_skill, "trp_player","skl_power_strike",1),
           (troop_raise_skill, "trp_player","skl_power_throw",1),
           (troop_raise_skill, "trp_player","skl_prisoner_management",1),
           (troop_raise_proficiency, "trp_player", 0, 10),
           (troop_raise_proficiency, "trp_player", 1, 10),
           (troop_raise_proficiency, "trp_player", 2, 10),
           (troop_raise_proficiency, "trp_player", 3, 10),
           (troop_raise_proficiency, "trp_player", 4, 10),
           (troop_raise_proficiency, "trp_player", 5, 10),
           (troop_raise_proficiency, "trp_player", 6, 10),
		   (troop_raise_attribute, "trp_player", ca_strength, 2),
		   (troop_raise_attribute, "trp_player", ca_agility, 2),
		   (troop_raise_attribute, "trp_player", ca_charisma, 2),
		   (troop_raise_attribute, "trp_player", ca_intelligence, 2),
		   
		   
		   
	       #samopal
		   #(troop_add_item, "trp_player","itm_sablya_pure_c", 0),
		   (troop_add_item, "trp_player", "itm_bolts",0),
		   #(troop_add_item, "trp_player", "itm_samopal",0),
		   (store_random_in_range, ":rand", 0, 4),
		   (try_begin), 
				(eq, ":rand", 0), 
				(troop_add_item, "trp_player","itm_ukraine_svitka_a",0),
		   (else_try),
				(eq, ":rand", 1), 
				(troop_add_item, "trp_player","itm_poland_svitka_a",0),
		   (else_try),
				(eq, ":rand", 2), 
				(troop_add_item, "trp_player","itm_evropa_odejda_sela_b",0),
		   (else_try),
				(eq, ":rand", 3), 		   
				(troop_add_item, "trp_player","itm_tatar_halat_pure_b",0),
		   (else_try),
				(troop_add_item, "trp_player","itm_streletzkiy_mundir_spear",0),
		   (try_end), 
           #(troop_add_item, "trp_player","itm_ukraine_svitka_a",0),
           (troop_add_item, "trp_player","itm_selo_boots",0),
           #(troop_add_item, "trp_player","itm_sumpter_horse",imod_heavy),
           (troop_add_item, "trp_player","itm_dried_meat",0),
		   (troop_add_item, "trp_player","itm_bread",0),
		   (troop_add_item, "trp_player","itm_bread",0),		   
           (troop_add_item, "trp_player","itm_dried_meat",0),
			(try_begin), 	   
				(eq, debug_mode, 1), 		   
				(troop_add_item, "trp_player","itm_granata",0),
				(troop_add_item, "trp_player","itm_granata",0),
				(troop_add_item, "trp_player","itm_granata",0),
				(troop_add_item, "trp_player","itm_granata",0),
				(troop_add_item, "trp_player","itm_zakaz_pistol1"),
				(troop_add_item, "trp_player","itm_zakaz_pistol2"),
				(troop_add_item, "trp_player","itm_zakaz_2stwol_koleso2"),
				(troop_add_item, "trp_player","itm_zakaz_2stwol_koleso"),
				(troop_add_item, "trp_player","itm_zakaz_2stwol_udar1"),
				(troop_add_item, "trp_player","itm_zakaz_2stwol_udar2"),
            (end_try), 
           
           (troop_raise_skill, "trp_player","skl_leadership",3),
           (troop_raise_skill, "trp_player","skl_riding",2),			
		   
		   (troop_equip_items, "trp_player"),	
		   (set_show_messages, 1),		
	],
    [
      ("start_easy",[],"Easy",
       [
			(options_set_damage_to_player, 0),  #    = 261 # (options_set_damage_to_player, <value>), #0 = 1/4, 1 = 1/2, 2 = 1/1
			(options_set_damage_to_friends, 0), #    = 263 # (options_set_damage_to_friends, <value>), #0 = 1/2, 1 = 3/4, 2 = 1/1
			(options_set_combat_ai, 2),         #    = 265 # (options_set_combat_ai, <value>), #0 = good, 1 = average, 2 = poor
			(options_set_campaign_ai, 2),       #    = 267 # (options_set_campaign_ai, <value>), #0 = good, 1 = average, 2 = poor
			(options_set_combat_speed, 0),      #    = 269 # (options_set_combat_speed, <value>), #0 = slowest, 1 = slower, 2 = normal, 3 = faster, 4 = fastest
		    #(change_screen_return, 0),	
			(jump_to_menu, "mnu_start_game_1"),
        ]
       ),
	   
      ("start_normal",[],"Normal",
       [
		   (options_set_damage_to_player, 1),  #    = 261 # (options_set_damage_to_player, <value>), #0 = 1/4, 1 = 1/2, 2 = 1/1
		   (options_set_damage_to_friends, 1), #    = 263 # (options_set_damage_to_friends, <value>), #0 = 1/2, 1 = 3/4, 2 = 1/1
		   (options_set_combat_ai, 0),         #    = 265 # (options_set_combat_ai, <value>), #0 = good, 1 = average, 2 = poor
		   (options_set_campaign_ai, 1),       #    = 267 # (options_set_campaign_ai, <value>), #0 = good, 1 = average, 2 = poor
		   (options_set_combat_speed, 2),      #    = 269 # (options_set_combat_speed, <value>), #0 = slowest, 1 = slower, 2 = normal, 3 = faster, 4 = fastest
		   #(change_screen_return, 0),	
			(jump_to_menu, "mnu_start_game_1"),
        ]
       ),

      ("start_hard",[],"Hard",
       [
		    (options_set_damage_to_player, 2),  #    = 261 # (options_set_damage_to_player, <value>), #0 = 1/4, 1 = 1/2, 2 = 1/1
		    (options_set_damage_to_friends, 2), #    = 263 # (options_set_damage_to_friends, <value>), #0 = 1/2, 1 = 3/4, 2 = 1/1
		    (options_set_combat_ai, 0),         #    = 265 # (options_set_combat_ai, <value>), #0 = good, 1 = average, 2 = poor
		    (options_set_campaign_ai, 0),       #    = 267 # (options_set_campaign_ai, <value>), #0 = good, 1 = average, 2 = poor
		    (options_set_combat_speed, 4),      #    = 269 # (options_set_combat_speed, <value>), #0 = slowest, 1 = slower, 2 = normal, 3 = faster, 4 = fastest
			#(change_screen_return, 0),	
			(jump_to_menu, "mnu_start_game_1"),
        ]
       ),
	   

      ("go_back_dot",[],"Go back.",
       [(change_screen_quit),
    ]
  ),
      ]
  ),




#This needs to be the second window!!!
  (
    "start_phase_2",mnf_disable_all_keys,"{s10}",
    "none",
    [
		(try_begin), 
			(eq, "$g_tutoral_mission_done", 0),
			(str_store_string, s10, "str_oim_training_6_text"),
		(else_try), 
			(eq, "$g_battle_result", -1), 
			(str_store_string, s10, "str_oim_training_7_text"),
		(else_try), 
			(str_store_string, s10, "str_oim_training_13_text"),
		(end_try), 
	],
    [
      ("get_deal_with",[
		(eq, "$g_tutoral_mission_done", 0),
	  ],"See what trouble is afoot.",
       [
			(assign, ":town_scene", "scn_oim_river_village_euro"),
			(modify_visitors_at_site, ":town_scene"),
			(reset_visitors),
			(try_begin), 
				(eq, tw_verision, 1), 
				(set_jump_mission,"mt_tw_tutorial_training_ground"),
			(else_try), 
				(set_jump_mission,"mt_oim_tutorial_training_ground"),
			(end_try), 	
			(set_visitor, "trp_player", 0),
			(jump_to_scene, ":town_scene"),
			(change_screen_mission),
       ]),

      ("talk_to_monfore",[
		(eq, "$g_tutoral_mission_done", 1),
	  ],"Continue...",
       [
			(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,"trp_oim_monfor"),
			(set_jump_mission,"mt_conversation_encounter"),
			(jump_to_scene,"scn_meeting_scene_plain_forest"),
			(change_screen_map_conversation, "trp_oim_monfor"),        ]),
       
      ("camp_train_archery",[(eq, "$oim_monfor_ready_to_fire_musquet", 1)],"Begin practice.",
       [
         (assign, "$g_mt_mode", ctm_ranged),
         (assign, "$temp", itp_type_crossbow),
	     (assign, "$g_training_ground_training_scene", "scn_oim_training_ground_ranged_melee_monfor"),
         (jump_to_menu, "mnu_oim_training_ground_selection_details_ranged"),
       ]),
       
   ("continue",[(check_quest_active, "qst_talk_to_zamoshie_elder")],"Continue...",
       [
         #(change_screen_return),
		 (jump_to_menu, "mnu_auto_return_to_map"),
        ]
       ),

      ("tutorial_cheat",[(eq,1,0)],"{!}CHEAT!",
       [
         (change_screen_return),
         (assign, "$cheat_mode", 1),
         (set_show_messages, 0),
		 (add_xp_to_troop, 15000, "trp_player"),
         (troop_raise_skill, "trp_player", skl_leadership, 7),
         (troop_raise_skill, "trp_player", skl_prisoner_management, 5),
         
         (set_show_messages, 1),

         (try_for_range, ":cur_place", scenes_begin, scenes_end),
           (scene_set_slot, ":cur_place", slot_scene_visited, 1),
         (try_end),
         (call_script, "script_get_player_party_morale_values"),
         (party_set_morale, "p_main_party", reg0),
         ]),
       ]
	   ),
	   
	   # This needs to be the third window!!!  
  (
    "start_game_3",mnf_disable_all_keys,"{!}Unused",
    "none",
    [],
    []
  ),

# This needs to be the fourth window!!!
  (
    "tutorial",mnf_disable_all_keys,"{!}Unused",
    "none",
    [],
    []
  ),

 # This needs to be the fifth window!!!
 ("reports",0,"Character Renown: {reg5}^Honor Rating: {reg6}^Party Morale: {reg8}^Party Size Limit: {reg7}^",
   "none",
   [(call_script, "script_game_get_party_companion_limit"),
    (assign, ":party_size_limit", reg0),
    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (assign, reg5, ":renown"),
    (assign, reg6, "$player_honor"),
    (assign, reg7, ":party_size_limit"),
    (party_get_morale, reg8, "p_main_party"),
   ],
    [
      ("cheat_faction_orders",[(ge,"$cheat_mode",1)],"{!}Cheat: Faction orders.",
       [(jump_to_menu, "mnu_faction_orders"),
        ]
       ),
	   
      ("view_character_report",[],"View character report.",
       [(jump_to_menu, "mnu_character_report"),
        ]
       ),
      ("view_party_size_report",[],"View party size report.",
       [(jump_to_menu, "mnu_party_size_report"),
        ]
       ),
      ("view_morale_report",[],"View party morale report.",
       [(jump_to_menu, "mnu_morale_report"),
        ]
       ),
#NPC companion changes begin
	   
      ("view_character_report_cheat",[(eq, debug_mode,1)],"{!}NPC status check.",
       [
        (try_for_range, ":npc", companions_begin, companions_end),
            (main_party_has_troop, ":npc"),
            (str_store_troop_name, 4, ":npc"),
            (troop_get_slot, reg3, ":npc", slot_troop_morality_state),
            (troop_get_slot, reg4, ":npc", slot_troop_2ary_morality_state),
            (troop_get_slot, reg5, ":npc", slot_troop_personalityclash_state),    
            (troop_get_slot, reg6, ":npc", slot_troop_personalityclash2_state),    
            (troop_get_slot, reg7, ":npc", slot_troop_personalitymatch_state),    
            (display_message, "@{!}{s4}: M{reg3}, 2M{reg4}, PC{reg5}, 2PC{reg6}, PM{reg7}"),
        (try_end),
        ]
       ),
#NPC companion changes end



      ("view_faction_relations_report",[],"View nation relations report.",
       [(jump_to_menu, "mnu_faction_relations_report"),
        ]
       ),
	   
      ("view_banking_reports",[],"View money reports.",
       [(jump_to_menu, "mnu_banks_report"),
        ]
       ),
	   
	   
      ("resume_travelling",[],"Continue traveling...",
       [(change_screen_return),
        ]
       ),
      ]
  ),

  (
    "custom_battle_scene",menu_text_color(0xFF000000)|mnf_disable_all_keys,"{!}(NO TRANS)",
	
    "none",
    [],
    [

      ("quick_battle_scene_1",[],"{!}quick_battle_scene_1",
       [
           (set_jump_mission,"mt_ai_training"),
           (jump_to_scene,"scn_quick_battle_scene_1"),(change_screen_mission)        
		]
       ),
      ("quick_battle_scene_2",[],"{!}quick_battle_scene_2",
       [
           (set_jump_mission,"mt_ai_training"),
           (jump_to_scene,"scn_quick_battle_scene_2"),(change_screen_mission)        
		]
       ),
      ("quick_battle_scene_3",[],"{!}quick_battle_scene_3",
       [
           (set_jump_mission,"mt_ai_training"),
           (jump_to_scene,"scn_quick_battle_scene_3"),(change_screen_mission)        
		]
       ),
      ("quick_battle_scene_4",[],"{!}quick_battle_scene_4",
       [
           (set_jump_mission,"mt_ai_training"),
           (jump_to_scene,"scn_quick_battle_scene_4"),(change_screen_mission)        
		]
       ),
      ("quick_battle_scene_5",[],"{!}quick_battle_scene_5",
       [
           (set_jump_mission,"mt_ai_training"),
           (jump_to_scene,"scn_quick_battle_scene_5"),(change_screen_mission)        
		]
       ),
	   
      ("go_back",[],"{!}Go back",
       [(change_screen_quit),
        ]
       ),
      ]
  ),
  
  (
    "custom_battle_end",mnf_disable_all_keys,"The battle has ended. {s1} Your side killed {reg5} enemies and lost {reg6} troops. You personally slew {reg7} men in the battle.",
    "none",
    [(music_set_situation, 0),
     (assign, reg5, "$g_custom_battle_team2_death_count"),
     (assign, reg6, "$g_custom_battle_team1_death_count"),
     (get_player_agent_kill_count, ":kill_count"),
     (get_player_agent_kill_count, ":wound_count", 1),
     (store_add, reg7, ":kill_count", ":wound_count"),
     (try_begin),
       (eq, "$g_battle_result", 1),
       (str_store_string, s1, "str_battle_won"),
     (else_try),
       (str_store_string, s1, "str_battle_lost"),
     (try_end),],
    [
      ("continue",[],"Continue...",
       [(change_screen_quit),
        ]
       ),
    ]
  ),
  
  ("start_game_1",menu_text_color(0xFF000000)|mnf_disable_all_keys,"Select your character's gender.",
    "none",
    [],
    [
      ("start_male_2",[],"Male",
       [
         (troop_set_type,"trp_player",0),
         (assign,"$character_gender",tf_male),
         #(jump_to_menu,"mnu_start_game_0"),
		 (change_screen_return, 0),
        ]
       ),
      ("start_female",[],"Female",
       [
         (troop_set_type, "trp_player", 1),
         (assign, "$character_gender", tf_female),
         #(jump_to_menu, "mnu_start_game_0"),
		 (change_screen_return, 0),
       ]
       ),
	  ("go_back",[],"Go back",
       [
	     (jump_to_menu,"mnu_start_game_0"),
       ]),
    ]
  ),

  (
    "start_character_1",mnf_disable_all_keys,"So what nation do you hail from? And what of your family?",
    "none",
    [
    (str_clear,s10),
    (str_clear,s11),
    (str_clear,s12),
    (str_clear,s13),
    (str_clear,s14),
    (str_clear,s15),
    ],
    [
    ("start_noble",[],"My father and mother are of noble gentry.",[
      (assign,"$background_type",cb_noble),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@You came into the world a {reg3?daughter:son} of declining nobility,\
 owning only the house in which they lived. However, despite your family's hardships,\
 they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court."),
	(jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_merchant",[],"A travelling merchant.",[
      (assign,"$background_type",cb_merchant),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@You were born the {reg3?daughter:son} of travelling merchants,\
 always moving from place to place in search of a profit. Although your parents were wealthier than most\
 and educated you as well as they could, you found little opportunity to make friends on the road,\
 living mostly for the moments when you could sell something to somebody."),
	(jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_guard",[],"A veteran warrior.",[
      (assign,"$background_type",cb_guard),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@As a child, your family scrabbled out a meagre living from your father's wages\
 as a guardsman to the local lord. It was not an easy existence, and you were too poor to get much of an\
 education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand."),
	(jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_forester",[],"A hunter.",[
      (assign,"$background_type",cb_forester),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@{reg3?daughter:son}"),
      (str_store_string,s10,"@You were the {reg3?daughter:son} of a family who lived off the woods,\
 doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows,\
 even a spot of poaching whenever things got tight. Winter was never a good time for your family\
 as the cold took animals and people alike, but you always lived to see another dawn,\
 though your brothers and sisters might not be so fortunate."),
	(jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_nomad",[],"A steppe nomad.",[
      (assign,"$background_type",cb_nomad),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@{reg3?daughter:son}"),
      (str_store_string,s10,"@You were a child of the steppe, born to a tribe of wandering nomads who lived\
 in great camps throughout the arid grasslands.\
 Like the other tribesmen, your family revered horses above almost everything else, and they taught you\
 how to ride almost before you learned how to walk. "),
	(jump_to_menu,"mnu_start_character_2"),
    ]),
    ("start_thief",[],"A thief.",[
      (assign,"$background_type",cb_thief),
      (assign, reg3, "$character_gender"),
      (str_store_string,s10,"@As the {reg3?daughter:son} of a thief, you had very little 'formal' education.\
 Instead you were out on the street, begging until you learned how to cut purses, cutting purses\
 until you learned how to pick locks, all the way through your childhood.\
 Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."),
	(jump_to_menu,"mnu_start_character_2"),
    ]),
##    ("start_priest",[],"Priests.",[
##      (assign,"$background_type",cb_priest),
##      (assign, reg3, "$character_gender"),
##      (str_store_string,s10,"@A {reg3?daughter:son} that nobody wanted, you were left to the church as a baby,\
## a foundling raised by the priests and nuns to their own traditions.\
## You were only one of many other foundlings and orphans, but you nonetheless received a lot of attention\
## as well as many years of study in the church library and before the altar. They taught you many things.\
## Gradually, faith became such a part of your life that it was no different from the blood coursing through your veins."),
##	(jump_to_menu,"mnu_start_character_2"),
##    ]),
    ("go_back_dot",[],"Go back.",
     [(jump_to_menu,"mnu_start_game_1"),
    ]),
    ]
  ),
  (
    "start_character_2",0,"{s10}^^ You began learning of the world almost as soon as you could walk and talk. You spent your early years as...",
    "none",
    [],
    [
      ("page",[
          ],"A page at a nobleman's court.",[
      (assign,"$background_answer_2", cb2_page),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you were sent to live in the court of one of the nobles of the land.\
 There, your first lessons were in humility, as you waited upon the lords and ladies of the household.\
 But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict\
 and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."),
	(jump_to_menu,"mnu_start_character_3"),
    ]),
      ("apprentice",[
          ],"A craftsman's apprentice.",[
      (assign,"$background_answer_2", cb2_apprentice),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your\
 new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as\
 you wished to stay."),
	(jump_to_menu,"mnu_start_character_3"),
    ]),
      ("stockboy",[
          ],"A shop assistant.",[
      (assign,"$background_answer_2",cb2_merchants_helper),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans.\
 You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd\
 got the better deal."),
	(jump_to_menu,"mnu_start_character_3"),
    ]),
      ("urchin",[
          ],"A street urchin.",[
      (assign,"$background_answer_2",cb2_urchin),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you took to the streets, doing whatever you must to survive.\
 Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world,\
 always one step ahead of the law and those who wished you ill."),
	(jump_to_menu,"mnu_start_character_3"),
    ]),
      ("nomad",[
          ],"A steppe child.",[
      (assign,"$background_answer_2",cb2_steppe_child),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 you rode the great steppes on a horse of your own, learning the ways of the grass and the desert.\
 Although you sometimes went hungry, you became a skillful hunter and pathfinder in this trackless country.\
 Your body too started to harden with muscle as you grew into the life of a nomad {reg3?woman:man}."),
	(jump_to_menu,"mnu_start_character_3"),
    ]),
      
##      ("mummer",[],"Mummer.",[
##      (assign,"$background_answer_2",5),
##      (assign, reg3, "$character_gender"),
##      (str_store_string,s13,"@{reg3?woman:man}"),
##      (str_store_string,s12,"@{reg3?girl:boy}"),
##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
## you attached yourself to a troupe of wandering entertainers, going from town to town setting up mummer's\
## shows. It was a life of hard work, selling, begging and stealing your living from the punters who flocked\
## to watch your antics. Over time you became a performer well capable of attracting a crowd."),
##	(jump_to_menu,"mnu_start_character_3"),
##    ]),
##      ("courtier",[],"Courtier.",[
##      (assign,"$background_answer_2",6),
##      (assign, reg3, "$character_gender"),
##      (str_store_string,s13,"@{reg3?woman:man}"),
##      (str_store_string,s12,"@{reg3?girl:boy}"),
##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
## you spent much of your life at court, inserting yourself into the tightly-knit circles of nobility.\
## With the years you became more and more involved with the politics and intrigue demanded of a high-born {s13}.\
## You could not afford to remain a stranger to backstabbing and political violence, even if you wanted to."),
##	(jump_to_menu,"mnu_start_character_3"),
##    ]),
##      ("noble",[],"Noble in training.",[
##      (assign,"$background_answer_2",7),
##      (assign, reg3, "$character_gender"),
##      (str_store_string,s13,"@{reg3?woman:man}"),
##      (str_store_string,s12,"@{reg3?girl:boy}"),
##      (try_begin),
##      (eq,"$character_gender",tf_male),
##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
## you were trained and educated to perform the duties and wield the rights of a noble landowner.\
## The managing of taxes and rents were equally important in your education as diplomacy and even\
## personal defence. You learned everything you needed to become a lord of your own hall."),
##      (else_try),
##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
## you were trained and educated to the duties of a noble {s13}. You learned much about the household arts,\
## but even more about diplomacy and decorum, and all the things that a future husband might choose to speak of.\
## Truly, you became every inch as shrewd as any lord, though it would be rude to admit it aloud."),
##      (try_end),
##	(jump_to_menu,"mnu_start_character_3"),
##    ]),
##      ("acolyte",[],"Cleric acolyte.",[
##    (assign,"$background_answer_2",8),
##      (assign, reg3, "$character_gender"),
##      (str_store_string,s13,"@{reg3?woman:man}"),
##      (str_store_string,s12,"@{reg3?girl:boy}"),
##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
## you became an acolyte in the church, the lowest rank on the way to priesthood.\
## Years of rigorous learning and hard work followed. You were one of several acolytes,\
## performing most of the menial labour in the church in addition to being trained for more holy tasks.\
## On the night of your adulthood you were allowed to conduct your first service.\
## After that you were no longer an acolyte {s12}, but a {s13} waiting to take your vows into the service of God."),
##	(jump_to_menu,"mnu_start_character_3"),
##    ]),
      ("go_back_dot",[],"Go back.",
     [(jump_to_menu,"mnu_start_character_1"),
    ]),
    ]
  ),
  (
    "start_character_3",mnf_disable_all_keys,"{s11}^^ Then, as a young adult, life changed, as it always does. You became...",
    "none",
    [(assign, reg3, "$character_gender"),],
    [
##      ("bravo",[],"A travelling bravo.",[
##        (assign,"$background_answer_3",1),
##      (str_store_string,s14,"@{reg3?daughter:man}"),
##      (str_store_string,s13,"@{reg3?woman:man}"),
##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
## You left your old life behind to travel the roads as a mercenary, a bravo, guarding caravans for coppers\
## or bashing in heads for silvers. You became a {s14} of the open road, working with bandits as often as against.\
## Going from fight to fight, you grew experienced at battle, and you learned what it was to kill."),
##	(jump_to_menu,"mnu_start_character_4"),
##        ]),
##      ("merc",[],"A sellsword in foreign lands.",[
##        (assign,"$background_answer_3",2),
##      (str_store_string,s14,"@{reg3?daughter:man}"),
##      (str_store_string,s13,"@{reg3?woman:man}"),
##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
## You signed on with a mercenary company and travelled far from your home. The life you found was rough and\
## ready, marching to the beat of strange drums and learning unusual ways of fighting.\
## There were men who taught you how to wield any weapon you desired, and plenty of battles to hone your skills.\
## You were one of the charmed few who survived through every campaign in which you marched."),
##	(jump_to_menu,"mnu_start_character_4"),
##        ]),

      ("squire",[(eq,"$character_gender",tf_male)],"A landlord.",[
        (assign,"$background_answer_3",cb3_squire),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
 When you were named squire to a noble at court, you practiced long hours with weapons,\
 learning how to deal out hard knocks and how to take them, too.\
 You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals.\
 But in addition to learning the chivalric ideal, you also learned about the less uplifting side\
 -- old warriors' stories of ruthless power politics, of betrayals and usurpations,\
 of men who used guile as well as valor to achieve their aims."),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("lady",[(eq,"$character_gender",tf_female)],"A lady-in-waiting.",[
        (assign,"$background_answer_3",cb3_lady_in_waiting),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things,\
 the wives and mistresses of noble men as well as maidens who had yet to find a husband.\
 However, even here you found politics at work as the ladies schemed for prominence and fought each other\
 bitterly to catch the eye of whatever unmarried man was in fashion at court.\
 You soon learned ways of turning these situations and goings-on to your advantage. With it came the\
 realisation that you yourself could wield great influence in the world, if only you applied yourself\
 with a little bit of subtlety."),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("troubadour",[],"A troubadour.",[
        (assign,"$background_answer_3",cb3_troubadour),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You set out on your own with nothing except the instrument slung over your back and your own voice.\
 It was a poor existence, with many a hungry night when people failed to appreciate your play,\
 but you managed to survive on your music alone. As the years went by you became adept at playing the\
 drunken crowds in your taverns, and even better at talking anyone out of anything you wanted."),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("student",[],"A university student.",[
        (assign,"$background_answer_3",cb3_student),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
 You found yourself as a student in the university of one of the great cities,\
 where you studied theology, philosophy, and medicine.\
 But not all your lessons were learned in the lecture halls.\
 You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight.\
 However, you certainly were able to observe how a broken jaw is set,\
 or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop."),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("peddler",[],"A goods peddler.",[
        (assign,"$background_answer_3",cb3_peddler),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 Heeding the call of the open road, you travelled from village to village buying and selling what you could.\
 It was not a rich existence, but you became a master at haggling even the most miserly elders into\
 giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("craftsman",[],"A smith.",[
        (assign,"$background_answer_3", cb3_craftsman),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You pursued a career as a smith, crafting items of function and beauty out of simple metal.\
 As time wore on you became a master of your trade, and fine work started to fetch fine prices.\
 With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
      ("poacher",[],"A poacher.",[
        (assign,"$background_answer_3", cb3_poacher),
      (str_store_string,s14,"@{reg3?daughter:man}"),
      (str_store_string,s13,"@{reg3?woman:man}"),
      (str_store_string,s12,"@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests\
 and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold\
 the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into\
 firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
	(jump_to_menu,"mnu_start_character_4"),
        ]),
##      ("preacher",[],"Itinerant preacher.",[
##        (assign,"$background_answer_3",6),
##      (str_store_string,s14,"@{reg3?daughter:man}"),
##      (str_store_string,s13,"@{reg3?woman:man}"),
##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
## You packed your few belongings and went out into the world to spread the word of God. You preached to\
## anyone who would listen, and impressed many with the passion of your sermons. Though you had taken a vow\
## to remain in poverty through your itinerant years, you never lacked for food, drink or shelter; the\
## hospitality of the peasantry was always generous to a rising {s13} of God."),
##	(jump_to_menu,"mnu_start_character_4"),
##        ]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu,"mnu_start_character_2"),
        ]
       ),
    ]
  ),

  (
    "start_character_4",mnf_disable_all_keys,"{s12}^^But soon everything changed and you decided to strike out on your own as an adventurer. Driving you to this decision was...",
    #Finally, what made you decide to strike out on your own as an adventurer?",
    "none",
    [],
    [
      ("revenge",[],"Personal revenge.",[
        (assign,"$background_answer_4", cb4_revenge),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 Still, it was not a difficult choice to leave, with the rage burning brightly in your heart.\
 You want vengeance. You want justice. What was done to you cannot be undone,\
 and these debts can only be paid in blood..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("death",[],"The loss of a loved one.",[
        (assign,"$background_answer_4",cb4_loss),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so\
 painful. Perhaps your new life will let you forget,\
 or honour the name that you can no longer bear to speak..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("wanderlust",[],"Wanderlust.",[
        (assign,"$background_answer_4",cb4_wanderlust),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of\
 wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the\
 freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
##      ("fervor",[],"Religious fervor.",[
##        (assign,"$background_answer_4",4),
##      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
## Regardless, the intense faith burning in your soul would not let you find peace in any single place.\
## There were others in the world, souls to be washed in the light of God. Now you preach wherever you go,\
## seeking to bring salvation and revelation to the masses, be they faithful or pagan. They will all know the\
## glory of God by the time you're done..."),
##        (jump_to_menu,"mnu_choose_skill"),
##        ]),
      ("disown",[],"Being forced out of your home.",[
        (assign,"$background_answer_4",cb4_disown),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone\
 now, and you must face the fact that you're out in the wide wide world. Alone to sink or swim..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
     ("greed",[],"Lust for money and power.",[
        (assign,"$background_answer_4",cb4_greed),
      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 To everyone else, it's clear that you're now motivated solely by personal gain.\
 You want to be rich, powerful, respected, feared.\
 You want to be the one whom others hurry to obey.\
 You want people to know your name, and tremble whenever it is spoken.\
 You want everything, and you won't let anyone stop you from having it..."),
        (jump_to_menu,"mnu_choose_skill"),
        ]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu,"mnu_start_character_3"),
        ]
       ),
    ]
  ),
  (
    "choose_skill",mnf_disable_all_keys,"You spot a battle-ready men in the distance.", 
    "none",
    [(assign,"$current_string_reg",10)],
    [
      ("begin_adventuring",[],"See what trouble is afoot.",[
           (set_show_messages, 0),
           (try_begin),
             (eq,"$character_gender",0),
             (troop_raise_attribute, "trp_player",ca_strength,1),
             (troop_raise_attribute, "trp_player",ca_charisma,1),
           (else_try),
             (troop_raise_attribute, "trp_player",ca_agility,1),
             (troop_raise_attribute, "trp_player",ca_intelligence,1),
           (try_end),

           (troop_raise_attribute, "trp_player",ca_strength,1),
           (troop_raise_attribute, "trp_player",ca_agility,1),
           (troop_raise_attribute, "trp_player",ca_charisma,1),
           
           (troop_raise_skill, "trp_player","skl_leadership",1),
           (troop_raise_skill, "trp_player","skl_riding",1),


        ]),
    ]
  ),

  (
    "past_life_explanation",mnf_disable_all_keys,"{s3}",
    "none",
    [
     (try_begin),
       (gt,"$current_string_reg",14),
       (assign,"$current_string_reg",10),
     (try_end),
     (str_store_string_reg,s3,"$current_string_reg"),
     (try_begin),
       (ge,"$current_string_reg",14),
       (str_store_string,s5,"@Back to the beginning..."),
     (else_try),
       (str_store_string,s5,"@View next segment..."),
     (try_end),
     ],
    [
      ("view_next",[],"{s5}",[
        (val_add,"$current_string_reg",1),
        (jump_to_menu, "mnu_past_life_explanation"),
        ]),
      ("continue",[],"Continue...",
       [
        ]),
      ("go_back_dot",[],"Go back.",[
        (jump_to_menu, "mnu_choose_skill"),
        ]),
    ]
  ),

  (
    "auto_return",0,"This menu automatically returns to...",
    "none",
    [(change_screen_return, 0)],
    [
    ]
  ),
  ("morale_report",0,"{s1}",
   "none",
   [(call_script, "script_get_player_party_morale_values"),
    (assign, ":target_morale", reg0),
    (assign, reg1, "$g_player_party_morale_modifier_party_size"),
    (try_begin),
      (gt, reg1, 0),
      (str_store_string, s2, "@ -"),
    (else_try),
      (str_store_string, s2, "@ "),
    (try_end),

    (assign, reg2, "$g_player_party_morale_modifier_leadership"),
    (try_begin),
      (gt, reg2, 0),
      (str_store_string, s3, "@ +"),
    (else_try),
      (str_store_string, s3, "@ "),
    (try_end),

    (try_begin),
      (gt, "$g_player_party_morale_modifier_no_food", 0),
      (assign, reg7, "$g_player_party_morale_modifier_no_food"),
      (str_store_string, s5, "@^No food:  -{reg7}"),
    (else_try),
      (str_store_string, s5, "@ "),
    (try_end),
    (assign, reg3, "$g_player_party_morale_modifier_food"),
    (try_begin),
      (gt, reg3, 0),
      (str_store_string, s4, "@ +"),
    (else_try),
      (str_store_string, s4, "@ "),
    (try_end),

    (try_begin),
      (gt, "$g_player_party_morale_modifier_debt", 0),
      (assign, reg6, "$g_player_party_morale_modifier_debt"),
      (str_store_string, s6, "@^Wage debt:  -{reg6}"),
    (else_try),
      (str_store_string, s6, "@ "),
    (try_end),

    (party_get_morale, reg5, "p_main_party"),
    (store_sub, reg4, reg5, ":target_morale"),
    (try_begin),
      (gt, reg4, 0),
      (str_store_string, s7, "@ +"),
    (else_try),
      (str_store_string, s7, "@ "),
    (try_end),        
    (str_store_string, s1, "@Current party morale is {reg5}.^Current party morale modifiers are:^^Base morale:  +50^Party size: {s2}{reg1}^Leadership: {s3}{reg2}^Food variety: {s4}{reg3}{s5}{s6}^Recent events: {s7}{reg4}^TOTAL:  {reg5}"),
    ],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  ("faction_orders",0,"{s9}",
   "none",
   [
    (str_clear, s9),
    (store_current_hours, ":cur_hours"),
    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        (neq, ":faction_no", "fac_player_supporters_faction"),
        (faction_get_slot, ":faction_ai_state", ":faction_no", slot_faction_ai_state),
        (faction_get_slot, ":faction_ai_object", ":faction_no", slot_faction_ai_object),
        (faction_get_slot, ":faction_marshall", ":faction_no", slot_faction_marshall),
       (faction_get_slot, ":faction_ai_last_offensive_time", ":faction_no", slot_faction_ai_last_offensive_time),
        (faction_get_slot, ":faction_ai_offensive_max_followers", ":faction_no", slot_faction_ai_offensive_max_followers),
        (str_store_faction_name, s10, ":faction_no"),
       (store_sub, reg1, ":cur_hours", ":faction_ai_last_offensive_time"),
       (assign, reg2, ":faction_ai_offensive_max_followers"),
       (try_begin),
         (eq, ":faction_ai_state", sfai_default),
         (str_store_string, s11, "@Defending"),
       (else_try),
         (eq, ":faction_ai_state", sfai_gathering_army),
         (str_store_string, s11, "@Gathering army"),
       (else_try),
         (eq, ":faction_ai_state", sfai_attacking_center),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@Besieging {s11}"),
       (else_try),
         (eq, ":faction_ai_state", sfai_raiding_village),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@Raiding {s11}"),
       (else_try),
         (eq, ":faction_ai_state", sfai_attacking_enemy_army),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@Attacking enemies around {s11}"),
	   (try_end),
       (str_store_faction_name, s10, ":faction_no"),
       (try_begin),
         (lt, ":faction_marshall", 0),
         (str_store_string, s12, "@No one"),
       (else_try),
         (str_store_troop_name, s12, ":faction_marshall"),
        (try_end),
       (str_store_string, s9, "@{s9}{s10}^Current state: {s11}^Marshall: {s12}^Since the last offensive: {reg1} hours^Offensive maximum followers: {reg2}^^"),
     (try_end),
     (try_begin),
       (neg|is_between, "$g_cheat_selected_faction", kingdoms_begin, kingdoms_end),
       (call_script, "script_get_next_active_kingdom", kingdoms_end),
       (assign, "$g_cheat_selected_faction", reg0),
     (try_end),
     (str_store_faction_name, s10, "$g_cheat_selected_faction"),
     (str_store_string, s9, "@Selected faction is: {s10}^^{s9}"),
    ],
    [
      ("faction_orders_next_faction", [],"Select next nation.",
       [
         (call_script, "script_get_next_active_kingdom", "$g_cheat_selected_faction"),
         (assign, "$g_cheat_selected_faction", reg0),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_defend", [],"Force defend.",
       [
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, sfai_default),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, -1),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_gather", [],"Force gather army.",
       [
         (store_current_hours, ":cur_hours"),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, sfai_gathering_army),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_last_offensive_time, ":cur_hours"),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_offensive_max_followers, 1),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, -1),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_increase_time", [],"Increase last offensive time by 24 hours.",
       [
         (faction_get_slot, ":faction_ai_last_offensive_time", "$g_cheat_selected_faction", slot_faction_ai_last_offensive_time),
         (val_sub, ":faction_ai_last_offensive_time", 24),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_last_offensive_time, ":faction_ai_last_offensive_time"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_rethink", [],"Force rethink.",
       [
         (call_script, "script_init_ai_calculation"),
         (call_script, "script_decide_faction_ai", "$g_cheat_selected_faction"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_rethink_all", [],"Force rethink for all nations.",
       [
         (call_script, "script_recalculate_ais"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  
  ("character_report",0,"{s9}",
   "none",
   [(try_begin),
      (gt, "$g_player_reading_book", 0),
      (player_has_item, "$g_player_reading_book"),
      (str_store_item_name, s8, "$g_player_reading_book"),
      (str_store_string, s9, "@You are currently reading {s8}."),
    (else_try),
      (assign, "$g_player_reading_book", 0),
      (str_store_string, s9, "@You are not reading any books."),
    (try_end),
    (assign, ":num_friends", 0),
    (assign, ":num_enemies", 0),
    (str_store_string, s6, "@none"),
    (str_store_string, s8, "@none"),
    (try_for_range, ":troop_no", kingdom_heroes_begin, kingdom_heroes_end),
	  (call_script, "script_troop_get_player_relation", ":troop_no"),
      (assign, ":player_relation", reg0),
      #(troop_get_slot, ":player_relation", ":troop_no", slot_troop_player_relation),
      (try_begin),
        (gt, ":player_relation", 20),
        (try_begin),
          (eq, ":num_friends", 0),
          (str_store_troop_name, s8, ":troop_no"),
        (else_try),
          (eq, ":num_friends", 1),
          (str_store_troop_name, s7, ":troop_no"),
          (str_store_string, s8, "@{s7} and {s8}"),
        (else_try),
          (str_store_troop_name, s7, ":troop_no"),
          (str_store_string, s8, "@{s7}, {s8}"),
        (try_end),
        (val_add, ":num_friends", 1),
      (else_try),
        (lt, ":player_relation", -20),
        (try_begin),
          (eq, ":num_enemies", 0),
          (str_store_troop_name, s6, ":troop_no"),
        (else_try),
          (eq, ":num_enemies", 1),
          (str_store_troop_name, s5, ":troop_no"),
          (str_store_string, s6, "@{s5} and {s6}"),
        (else_try),
          (str_store_troop_name, s5, ":troop_no"),
          (str_store_string, s6, "@{s5}, {s6}"),
        (try_end),
        (val_add, ":num_enemies", 1),
      (try_end),
    (try_end),
    (assign, reg3, "$player_honor"),
    (troop_get_slot, reg2, "trp_player", slot_troop_renown),
    (str_store_string, s9, "@Renown: {reg2}.^Honour rating: {reg3}.^Friends: {s8}.^Enemies: {s6}.^{s9}"),
	
    (call_script, "script_get_number_of_hero_centers", "trp_player"),
    (assign, ":no_centers", reg0),
    (try_begin),
      (gt, ":no_centers", 0),
      (try_for_range, ":i_center", 0, ":no_centers"),
        (call_script, "script_troop_get_leaded_center_with_index", "trp_player", ":i_center"),
        (assign, ":cur_center", reg0),
        (try_begin),
          (eq, ":i_center", 0),
          (str_store_party_name, s8, ":cur_center"),
        (else_try),
          (eq, ":i_center", 1),
          (str_store_party_name, s7, ":cur_center"),
          (str_store_string, s8, "@{s7} and {s8}"),
        (else_try),
          (str_store_party_name, s7, ":cur_center"),
          (str_store_string, s8, "@{s7}, {s8}"),
        (try_end),
      (try_end),
      (str_store_string, s9, "@Your estates are: {s8}.^{s9}"),
    (try_end),
    (try_begin),
      (gt, "$players_kingdom", 0),
      (str_store_faction_name, s8, "$players_kingdom"),
	  (try_begin), 
		(faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
		(str_store_string, s9, "str_oim_you_are_the_marshal"),
	  (else_try), 
		(faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
		(str_store_string, s9, "str_oim_you_are_the_king"),
	  (else_try), 
      (str_store_string, s9, "@You are a lord of {s8}.^{s9}"),
	  (end_try), 	
    (try_end),
    ],
    [
	("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
	   ]
  ),

  ("party_size_report",0,"{s1}",
   "none",
   [(call_script, "script_game_get_party_companion_limit"),
    (assign, ":party_size_limit", reg0),

    (options_get_campaign_ai, ":difficulty"),

    (store_skill_level, ":leadership", "skl_leadership", "trp_player"),    
    (store_attribute_level, ":charisma", "trp_player", ca_charisma),
	(store_mul, ":charisma_mul_2", ":charisma", 2),

    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),

	(try_begin), #easy
	  (eq, ":difficulty", 2),
      (val_div, ":renown", 15),
	  (assign, reg4, 30),
	  (store_mul, ":leadership_mul_5_7_10", ":leadership", 10),
	(else_try), #moderate
	  (eq, ":difficulty", 1),
	  (val_div, ":renown", 20),
	  (assign, reg4, 20),
	  (store_mul, ":leadership_mul_5_7_10", ":leadership", 7),
	(else_try), #hard
	  (val_div, ":renown", 25),
	  (assign, reg4, 10),
	  (store_mul, ":leadership_mul_5_7_10", ":leadership", 5),
	(try_end),

    (try_begin),
      (gt, ":leadership", 0),
      (str_store_string, s2, "@ +"),
    (else_try),
      (str_store_string, s2, "@ "),
    (try_end),
    (try_begin),
      (gt, ":charisma", 0),
      (str_store_string, s3, "@ +"),
    (else_try),
      (str_store_string, s3, "@ "),
    (try_end),
    (try_begin),
      (gt, ":renown", 0),
      (str_store_string, s4, "@ +"),
    (else_try),
      (str_store_string, s4, "@ "),
    (try_end),
    (assign, reg5, ":party_size_limit"),
    (assign, reg1, ":leadership_mul_5_7_10"),
    (assign, reg2, ":charisma_mul_2"),
    (assign, reg3, ":renown"),
    (str_store_string, s1, "@Current party size limit is {reg5}.^Current party size modifiers are:^^Base size:  +{reg4}^Leadership: {s2}{reg1}^Charisma: {s3}{reg2}^Renown: {s4}{reg3}^TOTAL:  {reg5}"),
    ],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  ("faction_relations_report",0,"{s1}",
   "none",
   [(str_clear, s2),
    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
      (neq, ":cur_kingdom", "fac_player_supporters_faction"),
      (store_relation, ":cur_relation", "fac_player_supporters_faction", ":cur_kingdom"),
      (try_begin),
        (ge, ":cur_relation", 90),
        (str_store_string, s3, "@Loyal"),
      (else_try),
        (ge, ":cur_relation", 80),
        (str_store_string, s3, "@Devoted"),
      (else_try),
        (ge, ":cur_relation", 70),
        (str_store_string, s3, "@Fond"),
      (else_try),
        (ge, ":cur_relation", 60),
        (str_store_string, s3, "@Gracious"),
      (else_try),
        (ge, ":cur_relation", 50),
        (str_store_string, s3, "@Friendly"),
      (else_try),
        (ge, ":cur_relation", 40),
        (str_store_string, s3, "@Supportive"),
      (else_try),
        (ge, ":cur_relation", 30),
        (str_store_string, s3, "@Favorable"),
      (else_try),
        (ge, ":cur_relation", 20),
        (str_store_string, s3, "@Cooperative"),
      (else_try),
        (ge, ":cur_relation", 10),
        (str_store_string, s3, "@Accepting"),
      (else_try),
        (ge, ":cur_relation", 0),
        (str_store_string, s3, "@Indifferent"),
      (else_try),
        (ge, ":cur_relation", -10),
        (str_store_string, s3, "@Suspicious"),
      (else_try),
        (ge, ":cur_relation", -20),
        (str_store_string, s3, "@Grumbling"),
      (else_try),
        (ge, ":cur_relation", -30),
        (str_store_string, s3, "@Hostile"),
      (else_try),
        (ge, ":cur_relation", -40),
        (str_store_string, s3, "@Resentful"),
      (else_try),
        (ge, ":cur_relation", -50),
        (str_store_string, s3, "@Angry"),
      (else_try),
        (ge, ":cur_relation", -60),
        (str_store_string, s3, "@Hateful"),
      (else_try),
        (ge, ":cur_relation", -70),
        (str_store_string, s3, "@Revengeful"),
      (else_try),
        (str_store_string, s3, "@Vengeful"),
      (try_end),
      (str_store_faction_name, s4, ":cur_kingdom"),
      (assign, reg1, ":cur_relation"),
      (str_store_string, s2, "@{s2}^{s4}: {reg1} ({s3})"),
    (try_end),
    (str_store_string, s1, "@Your relation with the factions are:^{s2}"),
    ],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  ("camp",mnf_scale_picture,"You set up camp. What do you wish to do?",
   "none",
   [
     (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
    ],
    [
      ("camp_action_1",[(eq,"$cheat_mode",1)],"{!}Cheat: Walk around.",
       [(set_jump_mission,"mt_ai_training"),
        (call_script, "script_setup_random_scene"),
        (change_screen_mission),
        ]
       ),
   ("test", [
		(eq, debug_mode, 1),
   ],"{!}test menu", 
		[
			#(jump_to_menu, "mnu_oim_test_menus")
			#(call_script, "script_change_party_morale", "p_main_party", -100),
			##(assign, ":town_scene", "scn_oim_river_village"),
			##(modify_visitors_at_site, ":town_scene"),
			##(reset_visitors),
			##(set_jump_mission,"mt_oim_tutorial_training_ground"),
			##(set_visitor, "trp_player", 0),
			##(jump_to_scene, ":town_scene"),
			##(change_screen_mission),			
			(set_fixed_point_multiplier, 1000), 
			(party_set_extra_icon, "p_town_6", "icon_extra_icon_a", 0, 0, 50, 0), 
		]
   ),
      ("camp_action",[],"Take an action.",
       [(jump_to_menu, "mnu_camp_action"),
        ]
       ),
      ("oim_diplomacy_menu",[
		(faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
		(this_or_next|eq, "$players_kingdom", "fac_kingdom_1"),
		(             eq, "$players_kingdom", "fac_kingdom_2"),
		(eq, 1, 0), #disabled in Gold Edition
	  ],"Diplomacy",
       [
			(jump_to_menu, "mnu_oim_diplomacy_window"),
        ]
       ), 
	   
	   ("oim_cheatss",[(eq, debug_mode, 1),],"{!}Viv building process",
    [
	    (assign, "$talk_context", 0),
         #(party_get_slot, ":town_scene", "$current_town", slot_town_center),
		(assign, ":town_scene", "scn_oim_river_village"),
        (modify_visitors_at_site, ":town_scene"),
        (reset_visitors),
        (assign, "$g_mt_mode", tcm_default),
        (assign, "$g_mt_mode", tcm_default),
        (set_jump_mission,"mt_town_center"),
		(set_visitor, "trp_player", 0),
        (jump_to_scene, ":town_scene"),
        (change_screen_mission),
    ],"{!}Menu to edit AI-Mesh."),
	   
	   
	   ("oim_cheatss2",[(eq, debug_mode, 1),],"{!}Make a God 3",
       [
	    #(party_add_members, "p_main_party", "trp_moskow_dragoon", 10),
        #(party_add_members, "p_main_party", "trp_nord_veteran", 5),
		#(call_script, "script_troop_add_gold", "trp_player", 25000),
		
		#(troop_add_item, "trp_player","itm_zakaz_2stwol_udar1", 0),
			(try_for_range, ":troop", kingdom_heroes_begin, kingdom_heroes_end), 
				(store_troop_faction, ":faction", ":troop"), 
				(eq, ":faction", "fac_kingdom_2"),
				(neq, ":troop", "trp_kingdom_2_lord"),
		        (troop_set_slot, ":troop", slot_troop_discussed_rebellion, 1),
				(call_script, "script_change_troop_faction", ":troop", "fac_player_supporters_faction"),
				(troop_get_slot, ":lords_party", ":troop", slot_troop_leaded_party),
				(party_set_faction, ":lords_party", "fac_player_supporters_faction"),
			(end_try), 	

		
        ]
       ),
	  ("oim_cheass",[(eq, debug_mode, 1),],"{!}Build all",
    [
	    (party_add_members, "p_main_party", "trp_swadian_infantry", 10),
       	(call_script, "script_troop_add_gold", "trp_player", 25000),
	   ]
       ),	   

	  ("oim_cheass",[(eq, debug_mode, 1),],"{!}Build all",
       [
	    #(party_add_members, "p_main_party", "trp_swadian_infantry", 10),
       	#(call_script, "script_troop_add_gold", "trp_player", 25000),
		  (try_for_range, ":town_no", walled_centers_begin, walled_centers_end), 
			(try_for_range, ":upgrade_no", ms_towns_elements_start, ms_towns_elements_end),
				 (call_script, "script_add_upgrade_to_town", ":town_no", ":upgrade_no"),
			(end_try),
			(try_for_range, ":upgrade_no", ms_towns_upgrade_start, ms_towns_upgrade_end),
				 (call_script, "script_add_upgrade_to_town", ":town_no", ":upgrade_no"),
			(end_try),
		  (end_try),
	   
		  (try_for_range, ":village_no", villages_begin, villages_end), 
			(try_for_range, ":upgrade_no", ms_village_elements_start, ms_village_elements_end),
				 (call_script, "script_add_upgrade_to_town", ":village_no", ":upgrade_no"),
			(end_try),
			(try_for_range, ":upgrade_no", ms_village_upgrade_start, ms_village_upgrade_end),
				 (call_script, "script_add_upgrade_to_town", ":village_no", ":upgrade_no"),
			(end_try),
		  (end_try),
        ]
       ),
	   
	   ("oim_cheatss",[
		(eq, debug_mode, 1),
	   ],"{!}Viv building process",
       [

	    (try_for_range, ":cur_center", ms_parties_start, villages_end),
			(store_sub, ":offset", ":cur_center", towns_begin),
			(val_add, ":offset", ms_party_has_element_start_slot),
			(assign, ":end_element", ms_elements_end),
			(assign, ":start_element", ms_towns_elements_start),
			(store_add, ":time_to_built_slot", ms_time_to_build_start_slot, ":offset"),
			(try_for_range, ":temp_element", ":start_element", ":end_element"),
				(try_begin),
					(troop_slot_eq, ":temp_element", ":offset", ms_flag_is_building),
					(troop_get_slot, ":wait_time", ":temp_element",  ":time_to_built_slot"),
					(str_store_party_name, s10, ":cur_center"),
					(str_store_troop_name, s11, ":temp_element"),
					(assign, reg4, ":wait_time"),
					(store_div, reg5, reg4, 24),
					(display_log_message, "@V {s10} stroitsya {s11}. ostalos {reg4} = {reg5}"),
				(else_try),
					(troop_slot_eq, ":temp_element", ":offset", ms_flag_already_builded),
					(str_store_party_name, s10, ":cur_center"),
					(str_store_troop_name, s11, ":temp_element"),
					(display_log_message, "@V {s10} postroeno {s11}"),
				(try_end),
         (try_end),
         (try_end),		
        ]
       ),	   
	   
	   ("wagenburg_action_on",[
			(call_script, "script_party_count_fit_for_battle", "p_main_party"), 
			(gt, reg(0), 5),
			(eq, "$g_wagenburg_is_on", 0), 
		],"Build a wagon fort.",
       [
	    (assign, "$g_wagenburg_is_on", 1),
		(call_script, "script_game_get_party_speed_multiplier","p_main_party"),
        (unlock_achievement, ACHIEVEMENT_HUNKER_DOWN),		
		(change_screen_return),
        ]
       ),	

		("wagenburg_action_off",[(eq, "$g_wagenburg_is_on", 1),],"Pull down the wagon fort.",
       [
	    (assign, "$g_wagenburg_is_on", 0),
		(change_screen_return),
        ]
       ),	   
	   
      ("camp_wait_here",[],"Wait here for some time.",
       [
         (assign,"$g_camp_mode", 1),
		   (call_script, "script_recalculate_ills_count"), 
		   (try_begin),
				(gt, "$oim_illness_count", 0),
				(assign, "$oim_illness_camp_start", 1),
		   (try_end),
#           (assign,"$auto_menu","mnu_camp"),
         (assign, "$g_player_icon_state", pis_camping),
           (rest_for_hours_interactive, 24 * 7, 5, 1), #rest while attackable
         (change_screen_return),
        ]
       ),	   

      ("camp_cheat",
       [(eq, "$cheat_mode", 1)
        ],"CHEAT MENU!",
       [(jump_to_menu, "mnu_camp_cheat"),
     ],
       ),	   

	   ("ms_extra_adviser", [],"Send a messenger to the mayor's aide.",
						   [
								(jump_to_menu, "mnu_ms_additional_adviser"),
							]
       ),  	   
	   
      ("resume_travelling",[],"Continue traveling...",
       [
           (change_screen_return),
        ]
       ),
      ]
  ),

  ("camp_cheat",0,
   "Select a cheat:",
   "none",
   [
     ],
    [
      ("camp_cheat_1",[],"Increase player renown.",
       [(str_store_string, s1, "@Player renown is increased by 100. "),
        (call_script, "script_change_troop_renown", "trp_player" ,100),
        (jump_to_menu, "mnu_camp_cheat"),
	   ]
       ),
      ("camp_action_4",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action",0,
   "Choose an action:",
   "none",
   [
     ],
    [
      ("camp_recruit_prisoners",
       [(troops_can_join, 1),
        (store_current_hours, ":cur_time"),
        (val_sub, ":cur_time", 24),
        (gt, ":cur_time", "$g_prisoner_recruit_last_time"),
        (try_begin),
          (gt, "$g_prisoner_recruit_last_time", 0),
          (assign, "$g_prisoner_recruit_troop_id", 0),
          (assign, "$g_prisoner_recruit_size", 0),
          (assign, "$g_prisoner_recruit_last_time", 0),
        (try_end),
        ],"Recruit some of your prisoners to your party.",
       [(jump_to_menu, "mnu_camp_recruit_prisoners"),
        ],
       ),
      ("action_read_book",[],"Select a book to read.",
       [(jump_to_menu, "mnu_camp_action_read_book"),
        ]
       ),
      ("action_modify_banner",[(eq, "$cheat_mode", 1)],"{!}Cheat: Modify your banner.",
       [
           (start_presentation, "prsnt_banner_selection"),
        ]
       ),
      ("action_retire",[
		(eq, 0, 1),
	  ],"Retire from adventuring.",
       [(jump_to_menu, "mnu_retirement_verify"),
        ]
       ),
      ("camp_action_4",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_recruit_prisoners",0,
   "You offer your prisoners freedom if they agree to join you as soldiers. {s18}",
   "none",
   [(assign, ":num_regular_prisoner_slots", 0),
    (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
    (try_for_range, ":cur_stack", 0, ":num_stacks"),
      (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
      (neg|troop_is_hero, ":cur_troop_id"),
      (val_add, ":num_regular_prisoner_slots", 1),
    (try_end),
    (try_begin),
      (eq, ":num_regular_prisoner_slots", 0),
      (jump_to_menu, "mnu_camp_no_prisoners"),
    (else_try),
      (eq, "$g_prisoner_recruit_troop_id", 0),
      (store_current_hours, "$g_prisoner_recruit_last_time"),
      (store_random_in_range, ":rand", 0, 100),
      (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
      (store_sub, ":reject_chance", 15, ":persuasion_level"),
      (val_mul, ":reject_chance", 4),
      (try_begin),
        (lt, ":rand", ":reject_chance"),
        (assign, "$g_prisoner_recruit_troop_id", -7),
      (else_try),
        (assign, ":num_regular_prisoner_slots", 0),
        (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
        (try_for_range, ":cur_stack", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
          (neg|troop_is_hero, ":cur_troop_id"),
          (val_add, ":num_regular_prisoner_slots", 1),
        (try_end),
        (store_random_in_range, ":random_prisoner_slot", 0, ":num_regular_prisoner_slots"),
        (try_for_range, ":cur_stack", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
          (neg|troop_is_hero, ":cur_troop_id"),
          (val_sub, ":random_prisoner_slot", 1),
          (lt, ":random_prisoner_slot", 0),
          (assign, ":num_stacks", 0),
          (assign, "$g_prisoner_recruit_troop_id", ":cur_troop_id"),
          (party_prisoner_stack_get_size, "$g_prisoner_recruit_size", "p_main_party", ":cur_stack"),
        (try_end),
      (try_end),

      (try_begin),
        (gt, "$g_prisoner_recruit_troop_id", 0),
        (party_get_free_companions_capacity, ":capacity", "p_main_party"),
        (val_min, "$g_prisoner_recruit_size", ":capacity"),
        (assign, reg1, "$g_prisoner_recruit_size"),
        (gt, "$g_prisoner_recruit_size", 0),
        (try_begin),
          (gt, "$g_prisoner_recruit_size", 1),
          (assign, reg2, 1),
        (else_try),
          (assign, reg2, 0),
        (try_end),
        (str_store_troop_name_by_count, s1, "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        (str_store_string, s18, "@{reg1} {s1} {reg2?accept:accepts} the offer."),
      (else_try),
        (str_store_string, s18, "@No one accepts the offer."),
      (try_end),
    (try_end),
    ],
    [
      ("camp_recruit_prisoners_accept",[(gt, "$g_prisoner_recruit_troop_id", 0)],"Take them.",
       [(remove_troops_from_prisoners, "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        (party_add_members, "p_main_party", "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        (store_mul, ":morale_change", -3, "$g_prisoner_recruit_size"),
        (call_script, "script_change_player_party_morale", ":morale_change"),
        (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("camp_recruit_prisoners_reject",[(gt, "$g_prisoner_recruit_troop_id", 0)],"Reject them.",
       [(jump_to_menu, "mnu_camp"),
        (assign, "$g_prisoner_recruit_troop_id", 0),
        (assign, "$g_prisoner_recruit_size", 0),
        ]
       ),
      ("go_back_dot",[(le, "$g_prisoner_recruit_troop_id", 0)],"Go back.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),
  
  ("camp_no_prisoners",0,"You have no prisoners to recruit.",
   "none",
   [],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action_read_book",0,"Choose a book to read:",
   "none",
   [],
    [
      ("action_read_book_1",[(player_has_item, "itm_book_tactics"),
                             (item_slot_eq, "itm_book_tactics", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_tactics"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_tactics"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_2",[(player_has_item, "itm_book_persuasion"),
                             (item_slot_eq, "itm_book_persuasion", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_persuasion"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_persuasion"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_3",[(player_has_item, "itm_book_leadership"),
                             (item_slot_eq, "itm_book_leadership", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_leadership"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_leadership"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_4",[(player_has_item, "itm_book_intelligence"),
                             (item_slot_eq, "itm_book_intelligence", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_intelligence"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_intelligence"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_5",[(player_has_item, "itm_book_trade"),
                             (item_slot_eq, "itm_book_trade", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_trade"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_trade"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_6",[(player_has_item, "itm_book_weapon_mastery"),
                             (item_slot_eq, "itm_book_weapon_mastery", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_weapon_mastery"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_weapon_mastery"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_7",[(player_has_item, "itm_book_engineering"),
                             (item_slot_eq, "itm_book_engineering", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_engineering"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_engineering"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("camp_action_4",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action_read_book_start",0,"{s1}",
   "none",
   [(assign, ":new_book", "$temp"),
    (str_store_item_name, s2, ":new_book"),
    (try_begin),
      (store_attribute_level, ":int", "trp_player", ca_intelligence),
      (item_get_slot, ":int_req", ":new_book", slot_item_intelligence_requirement),
      (le, ":int_req", ":int"),
      (str_store_string, s1, "@You start reading {s2}. After a few pages,\
 you feel you could learn a lot from this book. You decide to keep it close by and read whenever you have the time."),
      (assign, "$g_player_reading_book", ":new_book"),
    (else_try),
      (str_store_string, s1, "@You flip through the pages of {s2}, but you find the text confusing and difficult to follow.\
 Try as you might, it soon gives you a headache, and you're forced to give up the attempt."),
    (try_end),],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),


  ("retirement_verify",0,"mno_leave",
   "none",
   [
     (store_current_day, reg0),
     (assign, reg1, "$g_player_luck"),
     ],
    [
      ("retire_yes",[],"Yes.",
       [
         (start_presentation, "prsnt_retirement"),
        ]
       ),
      ("retire_no",[],"No.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("end_game",0,"The decision is made, and you resolve to give up your adventurer's life and settle down. You sell off your weapons and armor, gather up all your money, and ride off into the sunset....",
   "none",
   [],
    [
      ("end_game_bye",[],"Farewell.",
       [
         (change_screen_quit),
        ]
       ),
      ]
  ),

  (
    "pay_day",mnf_scale_picture|mnf_disable_all_keys,"{s1}.",
    "none",
    [
        (set_background_mesh, "mesh_pic_payment"),
        
        (call_script, "script_calculate_player_faction_wage"),
        (assign, ":total_wages", reg0),
        (assign, reg6, ":total_wages"),

        (assign, reg2, "$g_player_debt_to_party_members"),
        (store_add, reg3, reg6, reg2),
        (store_troop_gold, ":player_wealth", "trp_player"),
        (assign, reg4, ":player_wealth"),

        (val_add, ":total_wages", "$g_player_debt_to_party_members"),

        (try_begin),
          (ge, ":player_wealth", ":total_wages"),
          (assign, "$g_player_debt_to_party_members", 0),		  
          (troop_remove_gold, "trp_player",":total_wages"),
          (store_sub, reg5, reg4, reg3),
          (str_store_string, s1, "@You paid {reg3} of your {reg4} denars to your men. You have {reg5} denars left."),
        (else_try),		  
          (troop_remove_gold, "trp_player",":player_wealth"),
          (store_sub, ":unpaid", ":total_wages", ":player_wealth"),
          (assign, reg5, ":unpaid"),
          (str_store_string, s1, "@Your debt to your men amounted to {reg3} denars, however you only had {reg4}. Unpaid sum of {reg5} denars is added as debt. Your party loses morale."),
          (assign, "$g_player_debt_to_party_members", ":unpaid"),
          (call_script, "script_objectionable_action", tmt_egalitarian, "str_men_unpaid"),
        (try_end),

        (str_store_string, s1, "@This week's wages: {reg6} denars^Earlier debts: {reg2} denars^Total payment: {reg3} denars^Current wealth: {reg4} denars^^{s1}"),
    ],
    [
      ("continue",[],"Continue...",
       [
        (change_screen_return,0),
        ]
       ),
    ]
  ),
  
  ("cattle_herd",mnf_scale_picture,"You encounter a herd of cattle.",
   "none",
   [(play_sound, "snd_cow_moo"),
    (set_background_mesh, "mesh_pic_cattle"),
   ],
    [
      ("cattle_drive_away",[],"Drive the cattle onward.",
       [
        #(party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 1),
        #(party_set_ai_behavior, "$g_encountered_party", ai_bhvr_driven_by_party),
        #(party_set_ai_object,"$g_encountered_party", "p_main_party"),
		
		(party_set_slot, "$g_encountered_party", slot_party_ai_state, spai_undefined),
		(party_set_ai_behavior, "$g_encountered_party", ai_bhvr_escort_party),
        (party_set_ai_object,"$g_encountered_party", "p_main_party"),
		(party_set_flags, "$g_encountered_party", pf_default_behavior, 0),
		
        (change_screen_return),
        ]
       ),
      ("cattle_stop",[],"Bring the herd to a stop.",
       [
        #(party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 0),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_hold),
        (change_screen_return),
        ]
       ),
      ("cattle_kill",[(assign, ":continue", 1),
                      (try_begin),
                        (check_quest_active, "qst_move_cattle_herd"),
                        (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, "$g_encountered_party"),
                        (assign, ":continue", 0),
                      (try_end),
                      (eq, ":continue", 1)],"Slaughter some of the animals.",
       [(jump_to_menu, "mnu_cattle_herd_kill"),
        ]
       ),
      ("leave",[],"Leave.",
       [(change_screen_return),
        ]
       ),
      ]
  ),

  ("cattle_herd_kill",0,"How many animals do you want to slaughter?",
   "none",
   [(party_get_num_companions, reg5, "$g_encountered_party")],
    [
      ("cattle_kill_1",[(ge, reg5, 1),],"One.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 1),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_2",[(ge, reg5, 2),],"Two.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 2),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_3",[(ge, reg5, 3),],"Three.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 3),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_4",[(ge, reg5, 4),],"Four.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 4),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_5",[(ge, reg5, 5),],"Five.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 5),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_cattle_herd"),
        ]
       ),
      ]
  ),

  ("cattle_herd_kill_end",0,"You shouldn't be reading this.",
   "none",
   [(change_screen_return)],
    [
      ]
  ),


  ("arena_duel_fight",0,"You and your opponent prepare for combat.",
   "none",
   [],
   [
     ("continue",[],"Continue...",
      [
        (jump_to_menu, "mnu_simple_encounter"),
        (change_screen_mission),        
      ]),
    ]
  ),

  (
    "simple_encounter",mnf_enable_hot_keys|mnf_scale_picture,"{s2} You have {reg10} troops fit for battle against their {reg11}. ^{s4}",
    "none",
    [      
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (assign, "$g_encounter_is_in_village", 0),
          (assign, "$g_encounter_type", 0),
          (try_begin),
            (party_slot_eq, "$g_enemy_party", slot_party_ai_state, spai_raiding_around_center),        
            (party_get_slot, ":village_no", "$g_enemy_party", slot_party_ai_object),
            (store_distance_to_party_from_party, ":dist", ":village_no", "$g_enemy_party"),
            (try_begin),
              (lt, ":dist", raid_distance),
              (assign, "$g_encounter_is_in_village", ":village_no"),
              (assign, "$g_encounter_type", enctype_fighting_against_village_raid),
            (try_end),
          (try_end),
          (try_begin),
            (gt, "$g_player_raiding_village", 0),
            (assign, "$g_encounter_is_in_village", "$g_player_raiding_village"),
            (assign, "$g_encounter_type", enctype_catched_during_village_raid),
            (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 1), #attach as enemy
            (str_store_string, s1, "@Villagers"),
            (display_message, "str_s1_joined_battle_enemy"),
          (else_try),
            (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
            (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 0), #attach as friend
            (str_store_string, s1, "@Villagers"),
            (display_message, "str_s1_joined_battle_friend"),
            # Let village party join battle at your side
          (try_end),
          (call_script, "script_let_nearby_parties_join_current_battle", 0, 0),
          (call_script, "script_encounter_init_variables"),
          (assign, "$encountered_party_hostile", 0),
          (assign, "$encountered_party_friendly", 0),
          (try_begin),
            (gt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_friendly", 1),
          (try_end),
          (try_begin),
            (lt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_hostile", 1),
            (try_begin),
              (encountered_party_is_attacker),
              (assign, "$cant_leave_encounter", 1),
            (try_end),
          (try_end),
          (assign, "$talk_context", tc_party_encounter),
          (call_script, "script_setup_party_meeting", "$g_encountered_party"),
        (else_try), #second or more turn
#          (try_begin),
#            (call_script, "script_encounter_calculate_morale_change"),
#          (try_end),
          (try_begin),
            # We can leave battle only after some troops have been killed. 
            (eq, "$cant_leave_encounter", 1),
            (call_script, "script_party_count_members_with_full_health", "p_main_party_backup"),
            (assign, ":org_total_party_counts", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_encountered_party_backup"),
            (val_add, ":org_total_party_counts", reg0),

            (call_script, "script_party_count_members_with_full_health", "p_main_party"),
            (assign, ":cur_total_party_counts", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
            (val_add, ":cur_total_party_counts", reg0),

            (store_sub, ":leave_encounter_limit", ":org_total_party_counts", 10),
            (lt, ":cur_total_party_counts", ":leave_encounter_limit"),
            (assign, "$cant_leave_encounter", 0),
          (try_end),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),
		(str_store_string, s4,"@ "),
		(assign, "$g_ai_wagenburg_is_on", 0),
        #setup s2
        (try_begin),
          (party_is_active, "$g_encountered_party"),
          (str_store_party_name, s1,"$g_encountered_party"),
          (try_begin),
            (eq, "$g_encounter_type", 0),
            (str_store_string, s2,"@You have encountered {s1}."),
			(try_begin),
				(neg|encountered_party_is_attacker),
				(eq, "$g_wagenburg_is_on", 0),
				(call_script, "script_check_ai_wagenburg"),
				(try_begin),
					(eq, "$g_ai_wagenburg_is_on",1),
					(str_store_string, s4,"@Armiya protivnika postroila lager (wagenburg)."),
				(try_end),
			(try_end),
          (else_try),
            (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
            (str_store_party_name, s3, "$g_encounter_is_in_village"),
            (str_store_string, s2,"@You have engaged {s1} while they were raiding {s3}."),
          (else_try),
            (eq, "$g_encounter_type", enctype_catched_during_village_raid),
            (str_store_party_name, s3, "$g_encounter_is_in_village"),
            (str_store_string, s2,"@You were caught by {s1} while your forces were raiding {s3}."),
          (try_end),
        (try_end),
        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (assign, ":num_enemy_regulars_remaining", reg0),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1), #battle won
                        
            (this_or_next|le, ":num_enemy_regulars_remaining", 0), #battle won
            (le, ":num_enemy_regulars_remaining",  "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

            (assign, ":enemy_finished",1),
          (else_try),
            (eq, "$g_engaged_enemy", 1), 
            
            (this_or_next|le, ":num_enemy_regulars_remaining", 0), 
            (le, "$g_enemy_fit_for_battle", "$num_routed_enemies"),  #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
            
            (ge, "$g_friend_fit_for_battle",1),
            (assign, ":enemy_finished",1),
          (try_end),
                
          (this_or_next|eq, ":enemy_finished",1),
          (eq,"$g_enemy_surrenders",1),
          (assign, "$g_next_menu", -1),
          (jump_to_menu, "mnu_total_victory"),
        (else_try),       
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),        
          (assign, ":num_our_regulars_remaining", reg0),
          (assign, ":friends_finished",0),
          (try_begin),
            (eq, "$g_battle_result", -1),

            #(eq, ":num_our_regulars_remaining", 0), #battle lost
            (le, ":num_our_regulars_remaining",  "$num_routed_us"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

            (assign,  ":friends_finished", 1),
          (else_try),
            (eq, "$g_engaged_enemy", 1),
            (ge, "$g_enemy_fit_for_battle",1),
            (le, "$g_friend_fit_for_battle",0),
            (assign,  ":friends_finished",1),
          (try_end),
          
          (this_or_next|eq,  ":friends_finished",1),
          (eq,"$g_player_surrenders",1),
          (assign, "$g_next_menu", "mnu_captivity_start_wilderness"),
          (jump_to_menu, "mnu_total_defeat"),
        (try_end),

       
        (try_begin),
          (eq, "$g_encountered_party_template", "pt_looters"),
          (set_background_mesh, "mesh_pic_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_mountain_bandits"),
          (set_background_mesh, "mesh_pic_mountain_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_steppe_bandits"),
          (set_background_mesh, "mesh_pic_steppe_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_sea_raiders"),
          (set_background_mesh, "mesh_pic_sea_raiders"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_forest_bandits"),
          (set_background_mesh, "mesh_pic_forest_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_deserters"),
          (set_background_mesh, "mesh_pic_deserters"),
		#OiM code
        (else_try),
          (eq, "$g_encountered_party_template", "pt_zamoshie_bandits"),
          (set_background_mesh, "mesh_pic_forest_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_oim_swedish_army"),
          (set_background_mesh, "mesh_pic_swed_army"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_oim_kozak_army"),
          (set_background_mesh, "mesh_pic_kozak_army"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_oim_potop_mercs_army"),
          (set_background_mesh, "mesh_pic_swed_army"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_oim_potop_mercs_army2"),
          (set_background_mesh, "mesh_pic_swed_army"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_getman_deserters"),
          (set_background_mesh, "mesh_pic_deserters"),
        (else_try),
		  (this_or_next|eq, "$g_encountered_party_template", "pt_merchant_caravan"),
		  (this_or_next|eq, "$g_encountered_party_template", "pt_forager_party"),
		  (this_or_next|eq, "$g_encountered_party_template", "pt_scout_party"),
		  (this_or_next|eq, "$g_encountered_party_template", "pt_patrol_party"),
          (eq, "$g_encountered_party_template", "pt_kingdom_hero_party"),
		  (store_faction_of_party, ":faction_no", "$g_encountered_party"), 
		  (try_begin),
			(eq, ":faction_no", "fac_kingdom_1"), 
			(set_background_mesh, "mesh_pic_pol_army"),
		  (else_try),
			(eq, ":faction_no", "fac_kingdom_2"), 
			(set_background_mesh, "mesh_pic_moscow_army"),
		  (else_try),
			(eq, ":faction_no", "fac_kingdom_4"), 
			(set_background_mesh, "mesh_pic_swed_army"),
		  (else_try),
			(eq, ":faction_no", "fac_kingdom_5"), 
			(set_background_mesh, "mesh_pic_kozak_army"),
		  (end_try), 
		  (try_end),
		(try_begin), 
			#(eq, "$g_talk_troop", "trp_kingdom_1_lord"), 
			(party_is_active,  "$g_encountered_party"),
			(party_stack_get_troop_id, ":leader_troop_id", "$g_encountered_party", 0),
			(eq, ":leader_troop_id", "trp_kingdom_1_lord"), 
			(check_quest_active, "qst_oim_potop_execute_king"),
			(neg|check_quest_succeeded, "qst_oim_potop_execute_king"), 
			(neg|check_quest_finished,"qst_oim_potop_execute_king"),
			(assign, "$encountered_party_friendly", 0),
		(end_try), 
		(try_begin), 
			(eq, "$g_encountered_party_faction", "fac_commoners"), 
			(neq, "$g_encountered_party_template", "pt_oim_static_object"),
			(assign, "$encountered_party_friendly", 0),
        (try_end),
    ],
    [
      ("encounter_attack",[
	      (eq, "$g_ai_wagenburg_is_on", 0),
          (eq, "$encountered_party_friendly", 0),
          (neg|troop_is_wounded, "trp_player"),
##          (store_troop_health,reg(5)),
##          (ge,reg(5),5),
          ],"Charge the enemy.",[
                                (assign, "$g_battle_result", 0),
                                (assign, "$g_engaged_enemy", 1),
                                (call_script, "script_calculate_renown_value"),
                                (call_script, "script_calculate_battle_advantage"),
                                (set_battle_advantage, reg0),
                                (set_party_battle_mode),
                                (try_begin),
                                  (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
                                  (assign, "$g_village_raid_evil", 0),
                                  (set_jump_mission,"mt_village_raid"),
                                  (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_castle_exterior),
                                  (jump_to_scene, ":scene_to_use"),
                                (else_try),
                                  (eq, "$g_encounter_type", enctype_catched_during_village_raid),
                                  (assign, "$g_village_raid_evil", 0),
                                  (set_jump_mission,"mt_village_raid"),
                                  (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_castle_exterior),
                                  (jump_to_scene, ":scene_to_use"),
                                (else_try),
                                  (set_jump_mission,"mt_lead_charge"),
								  (try_begin),
								    (eq, "$g_wagenburg_is_on", 1),
#fix this for wagens
									(encountered_party_is_attacker),
										(call_script, "script_get_map_for_wagenburg_battle", "p_main_party"),
									    (jump_to_scene, reg0),
										(call_script, "script_get_map_for_wagenburg_battle", "p_main_party"),
										#(assign, reg0, "scn_test_scene"),
								  (else_try),
										(assign, "$g_wagenburg_is_on", 0),
                                  (call_script, "script_setup_random_scene"),
                                (try_end),
                                (try_end),
								# illness check
								(call_script, "script_remove_health"),
                                (assign, "$g_next_menu", "mnu_simple_encounter"),
                                (jump_to_menu, "mnu_battle_debrief"),
                                (change_screen_mission),
                                ]),
    ("encounter_attack_wagenburg_mounted",[
											  (eq, "$g_ai_wagenburg_is_on", 1),
											  (eq, "$encountered_party_friendly", 0),
											  (neg|troop_is_wounded, "trp_player"),
											 ],"Attack on horseback.",[
									(call_script, "script_ai_wagenburg_start", flag_mounted),
								]),      
	 ("encounter_attack_wagenburg_unmounted",[
											  (eq, "$g_ai_wagenburg_is_on", 1),
											  (eq, "$encountered_party_friendly", 0),
											  (neg|troop_is_wounded, "trp_player"),
											 ],"Attack on foot.",[
									(call_script, "script_ai_wagenburg_start", 1),
								]),       
      ("encounter_order_attack",[
          (eq, "$encountered_party_friendly", 0),
        (call_script, "script_party_count_members_with_full_health", "p_main_party"),(ge, reg0, 4),
          ],"Order your troops to attack without you.",
      [
        (jump_to_menu, "mnu_order_attack_begin"),
        #(simulate_battle,3),
                                                            ]),
      
      ("encounter_leave",[
          (eq,"$cant_leave_encounter", 0),
          ],"Leave.",[

###NPC companion changes begin
              (try_begin),
                  (eq, "$encountered_party_friendly", 0),
                  (encountered_party_is_attacker),
                  (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
              (try_end),
###NPC companion changes end
#Troop commentary changes begin
              (try_begin),
                  (eq, "$encountered_party_friendly", 0),
                  (encountered_party_is_attacker),
                  (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
                  (try_for_range, ":stack_no", 0, ":num_stacks"),
                    (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
                    (is_between, ":stack_troop", kingdom_heroes_begin, kingdom_heroes_end),
                    (store_troop_faction, ":victorious_faction", ":stack_troop"),
                    (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
                  (try_end),
              (try_end),
#Troop commentary changes end
          	(leave_encounter),(change_screen_return)]),
      ("encounter_retreat",[
         (eq,"$cant_leave_encounter", 1),
         (call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
         (assign, ":max_skill", reg0),
         (val_add, ":max_skill", 4),

         (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
         (assign, ":enemy_party_strength", reg0),
         (val_div, ":enemy_party_strength", 2),

         (val_div, ":enemy_party_strength", ":max_skill"),
         (val_max, ":enemy_party_strength", 1),

         (call_script, "script_party_count_fit_regulars", "p_main_party"),
         (assign, ":player_count", reg0),
         (ge, ":player_count", ":enemy_party_strength"),
         ],"Pull back, leaving some soldiers behind to cover your retreat.",[(jump_to_menu, "mnu_encounter_retreat_confirm"),]),
         
      ("encounter_surrender",[
         (eq,"$cant_leave_encounter", 1),
          ],"Surrender.",[(assign,"$g_player_surrenders",1)]),
    ]
  ),
  (
    "encounter_retreat_confirm",0,"As the party member with the highest understanding of tactics, ({reg2} tactics skill), {reg3?you devise:{s3} devises} a plan that will allow you and your men to escape with your lives. However, you'll have to leave {reg4} soldiers behind to stop the enemy from giving chase.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),
     (val_add, ":max_skill", 4),

     (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
     (assign, ":enemy_party_strength", reg0),
     (val_div, ":enemy_party_strength", 2),

     (store_div, reg4, ":enemy_party_strength", ":max_skill"),
     (val_max, reg4, 1),
     
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
     ],
    [
      ("leave_behind",[],"Sacrifice these men to save the rest.",[
          (assign, ":num_casualties", reg4),
          (try_for_range, ":unused", 0, ":num_casualties"),
            (call_script, "script_cf_party_remove_random_regular_troop", "p_main_party"),
            (assign, ":lost_troop", reg0),
            (store_random_in_range, ":random_no", 0, 100),
            (ge, ":random_no", 30),
            (party_add_prisoners, "$g_encountered_party", ":lost_troop", 1),
           (try_end),
           (call_script, "script_change_player_party_morale", -20),
           (jump_to_menu, "mnu_encounter_retreat"),
          ]),
      ("dont_leave_behind",[],"Remain on the battlefield.",[(jump_to_menu, "mnu_simple_encounter"),]),
    ]
  ),
  (
    "encounter_retreat",0,
    "You tell {reg4} of your troops to hold back the enemy, while you retreat with the rest of your party.",
    "none",
    [
     ],
    [
      ("continue",[],"Continue...",[
###Troop commentary changes begin
          (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
          (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
              (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
              (is_between, ":stack_troop", kingdom_heroes_begin, kingdom_heroes_end),
              (store_troop_faction, ":victorious_faction", ":stack_troop"),
              (call_script, "script_add_log_entry", logent_player_retreated_from_lord_cowardly, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
          (try_end),
###Troop commentary changes end          

          (leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "order_attack_begin",0,"Your troops prepare to attack the enemy.",
    "none",
    [],
    [
      ("order_attack_begin",[],"Order the attack to commence.", [
                                    (assign, "$g_engaged_enemy", 1),
                                    (jump_to_menu,"mnu_order_attack_2"),
                                    ]),
      ("call_back",[],"Call them back.",[(jump_to_menu,"mnu_simple_encounter")]),
    ]
  ),
  (
    "order_attack_2",mnf_disable_all_keys,"{s4}^^Your casualties: {s8}^^Enemy casualties: {s9}",
    "none",
    [
                                    (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
                                    (assign, ":player_party_strength", reg0),

                                    (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
                                    (assign, ":enemy_party_strength", reg0),
                                    
      (party_collect_attachments_to_party, "p_main_party", "p_collective_ally"),
      (call_script, "script_party_calculate_strength", "p_collective_ally", 1), #exclude player
      (assign, ":total_player_and_followers_strength", reg0),
                                    
      (try_begin),
        (le, ":total_player_and_followers_strength", ":enemy_party_strength"),
        (assign, ":minimum_power", ":total_player_and_followers_strength"),
      (else_try),
        (assign, ":minimum_power", ":enemy_party_strength"),
      (try_end),
      
      (try_begin),
        (le, ":minimum_power", 5),
        (assign, ":division_constant", 1),
      (else_try),
        (le, ":minimum_power", 10),
        (assign, ":division_constant", 2),
      (else_try),
        (le, ":minimum_power", 25),
        (assign, ":division_constant", 3),
      (else_try),
        (le, ":minimum_power", 50),
        (assign, ":division_constant", 4),
      (else_try),
        (le, ":minimum_power", 100),
        (assign, ":division_constant", 5),
      (else_try),
        (le, ":minimum_power", 200),
        (assign, ":division_constant", 6),
      (else_try),
        (le, ":minimum_power", 400),
        (assign, ":division_constant", 7),
      (else_try),
        (le, ":minimum_power", 800),
        (assign, ":division_constant", 8),
      (else_try),
        (le, ":minimum_power", 1600),
        (assign, ":division_constant", 9),
      (else_try),
        (le, ":minimum_power", 3200),
        (assign, ":division_constant", 10),
      (else_try),
        (le, ":minimum_power", 6400),
        (assign, ":division_constant", 11),
      (else_try),
        (le, ":minimum_power", 12800),
        (assign, ":division_constant", 12),
      (else_try),
        (le, ":minimum_power", 25600),
        (assign, ":division_constant", 13),
      (else_try),
        (le, ":minimum_power", 51200),
        (assign, ":division_constant", 14),
      (else_try),
        (le, ":minimum_power", 102400),
        (assign, ":division_constant", 15),
      (else_try),  
        (assign, ":division_constant", 16),
      (try_end),  
                                                                              
      (val_div, ":player_party_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
      (val_max, ":player_party_strength", 1), #1.126
      (val_div, ":enemy_party_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
      (val_max, ":enemy_party_strength", 1), #1.126
      (val_div, ":total_player_and_followers_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
      (val_max, ":total_player_and_followers_strength", 1), #1.126

      (store_mul, "$g_strength_contribution_of_player", ":player_party_strength", 100),
      (val_div, "$g_strength_contribution_of_player", ":total_player_and_followers_strength"),

                                    (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength", "p_temp_casualties"),
                                    (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
                                    (str_store_string_reg, s8, s0),
                                    
      (try_begin),
        (ge, "$g_ally_party", 0),
        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
        (str_store_string_reg, s8, s0),
      (try_end),  

      (inflict_casualties_to_party_group, "$g_encountered_party", ":total_player_and_followers_strength", "p_temp_casualties"),

      #ozan begin
      (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"), 
      (try_for_range, ":stack_no", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"), 
        (try_begin),
          (party_stack_get_size, ":stack_size", "p_temp_casualties", ":stack_no"),
          (gt, ":stack_size", 0),
          (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
          (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties", ":stack_no"),                                    
          (gt, ":stack_wounded_size", 0),
          (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
        (try_end),
      (try_end),
      #ozan end

      (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
      (str_store_string_reg, s9, s0),

      (party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"),
                                    (assign, "$no_soldiers_left", 0),
                                    (try_begin),
                                      (call_script, "script_party_count_members_with_full_health", "p_main_party"),
        (assign, ":num_our_regulars_remaining", reg0),
        (store_add, ":num_routed_us_plus_one", "$num_routed_us", 1),
        (le, ":num_our_regulars_remaining", ":num_routed_us_plus_one"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
                                      (assign, "$no_soldiers_left", 1),
                                      (str_store_string, s4, "str_order_attack_failure"),
                                    (else_try),
                                      (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
        (assign, ":num_enemy_regulars_remaining", reg0),
        (this_or_next|le, ":num_enemy_regulars_remaining", 0),
        (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
                                      (assign, ":continue", 0),
                                      (party_get_num_companion_stacks, ":party_num_stacks", "p_collective_enemy"),
                                      (try_begin),
                                        (eq, ":party_num_stacks", 0),
                                        (assign, ":continue", 1),
                                      (else_try),
                                        (party_stack_get_troop_id, ":party_leader", "p_collective_enemy", 0),
                                        (try_begin),
                                          (neg|troop_is_hero, ":party_leader"),
                                          (assign, ":continue", 1),
                                        (else_try),
                                          (troop_is_wounded, ":party_leader"),
                                          (assign, ":continue", 1),
                                        (try_end),
                                      (try_end),
                                      (eq, ":continue", 1),
                                      (assign, "$g_battle_result", 1),
                                      (assign, "$no_soldiers_left", 1),
                                      (str_store_string, s4, "str_order_attack_success"),
                                    (else_try),
                                      (str_store_string, s4, "str_order_attack_continue"),
                                    (try_end),
    ],
    [
      ("order_attack_continue",[(eq, "$no_soldiers_left", 0)],"Order your soldiers to continue the attack.",[
          (jump_to_menu,"mnu_order_attack_2"),
          ]),
      ("order_retreat",[(eq, "$no_soldiers_left", 0)],"Call your soldiers back.",[
          (jump_to_menu,"mnu_simple_encounter"),
          ]),
      ("continue",[(eq, "$no_soldiers_left", 1)],"Continue...",[
          (jump_to_menu,"mnu_simple_encounter"),
          ]),
    ]
  ),

  (
    "battle_debrief",mnf_scale_picture|mnf_disable_all_keys,"{s11}^^Your Casualties:{s8}{s10}^^Enemy Casualties:{s9}",
    "none",
    [
     (try_begin),
       (eq, "$g_battle_result", 1),
       (call_script, "script_change_troop_renown", "trp_player", "$battle_renown_value"),
     (try_end),
          
     (call_script, "script_encounter_calculate_fit"),

     (call_script, "script_party_count_fit_regulars", "p_main_party"),
     (assign, "$playerparty_postbattle_regulars", reg0),
     
     (try_begin),
       (eq, "$g_battle_result", 1),
       (eq, "$g_enemy_fit_for_battle", 0),
       (str_store_string, s11, "@You were victorious!"),
#       (play_track, "track_bogus"), #clear current track.
#       (call_script, "script_music_set_situation_with_culture", mtf_sit_victorious),
       (try_begin),
         (gt, "$g_friend_fit_for_battle", 1),
         (set_background_mesh, "mesh_pic_victory"),
       (try_end),
     (else_try),
       (eq, "$g_battle_result", -1),
       (ge, "$g_enemy_fit_for_battle",1),
       (this_or_next|le, "$g_friend_fit_for_battle",0),
       (le, "$playerparty_postbattle_regulars", 0),
       (str_store_string, s11, "@Battle was lost. Your forces were utterly crushed."),
	   (assign, "$g_siege_method", 0),
       (set_background_mesh, "mesh_pic_defeat"),
     (else_try),
       (eq, "$g_battle_result", -1),
       (str_store_string, s11, "@Your companions carry you away from the fighting."),
	   (assign, "$g_siege_method", 0),
       (troop_get_type, ":is_female", "trp_player"),
       (try_begin),
         (eq, ":is_female", 1),
         (set_background_mesh, "mesh_pic_wounded_fem"),
       (else_try),
         (set_background_mesh, "mesh_pic_wounded"),
       (try_end),
     (else_try),
       (eq, "$g_battle_result", 1),
       (str_store_string, s11, "@You have defeated the enemy."),
       (try_begin),
         (gt, "$g_friend_fit_for_battle", 1),
         (set_background_mesh, "mesh_pic_victory"),
       (try_end),
     (else_try),
       (eq, "$g_battle_result", 0),
       (str_store_string, s11, "@You have retreated from the fight."),
     (try_end),
#NPC companion changes begin
##check for excessive casualties, more forgiving if battle result is good
     (try_begin),
        (gt, "$playerparty_prebattle_regulars", 9),
        (store_add, ":divisor", 3, "$g_battle_result"), 
        (store_div, ":half_of_prebattle_regulars", "$playerparty_prebattle_regulars", ":divisor"),
        (lt, "$playerparty_postbattle_regulars", ":half_of_prebattle_regulars"),
        (call_script, "script_objectionable_action", tmt_egalitarian, "str_excessive_casualties"),
     (try_end),
#NPC companion changes end



     (call_script, "script_print_casualties_to_s0", "p_player_casualties", 0),
     (str_store_string_reg, s8, s0),
     (call_script, "script_print_casualties_to_s0", "p_enemy_casualties", 0),
	 (try_begin),
		(eq, "$g_enemy_party", "$oim_deserters_party"),
		(try_begin),
			(eq, "$g_battle_result", 1),
			(assign, ":total_enemy_kills", reg4),
			(val_mul, ":total_enemy_kills", 20),
			(troop_add_gold,"trp_player",":total_enemy_kills"),
		(else_try),
			(eq, "$g_battle_result", -1),
			(store_troop_gold,":cur_player_gold","trp_player"),
			(val_div, ":cur_player_gold", 4),			
			(troop_remove_gold,"trp_player",":cur_player_gold"),
			(assign, "$g_next_menu", "mnu_captivity_wilderness_taken_prisoner"),
			(assign, "$g_siege_method", 0),
		(try_end),
	 (try_end),
	 
     (str_store_string_reg, s9, s0),
     (str_clear, s10),
     (try_begin),
       (eq, "$any_allies_at_the_last_battle", 1),
       (call_script, "script_print_casualties_to_s0", "p_ally_casualties", 0),
       (str_store_string, s10, "@^^Ally Casualties:{s0}"),
     (try_end),
     ],
    [
      ("continue",[],"Continue...",[
	   #(call_script, "script_replace_shturm_item_end"),
       (jump_to_menu, "$g_next_menu"),
      ]),
    ]
  ),


  
  (
    "total_victory", 0,"You shouldn't be reading this... {s9}",
    "none",
    [
        # We exploit the menu condition system below.
        # The conditions should make sure that always another screen or menu is called.
        (assign, ":break", 0),
        (try_begin),
          (eq, "$routed_party_added", 0), #new
          (assign, "$routed_party_added", 1),
          
           #add new party to map (routed_warriors)
          (call_script, "script_add_routed_party"),
        (end_try),
        		
		#new - begin
        (party_get_num_companion_stacks, ":num_stacks", "p_collective_enemy"),          
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", "p_collective_enemy", ":i_stack"),
          (is_between, ":stack_troop", kingdom_heroes_begin, kingdom_heroes_end),
          (troop_is_wounded, ":stack_troop"),
          (party_add_members, "p_total_enemy_casualties", ":stack_troop", 1),
        (try_end),                      
        #new - end

        (try_begin),
          # Talk to ally leader
          (eq, "$thanked_by_ally_leader", 0),
          (assign, "$thanked_by_ally_leader", 1),

          (gt, "$g_ally_party", 0),          
          
          (store_add, ":total_str_without_player", "$g_starting_strength_friends", "$g_starting_strength_enemy_party"),
          (val_sub, ":total_str_without_player", "$g_starting_strength_main_party"),

          (store_sub, ":ally_strength_without_player", "$g_starting_strength_friends", "$g_starting_strength_main_party"),
        
          (store_mul, ":ally_advantage", ":ally_strength_without_player", 100),
          (val_add, ":total_str_without_player", 1),
          (val_div, ":ally_advantage", ":total_str_without_player"),
          #Ally advantage=50  means battle was evenly matched

          (store_sub, ":enemy_advantage", 100, ":ally_advantage"),
        
          (store_mul, ":faction_reln_boost", ":enemy_advantage", "$g_starting_strength_enemy_party"),
          (val_div, ":faction_reln_boost", 3000),
          (val_min, ":faction_reln_boost", 4),

          (store_mul, "$g_relation_boost", ":enemy_advantage", ":enemy_advantage"),
          (val_div, "$g_relation_boost", 700),
          (val_clamp, "$g_relation_boost", 0, 20),
        
          (party_get_num_companion_stacks, ":num_ally_stacks", "$g_ally_party"),
          (gt, ":num_ally_stacks", 0),
          (store_faction_of_party, ":ally_faction","$g_ally_party"),
          (call_script, "script_change_player_relation_with_faction", ":ally_faction", ":faction_reln_boost"),
          (party_stack_get_troop_id, ":ally_leader", "$g_ally_party"),
          (party_stack_get_troop_dna, ":ally_leader_dna", "$g_ally_party", 0),
          (try_begin),
            (troop_is_hero, ":ally_leader"),
            (troop_get_slot, ":hero_relation", ":ally_leader", slot_troop_player_relation),
            (assign, ":rel_boost", "$g_relation_boost"),
            (try_begin),
              (lt, ":hero_relation", -5),
              (val_div, ":rel_boost", 3),
            (try_end),
            (call_script,"script_change_player_relation_with_troop", ":ally_leader", ":rel_boost"),
          (try_end),
          (assign, "$talk_context", tc_ally_thanks),
          (call_script, "script_setup_troop_meeting",":ally_leader", ":ally_leader_dna"),
        (else_try),
          # Talk to enemy leaders                    
          (assign, ":break", 0),
          
          (try_for_range, ":stack_no", "$last_defeated_hero", ":num_stacks"),
            (eq, ":break", 0),
            (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
            (party_stack_get_troop_dna,   ":stack_troop_dna","p_encountered_party_backup",":stack_no"),
            
            (troop_is_hero, ":stack_troop"),
            (store_add, "$last_defeated_hero", ":stack_no", 1),
        
            (call_script, "script_remove_troop_from_prison", ":stack_troop"),
                                    
            (troop_set_slot, ":stack_troop", slot_troop_leaded_party, -1),
            (store_troop_faction, ":defeated_faction", ":stack_troop"),
            #steve post 0912 changes begin - removed, this is duplicated elsewhere in game menus
            #(call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":stack_troop", ":defeated_faction"),
            (try_begin),
              (call_script, "script_cf_check_hero_can_escape_from_player", ":stack_troop"),
              (neq, reg0, 1),
              (neq, ":stack_troop", "trp_oim_zagloba_qst"),                             
              (str_store_troop_name, s1, ":stack_troop"),
              (str_store_faction_name, s3, ":defeated_faction"),
              (str_store_string, s17, "@{s1} of {s3} managed to escape."),
              (display_log_message, "@{s17}"),
              (jump_to_menu, "mnu_enemy_slipped_away"),
              (assign, ":break", 1),			  
			(else_try),			  			  			
			  (neq, ":stack_troop", "trp_oim_zagloba_qst"), 
			  
			  (try_begin),
                (store_random_in_range, ":rand", 0, 100),
			    (lt, ":rand", "$g_strength_contribution_of_player"),

                (assign, "$talk_context", tc_hero_defeated),			  
                (call_script, "script_setup_troop_meeting",":stack_troop", ":stack_troop_dna"),
                (assign, ":break", 1),
			  (else_try),
                (troop_set_slot, ":stack_troop", slot_troop_prisoner_of_party, "$g_ally_party"),
                (party_force_add_prisoners, "$g_ally_party", ":stack_troop", 1),#take prisoner
			    #(str_store_troop_name, s1, ":stack_troop"),
			    #(display_message, "@{s1} is catched by allies."),
			  (try_end),
            (try_end),
          (try_end),          
                  
          (eq, ":break", 1),          
        (else_try),
          # Talk to freed heroes
          (assign, ":break", 0),
          (party_get_num_prisoner_stacks, ":num_prisoner_stacks", "p_collective_enemy"),
          (try_for_range, ":stack_no", "$last_freed_hero", ":num_prisoner_stacks"),
            (eq, ":break", 0),
            (party_prisoner_stack_get_troop_id, ":stack_troop", "p_collective_enemy", ":stack_no"),
            (troop_is_hero, ":stack_troop"),
            (party_prisoner_stack_get_troop_dna, ":stack_troop_dna", "p_collective_enemy", ":stack_no"),
            (store_add, "$last_freed_hero", ":stack_no", 1),
            (assign, "$talk_context", tc_hero_freed),
            (call_script, "script_setup_troop_meeting", ":stack_troop", ":stack_troop_dna"),
            (assign, ":break", 1),
          (try_end),
          (eq, ":break", 1),          
        (else_try),       
          (eq, "$capture_screen_shown", 0),
          (assign, "$capture_screen_shown", 1),
          (party_clear, "p_temp_party"),
          (assign, "$g_move_heroes", 0),
          #(call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_collective_enemy"),

          #p_total_enemy_casualties deki yarali askerler p_temp_party'e prisoner olarak eklenecek.
          (call_script, "script_party_add_wounded_members_as_prisoners", "p_temp_party", "p_total_enemy_casualties"),

          (call_script, "script_party_add_party_prisoners", "p_temp_party", "p_collective_enemy"),          
          (try_begin),
            (call_script, "script_party_calculate_strength", "p_collective_friends_backup",0),
            (assign,":total_initial_strength", reg(0)),
            (gt, ":total_initial_strength", 0),
            #(gt, "$g_ally_party", 0),
            (call_script, "script_party_calculate_strength", "p_main_party_backup",0),
            (assign,":player_party_initial_strength", reg(0)),
            # move ally_party_initial_strength/(player_party_initial_strength + ally_party_initial_strength) prisoners to ally party.
            # First we collect the share of prisoners of the ally party and distribute those among the allies.
            (store_sub, ":ally_party_initial_strength", ":total_initial_strength", ":player_party_initial_strength"),

            #(call_script, "script_party_calculate_strength", "p_ally_party_backup"),
            #(assign,":ally_party_initial_strength", reg(0)),
            #(store_add, ":total_initial_strength", ":player_party_initial_strength", ":ally_party_initial_strength"),
            (store_mul, ":ally_share", ":ally_party_initial_strength", 1000),
            (val_div, ":ally_share", ":total_initial_strength"),
            (assign, "$pin_number", ":ally_share"), #we send this as a parameter to the script.
            (party_clear, "p_temp_party_2"),
            (call_script, "script_move_members_with_ratio", "p_temp_party", "p_temp_party_2"),
        
            #TODO: This doesn't handle prisoners if our allies joined battle after us.
            (try_begin),
              (gt, "$g_ally_party", 0),
              (distribute_party_among_party_group, "p_temp_party_2", "$g_ally_party"),
            (try_end),
            #next if there's anything left, we'll open up the party exchange screen and offer them to the player.
          (try_end),
          (party_get_num_companions, ":num_rescued_prisoners", "p_temp_party"),
          (party_get_num_prisoners,  ":num_captured_enemies", "p_temp_party"),

          (store_add, ":total_capture_size", ":num_rescued_prisoners", ":num_captured_enemies"),
          
          (gt, ":total_capture_size", 0),
          (change_screen_exchange_with_party, "p_temp_party"),
      (else_try),
		(eq, "$after_capture_screen_shown", 0),
		(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
		(             party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
        	(assign, "$after_capture_screen_shown", 1),
			(party_get_num_prisoners,  ":num_captured_enemies", "p_temp_party"),
			(try_begin),
				(gt, ":num_captured_enemies", 0),
				(eq, 0, 1),
				(assign, reg0, ":num_captured_enemies"),
				(str_store_string, s17, "@ V gorode ostalos {reg0} vragov, zahvachenih v plen. Chto vi hotite sdelat?"),
				(jump_to_menu, "mnu_captured_enemy_menu"),
			(else_try),
				(jump_to_menu, "mnu_total_victory"),
			(try_end),
		(else_try),
		(eq, "$after_capture_screen_shown_1", 0),
		(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
		(             party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
        	(assign, "$after_capture_screen_shown_1", 1),
			(party_get_num_companions, ":num_rescued_prisoners", "p_temp_party"),
          	(try_begin),
				(gt, ":num_rescued_prisoners", 0),
				(eq, 0, 1),
				(assign, reg0, ":num_rescued_prisoners"),
				(str_store_string, s17, "@ V gorode ostalos {reg0} osvobozhdennih plennikov. Zhelaete naznachit ih v garnizon zahvachenogo goroda?"),
				(jump_to_menu, "mnu_capture_prisoners_as_guards"),
			(else_try),
				(jump_to_menu, "mnu_total_victory"),
			(try_end),
		(else_try),
          (eq, "$loot_screen_shown", 0),
          (assign, "$loot_screen_shown", 1),
          #(try_begin),
          #  (gt, "$g_ally_party", 0),
          #  (call_script, "script_party_add_party", "$g_ally_party", "p_temp_party"), #Add remaining prisoners to ally TODO: FIX it.
          #(else_try),
          #  (party_get_num_attached_parties, ":num_quick_attachments", "p_main_party"),
          #  (gt, ":num_quick_attachments", 0),
          #  (party_get_attached_party_with_rank, ":helper_party", "p_main_party", 0),
          #  (call_script, "script_party_add_party", ":helper_party", "p_temp_party"), #Add remaining prisoners to our reinforcements
          #(try_end),
          (troop_clear_inventory, "trp_temp_troop"),
          (call_script, "script_party_calculate_loot", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties
          (gt, reg0, 0),
          (troop_sort_inventory, "trp_temp_troop"),
          (change_screen_loot, "trp_temp_troop"),
        (else_try),
          #finished all
          (try_begin),
            (le, "$g_ally_party", 0),
            (end_current_battle),
          (try_end),
          (call_script, "script_party_give_xp_and_gold", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties
          (try_begin),
            (eq, "$g_enemy_party", 0),
            (display_message,"str_error_string"),
          (try_end),
          (call_script, "script_event_player_defeated_enemy_party", "$g_enemy_party"),
          (call_script, "script_clear_party_group", "$g_enemy_party"),
  			(try_begin), 
				(eq, "$g_oim_fight_with_king", 1),
				(assign, "$g_next_menu", "mnu_oim_potop_fight_with_king_result"), 
			(end_try), 

		(try_begin), 
			(check_quest_active, "qst_oim_alevtina_hanum"),
			(neg|check_quest_succeeded, "qst_oim_alevtina_hanum"),
			(neg|check_quest_finished,"qst_oim_alevtina_hanum"),
			(quest_slot_ge, "qst_oim_alevtina_hanum", slot_quest_current_state, 1),
			(quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_target_center, "$g_encountered_party"),
			#(quest_set_slot, "qst_oim_alevtina_hanum", slot_quest_current_state, 10),
			(assign, "$oim_auto_talk_troop", "trp_alevtina"), 
			(assign, "$g_next_menu", "mnu_oim_auto_talk_menu"),
		(end_try),
		
		(try_begin), 
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
			(             party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
			(quest_slot_eq, "qst_oim_potop_main", slot_quest_current_state, 12),
			(assign, "$g_center_to_give_to_player", "$current_town"),
			(quest_set_slot, "qst_oim_potop_main", slot_quest_current_state, 13),
			(call_script, "script_succeed_quest", "qst_oim_potop_capture_city"),
			(assign, "$g_next_menu", "mnu_requested_castle_granted_to_player"), 
		(try_end),	

		(try_begin),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
			(             party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
			(check_quest_active,"qst_oim_getman_hmel_casus_beli"),
			(neg|check_quest_succeeded,"qst_oim_getman_hmel_casus_beli"),
			(quest_slot_eq, "qst_oim_getman_hmel_casus_beli", slot_quest_current_state, 1),			
			(neg|check_quest_finished,"qst_oim_getman_hmel_casus_beli"),
			(eq, "$g_encountered_party_faction", "fac_kingdom_2"), 
			(quest_set_slot, "qst_oim_getman_hmel_casus_beli", slot_quest_current_state, 2),	
			(try_begin), 
				(call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_5", "fac_kingdom_2", 1),					
				(call_script, "script_troop_add_gold", "trp_player", 5000),
				(add_xp_as_reward, 6000),
			(end_try), 
			(call_script, "script_oim_restore_player_to_faction", "fac_kingdom_5"),
		(end_try),	
		(try_begin),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
			(             party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
			(check_quest_active,"qst_oim_getman_barabash_casus_beli"),
			(neg|check_quest_succeeded,"qst_oim_getman_barabash_casus_beli"),
			(quest_slot_eq, "qst_oim_getman_barabash_casus_beli", slot_quest_current_state, 1),			
			(neg|check_quest_finished,"qst_oim_getman_barabash_casus_beli"),
			(eq, "$g_encountered_party_faction", "fac_kingdom_1"), 
			(quest_set_slot, "qst_oim_getman_barabash_casus_beli", slot_quest_current_state, 2),	
			(try_begin), 
				(call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_5", "fac_kingdom_1", 1),					
				(call_script, "script_troop_add_gold", "trp_player", 5000),
				(add_xp_as_reward, 6000),
			(end_try), 
			(call_script, "script_oim_restore_player_to_faction", "fac_kingdom_5"),
		(try_end), 
		  
          #(call_script, "script_event_player_defeated_enemy_party", "$g_enemy_party"),
          (call_script, "script_clear_party_group", "$g_enemy_party"),
          (try_begin),
            (eq, "$g_next_menu", -1),

            #NPC companion changes begin
            (call_script, "script_post_battle_personality_clash_check"),
            #NPC companion changes end

            #Post 0907 changes begin
            (party_stack_get_troop_id, ":enemy_leader", "p_encountered_party_backup",0),
            (try_begin),
            (is_between, ":enemy_leader", kingdom_heroes_begin, kingdom_heroes_end),
              (neg|is_between, "$g_encountered_party", centers_begin, centers_end),
              (store_troop_faction, ":enemy_leader_faction", ":enemy_leader"),

              (try_begin),
                (eq, "$g_ally_party", 0),
                (call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":enemy_leader", ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@Victory comment. Player was alone"),
                (try_end),
              (else_try),
                (ge, "$g_strength_contribution_of_player", 40), 
                (call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":enemy_leader", ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@Ordinary victory comment. The player provided at least 40 percent forces."),
                (try_end),
              (else_try),
                (gt, "$g_starting_strength_enemy_party", 1000),
                (call_script, "script_get_closest_center", "p_main_party"),
                (assign, ":battle_of_where", reg0),
                (call_script, "script_add_log_entry", logent_player_participated_in_major_battle, "trp_player",  ":battle_of_where", -1, ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@Player participation comment. The enemy had at least 1k starting strength."),
                (try_end),
              (else_try),
                (eq, "$cheat_mode", 1),
                (display_message, "@No victory comment. The battle was small, and the player provided less than 40 percent of allied strength"),
              (try_end),
            (try_end),
            #Post 0907 changes end
            (val_add, "$g_total_victories", 1),
            (leave_encounter),
            (change_screen_return),
          (else_try),
                (jump_to_menu, "$g_next_menu"),
                  (try_end),
                  (try_end),
                  
      ],
    [
      ("continue",[],"Continue...",[]),
        ]
  ),

  (
    "enemy_slipped_away",0,"{s17}",
    "none",
    [],
    [
      ("continue",[],"Continue...",[(jump_to_menu,"mnu_total_victory")]),
    ]
  ),

  (
    "total_defeat",0,"You shouldn't be reading this...",
    "none",
    [
        (play_track, "track_captured", 1),
           # Free prisoners
          (party_get_num_prisoner_stacks, ":num_prisoner_stacks","p_main_party"),
          (try_for_range, ":stack_no", 0, ":num_prisoner_stacks"),
            (party_prisoner_stack_get_troop_id, ":stack_troop","p_main_party",":stack_no"),
            (troop_is_hero, ":stack_troop"),
            (call_script, "script_remove_troop_from_prison", ":stack_troop"),
          (try_end),

          (call_script, "script_loot_player_items", "$g_enemy_party"),

          (assign, "$g_move_heroes", 0),
          (party_clear, "p_temp_party"),
          (call_script, "script_party_add_party_prisoners", "p_temp_party", "p_main_party"),
          (call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_main_party"),
          (distribute_party_among_party_group, "p_temp_party", "$g_enemy_party"),
        
          (call_script, "script_party_remove_all_companions", "p_main_party"),
          (assign, "$g_move_heroes", 1),
          (call_script, "script_party_remove_all_prisoners", "p_main_party"),

          (val_add, "$g_total_defeats", 1),

          (try_begin),
            (neq, "$g_player_surrenders", 1),
            (store_random_in_range, ":random_no", 0, 100),
            (ge, ":random_no", "$g_player_luck"),
            (jump_to_menu, "mnu_permanent_damage"),
          (else_try),
            (try_begin),
              (eq, "$g_next_menu", -1),
              (leave_encounter),
              (change_screen_return),
            (else_try),
              (jump_to_menu, "$g_next_menu"),
            (try_end),
          (try_end),
          (try_begin),
            (gt, "$g_ally_party", 0),
            (call_script, "script_party_wound_all_members", "$g_ally_party"),
          (try_end),

#Troop commentary changes begin
          (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
            (is_between, ":stack_troop", kingdom_heroes_begin, kingdom_heroes_end),
            (store_troop_faction, ":victorious_faction", ":stack_troop"),
            (call_script, "script_add_log_entry", logent_player_defeated_by_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
          (try_end),
	  (try_begin), 
		(eq, "$g_oim_fight_with_king", 1),
		(jump_to_menu, "mnu_oim_potop_fight_with_king_result"), 
	  (end_try), 
#Troop commentary changes end

      ],
    []
  ),

  (
    "permanent_damage",mnf_disable_all_keys,"{s0}",
    "none",
    [
      (assign, ":end_cond", 1),
      (try_for_range, ":unused", 0, ":end_cond"),
        (store_random_in_range, ":random_attribute", 0, 4),
        (store_attribute_level, ":attr_level", "trp_player", ":random_attribute"),
        (try_begin),
          (gt, ":attr_level", 3),
          (neq, ":random_attribute", ca_charisma),
          (try_begin),
            (eq, ":random_attribute", ca_strength),
            (str_store_string, s0, "@Some of your tendons have been damaged in the battle. You lose 1 strength."),
          (else_try),
            (eq, ":random_attribute", ca_agility),
            (str_store_string, s0, "@You took a nasty wound which will cause you to limp slightly even after it heals. Your lose 1 agility."),
##          (else_try),
##            (eq, ":random_attribute", ca_charisma),
##            (str_store_string, s0, "@After the battle you are aghast to find that one of the terrible blows you suffered has left a deep, disfiguring scar on your face, horrifying those around you. Your charisma is reduced by 1."),
          (else_try),
##            (eq, ":random_attribute", ca_intelligence),
            (str_store_string, s0, "@You have trouble thinking straight after the battle, perhaps from a particularly hard hit to your head, and frequent headaches now plague your existence. Your intelligence is reduced by 1."),
          (try_end),
        (else_try),
          (lt, ":end_cond", 200),
          (val_add, ":end_cond", 1),
        (try_end),
      (try_end),
      (try_begin),
        (eq, ":end_cond", 200),
        (try_begin),
          (eq, "$g_next_menu", -1),
          (leave_encounter),
          (change_screen_return),
        (else_try),
          (jump_to_menu, "$g_next_menu"),
        (try_end),
      (else_try),
        (troop_raise_attribute, "trp_player", ":random_attribute", -1),
      (try_end),
      ],
    [
      ("s0",
       [
         (store_random_in_range, ":random_no", 0, 4),
         (try_begin),
           (eq, ":random_no", 0),
           (str_store_string, s0, "@Perhaps I'm getting unlucky..."),
         (else_try),
           (eq, ":random_no", 1),
           (str_store_string, s0, "@Retirement is starting to sound better and better."),
         (else_try),
           (eq, ":random_no", 2),
           (str_store_string, s0, "@No matter! I will persevere!"),
         (else_try),
           (eq, ":random_no", 3),
           (troop_get_type, ":is_female", "trp_player"),
           (try_begin),
             (eq, ":is_female", 1),
             (str_store_string, s0, "@What did I do to deserve this?"),
           (else_try),
             (str_store_string, s0, "@I suppose it'll make for a good story, at least..."),
           (try_end),
         (try_end),
         ],"{s0}",
       [
         (try_begin),
           (eq, "$g_next_menu", -1),
           (leave_encounter),
           (change_screen_return),
         (else_try),
           (jump_to_menu, "$g_next_menu"),
         (try_end),
         ]),
      ]
  ),
  
  (
    "pre_join",0,"You arrive at a field where you see a battle raging between {s2} and {s1}. Whom shall you support?",
    "none",
    [
        (str_store_party_name, s1,"$g_encountered_party"),
        (str_store_party_name, s2,"$g_encountered_party_2"),
      ],
    [
      ("pre_join_help_attackers",[
          (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
          (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
          (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
          (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
          (ge, ":attacker_relation", 0),
          (lt, ":defender_relation", 0),
          ],"{s2}.",[
              (select_enemy,0),
              (assign,"$g_enemy_party","$g_encountered_party"),
              (assign,"$g_ally_party","$g_encountered_party_2"),
              (jump_to_menu,"mnu_join_battle")]),
      ("pre_join_help_defenders",[
          (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
          (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
          (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
          (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
          (ge, ":defender_relation", 0),
          (lt, ":attacker_relation", 0),
          ],"{s1}.",[
              (select_enemy,1),
              (assign,"$g_enemy_party","$g_encountered_party_2"),
              (assign,"$g_ally_party","$g_encountered_party"),
              (jump_to_menu,"mnu_join_battle")]),
      ("pre_join_talk",
	  [
	    (store_faction_of_party, ":defender_faction", "$g_encountered_party"),		
        (this_or_next|eq, ":defender_faction", "$players_kingdom"),
        (eq, ":defender_faction", "fac_player_faction"),		
		(party_slot_eq, "$g_encountered_party", slot_party_type, spt_kingdom_caravan),		
		(party_get_template_id, ":attacker_template", "$g_encountered_party_2"),
		(this_or_next|eq, ":attacker_template", "pt_deserters"),
		(this_or_next|eq, ":attacker_template", "pt_looters"),
		(this_or_next|eq, ":attacker_template", "pt_steppe_bandits"),
		(this_or_next|eq, ":attacker_template", "pt_forest_bandits"),
		(this_or_next|eq, ":attacker_template", "pt_mountain_bandits"),
		(eq, ":attacker_template", "pt_sea_raiders"),		
	  ],"Have a word with the attackers.",[	  
		
		 (party_stack_get_troop_id, ":bandit_leader", "$g_encountered_party_2", 0),
		 (party_stack_get_troop_dna, ":bandit_leader_dna", "$g_encountered_party_2", 0),
		 (assign,"$talk_context",tc_party_encounter),
		 #(assign, "$g_temp_encountered_party", "$g_encountered_party"),
		 (assign, "$g_encountered_party", "$g_encountered_party_2"),

         (store_faction_of_party, "$g_encountered_party_faction","$g_encountered_party"),
         (store_relation, "$g_encountered_party_relation", "$g_encountered_party_faction", "fac_player_faction"),
              
         (party_get_slot, "$g_encountered_party_type", "$g_encountered_party", slot_party_type),
         (party_get_template_id,"$g_encountered_party_template","$g_encountered_party"),

         (assign, "$talk_context", tc_bandit_talk),		  
        (call_script, "script_setup_troop_meeting",":bandit_leader", ":bandit_leader_dna"),		
	  ]),
      ("pre_join_leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "join_battle",0,"You ally with {s2} against {s1}, who prepare to attack you. You have {reg10} troops fit for battle, against the enemy's {reg11}.",
    "none",
    [
        (str_store_party_name, 1,"$g_enemy_party"),
        (str_store_party_name, 2,"$g_ally_party"),

        (call_script, "script_encounter_calculate_fit"),

        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_encounter_init_variables"),
        (else_try), #second or more turn
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (assign, ":num_enemy_regulars_remaining", reg0),
          (assign, ":enemy_finished",0),
          (try_begin),
            (eq, "$g_battle_result", 1), 
            
            (this_or_next|le, ":num_enemy_regulars_remaining", 0), #battle won
            (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
            
            (assign, ":enemy_finished",1),
          (else_try),
            (eq, "$g_engaged_enemy", 1),
            (le, "$g_enemy_fit_for_battle",0),
            (ge, "$g_friend_fit_for_battle",1),
            (assign, ":enemy_finished",1),
          (try_end),
          
          (this_or_next|eq, ":enemy_finished",1),
          (eq,"$g_enemy_surrenders",1),
          (assign, "$g_next_menu", -1),
          (jump_to_menu, "mnu_total_victory"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
          (assign, ":num_ally_regulars_remaining", reg0),
          (assign, ":battle_lost", 0),
          (try_begin),
            (eq, "$g_battle_result", -1),
            
            #(eq, ":num_ally_regulars_remaining", 0), #battle lost
            (le, ":num_ally_regulars_remaining",  "$num_routed_allies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
            
            (assign, ":battle_lost",1),
          (try_end),
          
          (this_or_next|eq, ":battle_lost",1),
          (eq,"$g_player_surrenders",1),
          (leave_encounter),
          (change_screen_return),
        (try_end),
      ],
    [
      ("join_attack",[
#          (neq, "$encountered_party_hostile", 0),
           (neg|troop_is_wounded, "trp_player"),
##          (store_troop_health,reg(5),"trp_player"),
##          (ge,reg(5),20),
          ],"Charge the enemy.",[
                                (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
                                (assign, "$g_battle_result", 0),
                                (call_script, "script_calculate_renown_value"),
                                (call_script, "script_calculate_battle_advantage"),
                                (set_battle_advantage, reg0),
                                (set_party_battle_mode),
                                (set_jump_mission,"mt_lead_charge"),
                                (call_script, "script_setup_random_scene"),
                                (assign, "$g_next_menu", "mnu_join_battle"),
                                (jump_to_menu, "mnu_battle_debrief"),
                                (change_screen_mission),
                                ]),

      ("join_order_attack",
      [
        (call_script, "script_party_count_members_with_full_health", "p_main_party"),
        (ge, reg0, 3),
          ],"Order your troops to attack with your allies while you stay back.",[(party_set_next_battle_simulation_time, "$g_encountered_party", -1),
                                                                         (jump_to_menu,"mnu_join_order_attack"),
                                                            ]),
      
#      ("join_attack",[],"Lead a charge against the enemies",[(set_jump_mission,"mt_charge_with_allies"),
#                                (call_script, "script_setup_random_scene"),
#                                                             (change_screen_mission,0)]),
      ("join_leave",[],"Leave.",[
        (try_begin),
           (neg|troop_is_wounded, "trp_player"),
           (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
           (party_stack_get_troop_id, ":enemy_leader","$g_enemy_party",0),
           (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":enemy_leader", -1),
           (display_message, "@Player retreats from battle"),
        (try_end),

          (leave_encounter),(change_screen_return)]),
    ]
  ),


  (
    "join_order_attack",mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
                                    (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
                                    (assign, ":player_party_strength", reg0),
                                    (val_div, ":player_party_strength", 5),
                                    (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
                                    (assign, ":friend_party_strength", reg0),
                                    (val_div, ":friend_party_strength", 5),
                                    
                                    (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
                                    (assign, ":enemy_party_strength", reg0),
                                    (val_div, ":enemy_party_strength", 5),

      (try_begin),
        (eq, ":friend_party_strength", 0),
        (store_div, ":enemy_party_strength_for_p", ":enemy_party_strength", 2),
      (else_try),
                                    (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
                                    (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
                                    (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
      (try_end),

                                    (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
                                    (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
                                    (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
                                    (str_store_string_reg, s8, s0),
                                    
                                    (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
                                    
      #ozan begin
      (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"), 
      (try_for_range, ":stack_no", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"), 
        (try_begin),
          (party_stack_get_size, ":stack_size", "p_temp_casualties", ":stack_no"),
          (gt, ":stack_size", 0),
          (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
          (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties", ":stack_no"),                                    
          (gt, ":stack_wounded_size", 0),
          (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
        (try_end),
      (try_end),
      #ozan end

                                    (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
                                    (str_store_string_reg, s10, s0),
                                    
                                    (call_script, "script_collect_friendly_parties"),
                                    #(party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),

                                    (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
                                    (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
                                    (str_store_string_reg, s9, s0),
                                    (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

                                    #(assign, "$cant_leave_encounter", 0),
                                    (assign, "$no_soldiers_left", 0),
                                    (try_begin),
                                      (call_script, "script_party_count_members_with_full_health","p_main_party"),
         (assign, ":num_our_regulars_remaining", reg0),
                                      
         #(le, ":num_our_regulars_remaining", 0),
         (le, ":num_our_regulars_remaining", "$num_routed_us"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
                                      
                                      (assign, "$no_soldiers_left", 1),
                                      (str_store_string, s4, "str_join_order_attack_failure"),
                                    (else_try),
                                      (call_script, "script_party_count_members_with_full_health","p_collective_enemy"),
         (assign, ":num_enemy_regulars_remaining", reg0),

         (this_or_next|le, ":num_enemy_regulars_remaining", 0),
         (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

                                      (assign, "$g_battle_result", 1),
                                      (assign, "$no_soldiers_left", 1),
                                      (str_store_string, s4, "str_join_order_attack_success"),
                                    (else_try),
                                      (str_store_string, s4, "str_join_order_attack_continue"),
                                    (try_end),
    ],
    [
      ("continue",[],"Continue...",
      [
          (jump_to_menu,"mnu_join_battle"),
          ]),
    ]
  ),

  
# Towns
  (
    "zendar",mnf_auto_enter,"You enter the town of Zendar.",
    "none",
    [(reset_price_rates,0),(set_price_rate_for_item,"itm_tools",70),(set_price_rate_for_item,"itm_salt",140)],
    [
      ("zendar_enter",[]," ",[(set_jump_mission,"mt_town_default"),(jump_to_scene,"scn_zendar_center"),(change_screen_mission)],"Go to the town center."),
      ("zendar_tavern",[]," ",[(set_jump_mission,"mt_town_default"),
                                                   (jump_to_scene,"scn_the_happy_boar"),
                                                   (change_screen_mission)],"Enter the tavern."),
      ("zendar_merchant",[]," ",[(set_jump_mission,"mt_town_default"),
                                                   (jump_to_scene,"scn_zendar_merchant"),
                                                   (change_screen_mission)],"Visit the merchant."),
      ("zendar_arena",[]," ",[(set_jump_mission,"mt_town_default"),
                                                   (jump_to_scene,"scn_zendar_arena"),
                                                   (change_screen_mission)],"Enter the arena."),
#      ("zendar_leave",[],"Leave town.",[[leave_encounter],[change_screen_return]]),
      ("town_1_leave",[]," ",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "salt_mine",mnf_auto_enter,"You enter the salt mine.",
    "none",
    [(reset_price_rates,0),(set_price_rate_for_item,"itm_salt",55)],
    [
      ("enter",[],"Enter.",[(set_jump_mission,"mt_town_center"),(jump_to_scene,"scn_salt_mine"),(change_screen_mission)]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "four_ways_inn",mnf_auto_enter,"You arrive at the Four Ways Inn.",
    "none",
    [],
    [

#      ("enter",[],"Enter.",[[set_jump_mission,"mt_town_default"],[jump_to_scene,"scn_meeting_scene_plain_forest"],[change_screen_mission]]),
      ("enter",[],"Enter.",[(set_jump_mission,"mt_camera_test"),(jump_to_scene,"scn_four_ways_inn"),(change_screen_mission)]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "test_scene",mnf_auto_enter,"You enter the test scene.",
    "none",
    [],
    [

      ("enter",[],"Enter.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_test_scene"],[change_screen_mission]]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "battlefields",0,"Select a field...",
    "none",
    [],
    [

      ("enter_f1",[],"Field 1",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_1"],[change_screen_mission]]),
      ("enter_f2",[],"Field 2",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_2"],[change_screen_mission]]),
      ("enter_f3",[],"Field 3",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_3"],[change_screen_mission]]),
      ("enter_f4",[],"Field 4",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_4"],[change_screen_mission]]),
      ("enter_f5",[],"Field 5",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_5"],[change_screen_mission]]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "dhorak_keep",0,"You enter Dhorak Keep.",
    "none",
    [],
    [
      ("enter",[],"Enter.",[(set_jump_mission,"mt_town_center"),(jump_to_scene,"scn_dhorak_keep"),(change_screen_mission)]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  
##  (
##    "center_under_attack_while_resting",0,
##    "{s1} has been besieged by {s2}, and the enemy seems to be preparing for an assault!\
## What will you do?",
##    "none",
##    [
##        (party_get_battle_opponent, ":besieger_party", "$auto_enter_town"),
##        (str_store_party_name, s1, "$auto_enter_town"),
##        (str_store_party_name, s2, ":besieger_party"),
##    ],
##    [
##      ("defend_against_siege", [],"Help the defenders of {s1}!",
##       [
##           (assign, "$g_last_player_do_nothing_against_siege_next_check", 0),
##           (rest_for_hours, 0, 0, 0),
##           (change_screen_return),
##           (start_encounter, "$auto_enter_town"),
##           ]),
##      ("do_not_defend_against_siege",[],"Find a secure place and wait there.",
##       [
##           (change_screen_return),
##           ]),
##    ]
##  ),

  (
    "join_siege_outside",mnf_scale_picture,"{s1} has come under siege by {s2}.",
    "none",
    [
        (str_store_party_name, s1, "$g_encountered_party"),
        (str_store_party_name, s2, "$g_encountered_party_2"),
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
    ],
    [
      ("approach_besiegers",[(store_faction_of_party, ":faction_no", "$g_encountered_party_2"),
                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             (ge, ":relation", 0),
                             (store_faction_of_party, ":faction_no", "$g_encountered_party"),
                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             (lt, ":relation", 0),
                             ],"Approach the siege camp.",[
          (jump_to_menu, "mnu_besiegers_camp_with_allies"),
                                ]),
      ("pass_through_siege",[(store_faction_of_party, ":faction_no", "$g_encountered_party"),
                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             (ge, ":relation", 0),
                             ],"Pass through the siege lines and enter {s1}.",
       [
            (jump_to_menu,"mnu_cut_siege_without_fight"),
          ]),
      ("leave",[],"Leave.",[(leave_encounter),
                            (change_screen_return)]),
    ]
  ),
  (
    "cut_siege_without_fight",0,"The besiegers allow you to approach the gates without challenge.",
    "none",
    [],
    [
      ("continue",[],"Continue...",[(try_begin),
                                   (this_or_next|eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
                                   (eq, "$g_encountered_party_faction", "$players_kingdom"),
                                   (jump_to_menu, "mnu_town"),
                                 (else_try),
                                   (jump_to_menu, "mnu_castle_outside"),
                                 (try_end)]),
      ]
  ),
  (
    "besiegers_camp_with_allies",0,"{s1} remains under siege. The banners of {s2} fly above the camp of the besiegers, where you and your men are welcomed.",
    "none",
    [
        (str_store_party_name, s1, "$g_encountered_party"),
        (str_store_party_name, s2, "$g_encountered_party_2"),
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", "$g_encountered_party_2"),
        (select_enemy, 0),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_encounter_init_variables"),
        (try_end),

        (try_begin),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (else_try),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1),
            (assign, ":enemy_finished", 1),
          (else_try),
            (le, "$g_enemy_fit_for_battle", 0),
            (ge, "$g_friend_fit_for_battle", 1),
            (assign, ":enemy_finished", 1),
          (try_end),
          (this_or_next|eq, ":enemy_finished", 1),
          (eq, "$g_enemy_surrenders", 1),
##          (assign, "$g_next_menu", -1),#"mnu_castle_taken_by_friends"),
##          (jump_to_menu, "mnu_total_victory"),
          (call_script, "script_party_wound_all_members", "$g_enemy_party"),
          (leave_encounter),
          (change_screen_return),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),          
          (assign, ":ally_num_soldiers", reg0),
          (eq, "$g_battle_result", -1),
          (eq, ":ally_num_soldiers", 0), #battle lost
          (leave_encounter),
          (change_screen_return),
        (try_end),
        ],
    [
      ("talk_to_siege_commander",[],"Request a meeting with the commander.",[
                                (modify_visitors_at_site,"scn_meeting_scene_plain_forest"),(reset_visitors),
                                (set_visitor,0,"trp_player"),
                                (party_stack_get_troop_id, ":siege_leader_id","$g_encountered_party_2",0),
                                (party_stack_get_troop_dna,":siege_leader_dna","$g_encountered_party_2",0),
                                (set_visitor,17,":siege_leader_id",":siege_leader_dna"),
                                (set_jump_mission,"mt_conversation_encounter"),
                                (jump_to_scene,"scn_meeting_scene_plain_forest"),
                                (assign, "$talk_context", tc_siege_commander),
                                (change_screen_map_conversation, ":siege_leader_id")]),
								
      ("join_siege_with_allies",[(neg|troop_is_wounded, "trp_player")],"Join the next assault.",
       [
           (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
           (try_begin),
             (check_quest_active, "qst_join_siege_with_army"),
             (quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
             (add_xp_as_reward, 250),
             (call_script, "script_end_quest", "qst_join_siege_with_army"),
             #Reactivating follow army quest
             (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
             (str_store_troop_name_link, s9, ":faction_marshall"),
             (setup_quest_text, "qst_follow_army"),
             (str_store_string, s2, "@{s9} wants you to follow his army until further notice."),
             (call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
             (assign, "$g_player_follow_army_warnings", 0),
           (try_end),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
           (try_end),
           (call_script, "script_calculate_battle_advantage"),
           (val_mul, reg0, 2),
           (val_div, reg0, 3), #scale down the advantage a bit in sieges.
           (set_battle_advantage, reg0),
           (set_party_battle_mode),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_center_siege_with_belfry, 1),
             (set_jump_mission,"mt_castle_attack_walls_belfry"),
           (else_try),
             (call_script, "script_get_ladder_mission"),
			 (set_jump_mission, reg0),
           (try_end),
           (jump_to_scene,":battle_scene"),
           (assign, "$g_siege_final_menu", "mnu_besiegers_camp_with_allies"),
           (assign, "$g_siege_battle_state", 1),
           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
##           (assign, "$g_next_menu", "mnu_besiegers_camp_with_allies"),
           (jump_to_menu, "mnu_battle_debrief"),
           (change_screen_mission),
          ]),
      ("join_siege_stay_back", [(call_script, "script_party_count_members_with_full_health", "p_main_party"),
                                (ge, reg0, 3),
                                ],"Order your soldiers to join the next assault without you.",
       [
         (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
         (try_begin),
           (check_quest_active, "qst_join_siege_with_army"),
           (quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
           (add_xp_as_reward, 100),
           (call_script, "script_end_quest", "qst_join_siege_with_army"),
           #Reactivating follow army quest
           (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
           (str_store_troop_name_link, s9, ":faction_marshall"),
           (setup_quest_text, "qst_follow_army"),
           (str_store_string, s2, "@{s9} wants you to follow his army until further notice."),
           (call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
           (assign, "$g_player_follow_army_warnings", 0),
         (try_end),
         (jump_to_menu,"mnu_castle_attack_walls_with_allies_simulate")]),
      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),

  (
    "castle_outside",0,"You are outside {s2}.{s11} {s3} {s4}",
    "none",
    [
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (str_store_party_name, s2,"$g_encountered_party"),
        (call_script, "script_encounter_calculate_fit"),
        (assign,"$all_doors_locked",1),
        (assign, "$current_town","$g_encountered_party"),
        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_let_nearby_parties_join_current_battle", 1, 0),
          (call_script, "script_encounter_init_variables"),
          (assign, "$entry_to_town_forbidden",0),
          (assign, "$sneaked_into_town",0),
          (assign, "$town_entered", 0),
           #oim code
		   (assign, "$g_otrava", 0),
		   (assign, "$g_diversiya_proval", 0),
           #oim code end
#          (assign, "$waiting_for_arena_fight_result", 0),
          (assign, "$encountered_party_hostile", 0),
          (assign, "$encountered_party_friendly", 0),
          (try_begin),
            (gt, "$g_player_besiege_town", 0),
            (neq,"$g_player_besiege_town","$g_encountered_party"),
            (party_slot_eq, "$g_player_besiege_town", slot_center_is_besieged_by, "p_main_party"),
            (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
            (assign,"$g_player_besiege_town",-1),
          (try_end),
          (try_begin),
            (lt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_hostile", 1),
            (assign,"$entry_to_town_forbidden",1),
          (try_end),

          (assign,"$cant_sneak_into_town",0),
          (try_begin),
            (eq,"$current_town","$last_sneak_attempt_town"),
            (store_current_hours,reg(2)),
            (val_sub,reg(2),"$last_sneak_attempt_time"),
            (lt,reg(2),12),
            (assign,"$cant_sneak_into_town",1),
          (try_end),
        (else_try), #second or more turn
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        (str_clear,s4),
        (try_begin), 
          (eq,"$entry_to_town_forbidden",1),
          (try_begin),
            (eq,"$cant_sneak_into_town",1),
            (str_store_string,s4,"str_sneaking_to_town_impossible"),
          (else_try),
            (str_store_string,s4,"str_entrance_to_town_forbidden"),
          (try_end),
        (try_end),

        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9,":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),			

        (try_begin), # same mnu_town
          (party_slot_eq,"$current_town",slot_party_type, spt_castle),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the castle gate."),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the castle gate."),
          (else_try),
            (str_store_string,s11,"@ This castle seems to belong to no one."),
          (try_end),
        (else_try),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the town gates."),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the town gates."),
          (else_try),
            (str_store_string,s11,"@ The townsfolk here have declared their independence."),
          (try_end),
        (try_end),

        (party_get_num_companions, reg(7),"p_collective_enemy"),
        (assign,"$castle_undefended",0),
        (str_clear, s3),
        (try_begin),
          (eq,reg(7),0),
          (assign,"$castle_undefended",1),
          (str_store_string, s3, "str_castle_is_abondened"),
        (else_try),
          (eq,"$g_encountered_party_faction","fac_player_supporters_faction"),
          (str_store_string, s3, "str_place_is_occupied_by_player"),
        (else_try),
          (lt, "$g_encountered_party_relation", 0),
          (str_store_string, s3, "str_place_is_occupied_by_enemy"),
        (else_try),
#          (str_store_string, s3, "str_place_is_occupied_by_friendly"),
        (try_end),

        (try_begin),
          (eq, "$g_leave_town_outside",1),
          (assign, "$g_leave_town_outside",0),
          (assign, "$g_permitted_to_center", 0),
          (change_screen_return),
        (else_try),
          (check_quest_active, "qst_escort_lady"),
          (quest_slot_eq, "qst_escort_lady", slot_quest_target_center, "$g_encountered_party"),
          (quest_get_slot, ":quest_object_troop", "qst_escort_lady", slot_quest_object_troop),
          (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
          (modify_visitors_at_site,":meeting_scene"),
          (reset_visitors),
          (set_visitor,0, "trp_player"),
          (set_visitor,17, ":quest_object_troop"),
          (set_jump_mission, "mt_conversation_encounter"),
          (jump_to_scene, ":meeting_scene"),
          (assign, "$talk_context", tc_entering_center_quest_talk),
          (change_screen_map_conversation, ":quest_object_troop"),
        (else_try),
          (check_quest_active, "qst_kidnapped_girl"),
          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_giver_center, "$g_encountered_party"),
          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 3),
          (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
          (modify_visitors_at_site,":meeting_scene"),
          (reset_visitors),
          (set_visitor,0, "trp_player"),
          (set_visitor,17, "trp_kidnapped_girl"),
          (set_jump_mission, "mt_conversation_encounter"),
          (jump_to_scene, ":meeting_scene"),
          (assign, "$talk_context", tc_entering_center_quest_talk),
          (change_screen_map_conversation, "trp_kidnapped_girl"),
##        (else_try),
##          (gt, "$lord_requested_to_talk_to", 0),
##          (store_current_hours, ":cur_hours"),
##          (neq, ":cur_hours", "$quest_given_time"),
##          (modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
##          (reset_visitors),
##          (assign, ":cur_lord", "$lord_requested_to_talk_to"),
##          (assign, "$lord_requested_to_talk_to", 0),
##          (set_visitor,0,"trp_player"),
##          (set_visitor,17,":cur_lord"),
##          (set_jump_mission,"mt_conversation_encounter"),
##          (jump_to_scene,"scn_meeting_scene_plain_forest"),
##          (assign, "$talk_context", tc_castle_gate_lord),
##          (change_screen_map_conversation, ":cur_lord"),
        (else_try),
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
          (jump_to_menu,"mnu_town"),
        (else_try),
          (party_slot_eq,"$g_encountered_party", slot_town_lord, "trp_player"),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),                    
          (jump_to_menu, "mnu_enter_your_own_castle"),
        (else_try),
          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_castle),
          (ge, "$g_encountered_party_relation", 0),
          (this_or_next|eq,"$castle_undefended", 1),
          (eq, "$g_permitted_to_center",1),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_town),
          (ge, "$g_encountered_party_relation", 0),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (eq, "$g_player_besiege_town", "$g_encountered_party"),
          (jump_to_menu, "mnu_castle_besiege"),
        (try_end),

        (try_begin),
##          (eq, "$g_center_under_siege_battle", 1),
##          (jump_to_menu,"mnu_siege_started_defender"),
##        (else_try),
          (eq, "$g_town_assess_trade_goods_after_rest", 1),
          (assign, "$g_town_assess_trade_goods_after_rest", 0),
          (jump_to_menu,"mnu_town_trade_assessment"),
        (try_end),		
		
		(try_begin),
			(call_script, "script_ms_store_remour_descr_to_s21"),
		(try_end),
        ],
    [
#        ("talk_to_castle_commander",[
#            (party_get_num_companions, ":no_companions", "$g_encountered_party"),
#            (ge, ":no_companions", 1),
#            (eq,"$ruler_meeting_denied",0), #this variable is removed
#            ],
#         "Request a meeting with the lord of the castle.",[
#             (modify_visitors_at_site,"scn_meeting_scene_plain_forest"),(reset_visitors),
#             (set_visitor,0,"trp_player"),
#             (party_stack_get_troop_id, reg(6),"$g_encountered_party",0),
#             (party_stack_get_troop_dna,reg(7),"$g_encountered_party",0),
#             (set_visitor,17,reg(6),reg(7)),
#             (set_jump_mission,"mt_conversation_encounter"),
#             (jump_to_scene,"scn_meeting_scene_plain_forest"),
#             (assign, "$talk_context", tc_castle_commander),
#             (change_screen_map_conversation, reg(6))
#             ]),
      ("approach_gates",[(this_or_next|eq,"$entry_to_town_forbidden",1),
                          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_castle)],"Approach the gates and hail the guard.",[
                                                  (jump_to_menu, "mnu_castle_guard"),
##                                                   (modify_visitors_at_site,"scn_meeting_scene_plain_forest"),(reset_visitors),
##                                                   (set_visitor,0,"trp_player"),
##                                                   (store_faction_of_party, ":cur_faction", "$g_encountered_party"),
##                                                   (faction_get_slot, ":cur_guard", ":cur_faction", slot_faction_guard_troop),
##                                                   (set_visitor,17,":cur_guard"),
##                                                   (set_jump_mission,"mt_conversation_encounter"),
##                                                   (jump_to_scene,"scn_meeting_scene_plain_forest"),
##                                                   (assign, "$talk_context", tc_castle_gate),
##                                                   (change_screen_map_conversation, ":cur_guard")
                                                   ]),
      
      ("town_sneak",[
					 (call_script, "script_kill_radzivill_sneak_condition"), 
					 (assign, ":condition", reg0), 
					 (this_or_next|party_slot_eq,"$g_encountered_party", slot_party_type,spt_town),
					 (             eq, ":condition", 1), 
                     (eq,"$entry_to_town_forbidden",1),
                     (eq,"$cant_sneak_into_town",0)],"Disguise yourself and try to sneak into the town.",
        [
          (try_begin),
			(check_quest_active, "qst_oim_getman_kill_radzivill"), 
			(neg|check_quest_succeeded, "qst_oim_getman_kill_radzivill"), 
			(neg|check_quest_finished,"qst_oim_getman_kill_radzivill"),
			(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 0),
			(call_script, "script_get_troop_attached_party", "trp_kingdom_1_pretender"), 
			(assign, ":cur_center", reg0),
			(eq, ":cur_center", "$g_encountered_party"), 
			(call_script, "script_cf_oim_check_radzivil_sneak_in"), 
			(jump_to_menu, "mnu_oim_getman_sneack_in"), 
          (else_try),  
         (faction_get_slot, ":player_alarm", "$g_encountered_party_faction", slot_faction_player_alarm),
         (party_get_num_companions, ":num_men", "p_main_party"),
         (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
         (val_add, ":num_men", ":num_prisoners"),
         (val_mul, ":num_men", 2),
         (val_div, ":num_men", 3),
         (store_add, ":get_caught_chance", ":player_alarm", ":num_men"),
         (store_random_in_range, ":random_chance", 0, 100),
         (try_begin),
           (this_or_next|ge, ":random_chance", ":get_caught_chance"),
           (eq, "$g_last_defeated_bandits_town", "$g_encountered_party"),
           (assign, "$g_last_defeated_bandits_town", 0),
           (assign, "$sneaked_into_town",1),
           (assign, "$town_entered", 1),
           (jump_to_menu,"mnu_sneak_into_town_suceeded"),
         (else_try),
           (jump_to_menu,"mnu_sneak_into_town_caught"),
			(try_end),
		(end_try),  
         ]),
         
      ("castle_start_siege",
       [
           (this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
           (             party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
           (store_relation, ":reln", "$g_encountered_party_faction", "fac_player_supporters_faction"),
           (lt, ":reln", 0),
           (lt, "$g_encountered_party_2", 1),
           (call_script, "script_party_count_fit_for_battle","p_main_party"),
           (gt, reg(0), 5),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (assign, reg6, 1),
           (else_try),
             (assign, reg6, 0),
           (try_end),
           ],"Besiege the {reg6?town:castle}.",
       [
	 
         (assign,"$g_player_besiege_town","$g_encountered_party"),
         (store_relation, ":relation", "fac_player_supporters_faction", "$g_encountered_party_faction"),
         (val_min, ":relation", -40),
         (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":relation"),
         (call_script, "script_update_all_notes"),
         (jump_to_menu, "mnu_castle_besiege"),
         ]),

#oim code
      ("talk_to_pafnutiy_menu",
       [
		(check_quest_active, "qst_oim_getman_voron_translate"),
		(neg|check_quest_finished,"qst_oim_getman_voron_translate"),
		(quest_slot_eq, "qst_oim_getman_voron_translate", slot_quest_current_state, 1), 
		(eq, "$current_town", "p_castle_6"),
           ],"Talk to Pafnuty.",
       [
		(assign, "$oim_auto_talk_troop", "trp_oim_getman_pafnutiy"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
   ]),
   
      ("talk_to_borzobogataya",[
			(check_quest_active,"qst_oim_potop_volodievskiy"),
			(neg|check_quest_finished,"qst_oim_potop_volodievskiy"),
			(quest_slot_eq, "qst_oim_potop_volodievskiy", slot_quest_current_state, 3),
			(quest_slot_eq, "qst_oim_potop_volodievskiy", slot_quest_target_center, "$g_encountered_party"),
   ],"Talk to Anusia.",
       [
			(party_get_slot, ":castle_scene", "$g_encountered_party", slot_town_castle),
			(modify_visitors_at_site, ":castle_scene"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,"trp_knight_1_2_wife"),
			(jump_to_scene, ":castle_scene"),
			(change_screen_map_conversation, "trp_knight_1_2_wife"),  
        ], "Talk to Anusia."),		
   
   
   #castle_22
      ("talk_to_ransom_broker",
       [
		(eq, "$current_town", "p_castle_22"),
           ],"Talk to the slaver.",
       [
		(assign, "$oim_auto_talk_troop", "trp_ransom_broker_1"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
   ]),
   
      ("talk_to_pafnutiy_dlg",[
			#code
			(check_quest_active, "qst_oim_getman_voron_translate"),
			(check_quest_succeeded, "qst_oim_getman_voron_translate"),
			(neg|check_quest_finished,"qst_oim_getman_voron_translate"),
			(quest_slot_eq, "qst_oim_getman_voron_translate", slot_quest_current_state, 3), 
			(quest_slot_eq, "qst_oim_getman_voron_translate", slot_quest_target_center, "$current_town"), 
  ],"Talk to Pafnuty.",[
			#code 
			(assign, "$oim_auto_talk_troop", "trp_oim_getman_pafnutiy"), 
			(jump_to_menu, "mnu_oim_auto_talk_menu"),
			(finish_mission),
			(music_set_situation, 0),
          ],"Talk to Pafnuty."),

#oim code end	 
		
      ("Edit_scenes",[
		(eq, debug_mode, 1),
  ],"{!}Edit scenes",[
			(jump_to_menu, "mnu_oim_edit_scenes_in_this_town"),  
          ],"{!}Edit_scenes"),

		

      ("cheat_castle_start_siege",
       [
         (eq, "$cheat_mode", 1),
         (this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
         (             party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
         (store_relation, ":reln", "$g_encountered_party_faction", "fac_player_supporters_faction"),
         (ge, ":reln", 0),
         (lt, "$g_encountered_party_2", 1),
         (call_script, "script_party_count_fit_for_battle","p_main_party"),
         (gt, reg(0), 1),
         (try_begin),
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
           (assign, reg6, 1),
         (else_try),
           (assign, reg6, 0),
         (try_end),
           ],"{!}CHEAT: Besiege the {reg6?town:castle}...",
       [
           (assign,"$g_player_besiege_town","$g_encountered_party"),
           (jump_to_menu, "mnu_castle_besiege"),
           ]),

      ("castle_leave",[],"Leave.",[(change_screen_return,0)]),
      ("castle_cheat_interior",[(eq, "$cheat_mode", 1)],"{!}CHEAT! Interior.",[(set_jump_mission,"mt_ai_training"),
                                                       (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
                                                       (jump_to_scene,":castle_scene"),
                                                       (change_screen_mission)]),
      ("castle_cheat_exterior",[(eq, "$cheat_mode", 1)],"{!}CHEAT! Exterior.",[
#                                                       (set_jump_mission,"mt_town_default"),
                                                       (set_jump_mission,"mt_ai_training"),
                                                       (party_get_slot, ":castle_scene", "$current_town", slot_castle_exterior),
                                                       (jump_to_scene,":castle_scene"),
                                                       (change_screen_mission)]),
      ("castle_cheat_town_walls",[(eq, "$cheat_mode", 1),(party_slot_eq,"$current_town",slot_party_type, spt_town),],"{!}CHEAT! Town Walls.",
       [
         (party_get_slot, ":scene", "$current_town", slot_town_walls),
         (set_jump_mission,"mt_ai_training"),
         (jump_to_scene,":scene"),
         (change_screen_mission)]),

    ]
  ),
   (
    "castle_guard",0,"You approach the gate. The men on the walls watch you closely.",
    "none",
    [
    ],
    [
      ("request_shelter",[(party_slot_eq, "$g_encountered_party",slot_party_type, spt_castle),
                          (ge, "$g_encountered_party_relation", 0)],"Request entry into the fortress.",
       [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
        (try_begin),
          (lt, ":castle_lord", 0),
          (jump_to_menu, "mnu_castle_entry_granted"),
        (else_try),
          (call_script, "script_troop_get_player_relation", ":castle_lord"),
          (assign, ":castle_lord_relation", reg0),
          #(troop_get_slot, ":castle_lord_relation", ":castle_lord", slot_troop_player_relation),
          (try_begin),
            (gt, ":castle_lord_relation", -15),
            (jump_to_menu, "mnu_castle_entry_granted"),
          (else_try),
            (jump_to_menu, "mnu_castle_entry_denied"),
          (try_end),
        (try_end),
       ]),
      ("request_meeting_commander",[
		(neg|check_quest_active, "qst_oim_potop_execute_king"),
	  ],"Request a meeting with someone.",
       [
          (jump_to_menu, "mnu_castle_meeting"),
       ]),
      ("guard_leave",[],"Leave.",
       [(change_screen_return,0)]),
    ]
  ),
  (
    "castle_entry_granted",0,"After a brief wait, the guards open the gates, and allow your party inside.",
    "none",
    [

    ],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu,"mnu_town")]),
    ]
  ),
  (
    "castle_entry_denied",0,"The lord of this fortress has forbidden you from entering these walls, and the guard sergeant informs you that his men will fire if you attempt to come any closer.",
    "none",
    [
    ],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu,"mnu_castle_guard")]),
    ]
  ),
  (
    "castle_meeting",0,"With whom do you want to meet?",
    "none",
    [
        (assign, "$num_castle_meeting_troops", 0),
        (try_for_range, ":troop_no", kingdom_heroes_begin, kingdom_heroes_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (call_script, "script_get_troop_attached_party", ":troop_no"),
          (eq, "$g_encountered_party", reg0),
          (troop_set_slot, "trp_temp_array_a", "$num_castle_meeting_troops", ":troop_no"),
          (val_add, "$num_castle_meeting_troops", 1),
        (try_end),
    ],
    [
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 0),(troop_get_slot, ":troop_no", "trp_temp_array_a", 0),(str_store_troop_name, s5, ":troop_no")],"{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 0),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 1),(troop_get_slot, ":troop_no", "trp_temp_array_a", 1),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 1),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 2),(troop_get_slot, ":troop_no", "trp_temp_array_a", 2),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 2),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 3),(troop_get_slot, ":troop_no", "trp_temp_array_a", 3),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 3),(jump_to_menu,"mnu_castle_meeting_selected")]),
      
      ("forget_it",[],"Forget it.",
       [(jump_to_menu,"mnu_castle_guard")]),
    ]
  ),
  (
    "castle_meeting_selected",0,"Your request for a meeting is relayed inside, and finally {s6} appears in the courtyard to speak with you.",
    "none",
    [(str_store_troop_name, s6, "$castle_meeting_selected_troop")],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu, "mnu_castle_outside"),
        (modify_visitors_at_site,"scn_meeting_scene_plain_forest"),(reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,17,"$castle_meeting_selected_troop"),
        (set_jump_mission,"mt_conversation_encounter"),
        (jump_to_scene,"scn_meeting_scene_plain_forest"),
        (assign, "$talk_context", tc_castle_gate),
        (change_screen_map_conversation, "$castle_meeting_selected_troop"),
        ]),
    ]
  ),


   (
    "castle_besiege",mnf_scale_picture,"You are laying siege to {s1}. {s2} {s3}",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
        (assign, "$g_siege_force_wait", 0),
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
          (party_set_slot, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
          (store_current_hours, ":cur_hours"),
          (party_set_slot, "$g_encountered_party", slot_center_siege_begin_hours, ":cur_hours"),
          (assign, "$g_siege_method", 0),
          (assign, "$g_siege_sallied_out_once", 0),
        (try_end),

        (party_get_slot, ":town_food_store", "$g_encountered_party", slot_party_food_store),
        (call_script, "script_center_get_food_consumption", "$g_encountered_party"),
        (assign, ":food_consumption", reg0),
        (assign, reg7, ":food_consumption"),
        (assign, reg8, ":town_food_store"),
        (store_div, reg3, ":town_food_store", ":food_consumption"),

        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (assign, reg6, 1),
        (else_try),
          (assign, reg6, 0),
        (try_end),
        
        (try_begin),
          (gt, reg3, 0),
          (str_store_string, s2, "@Zapasov edi v {reg6?gorode:zamke} hvatit esche {reg3} dney."),
        (else_try),
          (str_store_string, s2, "@Zapasov edi v {reg6?gorode:zamke} zakonchilis i zaschitniki golodayut."),
        (try_end),

        (str_store_string, s3, "str_empty_string"),
        (try_begin),
          (ge, "$g_siege_method", 1),
          (store_current_hours, ":cur_hours"),
          (try_begin),
            (lt, ":cur_hours",  "$g_siege_method_finish_hours"),
            (store_sub, reg9, "$g_siege_method_finish_hours", ":cur_hours"),
            (try_begin),
              (eq, "$g_siege_method", 1),
              (str_store_string, s3, "@Vi stroite lestnici dly shturma. Do konca robot ostalos {reg9} chasov."),
            (else_try),
              (eq, "$g_siege_method", 2),
              (str_store_string, s3, "@Prokladka podkopa dlya razmescheniya minu zavershitsya cherez {reg9} chasov."),
            (try_end),
          (else_try),
            (try_begin),
              (eq, "$g_siege_method", 1),
              (str_store_string, s3, "@Postroika lestnic zavershena. Vi mozhete nachat ataku v luboe vremya."),
            (else_try),
              (eq, "$g_siege_method", 2),
              (str_store_string, s3, "@Postroika podkopa zavershena. Vi mozhete vzorvat minu i nachat ataku v luboe vremya."),
            (try_end),
          (try_end),
        (try_end),
        
        #Check if enemy leaves the castle to us...
        (try_begin),
          (eq, "$g_castle_left_to_player",1), #we come here after dialog. Empty the castle and send parties away.
          (assign, "$g_castle_left_to_player",0),
          (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
          (party_set_faction,"$g_encountered_party","fac_neutral"), #temporarily erase faction so that it is not the closest town
          (party_get_num_attached_parties, ":num_attached_parties_to_castle","$g_encountered_party"),
          (try_for_range_backwards, ":iap", 0, ":num_attached_parties_to_castle"),
            (party_get_attached_party_with_rank, ":attached_party", "$g_encountered_party", ":iap"),
            (party_detach, ":attached_party"),
            (party_get_slot, ":attached_party_type", ":attached_party", slot_party_type),
            (eq, ":attached_party_type", spt_kingdom_hero_party),
            (store_faction_of_party, ":attached_party_faction", ":attached_party"),
            (call_script, "script_get_closest_walled_center_of_faction", ":attached_party", ":attached_party_faction"),
            (try_begin),
              (gt, reg0, 0),
              (call_script, "script_party_set_ai_state", ":attached_party", spai_holding_center, reg0),
            (else_try),
              (call_script, "script_party_set_ai_state", ":attached_party", spai_patrolling_around_center, "$g_encountered_party"),
            (try_end),
          (try_end),
          (call_script, "script_party_remove_all_companions", "$g_encountered_party"),
          (change_screen_return),
          (party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"), #recalculate so that
          (call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"), #leaving troops will not be considered as captured
          (party_set_faction,"$g_encountered_party",":castle_faction"), 
        (try_end),

        #Check for victory or defeat....
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (str_store_party_name, 1,"$g_encountered_party"),
        (call_script, "script_encounter_calculate_fit"),
        
        (assign, reg11, "$g_enemy_fit_for_battle"),
        (assign, reg10, "$g_friend_fit_for_battle"),


        (try_begin),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (else_try),
          (call_script, "script_party_count_fit_regulars","p_collective_enemy"),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1),
            (assign, ":enemy_finished", 1),
          (else_try),
            (le, "$g_enemy_fit_for_battle", 0),
            (ge, "$g_friend_fit_for_battle", 1),
            (assign, ":enemy_finished", 1),
          (try_end),
          (this_or_next|eq, ":enemy_finished", 1),
          (eq, "$g_enemy_surrenders", 1),
          (assign, "$g_next_menu", "mnu_castle_taken"), 
          (jump_to_menu, "mnu_total_victory"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (assign, ":main_party_fit_regulars", reg(0)),
          (eq, "$g_battle_result", -1),
          (eq, ":main_party_fit_regulars", 0), #all lost
          (assign, "$g_next_menu", "mnu_captivity_start_castle_defeat"),
          (jump_to_menu, "mnu_total_defeat"),
        (try_end),
		#(call_script, "script_replace_shturm_item_end"),
    ],
    [
    ("build_ladders",[
		(try_begin),
			(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
			(assign, ":koef", reg0),
			(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
			(val_add, ":koef", reg0),
		(try_end),
		
		(eq, "$g_siege_method", 0),
		(ge, ":koef", 0),
    ],"Prepare ladders to attack the walls.", [(jump_to_menu,"mnu_construct_ladders")]),
		
		
		
	("siege_request_meeting",
	[
		(this_or_next|eq, "$cant_talk_to_enemy", 0),
		(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
		(eq, "$g_siege_method", 0),
	],"Call for a meeting with the fortress commander.", 
	[
		(try_begin),
        (eq, "$g_otrava", 0),
		(eq, "$g_podkup", 0),
          (assign, "$cant_talk_to_enemy", 1),
          (assign, "$g_enemy_surrenders",0),
          (assign, "$g_castle_left_to_player",0),
          (assign, "$talk_context", tc_castle_commander),
          (party_get_num_attached_parties, ":num_attached_parties_to_castle","$g_encountered_party"),
          (try_begin),
            (gt, ":num_attached_parties_to_castle", 0),
            (party_get_attached_party_with_rank, ":leader_attached_party", "$g_encountered_party", 0),
            (call_script, "script_setup_party_meeting", ":leader_attached_party"),
          (else_try),
            (call_script, "script_setup_party_meeting", "$g_encountered_party"),
          (try_end),
		(else_try),
	    (jump_to_menu,"mnu_podkup_neg"),
		(try_end),
           ]),
        
   
	("town_diversiya",
	[
		(party_slot_eq,"$g_encountered_party", slot_party_type,spt_town),
        (eq,"$entry_to_town_forbidden",1),
		(try_begin),
			(call_script, "script_get_max_skill_of_player_party", "skl_riding"),
			(assign, ":koef", reg0),
			(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
			(val_add, ":koef", reg0),
		(try_end),
		(eq, "$g_siege_method", 0),
		(eq, "$g_diversiya_proval", 0),
		(ge, ":koef", 3),
	],"Poison the city's water.",
    [
		(assign, ":menu_next", "mnu_vzvesili"),
		(try_begin),
			(store_random_in_range, ":random_chance", 0, 5),
			(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
			(assign, ":koef", reg0),
			(val_add, ":random_chance", ":koef"), 
			#OiM crab mode
			(options_get_campaign_ai, ":ai"),
			(try_begin), 
				(eq, ":ai", 2), 
				(val_add, ":random_chance", 2), 
			(else_try), 
				(eq, ":ai", 1), 
				(val_mul, ":random_chance", 1), 
			(end_try),
			#OiM crab mode end
			(try_begin),
				(ge, ":random_chance", 9),
				(assign, ":menu_next", "mnu_udral_otravil"),
				(assign, "$g_otrava", 1),
			(else_try),
				(ge, ":random_chance", 7),
				(assign, ":menu_next", "mnu_neudral_otravil"),
				(assign, "$g_otrava", 1),
			(else_try),
				(lt, ":random_chance", 5),
				(assign, ":menu_next", "mnu_neudral_neotravil"),
			(else_try),
				(assign, ":menu_next", "mnu_udral_neotravil"),
			(try_end),
		(try_end),
#		(try_begin),
#			(store_random_in_range, ":random_chance", 0, 100),
#			(ge, ":random_chance", 90),
#			(troop_set_health,"trp_player",0),
#			(assign, ":menu_next", "mnu_vzvesili"),
#		(try_end),
		(jump_to_menu,":menu_next"),
    ]),

    ("town_vorvatsya",
	[
		(party_slot_eq,"$g_encountered_party", slot_party_type,spt_town),
 		(try_begin),
			(call_script, "script_horse_fifty_percen_check"),
			(assign, ":kon", reg0),
		(try_end),
		(eq, "$g_siege_method", 0),			
		(eq, "$g_otrava", 0),
		(this_or_next|eq, ":kon", 1),
		(eq, "$players_kingdom","fac_kingdom_5"),
    ],"Attempt to break into the city.",
    [ 
		(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),				
		(assign, ":koef", reg0),				
		(store_random_in_range, ":random_chance", 0, 100),
		(val_add, ":koef", ":random_chance"),			
		(try_begin)	,
			(ge, ":koef", 30),
			(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),				
			(store_sub, ":koef", 100, reg0),
			(val_div, ":koef", 3),
			(call_script, "script_party_count_fit_for_battle", "$g_encountered_party"), 
			(assign, "$g_enemy_count", reg(0)),
			(val_mul, ":koef", "$g_enemy_count"),
			(val_div, ":koef", 100),
			(val_sub, "$g_enemy_count", ":koef"),
			(assign, ":menu_next", "mnu_vorvatsya_uspeh"),
			(assign, "$g_diversiya_proval", 0),
		(else_try),
			(assign, ":menu_next", "mnu_vorvatsya_proval"),
			(assign, "$g_diversiya_proval", 1),
		(try_end),
        (jump_to_menu,":menu_next"),
    ]),
      
    ("build_podkop",[ (eq, "$g_diversiya_proval", 0),(eq, "$g_siege_method", 0)],"Demolish the wall using an explosive.", [
		(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
		(assign, ":koef", reg0),
		(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
		(val_add, ":koef", reg0),
		
		#OiM crab mode
		(options_get_campaign_ai, ":ai"),
		(try_begin), 
			(eq, ":ai", 2), 
			(val_mul, ":koef", 3), 
			(val_div, ":koef", 4), 
		(end_try),
		#OiM crab mode end
		
		(try_begin),
			(ge, ":koef", 5),
			(jump_to_menu,"mnu_podkop_uspih"),
		(else_try),
			(jump_to_menu,"mnu_podkop_neg"),
		(try_end),
   ]),
      
      ("castle_lead_attack",
       [
         (neg|troop_is_wounded, "trp_player"),
         (eq, "$g_siege_method", 1),
         (gt, "$g_friend_fit_for_battle", 3),
         (store_current_hours, ":cur_hours"),
         (ge, ":cur_hours", "$g_siege_method_finish_hours"),
    ],"Lead your soldiers in an assault.", 
	[
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
		(end_try),	
           (call_script, "script_calculate_battle_advantage"),
           (assign, ":battle_advantage", reg0),
           (val_mul, ":battle_advantage", 2),
           (val_div, ":battle_advantage", 3), #scale down the advantage a bit in sieges.
           (set_battle_advantage, ":battle_advantage"),
           (set_party_battle_mode),
           (assign, "$g_siege_battle_state", 1),
           (assign, ":siege_sally", 0),
           (try_begin),
             (le, ":battle_advantage", -4), #we are outnumbered, defenders sally out
             (eq, "$g_siege_sallied_out_once", 0),
             (set_jump_mission,"mt_castle_attack_walls_defenders_sally"),
             (assign, "$g_siege_battle_state", 0),
             (assign, ":siege_sally", 1),
           (else_try),
             (party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
             (set_jump_mission,"mt_castle_attack_walls_belfry"),
           (else_try),
			(call_script, "script_get_ladder_mission"),
			 (set_jump_mission, reg0),
           (try_end),
		(assign, "$g_podkup", 0), 
           (assign, "$cant_talk_to_enemy", 0),           
           (assign, "$g_siege_final_menu", "mnu_castle_besiege"),
           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
        #(assign, "$g_siege_method", 0), #reset siege timer
		(call_script, "script_ms_before_attack", "$g_encountered_party", "p_main_party", "trp_player"),
		#(call_script, "script_replace_shturm_item_begin"),
           (jump_to_scene,":battle_scene"),
           (try_begin),
             (eq, ":siege_sally", 1),
             (jump_to_menu, "mnu_siege_attack_meets_sally"),
           (else_try),
             (jump_to_menu, "mnu_battle_debrief"),
             (change_screen_mission),
           (try_end),
       ]),
  
	 ("castle_lead_attack_podkop",
       [
         (neg|troop_is_wounded, "trp_player"),
         (eq, "$g_siege_method", 2),
         (gt, "$g_friend_fit_for_battle", 3),
         (store_current_hours, ":cur_hours"),
         (ge, ":cur_hours", "$g_siege_method_finish_hours"),
        ],"Commence the assault.", 
		[
		 (store_random_in_range, ":random_chance", 0, 100),
		 (try_begin),
				(gt, ":random_chance", town_assault_chanse),
				(assign, ":menu_next", "mnu_podkop_uspih_uspih"),
		 (else_try),
				(assign, ":menu_next", "mnu_podkop_uspih_neg"),
		 (try_end),
		 (jump_to_menu, ":menu_next"),
        ]),

  
      ("attack_stay_back",
       [
         (ge, "$g_siege_method", 1),
         (gt, "$g_friend_fit_for_battle", 3),
         (store_current_hours, ":cur_hours"),
         (ge, ":cur_hours",  "$g_siege_method_finish_hours"),
         ],"Order your soldiers to attack while you stay back...", [(assign, "$cant_talk_to_enemy", 0),(jump_to_menu,"mnu_castle_attack_walls_simulate")]),



      ("build_siege_tower",[ (neg|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),(eq, "$g_siege_method", 0)],"Build a siege tower.", [(jump_to_menu,"mnu_construct_siege_tower")]),

      ("cheat_castle_lead_attack",[ (neg|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),(eq, "$cheat_mode", 1),
                                   (eq, "$g_siege_method", 0)],"{!}CHEAT: Instant build equipments.",
       [
         (assign, "$g_siege_method", 1),
         (assign, "$g_siege_method_finish_hours", 0),
         (jump_to_menu, "mnu_castle_besiege"),
       ]),


     ("wait_24_hours",[],"Wait until tomorrow.", [
          (assign,"$auto_besiege_town","$g_encountered_party"),
          (assign, "$g_siege_force_wait", 1),
          (store_time_of_day,":cur_time_of_day"),
          (val_add, ":cur_time_of_day", 1),
          (assign, ":time_to_wait", 31),
          (val_sub,":time_to_wait",":cur_time_of_day"),
          (val_mod,":time_to_wait",24),
          (val_add, ":time_to_wait", 1),
          (rest_for_hours_interactive, ":time_to_wait", 5, 1), #rest while attackable
          (assign, "$cant_talk_to_enemy", 0),
          (change_screen_return),
       ]),

	   

      ("lift_siege",[],"Abandon the siege.",
       [
         (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
		 #(call_script, "script_replace_shturm_item_end"),
         (assign,"$g_player_besiege_town", -1),
         (change_screen_return)]),
    ]
  ),
  
  (
    "siege_attack_meets_sally",0,"The defenders come forth to meet your assault.",
    "none",
    [
    ],
    [
      ("continue",[],
       "Continue...",
       [
             (jump_to_menu, "mnu_battle_debrief"),
             (change_screen_mission),
       ]),
    ]
  ),

   (
    "castle_besiege_inner_battle",mnf_scale_picture,"{s1}",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
        (assign, ":result", "$g_battle_result"),#will be reset at script_encounter_calculate_fit
        (call_script, "script_encounter_calculate_fit"),
        
# TODO: To use for the future:
            (str_store_string, s1, "@As a last defensive effort, you retreat to the main hall of the keep.\
 You and your remaining soldiers will put up a desperate fight here. If you are defeated, there's no other place to fall back to."),
            (str_store_string, s1, "@You've been driven away from the walls.\
 Now the attackers are pouring into the streets. IF you can defeat them, you can perhaps turn the tide and save the day."),
        (try_begin),
          (this_or_next|neq, ":result", 1),
          (this_or_next|le, "$g_friend_fit_for_battle", 0),
          (le, "$g_enemy_fit_for_battle", 0),
          (jump_to_menu, "$g_siege_final_menu"),
        (else_try),
          (call_script, "script_encounter_calculate_fit"),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (try_begin),
            (eq, "$g_siege_battle_state", 0),
            (eq, ":result", 1),
            (assign, "$g_battle_result", 0),
            (jump_to_menu, "$g_siege_final_menu"),
          (else_try),
            (eq, "$g_siege_battle_state", 1),
            (eq, ":result", 1),
            (str_store_string, s1, "@You've breached the town walls,\
 but the stubborn defenders continue to resist you in the streets!\
 You'll have to deal with them before you can attack the keep at the heart of the town."),
          (else_try),
            (eq, "$g_siege_battle_state", 2),
            (eq, ":result", 1),
            (str_store_string, s1, "@The town centre is yours,\
 but the remaining defenders have retreated to the castle.\
 It must fall before you can complete your victory."),
          (else_try),
            (jump_to_menu, "$g_siege_final_menu"),
          (try_end),
        (else_try),
          (try_begin),
            (eq, "$g_siege_battle_state", 0),
            (eq, ":result", 1),
            (assign, "$g_battle_result", 0),
            (jump_to_menu, "$g_siege_final_menu"),
          (else_try),
            (eq, "$g_siege_battle_state", 1),
            (eq, ":result", 1),
            (str_store_string, s1, "@The remaining defenders have retreated to the castle as a last defense. You must go in and crush any remaining resistance."),
          (else_try),
            (jump_to_menu, "$g_siege_final_menu"),
          (try_end),
        (try_end),
    ],
    [
      ("continue",[],
       "Continue...",
       [
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (try_begin),
               (eq, "$g_siege_battle_state", 1),
               (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_center),
               (set_jump_mission, "mt_besiege_inner_battle_town_center"),
             (else_try),
               (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_castle),
               (set_jump_mission, "mt_besiege_inner_battle_castle"),
             (try_end),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_castle),
             (set_jump_mission, "mt_besiege_inner_battle_castle"),
           (try_end),
##           (call_script, "script_calculate_battle_advantage"),
##           (set_battle_advantage, reg0),
           (set_party_battle_mode),
           (jump_to_scene, ":battle_scene"),
           (val_add, "$g_siege_battle_state", 1),
           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
           (jump_to_menu, "mnu_battle_debrief"),
		   #(call_script, "script_replace_shturm_item_begin"),
		   (assign, "$g_siege_method", 0),
           (change_screen_mission),
       ]),
    ]
  ),

  
  (
    "construct_ladders",0,"You estimate that it will take {reg4} hours to build enough scaling ladders for the assault.",
    "none",
    [
		(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
		(assign, ":max_engineer_skill", reg0),
		(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
		(assign, ":max_tactics_skill", reg0),
		(store_add, ":max_skill", ":max_engineer_skill", ":max_tactics_skill"), 
		(store_sub, reg4, 20, ":max_skill"),
		(val_max, reg4, 6),		
        (try_begin),
		  (is_between, ":max_skill", 0, 3),
		  (str_store_string,s3,"@ kriticheskie"),
		(else_try),
		  (is_between, ":max_skill", 3, 7),
		  (str_store_string,s3,"@ ogromnie"),
		(else_try),
		  (str_store_string,s3,"@ visokie"),
        (try_end),
    ],[
      ("build_ladders_cont",[],"Do it.", 
	[
           (assign, "$g_siege_method", 1),		   
           (store_current_hours, ":cur_hours"),		   
           (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
		   (val_mul, reg0, 3),
		   (val_div, reg0, 2),
  		   (store_sub, ":hours_takes", 20, reg0),
	 	   (call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
		   (val_mul, reg0, 3),
		   (val_div, reg0, 2),
		   (val_sub, ":hours_takes", reg0),
		   (val_max, ":hours_takes", 6),
           (store_add, "$g_siege_method_finish_hours",":cur_hours", ":hours_takes"),
           (assign,"$auto_besiege_town","$current_town"),
           (rest_for_hours_interactive, ":hours_takes", 5, 1), #rest while attackable. A trigger will divert control when attack is ready.
           (change_screen_return),
    ]),

	("go_back_assault",[],"Consider another assault plan.", [(jump_to_menu,"mnu_castle_besiege")]),
   ],),
  
  (
    "construct_siege_tower",0,"As the best engineer in the party ({reg2} Engineering skill), {reg3?you estimate:{s3} estimates} that building a siege tower will take {reg4} hours.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),
     (store_sub, reg4, 15, ":max_skill"),
     (val_mul, reg4, 6),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
    ],
    [
      ("build_siege_tower_cont",[],"Start building.", [
           (assign, "$g_siege_method", 2),
           (store_current_hours, ":cur_hours"),
           (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
           (store_sub, ":hours_takes", 15, reg0),
           (val_mul, ":hours_takes", 6),
           (store_add, "$g_siege_method_finish_hours",":cur_hours", ":hours_takes"),
           (assign,"$auto_besiege_town","$current_town"),
           (rest_for_hours_interactive, 240, 5, 1), #rest while attackable. A trigger will divert control when attack is ready.
           (change_screen_return),
           ]),
      ("go_back_assault",[],
       "Consider another assault plan.", [(jump_to_menu,"mnu_castle_besiege")]),
        ],
  ),

   (
    "castle_attack_walls_simulate",mnf_scale_picture|mnf_disable_all_keys,"{s4}^^Your casualties:{s8}^^Enemy casualties: {s9}",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
        
        (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
        (assign, ":player_party_strength", reg0),
        (val_div, ":player_party_strength", 10),

        (call_script, "script_party_calculate_strength", "$g_encountered_party", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 4),

        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s8, s0),

        (inflict_casualties_to_party_group, "$g_encountered_party", ":player_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s9, s0),

        (assign, "$no_soldiers_left", 0),
        (try_begin),
          (call_script, "script_party_count_members_with_full_health","p_main_party"),
          (le, reg0, 0), #(sdsd = TODO : compare with num_routed_us)
          (assign, "$no_soldiers_left", 1),
          (str_store_string, s4, "str_attack_walls_failure"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health","$g_encountered_party"),
          (le, reg0, 0), #(sdsd = TODO : compare with num_routed_enemies)
          (assign, "$no_soldiers_left", 1),
          (assign, "$g_battle_result", 1),
          (str_store_string, s4, "str_attack_walls_success"),
        (else_try),
          (str_store_string, s4, "str_attack_walls_continue"),
        (try_end),
     ],
    [
##      ("lead_next_wave",[(eq, "$no_soldiers_left", 0)],"Lead the next wave of attack personally.", [
##           (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
##           (set_party_battle_mode),
##           (set_jump_mission,"mt_castle_attack_walls"),
##           (jump_to_scene,":battle_scene"),
##           (jump_to_menu,"mnu_castle_outside"),
##           (change_screen_mission),
##       ]),
##      ("continue_attacking",[(eq, "$no_soldiers_left", 0)],"Order your soldiers to keep attacking...", [
##                                    (jump_to_menu,"mnu_castle_attack_walls_3"),
##                                    ]),
##      ("call_soldiers_back",[(eq, "$no_soldiers_left", 0)],"Call your soldiers back.",[(jump_to_menu,"mnu_castle_outside")]),
      ("continue",[],"Continue...",[(jump_to_menu,"mnu_castle_besiege")]),
    ]
  ),
  
   (
    "castle_attack_walls_with_allies_simulate",mnf_scale_picture|mnf_disable_all_keys,"{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),

        (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
        (assign, ":player_party_strength", reg0),
        (val_div, ":player_party_strength", 10),
        (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
        (assign, ":friend_party_strength", reg0),
        (val_div, ":friend_party_strength", 10),

        (val_max, ":friend_party_strength", 1),

        (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 4),

##        (assign, reg0, ":player_party_strength"),
##        (assign, reg1, ":friend_party_strength"),
##        (assign, reg2, ":enemy_party_strength"),
##        (assign, reg3, "$g_enemy_party"),
##        (assign, reg4, "$g_ally_party"),
##        (display_message, "@player_str={reg0} friend_str={reg1} enemy_str={reg2}"),
##        (display_message, "@enemy_party={reg3} ally_party={reg4}"),

        (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
        (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
        (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
        (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),

        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s8, s0),
                                    
        (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s10, s0),

        (call_script, "script_collect_friendly_parties"),

        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s9, s0),

        (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

        (assign, "$no_soldiers_left", 0),
        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (le, reg0, 0),
          (assign, "$no_soldiers_left", 1),
          (str_store_string, s4, "str_attack_walls_failure"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (le, reg0, 0),
          (assign, "$no_soldiers_left", 1),
          (assign, "$g_battle_result", 1),
          (str_store_string, s4, "str_attack_walls_success"),
        (else_try),
          (str_store_string, s4, "str_attack_walls_continue"),
        (try_end),
     ],
    [
      ("continue",[],"Continue...",[(jump_to_menu,"mnu_besiegers_camp_with_allies")]),
    ]
  ),

  (
    "castle_taken_by_friends",0,"Nothing to see here.",
    "none",
    [
        (party_clear, "$g_encountered_party"),
        (party_stack_get_troop_id, ":leader", "$g_encountered_party_2", 0),
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, ":leader"),
        (store_troop_faction, ":faction_no", ":leader"),
        #Reduce prosperity of the center by 5		
        (call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
        (call_script, "script_give_center_to_faction", "$g_encountered_party", ":faction_no"),
        (call_script, "script_add_log_entry", logent_player_participated_in_siege, "trp_player",  "$g_encountered_party", 0, "$g_encountered_party_faction"),
##        (call_script, "script_change_troop_renown", "trp_player", 1),
        (change_screen_return),
    ],
    [
    ],
  ),


  (
    "castle_taken",mnf_disable_all_keys,"{s3} has fallen to your troops. You now have full control of the {reg2?town:fortress}. {reg1? It would seem that there is nothing stopping you from taking it for yourself...:}",# Only visible when castle is taken without being a vassal of a kingdom.
    "none",
    [
		(try_begin),
        (party_clear, "$g_encountered_party"),
        (call_script, "script_lift_siege", "$g_encountered_party", 0),
        (assign, "$g_player_besiege_town", -1),
        (call_script, "script_add_log_entry", logent_castle_captured_by_player, "trp_player",  "$g_encountered_party", 0, "$g_encountered_party_faction"),
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
        #Reduce prosperity of the center by 5		
        (call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
        (call_script, "script_change_troop_renown", "trp_player", 5),		
        (call_script, "script_add_log_entry", logent_castle_captured_by_player, "trp_player", "$g_encountered_party", -1, "$g_encountered_party_faction"),
  	    #(try_begin),
		#	(eq, "$g_encountered_party", "p_town_6"), 
		#	(check_quest_active, "qst_oim_potop_defend_church"),
		#	(neg|check_quest_finished,"qst_oim_potop_defend_church"),
		#	(call_script, "script_succeed_quest", "qst_oim_potop_defend_church"),
	    #(try_end),
        
        (try_begin),
          (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
          (neq, "$players_kingdom", "fac_player_supporters_faction"),
          (assign, "$g_ms_player_win", 1),
          (call_script, "script_give_center_to_faction", "$g_encountered_party", "$players_kingdom"),
          (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "$players_kingdom"),
          (jump_to_menu, "mnu_castle_taken_2"),
        (else_try),
			(try_begin), 
			(check_quest_active,"qst_oim_potop_defend_get_back_warshaw"),
			(neg|check_quest_succeeded,"qst_oim_potop_defend_get_back_warshaw"),
			(neg|check_quest_finished,"qst_oim_potop_defend_get_back_warshaw"),
			(eq, "$g_encountered_party", "p_town_6"),
			(call_script, "script_give_center_to_faction", "$g_encountered_party", "fac_kingdom_1"),
			(call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "fac_kingdom_1"),
			(jump_to_menu, "mnu_castle_taken_2"),
		(else_try), 
          (call_script, "script_give_center_to_faction", "$g_encountered_party", "fac_player_supporters_faction"),
          (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "fac_player_supporters_faction"),
          (str_store_party_name, s3, "$g_encountered_party"),
          (assign, reg1, 0),
          (try_begin),
            (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
            (assign, reg1, 1),
          (try_end),          
			(end_try), 
        (try_end),
        (assign, reg2, 0),
        (try_begin),
          (is_between, "$g_encountered_party", towns_begin, towns_end),
          (assign, reg2, 1),
        (try_end),
    ],
    [
      ("continue",[],"Continue...",
       [         
		(try_begin),
			(eq, "$spawn_enemies_true", 1),
			(call_script, "script_spawn_enemies_as_deserters"),
			(assign, "$spawn_enemies_true", 0),
		(try_end),
		(try_begin),
			(eq, "$spawn_prisioners_true", 1),
			(call_script, "script_spawn_prisioners_as_deserters"),
			(assign, "$spawn_prisioners_true", 0),
		(try_end),
		(try_begin),
			(eq, "$capture_prisioners_true", 1),
			(call_script, "script_capture_as_guards"),
			(assign, "$capture_prisioners_true", 0),
		(try_end),
		#(try_begin), 
		#	(quest_slot_eq, "qst_oim_potop_main", slot_quest_current_state, 12),
		#	(assign, "$g_center_to_give_to_player", "$current_town"),
		#	(quest_set_slot, "qst_oim_potop_main", slot_quest_current_state, 13),
		#	(call_script, "script_succeed_quest", "qst_oim_potop_capture_city"),
		#	(jump_to_menu, "mnu_requested_castle_granted_to_player"), 
		#(try_end),	
		#(try_begin), 
		#	(check_quest_active, "qst_oim_alevtina_hanum"),
		#	(neg|check_quest_succeeded, "qst_oim_alevtina_hanum"),
		#	(neg|check_quest_finished,"qst_oim_alevtina_hanum"),
		#	#(quest_slot_ge, "qst_oim_alevtina_hanum", slot_quest_current_state, 1),
		#	(quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_target_center, "$g_encountered_party"),
		#	#code
		#	
		#	(assign, "$oim_auto_talk_troop", "trp_alevtina"), 
		#	(jump_to_menu, "mnu_oim_auto_talk_menu"),
		#	(finish_mission),

			
			#(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
			#(reset_visitors),
			#(set_visitor,0,"trp_player"),
			#(set_visitor,17,"trp_alevtina"),
			#(jump_to_scene,"scn_meeting_scene_plain_forest"),
			#(change_screen_map_conversation, "trp_alevtina"),         
		#(else_try),
         (assign, "$auto_enter_town", "$g_encountered_party"),                  
         (change_screen_return),
		#(end_try), 	
        ]),
    ],        
  ),
  
  (
    "castle_taken_2",mnf_disable_all_keys,"{s3} has fallen to your troops. You now have full control of the location. Your troops celebrate the victory.",
    "none",
    [
        (str_store_party_name, s3, "$g_encountered_party"),
        (str_clear, s5),
        (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
		(try_begin), 
			(check_quest_active,"qst_oim_potop_defend_get_back_warshaw"),
			(neg|check_quest_succeeded,"qst_oim_potop_defend_get_back_warshaw"),
			(neg|check_quest_finished,"qst_oim_potop_defend_get_back_warshaw"),
			(eq, "$g_encountered_party", "p_town_6"), 
			(str_store_troop_name, s9, "trp_kingdom_1_lord"),
		(else_try), 
        (str_store_troop_name, s9, ":faction_leader"),
		(end_try), 	
        (try_begin),
          (eq, "$player_has_homage", 0),
          (assign, reg8, 0),
          (try_begin),
            (party_slot_eq, "$g_encountered_party", spt_town),
            (assign, reg8, 1),
          (try_end),
          (str_store_string, s5, "@However, since you are not a sworn {man/follower} of {s9}, there is no chance he would recognize you as the {lord/lady} of this {reg8?town:castle}."),
        (try_end),
		
    ],
    [
      ("castle_taken_claim",[
		(eq, "$player_has_homage", 1), 
		(neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
		#(neg|check_quest_active,"qst_oim_potop_defend_get_back_warshaw"),
		#(check_quest_succeeded,"qst_oim_potop_defend_get_back_warshaw"),
		#(check_quest_finished,"qst_oim_potop_defend_get_back_warshaw"),
      ],"Request that {s3} be awarded to you.",
        [
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
        (assign, "$auto_enter_town", "$g_encountered_party"),
		(try_begin),
		#	(quest_slot_eq, "qst_oim_potop_main", slot_quest_current_state, 12),
		#	(assign, "$g_center_to_give_to_player", "$current_town"),
		#	(quest_set_slot, "qst_oim_potop_main", slot_quest_current_state, 13),
		#	(call_script, "script_succeed_quest", "qst_oim_potop_capture_city"),
		#	(jump_to_menu, "mnu_requested_castle_granted_to_player"), 
		#(else_try), 
	        (assign, "$g_castle_requested_by_player", "$current_town"),
        (change_screen_return),
		(end_try), 		
        ]),
      ("castle_taken_no_claim",[],"Ask no reward...",
       [
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, -1),
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (call_script, "script_cf_reinforce_party", "$g_encountered_party"),
        (change_screen_return),
#        (jump_to_menu, "mnu_town"),
        ]),
		
      ("castle_taken_oim",[
		(faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
	  ],"Seize {s3} for yourself.",
       [
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, -1),
        (assign, "$auto_enter_town", "$g_encountered_party"),
		(call_script, "script_give_center_to_lord", "$g_encountered_party", "trp_player", 0),
        (change_screen_return),
        ]),
    ],
  ),

(
    "requested_castle_granted_to_player",mnf_scale_picture,"You receive a message from {s3}.^^ {reg4?She:He} has decided to grant {s2}{reg3? and the nearby village of {s4}:} to you, with all due incomes and titles, to hold in {reg4?her:his} name for as long as you maintain your oath of homage.",
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
		(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
		(str_store_troop_name, s3, ":faction_leader"),
		(str_store_party_name, s2, "$g_center_to_give_to_player"),
		(str_store_party_name, s12, "$g_center_to_give_to_player"), #somewhat change for polish translation bug
			(try_for_range, ":cur_village", villages_begin, villages_end),
				(party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
		(call_script, "script_give_center_to_faction_aux", ":cur_village", "$players_kingdom"),
		(party_set_slot, ":cur_village", slot_town_lord, stl_unassigned),
			(try_end),
		(try_begin),
			(party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
			(assign, reg3, 1),
			(try_for_range, ":cur_village", villages_begin, villages_end),
				(party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
				(str_store_party_name, s4, ":cur_village"),
			(try_end),
		(else_try),
			(assign, reg3, 0),
		(try_end),
		(troop_get_type, reg4, ":faction_leader"),
    ],
    [
		("continue",[],"Continue...",
			[
	    (assign, "$g_ms_player_win", 1),
	    (call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
        (jump_to_menu, "mnu_give_center_to_player_2"),
        ]),
			],
		),
  
(
    "requested_castle_granted_to_another",mnf_scale_picture,"You receive a message from {s3}.^^ 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts. You also requested that I give you ownership of the fortress, but that is a favor which I fear I cannot grant, as you already hold significant estates in my realm. Instead I have sent you {reg6} thaler to cover the expenses of your campaign, but {s2} I give to {s5}.' ",
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
     (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
     (str_store_troop_name, s3, ":faction_leader"),
     (str_store_party_name, s2, "$g_center_to_give_to_player"),
     (party_get_slot, ":new_owner", "$g_center_to_give_to_player", slot_town_lord),
     (str_store_troop_name, s5, ":new_owner"),
     (call_script, "script_troop_get_player_relation", ":faction_leader"),
     (assign, ":leader_rel", reg0),
	 (val_mul, ":leader_rel", 30), 
	 (val_min, ":leader_rel", 300),
     (assign, reg6, 900),
	 (val_add, reg6, ":leader_rel"),
    ],
    [
      ("accept_decision",[],"Accept the decision.",
       [
       (call_script, "script_troop_add_gold", "trp_player", reg6),
       (change_screen_return),
       ]),
      ("leave_faction",[],"You have been wronged! Renounce you oath to this sovereign! ",
       [
         (jump_to_menu, "mnu_leave_faction"),
         (call_script, "script_troop_add_gold", "trp_player", reg6),
        ]),
     ],
  ),

  (
    "leave_faction",0,
    "Renouncing your oath is a grave act. Your lord may condemn you, and confiscate your lands and holdings. However, if you relinquish them of your own free will, he may let the betrayal stand without a fight.",
    "none",
    [
    ],
    [
      ("leave_faction_give_back", [],"Renounce your oath and give up your holdings.",
       [
#Troop commentary changes begin
#        (call_script, "script_add_log_entry", logent_renounced_allegiance,   "trp_player",  -1, "$g_talk_troop", "$g_talk_troop_faction"),
#Troop commentary changes end
        (call_script, "script_player_leave_faction", 1),
        (change_screen_return),
        ]),
      ("leave_faction_hold", [
          (str_store_party_name, s2, "$g_center_to_give_to_player"),
          ],"Renounce your oath and hold on to your lands, including {s2}.",
       [
        (faction_get_slot, ":old_leader", "$players_kingdom", slot_faction_leader),
        (call_script, "script_add_log_entry", logent_renounced_allegiance,   "trp_player",  -1, ":old_leader", "$players_kingdom"),

        #Initializing renounce war variables
        (assign, "$players_oath_renounced_against_kingdom", "$players_kingdom"),
        (assign, "$players_oath_renounced_given_center", 0),
        (store_current_hours, "$players_oath_renounced_begin_time"),
        (assign, "$g_ms_player_win", 1),
        (call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
        (call_script, "script_player_leave_faction", 0),
        (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
          (store_faction_of_party, ":cur_center_faction", ":cur_center"),
          (party_set_slot, ":cur_center", slot_center_faction_when_oath_renounced, ":cur_center_faction"),
        (try_end),
        (party_set_slot, "$g_center_to_give_to_player", slot_center_faction_when_oath_renounced, "$players_oath_renounced_against_kingdom"),
        (change_screen_return),
        ]),
      ("leave_faction_cancel", [],"Remain loyal and accept the decision.",
       [
        (change_screen_return),
        ]),
    ],
  ),

  (
    "give_center_to_player",mnf_scale_picture,"Your lord offers to extend your fiefs! {s1} sends word that he is willing to grant {s2} to you in payment for your loyal service, adding it to your holdings. What will be your answer?",
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
     (store_faction_of_party, ":center_faction", "$g_center_to_give_to_player"),
     (faction_get_slot, ":faction_leader", ":center_faction", slot_faction_leader),
     (str_store_troop_name, s1, ":faction_leader"),
     (str_store_party_name, s2, "$g_center_to_give_to_player"),
    ],
    [
      ("give_center_to_player_accept",[],"Accept the offer.",
       [
	    (assign, "$g_ms_player_win", 1),
	    (call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
        (jump_to_menu, "mnu_give_center_to_player_2"),
        ]),
      ("give_center_to_player_reject",[],"Reject it. You have no interest in {s2}.",
       [(party_set_slot, "$g_center_to_give_to_player", slot_town_lord, stl_rejected_by_player),
        (change_screen_return),
        ]),
    ],
  ),
  
  (
    "give_center_to_player_2",0,"With a brief ceremony, you are officially confirmed as the new lord of {s2}{reg3? and its neighboring village {s4}:}. You can now claim rents and revenues from your personal estates there, draft soldiers from the populace, and manage the lands as you see fit. However, you will also be expected to defend your fief and its people from harm, as well as maintaining the rule of law and order.",
    "none",
    [
      (str_store_party_name, s2, "$g_center_to_give_to_player"),
      (assign, reg3, 0),
      (try_begin),
        (party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
        (try_for_range, ":cur_village", villages_begin, villages_end),
          (party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
          (str_store_party_name, s4, ":cur_village"),
          (assign, reg3, 1),
        (try_end),
      (try_end),
	  #
	  
    ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
    ],
  ),


  (
    "oath_fulfilled",0,"You had a contract with {s1} to serve him for a certain period of time. This contract has now expired. What will you do?",
    "none",
    [
      (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
      (str_store_troop_name, s1, ":faction_leader"),
     ],
    [
      ("renew_oath",[(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
                     (str_store_troop_name, s1, ":faction_leader")],"Renew your contract with {s1} for another month.",
       [
         (store_current_day, ":cur_day"),
         (store_add, "$mercenary_service_next_renew_day", ":cur_day", 30),
         (change_screen_return),
         ]),
      ("dont_renew_oath",[],"Walk away from your bond.",
       [
         (call_script, "script_player_leave_faction", 1),
         (change_screen_return),
         ]),
    ]
  ),
  

##  (
##    "castle_garrison_stationed",0,
###    "The rest of the castle garrison recognizes that their situation is hopeless and surrenders. {s1} is at your mercy now. What do you want to do with this castle?",
##    "_",
##    "none",
##    [
##        (jump_to_menu, "mnu_town"),
##    ],
##    [],
##  ),

##  (
##    "castle_choose_captain",0,
##    "You will need to assign one of your companions as the castellan. Who will it be?",
##    "none",
##    [
##        (try_for_range, ":slot_no", 0, 20),
##          (troop_set_slot, "trp_temp_troop", ":slot_no", 0),
##        (try_end),
##        (assign, ":num_captains", 0),
##        (party_clear, "p_temp_party"),
##        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
##        (try_for_range, ":i_s", 1,":num_stacks"),
##          (party_stack_get_troop_id, ":companion","p_main_party", ":i_s"),
##          (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
##          (troop_set_slot, "trp_temp_troop", ":num_captains", ":companion"),
##        (try_end),
##    ],
##    [
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 0),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 0),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 1),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 1),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 2),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 2),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 3),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 3),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 4),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 4),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 5),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 5),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 6),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 6),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 7),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 7),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 8),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 8),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 9),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 9),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 10),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 10),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 11),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 11),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 12),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 12),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 13),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 13),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 14),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 14),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 15),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 15),(jump_to_menu,"mnu_castle_captain_chosen")]),
##      
##      ("cancel",[],
##         "Cancel...",
##         [(jump_to_menu, "mnu_town")]),
##    ],
##  ),
##  (
##    "castle_captain_chosen",0,
##    "h this castle?",
##    "none",
##    [
##        (party_add_leader, "$g_encountered_party",  "$selected_castellan"),
##        (party_remove_members, "p_main_party", "$selected_castellan",1),
##        (party_set_slot, "$g_encountered_party", slot_town_lord, "trp_player"),
##        (party_set_faction, "$g_encountered_party", "fac_player_supporters_faction"),
##        (try_for_range, ":slot_no", 0, 20), #clear temp troop slots just in case
##          (troop_set_slot, "trp_temp_troop", ":slot_no", 0),
##        (try_end),
##        (jump_to_menu, "mnu_town"),
##        (change_screen_exchange_members,0),
##    ],
##    [],
##  ),

##  (
##    "under_siege_attacked_continue",0,
##    "Nothing to see here.",
##    "none",
##    [
##        (assign, "$g_enemy_party", "$g_encountered_party_2"),
##        (assign, "$g_ally_party", "$g_encountered_party"),
##        (party_set_next_battle_simulation_time, "$g_encountered_party", 0),
##        (call_script, "script_encounter_calculate_fit"),
##        (try_begin),
##          (call_script, "script_party_count_fit_regulars", "p_collective_enemy"),
##          (assign, ":num_enemy_regulars_remaining", reg(0)),
##          (assign, ":enemy_finished",0),
##          (try_begin),
##            (eq, "$g_battle_result", 1),
##            (eq, ":num_enemy_regulars_remaining", 0), #battle won
##            (assign, ":enemy_finished",1),
##          (else_try),
##            (eq, "$g_engaged_enemy", 1),
##            (le, "$g_enemy_fit_for_battle",0),
##            (ge, "$g_friend_fit_for_battle",1),
##            (assign, ":enemy_finished",1),
##          (try_end),
##          (this_or_next|eq, ":enemy_finished",1),
##          (eq,"$g_enemy_surrenders",1),
####          (assign, "$g_center_under_siege_battle", 0),
##          (assign, "$g_next_menu", -1),
##          (jump_to_menu, "mnu_total_victory"),
##        (else_try),
##          (assign, ":battle_lost", 0),
##          (try_begin),
##            (eq, "$g_battle_result", -1),
##            (assign, ":battle_lost",1),
##          (try_end),
##          (this_or_next|eq, ":battle_lost",1),
##          (eq,"$g_player_surrenders",1),
####          (assign, "$g_center_under_siege_battle", 0),
##          (assign, "$g_next_menu", "mnu_captivity_start_under_siege_defeat"),
##          (jump_to_menu, "mnu_total_defeat"),
##        (else_try),
##    # Ordinary victory.
##          (try_begin),
##          #check whether enemy retreats
##            (eq, "$g_battle_result", 1),
##            (store_mul, ":min_enemy_str", "$g_enemy_fit_for_battle", 2),
##            (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
##            (party_set_slot, "$g_enemy_party", slot_party_retreat_flag, 1),
##
##            (try_for_range, ":troop_no", kingdom_heroes_begin, kingdom_heroes_end),
##              (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
##              (troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
##              (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
##              (gt, ":party_no", 0),
##              (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
##              (party_slot_eq, ":party_no", slot_party_ai_object, "$g_encountered_party"),
##              (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
##              (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
##              (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
##            (try_end),
##            (display_message, "@TODO: Enemy retreated. The assault has ended, siege continues."),
##            (change_screen_return),
##          (try_end),
####          (assign, "$g_center_under_siege_battle", 0),
##        (try_end),
##        ],
##    [
##    ]
##  ),


  (
    "siege_started_defender",0,"{s1} is launching an assault against the walls of {s2}. You have {reg10} troops fit for battle against the enemy's {reg11}. What will be your decision?",
    "none",
    [
        (select_enemy,1),
        (assign, "$g_enemy_party", "$g_encountered_party_2"),
        (assign, "$g_ally_party", "$g_encountered_party"),
        (str_store_party_name, 1,"$g_enemy_party"),
        (str_store_party_name, 2,"$g_ally_party"),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$g_siege_first_encounter", 1),
          (call_script, "script_let_nearby_parties_join_current_battle", 0, 1),
          (call_script, "script_encounter_init_variables"),
        (try_end),

        (try_begin),
          (eq, "$g_siege_first_encounter", 0),
          (try_begin),
            (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
            (assign, ":num_enemy_regulars_remaining", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
            (assign, ":num_ally_regulars_remaining", reg0),
            (assign, ":enemy_finished", 0),
            (try_begin),
              (eq, "$g_battle_result", 1),
              (eq, ":num_enemy_regulars_remaining", 0), #battle won
              (assign, ":enemy_finished",1),
            (else_try),
              (eq, "$g_engaged_enemy", 1),
              (le, "$g_enemy_fit_for_battle",0),
              (ge, "$g_friend_fit_for_battle",1),
              (assign, ":enemy_finished",1),
            (try_end),
            (this_or_next|eq, ":enemy_finished",1),
            (eq,"$g_enemy_surrenders",1),
            (assign, "$g_next_menu", -1),
            (jump_to_menu, "mnu_total_victory"),
          (else_try),
            (assign, ":battle_lost", 0),
            (try_begin),
              (this_or_next|eq, "$g_battle_result", -1),
              (troop_is_wounded,  "trp_player"),
              (eq, ":num_ally_regulars_remaining", 0), #(sdsd = TODO : compare with num_routed_allies)
              (assign, ":battle_lost",1),
            (try_end),
            (this_or_next|eq, ":battle_lost",1),
            (eq,"$g_player_surrenders",1),
            (assign, "$g_next_menu", "mnu_captivity_start_under_siege_defeat"),
            (jump_to_menu, "mnu_total_defeat"),
          (else_try),
            # Ordinary victory/defeat.
            (assign, ":attackers_retreat", 0),
            (try_begin),
            #check whether enemy retreats
              (eq, "$g_battle_result", 1),
  ##            (store_mul, ":min_enemy_str", "$g_enemy_fit_for_battle", 2),
  ##            (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
              (assign, ":attackers_retreat", 1),
            (else_try),
              (eq, "$g_battle_result", 0),
              (store_div, ":min_enemy_str", "$g_enemy_fit_for_battle", 3),
              (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
              (assign, ":attackers_retreat", 1),
            (else_try),
              (store_random_in_range, ":random_no", 0, 100),
              (store_mul, ":num_ally_regulars_remaining_multiplied", ":num_ally_regulars_remaining", 13),
              (val_div, ":num_ally_regulars_remaining_multiplied", 10),
              (ge, ":num_ally_regulars_remaining_multiplied", ":num_enemy_regulars_remaining"),
              (lt, ":random_no", 10),
              (neq, "$new_encounter", 1),
              (assign, ":attackers_retreat", 1),
            (try_end),
            (try_begin),
              (eq, ":attackers_retreat", 1),
              (party_get_slot, ":siege_hardness", "$g_encountered_party", slot_center_siege_hardness),
              (val_add, ":siege_hardness", 100),
              (party_set_slot, "$g_encountered_party", slot_center_siege_hardness, ":siege_hardness"),
              (party_set_slot, "$g_enemy_party", slot_party_retreat_flag, 1),

              (try_for_range, ":troop_no", kingdom_heroes_begin, kingdom_heroes_end),
                (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
                #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
                (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
                (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                (gt, ":party_no", 0),
                (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
                (party_slot_eq, ":party_no", slot_party_ai_object, "$g_encountered_party"),
                (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
                (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
                (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, "$g_encountered_party"),
              (try_end),
              (display_message, "@The enemy has been forced to retreat. The assault is over, but the siege continues."),
              (assign, "$g_battle_simulation_cancel_for_party", "$g_encountered_party"),
              (leave_encounter),
              (change_screen_return),
              (assign, "$g_battle_simulation_auto_enter_town_after_battle", "$g_encountered_party"),
            (try_end),
          (try_end),
        (try_end),
        (assign, "$g_siege_first_encounter", 0),
        (assign, "$new_encounter", 0),
        ],
    [
      ("siege_defender_join_battle",
       [
         (neg|troop_is_wounded, "trp_player"),
         ],"Join the battle.",[
              (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
              (assign, "$g_battle_result", 0),
              (try_begin),
                (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
              (else_try),
                (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
              (try_end),
              (call_script, "script_calculate_battle_advantage"),
              (val_mul, reg0, 2),
              (val_div, reg0, 3), #scale down the advantage a bit.
              (set_battle_advantage, reg0),
              (set_party_battle_mode),
              (try_begin),
                (party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
                (set_jump_mission,"mt_castle_attack_walls_belfry"),
              (else_try),
                (call_script, "script_get_ladder_mission"),
				(set_jump_mission, reg0),
              (try_end),
			  (call_script, "script_ms_before_attack", "p_main_party", "$g_enemy_party", "trp_player"),
			  #(call_script, "script_replace_shturm_item_begin"),
              (jump_to_scene,":battle_scene"),
              (assign, "$g_next_menu", "mnu_siege_started_defender"),
              (jump_to_menu, "mnu_battle_debrief"),
              (change_screen_mission)]),
      ("siege_defender_troops_join_battle",[(call_script, "script_party_count_members_with_full_health", "p_main_party"),
                                            (this_or_next|troop_is_wounded,  "trp_player"),
                                            (ge, reg0, 3)],"Order your men to join the battle without you.",[
              (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
              (select_enemy,1),
              (assign,"$g_enemy_party","$g_encountered_party_2"),
              (assign,"$g_ally_party","$g_encountered_party"),
              (assign,"$g_siege_join", 1),
              (jump_to_menu,"mnu_siege_join_defense")]),
##      ("siege_defender_do_not_join_battle",[(call_script, "script_party_count_fit_regulars","p_collective_ally"),
##                                            (gt, reg0, 0)],
##       "Don't get involved.", [(leave_encounter),
##                               (change_screen_return),
##           ]),

##      ("siege_defender_surrender",[(call_script, "script_party_count_fit_regulars","p_collective_ally"),
##                                   (this_or_next|eq, reg0, 0),
##                                   (party_slot_eq, "$g_encountered_party", slot_town_lord, "trp_player"),
##                                   ],
##       "Surrender.",[(assign, "$g_player_surrenders", 1),
##                     (jump_to_menu,"mnu_under_siege_attacked_continue")]),
    ]
  ),

  (
    "siege_join_defense",mnf_disable_all_keys,"{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
        (try_begin),
          (eq, "$g_siege_join", 1),
          (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
          (assign, ":player_party_strength", reg0),
          (val_div, ":player_party_strength", 5),
        (else_try),
          (assign, ":player_party_strength", 0),
        (try_end),
        
        (call_script, "script_party_calculate_strength", "p_collective_ally", 0),
        (assign, ":ally_party_strength", reg0),
        (val_div, ":ally_party_strength", 5),
        (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 10),

        (store_add, ":friend_party_strength", ":player_party_strength", ":ally_party_strength"),
        (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
        (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
        (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),

        (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s8, s0),

        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s9, s0),
        (party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),

        (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s10, s0),
        (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

        (try_begin),
          (call_script, "script_party_count_members_with_full_health","p_main_party"),
          (le, reg(0), 0),
          (str_store_string, s4, "str_siege_defender_order_attack_failure"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health","p_collective_enemy"),
          (le, reg(0), 0),
          (assign, "$g_battle_result", 1),
          (str_store_string, s4, "str_siege_defender_order_attack_success"),
        (else_try),
          (str_store_string, s4, "str_siege_defender_order_attack_continue"),
        (try_end),
    ],
    [
      ("continue",[],"Continue...",[
          (jump_to_menu,"mnu_siege_started_defender"),
          ]),
    ]
  ),

  (
    "enter_your_own_castle",0,"As you approach, you are spotted by the castle guards, who welcome you and open the gates wide before their {lord/lady}.",
    "none",
    [
      (str_store_party_name, s2, "$current_town"),
    ],
    [
      ("continue",[],"Continue...",
       [ (jump_to_menu,"mnu_town"),
        ]),
    ],
  ),


  (
    "village",mnf_enable_hot_keys,"{s10}{s11}{s6}{s7}{s20}{s21}",
    "none",
    [
        (assign, "$current_town", "$g_encountered_party"),
        (call_script, "script_update_center_recon_notes", "$current_town"),

        (assign, "$g_defending_against_siege", 0), #required for bandit check
        (assign, "$g_battle_result", 0),
        (assign, "$qst_collect_taxes_currently_collecting", 0),
        (assign, "$qst_train_peasants_against_bandits_currently_training", 0),

        (try_begin),
          (gt, "$auto_enter_menu_in_center", 0),
          (jump_to_menu, "$auto_enter_menu_in_center"),
          (assign, "$auto_enter_menu_in_center", 0),
        (try_end),

        (try_begin),
          (neq, "$g_player_raiding_village",  "$current_town"),
          (assign, "$g_player_raiding_village", 0),
        (else_try),
          (jump_to_menu, "mnu_village_loot_continue"),
        (try_end),

        (try_begin),#Fix for collecting taxes
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
        (try_end),

        (str_store_party_name,s2, "$current_town"),
        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9,":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),

        (str_clear, s10),
        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (str_store_string, s60, s2),
          (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
          (val_add, ":prosperity", 5),
          (store_div, ":str_offset", ":prosperity", 10),
          (store_add, ":str_id", "str_village_prosperity_0",  ":str_offset"),
          (str_store_string, s10, ":str_id"),
        (try_end),

        (str_clear, s11),
        (try_begin),
          (party_slot_eq, "$current_town", slot_village_state, svs_looted),
        (else_try),
          (eq, ":center_lord", "trp_player"),
          (str_store_string,s11,"@ This village and the surrounding lands belong to you."),
        (else_try),
          (ge, ":center_lord", 0),
          (str_store_string,s11,"@ You remember that this village and the surrounding lands belong to {s7}."),
        (else_try),
          (str_store_string,s11,"@ These lands belong to no one."),
        (try_end),

        (str_clear, s7),
        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
          (call_script, "script_describe_center_relation_to_s3", ":center_relation"),
          (assign, reg9, ":center_relation"),
          (str_store_string, s7, "@ {s3} ({reg9})."),
        (try_end),
        (str_clear, s6),
        (try_begin),
          (party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_get_slot, ":bandit_troop", "$current_town", slot_village_infested_by_bandits),
          (store_character_level, ":player_level", "trp_player"),
          (store_add, "$qst_eliminate_bandits_infesting_village_num_bandits", ":player_level", 10),
          		  
	      (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),                
	      (try_begin),
            (eq, ":reduce_campaign_ai", 0), #hard (1x)
            (val_mul, "$qst_eliminate_bandits_infesting_village_num_bandits", 3), #1.5x
          (else_try),
            (eq, ":reduce_campaign_ai", 1), #moderate (1.5x)
            (val_mul, "$qst_eliminate_bandits_infesting_village_num_bandits", 2), #1x                
          (else_try),                        
            (eq, ":reduce_campaign_ai", 2), #easy (2x)
            (val_mul, "$qst_eliminate_bandits_infesting_village_num_bandits", 3), #0.66x
			(val_div, "$qst_eliminate_bandits_infesting_village_num_bandits", 2),
          (try_end),        

          (store_random_in_range, "$qst_eliminate_bandits_infesting_village_num_villagers", 12, 24),
          (assign, reg8, "$qst_eliminate_bandits_infesting_village_num_bandits"),
          (str_store_troop_name_by_count, s35, ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
          (str_store_string, s6, "@ The village is infested by {reg8} {s35}."),
          (try_begin),
            (eq, ":bandit_troop", "trp_forest_bandit"),
            (set_background_mesh, "mesh_pic_forest_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_steppe_bandit"),
            (set_background_mesh, "mesh_pic_steppe_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_mountain_bandit"),
            (set_background_mesh, "mesh_pic_mountain_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_sea_raider"),
            (set_background_mesh, "mesh_pic_sea_raiders"),
          (else_try),
            (set_background_mesh, "mesh_pic_bandits"),
          (try_end),
        (else_try),
          (party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (str_store_string, s6, "@ The village has been looted. A handful of souls scatter as you pass through the burnt out houses."),
          (try_begin),
            (neq, "$g_player_raid_complete", 1),
            (play_track, "track_empty_village", 1),
          (try_end),
          (set_background_mesh, "mesh_pic_looted_village"),
        (else_try),
          (party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
          (str_store_string, s6, "@ The village is being raided."),
        (else_try),
          #(party_get_current_terrain, ":cur_terrain", "$current_town"),
		  (party_get_icon, ":cur_icon", "$current_town"),
          (try_begin),
			(eq, ":cur_icon", "icon_oim_rus_derevnya"), 
            (set_background_mesh, "mesh_pic_village_w"),
          (else_try),
		  	(eq, ":cur_icon", "icon_village_ukr_a"), 
            (set_background_mesh, "mesh_pic_village_u"),
          (else_try),
		  	(eq, ":cur_icon", "icon_village_ttr_a"), 
            (set_background_mesh, "mesh_pic_village_s"),
          (else_try),
 		  	(this_or_next|eq, ":cur_icon", "icon_village_swed_a"), 
			(			  eq, ":cur_icon", "icon_village_pol_a"), 
            (set_background_mesh, "mesh_pic_village_p"),
          (try_end),
        (try_end),

        (try_begin),
          (eq, "$g_player_raid_complete", 1),
          (assign, "$g_player_raid_complete", 0),
          (jump_to_menu, "mnu_village_loot_complete"),
        (else_try),
          (party_get_slot, ":raider_party", "$current_town", slot_village_raided_by),
          (gt, ":raider_party", 0),
        # Process here...
        (try_end),

         #Adding tax to player if player is the owner of the villager
        (try_begin),
          (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
          (party_get_slot, ":accumulated_rents", "$current_town", slot_center_accumulated_rents),
          (gt, ":accumulated_rents", 0),
          (jump_to_menu, "mnu_center_tax"),
        (try_end),

        (try_begin),
          (eq,"$g_leave_town",1),
          (assign,"$g_leave_town",0),
          (change_screen_return),
        (try_end),

        (try_begin), 
          (store_time_of_day, ":cur_hour"),
          (ge, ":cur_hour", 5),
          (lt, ":cur_hour", 21),
          (assign, "$town_nighttime", 0),
        (else_try),
          (assign, "$town_nighttime", 1),
        (try_end),
		(str_store_string, s21, "str_empty_string"),
		(try_begin),
			(neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
			(call_script, "script_ms_store_remour_descr_to_s21"),
		(try_end),
    ],
    [
      ("village_manage",[(neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
        (neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
        (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                         (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
						 (eq, 0, 1),]
       ,"Manage this village.",
       [
           (assign, "$g_next_menu", "mnu_village"),
           (jump_to_menu, "mnu_center_manage"),
        ]),
	  ("village_ms",[(neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
                         (neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
                         (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                         #(party_slot_eq, "$current_town", slot_town_lord, "trp_player")
						 ]
       ,"Talk to the elder...",
      [
           (call_script, "script_ms_elder_dialog", "mnu_village"),
        ]),
	  ("additional_menu_ms",[  
							(neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
							(neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
							(neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
							(party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
							(eq, 1, 0), #blocked!
       ]
       ,"Go to the center of the village...",
       [
           (assign, "$g_next_menu", "mnu_village"),
           (jump_to_menu, "mnu_ms_additional_menu"),
        ]),
      ("recruit_volunteers",[(call_script, "script_cf_village_recruit_volunteers_cond"),]
       ,"Recruit volunteers.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (jump_to_menu, "mnu_recruit_volunteers"),
         (try_end),
        ]),
      ("village_center",[(neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
                         (neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
                         (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),]
       ,"Go to the village center.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_thieves_check"),
		 (else_try),  
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":village_scene", "$current_town", slot_castle_exterior),
           (modify_visitors_at_site,":village_scene"),
           (reset_visitors),
           (party_get_slot, ":village_elder_troop", "$current_town",slot_town_elder),
           (set_visitor, 11, ":village_elder_troop"),

           (call_script, "script_init_town_walkers"),

           (try_begin),
             (check_quest_active, "qst_hunt_down_fugitive"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
             (neg|check_quest_failed, "qst_hunt_down_fugitive"),
             (set_visitor, 45, "trp_fugitive"),
           (try_end),

           (set_jump_mission,"mt_village_center"),
           (jump_to_scene,":village_scene"),
           (change_screen_mission),
         (try_end),
        ],"Door to the village center."),
      ("village_buy_food",[(party_slot_eq, "$current_town", slot_village_state, 0),
                           (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                           ],"Buy supplies from the peasants.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
           (change_screen_trade, ":merchant_troop"),
         (try_end),
         ]),

      ("village_attack_bandits",[(party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),],"Attack the bandits.",
       [(party_get_slot, ":bandit_troop", "$current_town", slot_village_infested_by_bandits),
        (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
        (modify_visitors_at_site,":scene_to_use"),
        (reset_visitors),
        (set_visitors, 0, ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
        (set_visitors, 2, "trp_farmer", "$qst_eliminate_bandits_infesting_village_num_villagers"),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission,"mt_village_attack_bandits"),
        (jump_to_scene, ":scene_to_use"),
        (assign, "$g_next_menu", "mnu_village_infest_bandits_result"),
        (jump_to_menu, "mnu_battle_debrief"),
        (assign, "$g_mt_mode", vba_normal),
        (change_screen_mission),
        ]),

      ("village_wait",
       [(party_slot_eq, "$current_town", slot_center_has_manor, 1),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
        ],"Wait here for some time.",
         [
		   (assign, "$g_last_rest_payment_until", -1),
           (assign,"$auto_enter_town","$current_town"),
           (assign, "$g_last_rest_center", "$current_town"),
           (rest_for_hours_interactive, 24 * 7, 5, 1), #rest while attackable
           (change_screen_return),
          ]),
      
      
      ("collect_taxes_qst",[(party_slot_eq, "$current_town", slot_village_state, 0),
                            (check_quest_active, "qst_collect_taxes"),
                            (quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
                            (quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, "$current_town"),
                            (neg|quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 4),
                            (str_store_troop_name, s1, ":quest_giver_troop"),
                            (quest_get_slot, reg5, "qst_collect_taxes", slot_quest_current_state),
                            ],"{reg5?Continue collecting taxes:Collect taxes} due to {s1}.",
       [(jump_to_menu, "mnu_collect_taxes"),]),

      ("train_peasants_against_bandits_qst",
       [
         (party_slot_eq, "$current_town", slot_village_state, 0),
         (check_quest_active, "qst_train_peasants_against_bandits"),
         (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
         (quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_center, "$current_town"),
         ],"Train the peasants.",
       [(jump_to_menu, "mnu_train_peasants_against_bandits"),]),

      ("village_hostile_action",[(party_slot_eq, "$current_town", slot_village_state, 0),
                                 (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),],"Take a hostile action.",
       [(jump_to_menu,"mnu_village_hostile_action"),
           ]),
      
      ("village_reports",[(eq, "$cheat_mode", 1),],"{!}CHEAT! Show reports.",
       [(jump_to_menu,"mnu_center_reports"),
           ]),
	   
		#oim code
      ("oim_potop_sneak_into_village",[			
			(quest_slot_eq, "qst_oim_potop_kshetuskiy", slot_quest_target_center, "$g_encountered_party"),
	    (check_quest_active,"qst_oim_potop_kshetuskiy"),
			(neg|check_quest_succeeded,"qst_oim_potop_kshetuskiy"), 
	    (neg|check_quest_failed,"qst_oim_potop_kshetuskiy"), 
  ],"Go to the stables.",
       [(jump_to_menu, "mnu_oim_potop_kshetuskiy"),
           ]),

      ("talk_to_pafnutiy_dlg",[
			#code
			(check_quest_active, "qst_oim_getman_voron_translate"),
			(check_quest_succeeded, "qst_oim_getman_voron_translate"),
			(neg|check_quest_finished,"qst_oim_getman_voron_translate"),
			(quest_slot_eq, "qst_oim_getman_voron_translate", slot_quest_current_state, 3), 
			(quest_slot_eq, "qst_oim_getman_voron_translate", slot_quest_target_center, "$current_town"), 
  ],"Talk to Pafnuty.",[
			#code 
			(assign, "$oim_auto_talk_troop", "trp_oim_getman_pafnutiy"), 
			(jump_to_menu, "mnu_oim_auto_talk_menu"),
			(finish_mission),
			(music_set_situation, 0),
          ],"Talk to Pafnuty."),

      ("Edit_scenes",[
	    (eq, debug_mode, 1),
		
           ],"{!}Edit_scenes",[
			(jump_to_menu, "mnu_oim_edit_scenes_in_this_town"),  
          ],"{!}Edit_scenes"),

	
      ("village_center_nesvz",[(neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
                         (neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
                         (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
					 (eq, "$g_can_enter_nesviz_dangeon", 1), 
					 (eq, "$g_encountered_party", "p_village_53"), 
					 ]
       ,"Go to the tomb",
       [
           #(party_get_slot, ":village_scene", "$current_town", slot_castle_exterior),
		   (assign, ":village_scene", "scn_oim_nesviz_dangeon"), 
           (modify_visitors_at_site,":village_scene"),
           (reset_visitors),
           (set_jump_mission,"mt_visit_town_castle"),
           (jump_to_scene,":village_scene"),
           (change_screen_mission),
        ],"Go to the tomb"),  
	
      ("talk_to_yavangelik",[
			(check_quest_active, "qst_oim_dmitriy_gerasim"),
			(neg|check_quest_succeeded, "qst_oim_dmitriy_gerasim"), 
			(neg|check_quest_finished,"qst_oim_dmitriy_gerasim"),
			(quest_slot_eq, "qst_oim_dmitriy_gerasim", slot_quest_target_center, "$current_town"),
					 ]
       ,"Talk to Evangelic.",
       [
			(jump_to_menu, "mnu_oim_dmitriy_yevangelik"),
        ],"Talk to Evangelic."),	
		
		
	
      ("village_leave",[],"Leave...",[(change_screen_return,0)]),
      
    ],
  ),


  (
    "village_hostile_action",0,
    "Take action!",
    "none",
    [],
    [
      ("village_take_food",[
          (party_slot_eq, "$current_town", slot_village_state, 0),
          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
          (assign, ":town_stores_not_empty", 0),
          (try_for_range, ":slot_no", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
            (troop_get_inventory_slot, ":slot_item", ":merchant_troop", ":slot_no"),
            (ge, ":slot_item", 0),
            (assign, ":town_stores_not_empty", 1),
          (try_end),
          (eq, ":town_stores_not_empty", 1),
          ],"Force the peasants to give you supplies.",
       [
           (jump_to_menu, "mnu_village_take_food_confirm")
        ]),
      ("village_steal_cattle",
       [
          (party_slot_eq, "$current_town", slot_village_state, 0),
          (party_slot_eq, "$current_town", slot_village_player_can_not_steal_cattle, 0),
          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
          (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
          (gt, ":num_cattle", 0),
          ],"Steal cattle.",
       [
           (jump_to_menu, "mnu_village_steal_cattle_confirm")
        ]),
      ("village_loot",[],"Loot and burn the village.",
       [
#           (party_clear, "$current_town"),
#           (party_add_template, "$current_town", "pt_villagers_in_raid"),
			#(call_script, "script_change_player_party_morale", 40),
			(try_begin), 
			#village_84
				(check_quest_active, "qst_mest_i_zakon"),
				(quest_slot_eq, "qst_mest_i_zakon", slot_quest_current_state, 0), 
				(eq, "$current_town", "p_village_84"),
				(assign, "$talk_context", 0),
				(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
				(reset_visitors),
				(set_visitor,0,"trp_player"),
				(set_visitor,17,"trp_village_84_elder"),
				(set_jump_mission,"mt_conversation_encounter"),
				(jump_to_scene,"scn_meeting_scene_plain_forest"),
				(change_screen_map_conversation, "trp_village_84_elder"),         
			(else_try),
           (jump_to_menu, "mnu_village_start_attack"),
			(try_end),
           ]),
      ("forget_it",[],
      "Forget it.",[(jump_to_menu,"mnu_village")]),
    ],
  ),
  


  
  (
    "recruit_volunteers",0,
    "{s18}",
    "none",
    [(party_get_slot, ":volunteer_troop", "$current_town", slot_center_volunteer_troop_type),
     (party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
     (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
     (val_min, ":volunteer_amount", ":free_capacity"),
     (store_troop_gold, ":gold", "trp_player"),
     (store_div, ":gold_capacity", ":gold", 10),#10 denars per man
     (val_min, ":volunteer_amount", ":gold_capacity"),
     (assign, reg5, ":volunteer_amount"),
     (try_begin),
       (eq, ":volunteer_amount", 0),
       (str_store_string, s18, "@No one here seems to be willing to join your party."),
     (else_try),
       (store_mul, reg6, ":volunteer_amount", 10),#10 denars per man
       (str_store_troop_name_by_count, s3, ":volunteer_troop", ":volunteer_amount"),
       (try_begin),
         (eq, reg5, 1),
         (str_store_string, s18, "@One {s3} volunteers to follow you."),
       (else_try),
         (str_store_string, s18, "@{reg5} {s3} volunteer to follow you."),
       (try_end),
       (set_background_mesh, "mesh_pic_recruits"),
     (try_end),
    ],
    [
      ("continue",[(eq, reg5, 0)],
       "Continue...",[(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),(jump_to_menu,"mnu_village")]),
      ("recruit_them",[(gt, reg5, 0)],"Recruit them for {reg6} thaler.",[(call_script, "script_village_recruit_volunteers_recruit"),
        (jump_to_menu,"mnu_village"),
      ]),
      ("forget_it",[(gt, reg5, 0)],
      "Forget it.",[(jump_to_menu,"mnu_village")]),
    ],
  ),

  (
    "village_hunt_down_fugitive_defeated",0,"A heavy blow sends you to the ground, and your vision spins and goes dark. Time passes. When you open your eyes once more, you find yourself battered and bloody, but luckily none of your wounds appear to be lethal.",
    "none",
    [],
    [
      ("continue",[],"Continue...",[(jump_to_menu, "mnu_village"),]),
    ],
  ),

  (
    "village_infest_bandits_result",mnf_scale_picture,"{s9}",
    "none",
    [(try_begin),
       (eq, "$g_battle_result", 1),
       (jump_to_menu, "mnu_village_infestation_removed"),
     (else_try),
       (str_store_string, s9, "@Try as you might, you could not defeat the bandits.\
 Infuriated, they raze the village to the ground to punish the peasants,\
 and then leave the burning wasteland behind to find greener pastures to plunder."),
       (set_background_mesh, "mesh_pic_looted_village"),
     (try_end),
    ],
    [
      ("continue",[],"Continue...",
       [(party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),	  
        (call_script, "script_village_set_state",  "$current_town", svs_looted),

        (party_add_particle_system, "$current_town", "psys_map_village_fire"), #new
        (party_add_particle_system, "$current_town", "psys_map_village_fire_smoke"), #new
        (party_set_icon, "$current_town", "icon_village_burnt_a"), #new
        (party_set_slot, "$current_town", slot_village_smoke_added, 1), #new
		
        (party_set_slot, "$current_town", slot_village_raid_progress, 100), #was 0
        (party_set_slot, "$current_town", slot_village_recover_progress, 0),

        (try_begin),
          (check_quest_active, "qst_eliminate_bandits_infesting_village"),
          (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -5),
          (call_script, "script_fail_quest", "qst_eliminate_bandits_infesting_village"),
        (else_try),
          (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
          (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -4),
          (call_script, "script_fail_quest", "qst_deal_with_bandits_at_lords_village"),
        (else_try),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
        (try_end),
        (jump_to_menu, "mnu_village"),]),
    ],
  ),


  (
    "village_infestation_removed",mnf_disable_all_keys,"In a battle worthy of song, you and your men drive the bandits from the village, making it safe once more. The villagers have little left in the way of wealth after their terrifying ordeal, but they offer you all they can find.",
    "none",
    [(party_get_slot, ":bandit_troop", "$g_encountered_party", slot_village_infested_by_bandits),
     (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
     (party_clear, "p_temp_party"),
     (party_add_members, "p_temp_party", ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
     (assign, "$g_strength_contribution_of_player", 50),
     (call_script, "script_party_give_xp_and_gold", "p_temp_party"),
     (try_begin),
       (check_quest_active, "qst_eliminate_bandits_infesting_village"),
       (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
       (call_script, "script_end_quest", "qst_eliminate_bandits_infesting_village"),
       #Add quest reward
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 5),
     (else_try),
       (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
       (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
       (call_script, "script_succeed_quest", "qst_deal_with_bandits_at_lords_village"),

       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
     (else_try),
     #Add normal reward
      (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 4),
     (try_end),
   
     (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
     (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 70),
        (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
     (try_end),
    ],
    [
      ("village_bandits_defeated_accept",[],"Take it as your just due.",[(jump_to_menu, "mnu_village"),
                                                                         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
                                                                         (troop_sort_inventory, ":merchant_troop"),
                                                                         (change_screen_loot, ":merchant_troop"),
                                                                       ]),
																	   
      ("village_bandits_defeated_cont",[],"Refuse, stating that they need these items more than you do.",
	  [	
	    (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
		(call_script, "script_change_player_honor", 1),	  
		(jump_to_menu, "mnu_village")]),
    ],
  ),

  (
    "center_manage",0,"{s19}^{reg6?^^You are currently building {s7}. The building will be completed in {reg8} day{reg9?s:}.:}",
    "none",
    [(assign, ":num_improvements", 0),
     (str_clear, s18),
     (try_begin),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
       (assign, ":begin", village_improvements_begin),
       (assign, ":end", village_improvements_end),
       (str_store_string, s17, "@village"),
     (else_try),
       (assign, ":begin", walled_center_improvements_begin),
       (assign, ":end", walled_center_improvements_end),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
       (str_store_string, s17, "@town"),
     (else_try),
       (str_store_string, s17, "@castle"),
     (try_end),
     
     (try_for_range, ":improvement_no", ":begin", ":end"),
       (party_slot_ge, "$g_encountered_party", ":improvement_no", 1),
       (val_add,  ":num_improvements", 1),
       (call_script, "script_get_improvement_details", ":improvement_no"),
       (try_begin),
         (eq,  ":num_improvements", 1),
         (str_store_string, s18, "@{s0}"),
       (else_try),
         (str_store_string, s18, "@{s18}, {s0}"),
       (try_end),
     (try_end),
     
     (try_begin),
       (eq,  ":num_improvements", 0),
       (str_store_string, s19, "@The {s17} has no improvements."),
     (else_try),
       (str_store_string, s19, "@The {s17} has the following improvements:{s18}."),
     (try_end),
     
     (assign, reg6, 0),
     (try_begin),
       (party_get_slot, ":cur_improvement", "$g_encountered_party", slot_center_current_improvement),
       (gt, ":cur_improvement", 0),
       (call_script, "script_get_improvement_details", ":cur_improvement"),
       (str_store_string, s7, s0),
       (assign, reg6, 1),
       (store_current_hours, ":cur_hours"),
       (party_get_slot, ":finish_time", "$g_encountered_party", slot_center_improvement_end_hour),
       (val_sub, ":finish_time", ":cur_hours"),
       (store_div, reg8, ":finish_time", 24),
       (val_max, reg8, 1),
       (store_sub, reg9, reg8, 1),
     (try_end),
    ],
    [
      ("center_build_manor",[(eq, reg6, 0),
                             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                             (party_slot_eq, "$g_encountered_party", slot_center_has_manor, 0),
                                  ],"Build a manor.",[(assign, "$g_improvement_type", slot_center_has_manor),
                         (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_fish_pond",[(eq, reg6, 0),
                                 (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                 (party_slot_eq, "$g_encountered_party", slot_center_has_fish_pond, 0),
                                  ],"Build a mill.",[(assign, "$g_improvement_type", slot_center_has_fish_pond),
                             (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_watch_tower",[(eq, reg6, 0),
                                   (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                   (party_slot_eq, "$g_encountered_party", slot_center_has_watch_tower, 0),
                                  ],"Build a watch tower.",[(assign, "$g_improvement_type", slot_center_has_watch_tower),
                               (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_school",[(eq, reg6, 0),
                              (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                              (party_slot_eq, "$g_encountered_party", slot_center_has_school, 0),
                                  ],"Build a school.",[(assign, "$g_improvement_type", slot_center_has_school),
                          (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_messenger_post",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_messenger_post, 0),
                                       ],"Build a messenger post.",[(assign, "$g_improvement_type", slot_center_has_messenger_post),
                                  (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_prisoner_tower",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_prisoner_tower, 0),
                                       ],"Build a prisoner tower.",[(assign, "$g_improvement_type", slot_center_has_prisoner_tower),
                                  (jump_to_menu, "mnu_center_improve"),]),
                           
      ("go_back_dot",[],"Go back.",[(jump_to_menu, "$g_next_menu")]),
    ],
  ),

  (
    "center_improve",0,"{s19} As the best engineer in the party ({reg2} Engineering skill), {reg3?you reckon:{s3} reckons} that building the {s4} will cost you {reg5} thaler and will take {reg6} days.",
    "none",
    [(call_script, "script_get_improvement_details", "$g_improvement_type"),
     (assign, ":improvement_cost", reg0),
     (str_store_string, s4, s0),
     (str_store_string, s19, s1),
     (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),

     (store_sub, ":multiplier", 20, ":max_skill"),
     (val_mul, ":improvement_cost", ":multiplier"),
     (val_div, ":improvement_cost", 20),
     
     (store_div, ":improvement_time", ":improvement_cost", 100),
     (val_add, ":improvement_time", 3),

     (assign, reg5, ":improvement_cost"),
     (assign, reg6, ":improvement_time"),

     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
    ],
    [
      ("improve_cont",[(store_troop_gold, ":cur_gold", "trp_player"),
                       (ge, ":cur_gold", reg5)],"Begin construction.", [(troop_remove_gold, "trp_player", reg5),
                  (party_set_slot, "$g_encountered_party", slot_center_current_improvement, "$g_improvement_type"),
                  (store_current_hours, ":cur_hours"),
                  (store_mul, ":hours_takes", reg6, 24),
                  (val_add, ":hours_takes", ":cur_hours"),
                  (party_set_slot, "$g_encountered_party", slot_center_improvement_end_hour, ":hours_takes"),
                  (jump_to_menu,"mnu_center_manage"),
                  ]),
      ("forget_it",[(store_troop_gold, ":cur_gold", "trp_player"),
                    (ge, ":cur_gold", reg5)],
       "Forget it.", [(jump_to_menu,"mnu_center_manage")]),
      ("improve_not_enough_gold",[(store_troop_gold, ":cur_gold", "trp_player"),
                                  (lt, ":cur_gold", reg5)],"That is too expensive.", [(jump_to_menu, "mnu_center_manage"),]),
    ],
  ),

  (
    "town_bandits_failed",mnf_disable_all_keys,"{s4} {s5}",
    "none",
    [
#      (call_script, "script_loot_player_items", 0),
      (store_troop_gold, ":total_gold", "trp_player"),
      (store_div, ":gold_loss", ":total_gold", 30),
      (store_random_in_range, ":random_loss", 40, 100),
      (val_add, ":gold_loss", ":random_loss"),
      (val_min, ":gold_loss", ":total_gold"),	  
      (troop_remove_gold, "trp_player",":gold_loss"),
      (party_set_slot, "$current_town", slot_center_has_bandits, 0),
      (party_get_num_companions, ":num_companions", "p_main_party"),
      (str_store_string, s4, "@The assasins beat you down and leave you for dead. ."),
      (str_store_string, s4, "@You have fallen. The bandits quickly search your body for every coin they can find,\
 then vanish into the night. They have left you alive, if only barely."),
      (try_begin),
        (gt, ":num_companions", 2),
        (str_store_string, s5, "@Luckily some of your companions come to search for you when you do not return, and find you lying by the side of the road. They hurry you to safety and dress your wounds."),
      (else_try),
        (str_store_string, s5, "@Luckily some passing townspeople find you lying by the side of the road, and recognise you as something other than a simple beggar. They carry you to the nearest inn and dress your wounds."),
      (try_end),

	  (try_begin),
	    (check_quest_active,"qst_oim_hunt_down_thieves"),
	    (call_script, "script_fail_quest", "qst_oim_hunt_down_thieves"),		
		(quest_set_slot, "qst_oim_hunt_down_thieves", slot_quest_dont_give_again_period, 10),
	  (try_end),
    ],
    [
      ("continue",[],"Continue...",[(change_screen_return)]),
    ],
  ),

  (
    "town_bandits_succeeded",mnf_disable_all_keys,"The bandits fall before you as wheat to the scythe! Soon you stand alone in the streets, while most of your attackers lie unconscious, dead or dying. Searching the bodies, you find a purse which must have belonged to a previous victim of these brutes. Or perhaps it was given to them by someone who wanted to arrange a suitable ending to your life...",
    "none",
    [
      (party_set_slot, "$current_town", slot_center_has_bandits, 0),
      (assign, "$g_last_defeated_bandits_town", "$g_encountered_party"),

      (try_begin),
        (check_quest_active, "qst_deal_with_night_bandits"),
        (neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
        (quest_slot_eq, "qst_deal_with_night_bandits", slot_quest_target_center, "$g_encountered_party"),
        (call_script, "script_succeed_quest", "qst_deal_with_night_bandits"),
      (try_end),
	  
      (try_begin),
        (check_quest_active, "qst_oim_hunt_down_thieves"),
        (neg|check_quest_succeeded, "qst_oim_hunt_down_thieves"),
        (quest_slot_eq, "qst_oim_hunt_down_thieves", slot_quest_target_center, "$g_encountered_party"),
        (call_script, "script_succeed_quest", "qst_oim_hunt_down_thieves"),
      (try_end),

      (store_mul, ":xp_reward", "$num_center_bandits", 50),
      (add_xp_to_troop, ":xp_reward", "trp_player"),
      (store_mul, ":gold_reward", "$num_center_bandits", 50),
      (call_script, "script_troop_add_gold","trp_player",":gold_reward"),
    ],
    [
      ("continue",[],"Continue...",[(change_screen_return)]),
    ],
  ),

  
   (
    "village_steal_cattle_confirm",0,"As the best looter in the party ({reg2} looting skill), {reg3?you reckon:{s1} reckons} that you can steal as many as {reg4} heads of village's cattle.",
    "none",
    [
      (call_script, "script_get_max_skill_of_player_party", "skl_looting"),
      (assign, reg2, reg0),
      (assign, ":max_skill_owner", reg1),
      (try_begin),
        (eq, ":max_skill_owner", "trp_player"),
        (assign, reg3, 1),
      (else_try),
        (assign, reg3, 0),
        (str_store_troop_name, s1, ":max_skill_owner"),
      (try_end),
      (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
      (assign, reg4, reg0),
      ],
    [
      ("village_steal_cattle_confirm",[],"Steal the cattle.",
       [
         (rest_for_hours_interactive, 3, 5, 1), #rest while attackable
         (assign, "$auto_menu", "mnu_village_steal_cattle"),
         (change_screen_return),
       ]),
      ("forget_it",[],"Forget it.",[(change_screen_return)]),
    ],
  ),

  (
    "village_steal_cattle",mnf_disable_all_keys,
    "{s1}",
    "none",
    [
      (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
      (assign, ":max_value", reg0),
      (val_add, ":max_value", 1),
      (store_random_in_range, ":random_value", 0, ":max_value"),
      (party_set_slot, "$current_town", slot_village_player_can_not_steal_cattle, 1),
      (party_get_slot, ":lord", "$current_town", slot_town_lord),
      (try_begin),
        (le, ":random_value", 0),
        (call_script, "script_change_player_relation_with_center", "$current_town", -3),
        (str_store_string, s1, "@You fail to steal any cattle."),
      (else_try),
        (assign, reg17, ":random_value"),
        (store_sub, reg12, ":random_value", 1),
        (try_begin),
          (gt, ":lord", 0),
          (call_script, "script_change_player_relation_with_troop", ":lord", -3),
        (try_end),
        (call_script, "script_change_player_relation_with_center", "$current_town", -5),
        (str_store_string, s1, "@You drive away {reg17} {reg12?heads:head} of cattle from the village's herd."),
        (call_script, "script_create_cattle_herd", "$current_town", ":random_value"),
        (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
        (val_sub, ":num_cattle", ":random_value"),
        (party_set_slot, "$current_town", slot_village_number_of_cattle, ":num_cattle"),
      (try_end),
    ],
    [
      ("continue",[],"Continue...",
       [
         (change_screen_return),
         ]),
    ],
  ),
  

   (
    "village_take_food_confirm",0,"It will be difficult to force and threaten the peasants into giving up their precious supplies. You think it will take at least one hour.",
    #TODO: mention looting skill?
    "none",
    [],
    [
      ("village_take_food_confirm",[],"Go on.",
       [
         (rest_for_hours_interactive, 1, 5, 0), #rest while not attackable
         (assign, "$auto_enter_town", "$current_town"),
         (assign, "$g_town_visit_after_rest", 1),
         (assign, "$auto_enter_menu_in_center", "mnu_village_take_food"),
         (change_screen_return),
         ]),
      ("forget_it",[],"Forget it.",[(jump_to_menu, "mnu_village_hostile_action")]),
    ],
  ),

  (
    "village_take_food",0,
    "The villagers grudgingly bring some items.",
    "none",
    [
       (call_script, "script_party_count_members_with_full_health","p_main_party"),
       (assign, ":player_party_size", reg0),
       (call_script, "script_party_count_members_with_full_health","$current_town"),
       (assign, ":villagers_party_size", reg0),
       (try_begin),
         (lt, ":player_party_size", 6),
         (ge, ":villagers_party_size", 40),
         (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
         (jump_to_menu, "mnu_village_start_attack"),
       (try_end),
    ],
    [
      ("take_supplies",[],"Take their supplies.",
       [
         (try_begin),
           (party_slot_ge, "$current_town", slot_center_player_relation, -55),
           (try_begin),
             (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
             (call_script, "script_change_player_relation_with_center", "$current_town", -1),
           (else_try),
             (call_script, "script_change_player_relation_with_center", "$current_town", -3),
           (try_end),
         (try_end),
         (party_get_slot, ":village_lord", "$current_town", slot_town_lord),
         (try_begin),
           (gt,  ":village_lord", 1),
          (call_script, "script_change_player_relation_with_troop", ":village_lord", -1),
          (try_end),
         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
         (party_get_skill_level, ":player_party_looting", "p_main_party", "skl_looting"),
         (val_mul, ":player_party_looting", 3),
         (store_sub, ":random_chance", 70, ":player_party_looting"), #Increases the chance of looting by 3% per skill level
         (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
           (store_random_in_range, ":rand", 0, 100), 
           (lt, ":rand", ":random_chance"),
           (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
         (try_end),

###NPC companion changes begin
         (call_script, "script_objectionable_action", tmt_humanitarian, "str_steal_from_villagers"),
#NPC companion changes end
#Troop commentary changes begin
#          (store_faction_of_party,":village_faction",  "$current_town"),
          (call_script, "script_add_log_entry", logent_village_extorted, "trp_player",  "$current_town", -1, -1),

#Troop commentary changes end          

         (jump_to_menu, "mnu_village"),
         (troop_sort_inventory, ":merchant_troop"),
         (change_screen_loot, ":merchant_troop"),       
         ]),
      ("let_them_keep_it",[],"Let them keep it.",[(jump_to_menu, "mnu_village")]),
    ],
  ),


  (
    "village_start_attack",mnf_disable_all_keys,"Some of the angry villagers grab their tools and prepare to resist you. It looks like you'll have a fight on your hands.",
    "none",
    [
       (call_script, "script_party_count_members_with_full_health","p_main_party"),
       (assign, ":player_party_size", reg(0)),
       (call_script, "script_party_count_members_with_full_health","$current_town"),
       (assign, ":villagers_party_size", reg(0)),
       
       (try_begin),
         (gt, ":player_party_size", 25),
         (jump_to_menu, "mnu_village_loot_no_resist"),
       (else_try),
         (this_or_next|eq, ":villagers_party_size", 0),
         (eq, "$g_battle_result", 1),
         (try_begin),
           (eq, "$g_battle_result", 1),
           (store_random_in_range, ":enmity", -30, -15),
           (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
           (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
           (gt, ":town_lord", 0),
           (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
         (try_end),
         (jump_to_menu, "mnu_village_loot_no_resist"),
       (else_try),
         (eq, "$g_battle_result", -1),
  (try_begin),
			(quest_slot_eq, "qst_mest_i_zakon", slot_quest_current_state, 0), 
			(eq, "$current_town", "p_village_84"),
			(call_script, "script_change_player_relation_with_faction", "fac_kingdom_5", -1),
			(quest_set_slot, "qst_mest_i_zakon", slot_quest_current_state, 1), 
			(call_script, "script_fail_quest", "qst_mest_i_zakon"),
			(call_script, "script_end_quest", "qst_mest_i_zakon"),
	 (try_end), 
         (jump_to_menu, "mnu_village_loot_defeat"),
       (try_end),
    ],
    [
      ("village_raid_attack",[],"Let the battle begin.",[
          (store_random_in_range, ":enmity", -10, -5),
          (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
          (try_begin),
            (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
            (gt, ":town_lord", 0),
            (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
          (try_end),
          (call_script, "script_calculate_battle_advantage"),
          (set_battle_advantage, reg0),
          (set_party_battle_mode),
          (assign, "$g_battle_result", 0),
          (assign, "$g_village_raid_evil", 1),
          (set_jump_mission,"mt_village_raid"),
          (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
          (jump_to_scene, ":scene_to_use"),
          (assign, "$g_next_menu", "mnu_village_start_attack"),

###NPC companion changes begin
          (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
#NPC companion changes end

          (jump_to_menu, "mnu_battle_debrief"),
          (change_screen_mission),
          ]),
      ("village_raid_leave",[],"Leave this village alone.",[(change_screen_return)]),
    ],
  ),
  
  (
    "village_loot_no_resist",0,"The villagers here are few and frightened, and they quickly scatter and run before you. The village is at your mercy.",
    "none",
    [],
    [
      ("village_loot",[], "Loot and burn the village.",
       [
          (call_script, "script_village_set_state", "$current_town", svs_being_raided),
          (party_set_slot, "$current_town", slot_village_raided_by, "p_main_party"),
          (assign,"$g_player_raiding_village","$current_town"),
          (rest_for_hours, 3, 5, 1), #rest while attackable (3 hours will be extended by the trigger)
          (change_screen_return),
           ]),
      ("village_raid_leave",[],"Leave this village alone.",[(change_screen_return)]),
    ],
  ),
  (
    "village_loot_complete",mnf_disable_all_keys,"On your orders, your troops sack the village, pillaging everything of any value, and putting the buildings to torch. From the coins and valuables that are found, you receive your share of {reg1} thaler.",
    "none",
    [
        (party_get_slot, ":village_lord", "$current_town", slot_town_lord),
        (try_begin),
          (gt,  ":village_lord", 0),
          (call_script, "script_change_player_relation_with_troop", ":village_lord", -5),
        (try_end),
        (store_random_in_range, ":enmity", -40, -20),
        (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
		
        (store_faction_of_party, ":village_faction", "$current_town"),
        #(store_relation, ":relation", ":village_faction", "fac_player_supporters_faction"),
          (call_script, "script_change_player_relation_with_faction", ":village_faction", -3),
        (store_random_in_range, ":morale_increase", 15, 35),
        (call_script, "script_change_player_party_morale", ":morale_increase"),
        (store_random_in_range, reg1, 100, 500),
        (call_script, "script_troop_add_gold", "trp_player", reg1),
#NPC companion changes begin
        (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
#NPC companion changes end
      ],
    [
      ("continue",[], "Continue...",
       [
          
		  #code
		(try_begin),
			(store_faction_of_party, ":faction", "$current_town"),	  
			(eq, ":faction", "fac_kingdom_1"), 
			(check_quest_active, "qst_oim_tzr_korsar"),
			(neg|check_quest_succeeded, "qst_oim_tzr_korsar"),
			(neg|check_quest_finished, "qst_oim_tzr_korsar"),
			(val_add, "$oim_villages_looted_count", 1),
			(try_begin),
				(ge, "$oim_villages_looted_count", 3),
				(call_script, "script_succeed_quest", "qst_oim_tzr_korsar"),
			(try_end),
		(try_end),
		(try_begin), 
			(check_quest_active, "qst_oim_black_lord"),
			(neg|check_quest_succeeded, "qst_oim_black_lord"),
			(neg|check_quest_finished,"qst_oim_black_lord"),
			(quest_slot_eq, "qst_oim_black_lord", slot_quest_current_state, 2),
			(party_get_slot, ":village_lord", "$current_town", slot_town_lord),
			(try_begin), 
				(troop_slot_eq, ":village_lord", slot_troop_support_hero, 1), 
				(call_script, "script_change_troop_faction", ":village_lord", "fac_kingdom_2"),
				(troop_get_slot, ":lords_party", ":village_lord", slot_troop_leaded_party),
				(party_set_faction, ":lords_party", "fac_kingdom_2"),
			(end_try),	
		(end_try), 

	    (try_begin),
			(quest_slot_eq, "qst_mest_i_zakon", slot_quest_current_state, 0), 
			(eq, "$current_town", "p_village_84"),
			(call_script, "script_change_player_relation_with_troop", "trp_kingdom_5_lord", -30),	
			(call_script, "script_change_player_relation_with_center", "$current_town", -10),
			(call_script, "script_change_player_relation_with_faction", "fac_kingdom_5", -5),
			(quest_set_slot, "qst_mest_i_zakon", slot_quest_current_state, 1), 
			(quest_get_slot, ":lord", "qst_mest_i_zakon", slot_quest_giver_troop), 
			(call_script, "script_change_player_relation_with_troop", ":lord", 10),
			(quest_set_slot, "qst_mest_i_zakon3", slot_quest_current_state, 0),
			(str_store_troop_name, s9, "trp_kingdom_5_lord"),	
			(setup_quest_text, "qst_mest_i_zakon2"),	
			(str_store_string, s2, "@OiM Teper luchshe {s9} na glaza ne popadat"),
			(call_script, "script_start_quest", "qst_mest_i_zakon3", "trp_kingdom_5_lord"),	
			(call_script, "script_succeed_quest", "qst_mest_i_zakon"),
	    (try_end), 
		
		(try_begin),
			(check_quest_active, "qst_dmitriy_loot_villages"),
			(neg|check_quest_succeeded, "qst_dmitriy_loot_villages"),
			(neg|check_quest_finished, "qst_dmitriy_loot_villages"),
			(quest_get_slot, ":looted_count", "qst_dmitriy_loot_villages", slot_quest_current_state),
			(store_faction_of_party, ":faction", "$current_town"),	  
			(eq, ":faction", "fac_kingdom_1"), 
			(val_add, ":looted_count", 1),
			(quest_set_slot, "qst_dmitriy_loot_villages", slot_quest_current_state, ":looted_count"),
			(try_begin),
				(ge, ":looted_count", 3),
				(call_script, "script_succeed_quest", "qst_dmitriy_loot_villages"),
			(try_end),
		(try_end),
		(try_begin), 
			(check_quest_active, "qst_oim_potop_kshetuskiy"),
			(neg|check_quest_finished,"qst_oim_potop_kshetuskiy"),
			(quest_slot_eq, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 3), 
			(quest_slot_eq, "qst_oim_potop_kshetuskiy", slot_quest_target_center, "$g_encountered_party"),
			(try_begin),
				(quest_slot_eq, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 10), #something like the quest is ended
				(str_store_string, s5, "@OiM_Potop Loshad teper u menya pora idti k kshetuskomu"),	
				(troop_add_item, "trp_player", "itm_oim_qst_horse"),
				(add_quest_note_from_sreg, "qst_oim_potop_kshetuskiy", 6, s5, 1),
			(try_end),
		(try_end),		  
		  #code_end		  
		  
		  
		  
          (jump_to_menu, "mnu_close"),
          (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
          (assign, ":max_cattle", reg0),
          (val_mul, ":max_cattle", 3),
          (val_div, ":max_cattle", 2),
          (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
          (val_min, ":max_cattle", ":num_cattle"),
          (val_add, ":max_cattle", 1),
          (store_random_in_range, ":random_value", 0, ":max_cattle"),
          (try_begin),
            (gt, ":random_value", 0),
            (call_script, "script_create_cattle_herd", "$current_town", ":random_value"),
            (val_sub, ":num_cattle", ":random_value"),
            (party_set_slot, "$current_town", slot_village_number_of_cattle, ":num_cattle"),
          (try_end),          

          (reset_item_probabilities,100),
		  (troop_clear_inventory, "trp_temp_troop"),
          (troop_add_merchandise,"trp_temp_troop",itp_type_goods,45),
          (troop_sort_inventory, "trp_temp_troop"),
          (change_screen_loot, "trp_temp_troop"),
        ]),
    ],
  ),
  (
    "village_loot_defeat",0,"Fighting with courage and determination, the villagers manage to hold together and drive off your forces.",
    "none",
    [],
    [
      ("continue",[],"Continue...",[(change_screen_return)]),
    ],
  ),
  
  (
    "village_loot_continue",0,"Continue looting the village?",
    "none",
    [],
    [
      ("disembark_yes",[],"Yes.",[ (rest_for_hours, 3, 5, 1), #rest while attackable (3 hours will be extended by the trigger)
                              (change_screen_return),
                              ]),
      ("disembark_no",[],"No.",[(call_script, "script_village_set_state", "$current_town", svs_normal),
                            (party_set_slot, "$current_town", slot_village_raided_by, -1),
                            (assign, "$g_player_raiding_village", 0),
                            (change_screen_return)]),
    ],
  ),
  
  (
    "close",0,"Nothing.",
    "none",
    [
        (change_screen_return),
      ],
    [],
  ),
 
  (
    "center_tax",mnf_disable_all_keys,"You receive the accumulated rents and taxes of this fief, amounting to {reg1} thaler.",
    "none",
    [
        (str_clear, s3),
        (try_begin),
          (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
          (party_get_slot, ":accumulated_rents", "$current_town", slot_center_accumulated_rents),
          (party_get_slot, ":accumulated_tariffs", "$current_town", slot_center_accumulated_tariffs),
          (store_add, ":total_tax", ":accumulated_rents", ":accumulated_tariffs"),
  		  (call_script, "script_cf_mul_total_tax", ":total_tax"),
		  (assign, reg0, ":total_tax"),
		  (try_begin), 
		    (party_slot_eq, "$current_town", slot_party_type, spt_town),
		    (val_mul, ":total_tax", tax_town_multiplier), 
		  (else_try), 
		    (party_slot_eq, "$current_town", slot_party_type, spt_castle),
		    (val_mul, ":total_tax", tax_castle_multiplier), 
		  (else_try),  
		    (val_mul, ":total_tax", tax_village_multiplier), 
		  (end_try), 
          (assign, reg1, ":total_tax"),
          (call_script, "script_troop_add_gold", "trp_player", ":total_tax"),
          (party_set_slot, "$current_town", slot_center_accumulated_rents, 0),
          (party_set_slot, "$current_town", slot_center_accumulated_tariffs, 0),
        (try_end),
      ],
    [
      ("continue",[], "Continue...",
       [
           (try_begin),
             (party_slot_eq, "$current_town", slot_party_type, spt_village),
             (jump_to_menu, "mnu_village"),
           (else_try),
             (jump_to_menu, "mnu_town"),
           (try_end),
        ]),
    ],
  ),

  (
    "town",mnf_enable_hot_keys,"{s10}{s11}{s12}{s13} {s20} {s21}",
    "none",
    [    		  
		(try_begin),
          (eq, "$sneaked_into_town", 1),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
        (try_end),
        (store_encountered_party, "$current_town"),
        (call_script, "script_update_center_recon_notes", "$current_town"),
        (assign, "$g_defending_against_siege", 0),
        (str_clear, s3),
        (party_get_battle_opponent, ":besieger_party", "$current_town"),
        (store_faction_of_party, ":encountered_faction", "$g_encountered_party"),
        (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
        (try_begin),
          (gt, ":besieger_party", 0),
          (ge, ":faction_relation", 0),
          (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
          (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
          (lt, ":besieger_party_relation", 0),
          (assign, "$g_defending_against_siege", 1),
          (assign, "$g_siege_first_encounter", 1),
          (jump_to_menu, "mnu_siege_started_defender"),
        (try_end),

        #Quest menus
        
        (assign, "$qst_collect_taxes_currently_collecting", 0),
        
        (try_begin),
          (gt, "$quest_auto_menu", 0),
          (jump_to_menu, "$quest_auto_menu"),
          (assign, "$quest_auto_menu", 0),
        (try_end),

        (try_begin),
          (eq, "$g_town_assess_trade_goods_after_rest", 1),
          (assign, "$g_town_assess_trade_goods_after_rest", 0),
          (jump_to_menu,"mnu_town_trade_assessment"),
        (try_end),

        (assign, "$talk_context", 0),
        (assign,"$all_doors_locked",0),

        (try_begin),
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
          (assign, "$town_entered", 1),
        (try_end),

        (try_begin),
          (eq,"$g_leave_town",1),
          (assign,"$g_leave_town",0),
          (assign,"$g_permitted_to_center",0),
          (leave_encounter),
          (change_screen_return),
        (try_end),
        
        #Adding tax to player if player is the owner of the town or castle
        (try_begin),
          (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
          (party_get_slot, ":accumulated_rents", "$current_town", slot_center_accumulated_rents),
          (gt, ":accumulated_rents", 0),
          (jump_to_menu, "mnu_center_tax"),
        (try_end),
        

        (str_store_party_name, s2, "$current_town"),
        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name, s9, ":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),
        
        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (str_store_string, s60, s2),
		  (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
          (val_add, ":prosperity", 5),
          (store_div, ":str_offset", ":prosperity", 10),
          (store_add, ":str_id", "str_town_prosperity_0",  ":str_offset"),
          (str_store_string, s10, ":str_id"),
        (else_try),
          (str_store_string,s10,"@You are at {s2}."),
        (try_end),
        
        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_castle),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the castle gate."),
		  (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the castle gate."),
          (else_try),
            (str_store_string,s11,"@ This castle seems to belong to no one."),
          (try_end),
        (else_try),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the town gates."),
		  (else_try),	
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the town gates."),
          (else_try),
            (str_store_string,s11,"@ The townsfolk here have declared their independence."),
          (try_end),
        (try_end),

        (str_clear, s12),
        (try_begin),
          #(party_slot_eq,"$current_town",slot_party_type, spt_town),
          (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
          (call_script, "script_describe_center_relation_to_s3", ":center_relation"),
          (assign, reg9, ":center_relation"),
          (str_store_string, s12, "@ {s3} ({reg9})."),
        (try_end),

        (str_clear, s13),
        (try_begin), 
          (gt,"$entry_to_town_forbidden",0),
          (str_store_string, s13, "@ You have successfully sneaked in."),
        (try_end),

        #forbidden to enter?
        (try_begin), 
          (store_time_of_day,reg(12)),
          (ge,reg(12),5),
          (lt,reg(12),21),
          (assign,"$town_nighttime",0),
        (else_try),
          (assign,"$town_nighttime",1),
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (str_store_string, s13, "str_town_nighttime"),
        (try_end),

        (assign,"$castle_undefended",0),
        (party_get_num_companions, ":castle_garrison_size", "p_collective_enemy"),
        (try_begin),
          (eq,":castle_garrison_size",0),
          (assign,"$castle_undefended",1),
        (try_end),
		
		(try_begin),
          (party_slot_eq, "$current_town", slot_ms_party_operation_type, ms_flag_credit),
		  (party_slot_ge, "$current_town", slot_ms_party_operation_time, 31),
		  (jump_to_menu, "mnu_ms_credit_fight"),
        (try_end),
		
		(try_begin),
			(call_script, "script_ms_store_remour_descr_to_s21"),
		(try_end),	
    ],
    [
      ("castle_castle",[(party_slot_eq,"$current_town",slot_party_type, spt_castle)],"Go to the Lord's hall.",
       [
           (try_begin),
             (eq,"$all_doors_locked",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_court", "$current_town"),
           (try_end),
        ], "To the lord's hall"),

      ("join_tournament", [(neg|is_currently_night),(party_slot_ge, "$current_town", slot_town_has_tournament, 1),(eq, 1, 0),]
       ,"Join the tournament.",
       [
           (call_script, "script_fill_tournament_participants_troop", "$current_town", 1),
           (assign, "$g_tournament_cur_tier", 0),
           (assign, "$g_tournament_player_team_won", -1),
           (assign, "$g_tournament_bet_placed", 0),
           (assign, "$g_tournament_bet_win_amount", 0),
           (assign, "$g_tournament_last_bet_tier", -1),
           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),
           (jump_to_menu, "mnu_town_tournament"),
        ]),
      
      ("town_castle",[
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (eq,"$entry_to_town_forbidden",0),
#          (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
#          (scene_slot_ge, ":castle_scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
          ],"Go to the fortress.",
       [
           (try_begin),
             (this_or_next|eq, "$all_doors_locked", 1),
             (eq, "$sneaked_into_town", 1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
		   #             (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
#             (scene_slot_eq, ":castle_scene", slot_scene_visited, 0),
#             (display_message,"str_door_locked",0xFFFFAAAA),
#           (else_try),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_court", "$current_town"),
           (try_end),
        ], "To the lord's hall"),
      
      ("town_center",[
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (this_or_next|eq,"$entry_to_town_forbidden",0),
          (eq, "$sneaked_into_town",1),		  
		]
       ,"Take a walk around the streets.",
       [
           (assign, "$talk_context", 0),
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":town_scene", "$current_town", slot_town_center),
           (modify_visitors_at_site, ":town_scene"),
           (reset_visitors),
           (assign, "$g_mt_mode", tcm_default),
           (store_faction_of_party, ":town_faction","$current_town"),
           (try_begin),
             (neq, ":town_faction", "fac_player_supporters_faction"),
             (faction_get_slot, ":troop_prison_guard", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
             (faction_get_slot, ":troop_castle_guard", "$g_encountered_party_faction", slot_faction_castle_guard_troop),
               (set_visitor, 23, ":troop_castle_guard"),
             (set_visitor, 24, ":troop_prison_guard"),
           (try_end),
           (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
           (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),

           (try_begin),
             (gt,":tier_2_troop", 0),
               (assign,reg(0),":tier_3_troop"),
               (assign,reg(1),":tier_3_troop"),
               (assign,reg(2),":tier_2_troop"),
               (assign,reg(3),":tier_2_troop"),
           (else_try),
               (assign,reg(0),"trp_vaegir_infantry"),
               (assign,reg(1),"trp_vaegir_infantry"),
               (assign,reg(2),"trp_vaegir_archer"),
               (assign,reg(3),"trp_vaegir_footman"),
           (try_end),
           (shuffle_range,0,4),
             (set_visitor,25,reg(0)),
             (set_visitor,26,reg(1)),
             (set_visitor,27,reg(2)),
             (set_visitor,28,reg(3)),
         
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_armorer),
           (set_visitor, 9, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_weaponsmith),
           (set_visitor, 10, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_elder),
           (set_visitor, 11, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_horse_merchant),
           (set_visitor, 12, ":spawned_troop"),

           (call_script, "script_init_town_walkers"),
           (set_jump_mission,"mt_town_center"),
           (assign, ":override_state", af_override_horse),
           (try_begin),
             (eq, "$sneaked_into_town", 1), #setup disguise
             (assign, ":override_state", af_override_all),
           (try_end),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 0, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 2, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 3, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 4, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 5, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 6, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 7, ":override_state"),
           (try_begin),
             (eq, "$town_entered", 0),
             (assign, "$town_entered", 1),
             (eq, "$town_nighttime", 0),
             (set_jump_entry, 1),
           (try_end),
           (jump_to_scene, ":town_scene"),
           (change_screen_mission),
         (try_end),	   
      ],"To the town center"),

      ("town_tavern",[
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (this_or_next|eq,"$entry_to_town_forbidden",0),
          (eq, "$sneaked_into_town",1),
#          (party_get_slot, ":scene", "$current_town", slot_town_tavern),
#          (scene_slot_eq, ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
          ]
       ,"Visit the tavern.",
       [
           (try_begin),
             (eq,"$all_doors_locked",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_horse),
				(mission_tpl_entry_set_override_flags, "mt_oim_trakai_icon", 0, af_override_horse),
             (try_begin),
               (eq, "$sneaked_into_town",1),
               (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_all),
             (try_end),
             (assign, "$town_entered", 1),
				(reset_visitors),		 
				(assign, ":cur_entry", 17),
			(try_begin),
				(check_quest_active, "qst_oim_trakay_icon"),
				(quest_slot_eq, "qst_oim_trakay_icon", slot_quest_current_state, 5),   
				(eq, "$current_town", "p_town_12"),
				(set_jump_mission, "mt_oim_trakai_icon"),
             (party_get_slot, ":cur_scene", "$current_town", slot_town_tavern),
             (jump_to_scene, ":cur_scene"),
				(reset_visitors),		
             (modify_visitors_at_site, ":cur_scene"),
             (assign, ":cur_entry", 17),
				(set_visitor, ":cur_entry", "trp_oim_trakai_ksendz"),
				(val_add, ":cur_entry", 1),
				(set_visitor, ":cur_entry", "trp_oim_polish_taver_visitor"),
				(val_add, ":cur_entry", 1),
				(set_visitor, ":cur_entry", "trp_oim_polish_taver_visitor"),				
				 (val_add, ":cur_entry", 1),
				(set_visitor, ":cur_entry", "trp_oim_polish_taver_visitor"),	
                (val_add, ":cur_entry", 1),
				(jump_to_scene, ":cur_scene"),			
			(else_try),
				(set_jump_mission, "mt_town_default"),
				(party_get_slot, ":cur_scene", "$current_town", slot_town_tavern),
				(jump_to_scene, ":cur_scene"),
				(reset_visitors),		 		
				(modify_visitors_at_site, ":cur_scene"),
             (party_get_slot, ":mercenary_troop", "$current_town", slot_center_mercenary_troop_type),
             (party_get_slot, ":mercenary_amount", "$current_town", slot_center_mercenary_troop_amount),
             (try_begin),
               (gt, ":mercenary_amount", 0),
               (set_visitor, ":cur_entry", ":mercenary_troop"),
               (val_add, ":cur_entry", 1),
             (try_end),
				#oim code tavern fights
				(try_begin),
					(lt, ":cur_entry", 32), 					
					(call_script, "script_cf_oim_get_tavern_visitor"), 
					(assign, ":visitor", reg0),
					(try_begin),
						(troop_slot_eq, ":visitor", slot_troop_alcohol_count, 0), 
						(store_random_in_range, ":rand", 0, 3), 
						(troop_set_slot, ":visitor", slot_troop_alcohol_count, ":rand"),
					(try_end),	
					(set_visitor, ":cur_entry", ":visitor"),
				 (val_add, ":cur_entry", 1),
			 (try_end),
				#oim code tavern fights end				
             (try_for_range, ":companion_candidate", companions_begin, companions_end),
               (troop_slot_eq, ":companion_candidate", slot_troop_occupation, 0),
               (troop_slot_eq, ":companion_candidate", slot_troop_cur_center, "$current_town"),
               (set_visitor, ":cur_entry", ":companion_candidate"),
               (val_add, ":cur_entry", 1),
             (try_end),
			 (try_begin),
					(eq, "$current_town", "p_town_5"),
					(neg|troop_slot_eq, "trp_npc4", slot_troop_cur_center, "p_town_5"),
					(check_quest_active, "qst_oim_getman_kozak_legend"),
					(neg|check_quest_failed, "qst_oim_getman_kozak_legend"), 		
					(neg|check_quest_finished, "qst_oim_getman_kozak_legend"),
					(set_visitor, ":cur_entry", "trp_npc4"),
				 (val_add, ":cur_entry", 1),
			 (try_end),
			 			 
				(try_begin),
               (party_get_slot, ":ransom_broker", "$current_town", slot_center_ransom_broker),
               (gt, ":ransom_broker", 0),
               (set_visitor, ":cur_entry", ":ransom_broker"),
               (val_add, ":cur_entry", 1),
			   (try_end),	
			   
			   
				(try_begin), 
					(try_for_range, ":pretender", pretenders_begin, pretenders_end),
						(troop_slot_eq, ":pretender", slot_troop_cur_center, "$current_town"),
						(lt, ":cur_entry", 32), 
						(set_visitor, ":cur_entry", ":pretender"),
               (val_add, ":cur_entry", 1),
					(end_try), 
             (try_end),
			 
             (try_begin),
					(check_quest_active, "qst_oim_trakay_icon"), 
					(quest_slot_eq, "qst_oim_trakay_icon", slot_quest_current_state, 1),
					(eq, "$current_town", "p_town_12"), 
					(neg|troop_slot_eq, "trp_kingdom_1_pretender", slot_troop_cur_center, "$current_town"),
					(lt, ":cur_entry", 32),
					(set_visitor, ":cur_entry", "trp_kingdom_1_pretender"),
               (val_add, ":cur_entry", 1),
             (try_end),
			 
				#add monfor to tavern
             (try_begin),
					(eq, "$current_town", "p_town_9"),
					(check_quest_active, "qst_oim_monfor_shved"), 
					(neg|check_quest_succeeded, "qst_oim_monfor_shved"), 
					(neg|check_quest_finished, "qst_oim_monfor_shved"), 
					(set_visitor, ":cur_entry", "trp_oim_monfor"),
               (val_add, ":cur_entry", 1),
			   (try_end),
			   
				(try_begin),
					(party_get_slot, ":tavern_traveler", "$current_town", slot_center_tavern_traveler),
					(gt, ":tavern_traveler", 0),
					(set_visitor, ":cur_entry", ":tavern_traveler"),
               (val_add, ":cur_entry", 1),
             (try_end),
##             (try_begin),
##               (party_get_slot, ":tavern_minstrel", "$current_town", slot_center_tavern_minstrel),
##               (gt, ":tavern_minstrel", 0),
##               (set_visitor, 21, ":tavern_minstrel"),
##               (val_add, ":cur_entry", 1),
##             (try_end),
             (try_begin),
               (party_get_slot, ":tavern_bookseller", "$current_town", slot_center_tavern_bookseller),
               (gt, ":tavern_bookseller", 0),
               (set_visitor, ":cur_entry", ":tavern_bookseller"),
               (val_add, ":cur_entry", 1),
             (try_end),
             (try_begin),
               (neg|check_quest_active, "qst_eliminate_bandits_infesting_village"),
               (neg|check_quest_active, "qst_deal_with_bandits_at_lords_village"),
               (assign, ":end_cond", villages_end),
               (try_for_range, ":cur_village", villages_begin, ":end_cond"),
                 (party_slot_eq, ":cur_village", slot_village_bound_center, "$current_town"),
                 (party_slot_ge, ":cur_village", slot_village_infested_by_bandits, 1),
                 (neg|party_slot_eq, ":cur_village", slot_town_lord, "trp_player"),
                 (set_visitor, ":cur_entry", "trp_farmer_from_bandit_village"),
                 (val_add, ":cur_entry", 1),
                 (assign, ":end_cond", 0),
               (try_end),
             (try_end),
			(end_try),	
				(scene_set_slot, ":cur_scene", slot_scene_visited, 1),
				(assign, "$talk_context", tc_tavern_talk),
            #(assign, ":cur_entry", 21),
             (change_screen_mission),
           (try_end),
        ],"To the tavern"),
      
#      ("town_smithy",[
#          (eq,"$entry_to_town_forbidden",0),
#          (eq,"$town_nighttime",0),
#          ],
#       "Visit the smithy.",
#       [
#           (set_jump_mission,"mt_town_default"),
#           (jump_to_scene,"$pout_scn_smithy"),
#           (change_screen_mission,0),
#        ]),
      
      ("town_merchant",
       [(party_slot_eq,"$current_town",slot_party_type, spt_town),
           (eq, 1, 0),
           (eq,"$town_nighttime",0),
           (this_or_next|eq,"$entry_to_town_forbidden",0),
           (eq, "$sneaked_into_town",1),
#           (party_get_slot, ":scene", "$current_town", slot_town_store),
#           (scene_slot_eq, ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
           ],"Speak with the merchant.",
       [           
           (try_begin),
             (this_or_next|eq,"$all_doors_locked",1),
             (eq,"$town_nighttime",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_horse),
             (try_begin),
               (eq, "$sneaked_into_town",1),
               (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_all),
             (try_end),
             (assign, "$town_entered", 1),
             (set_jump_mission, "mt_town_default"),
             (party_get_slot, ":cur_scene", "$current_town", slot_town_store),
             (jump_to_scene, ":cur_scene"),
             (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
             (change_screen_mission),
           (try_end),
        ],"To the shop"),
        
      ("town_arena",
       [(party_slot_eq,"$current_town",slot_party_type, spt_town),
        (eq, "$sneaked_into_town", 0),
		(eq, 0, 1),
#           (party_get_slot, ":scene", "$current_town", slot_town_arena),
#           (scene_slot_eq,  ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
           ],"Enter the arena.",
       [
           (try_begin),
             (this_or_next|eq,"$all_doors_locked",1),
             (eq,"$town_nighttime",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (assign, "$g_mt_mode", abm_visit),
             (assign, "$town_entered", 1),
             (set_jump_mission, "mt_arena_melee_fight"),
             (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
             (modify_visitors_at_site, ":arena_scene"),
             (reset_visitors),
             (set_visitor, 43, "trp_veteran_fighter"),
             (set_visitor, 44, "trp_hired_blade"),
             (set_jump_entry, 50),
             (jump_to_scene, ":arena_scene"),
             (scene_set_slot, ":arena_scene", slot_scene_visited, 1),
             (change_screen_mission),
           (try_end),
           (eq, 1, 0),        
        ],"Door to the arena."),
      ("town_dungeon",
       [(eq, 1, 0)],"{!}Never: Enter the prison.",
       [	   
           (try_begin),
             (eq,"$all_doors_locked",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (this_or_next|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
             (eq, "$g_encountered_party_faction", "$players_kingdom"),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle"),
           (else_try),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (try_end),
        ],"To the prisons"),
      
      ("castle_inspect", [
         (party_slot_eq,"$current_town",slot_party_type, spt_castle),
#           (this_or_next|ge, "$g_encountered_party_relation", 0),
#           (eq,"$castle_undefended",1),
      ],"Take a walk around the courtyard.",
       [
           (assign, "$talk_context", tc_town_talk),
           
           (party_get_slot, ":cur_castle_exterior", "$current_town", slot_castle_exterior),
           (modify_visitors_at_site,":cur_castle_exterior"),(reset_visitors),
		   (party_get_slot, ":elder_troop", "$current_town", slot_town_elder),
           (set_visitor, 23, ":elder_troop"),
           (try_begin),
             (neq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
             (faction_get_slot, ":troop_prison_guard", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
             (set_visitor, 24, ":troop_prison_guard"),
           (try_end),
           
           (assign, ":guard_no", 40),
           

           (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
           (try_for_range, ":troop_iterator", 0, ":num_stacks"),
             (lt, ":guard_no", 47),
             (party_stack_get_troop_id, ":cur_troop_id", "$g_encountered_party", ":troop_iterator"),
             (neg|troop_is_hero, ":cur_troop_id"),
			 (is_between, ":cur_troop_id", regular_troops_begin, regular_troops_end),
             (party_stack_get_size, ":stack_size","$g_encountered_party",":troop_iterator"),
             (party_stack_get_num_wounded, ":num_wounded","$g_encountered_party",":troop_iterator"),
             (val_sub, ":stack_size", ":num_wounded"),
             (gt, ":stack_size", 0),
             (party_stack_get_troop_dna,":troop_dna","$g_encountered_party",":troop_iterator"),
             (set_visitor, ":guard_no", ":cur_troop_id", ":troop_dna"),
             (val_add, ":guard_no", 1),
           (try_end),
           (set_jump_entry, 1),
           (try_begin),
             (eq, "$town_entered", 1),
             (assign, "$town_entered", 0),
			 (set_jump_entry, 2),
           (try_end),
		   

           (set_jump_mission, "mt_castle_visit"),
           (jump_to_scene, ":cur_castle_exterior"),
           (change_screen_mission),
        ], "To the fortress courtyard"),
      ("trade_with_merchants",
       [
           (party_slot_eq,"$current_town",slot_party_type, spt_town)
        ],"Go to the marketplace.",
         [
           (try_begin),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (jump_to_menu,"mnu_town_trade"),
           (try_end),
          ]),

	  ("town_ms",[
					  (neg|party_slot_eq, "$current_town", slot_village_state, svs_under_siege),
					  #(party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
                  ],"Talk to the mayor.",
											   [
													(call_script, "script_ms_elder_dialog", "mnu_town"),													
												]),    
	  ("additional_menu_town_ms",[  
									(neg|party_slot_eq, "$current_town", slot_village_state, svs_under_siege),
									#(party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
								]
       ,"Go to the town center...",
       [
           (assign, "$g_next_menu", "mnu_town"),
           (jump_to_menu, "mnu_ms_additional_menu"),
       ]),
	  
	  ("diplomatic_center",[
								(eq, "$current_town", "$g_diplomatic_capital"),
							]
       ,"Go to the diplomatic center.",
       [
           (assign, "$g_next_menu", "mnu_town"),
           (jump_to_menu, "mnu_select_ambassador"),
       ]),
	   
	#	("addi",[(store_faction_of_party, reg0, "$current_town"),]
    #   ,"Do {reg0}.",
    #   [
    #      
    #   ]),
	  
      ("walled_center_manage",[(neg|party_slot_eq, "$current_town", slot_village_state, svs_under_siege),
                      (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
					  (eq, 0, 1),
                      (assign, reg0, 1),
                      (try_begin),
                        (party_slot_eq, "$current_town", slot_party_type, spt_castle),
                        (assign, reg0, 0),
                      (try_end),]
       ,"Manage this {reg0?town:fortress}.",
       [
           (assign, "$g_next_menu", "mnu_town"),
           (jump_to_menu, "mnu_center_manage"),
        ]),

     ("castle_station_troops",
      [	  
          (party_slot_eq,"$current_town",slot_town_lord, "trp_player"),
       ],"Station a garrison here...",
         [
           (change_screen_exchange_members,1),
          ]),


      ("castle_wait",
       [
#           (party_slot_eq,"$current_town",slot_party_type, spt_castle),
           (this_or_next|ge, "$g_encountered_party_relation", 0),
           (eq,"$castle_undefended",1),
           (assign, ":can_rest", 1),
           (str_clear, s1),
           (try_begin),
             (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
             (party_get_num_companions, ":num_men", "p_main_party"),
             (store_div, reg1, ":num_men", 4),
             (val_add, reg1, 1),
             (str_store_string, s1, "@ ({reg1} denars per night)"),
             (store_troop_gold, ":gold", "trp_player"),
             (lt, ":gold", reg1),
             (assign, ":can_rest", 0),
           (try_end),
           (eq, ":can_rest", 1),
##           (eq, "$g_defending_against_siege", 0),
        ],"Wait here for some time{s1}.",
         [
           (assign, "$auto_enter_town", "$current_town"),
           (assign, "$g_town_visit_after_rest", 1),
           (assign, "$g_last_rest_center", "$current_town"),
           (assign, "$g_last_rest_payment_until", -1),

           (rest_for_hours_interactive, 24 * 7, 5, 0), #rest while not attackable
           (change_screen_return),
          ]),

##      ("rest_until_morning",
##       [
##           (this_or_next|ge, "$g_encountered_party_relation", 0),
##           (eq,"$castle_undefended",1),
##           (store_time_of_day,reg(1)),(neg|is_between,reg(1), 5, 18),
##           (eq, "$g_defending_against_siege", 0),
##        ],
##         "Rest until morning.",
##         [
##           (store_time_of_day,reg(1)),
##           (assign, reg(2), 30),
##           (val_sub,reg(2),reg(1)),
##           (val_mod,reg(2),24),
##           (assign,"$auto_enter_town","$current_town"),
##           (assign, "$g_town_visit_after_rest", 1),
##           (rest_for_hours_interactive, reg(2)),
##           (change_screen_return),
##          ]),
##      
##      ("rest_until_evening",
##       [
##           (this_or_next|ge, "$g_encountered_party_relation", 0),
##           (eq,"$castle_undefended",1),
##           (store_time_of_day,reg(1)), (is_between,reg(1), 5, 18),
##           (eq, "$g_defending_against_siege", 0),
##        ],
##         "Rest until evening.",
##         [
##           (store_time_of_day,reg(1)),
##           (assign, reg(2), 20),
##           (val_sub,reg(2),reg(1)),
##           (assign,"$auto_enter_town","$current_town"),
##           (assign, "$g_town_visit_after_rest", 1),
##           (rest_for_hours_interactive, reg(2)),
##           (change_screen_return),
##          ]),

      ("go_to_the_garem",[
        (this_or_next|eq,"$entry_to_town_forbidden",0),
        (eq, "$sneaked_into_town",1),
		(check_quest_active, "qst_oim_alevtina_hanum"),
		(neg|check_quest_succeeded, "qst_oim_alevtina_hanum"),
		(neg|check_quest_finished,"qst_oim_alevtina_hanum"),
		(quest_slot_ge, "qst_oim_alevtina_hanum", slot_quest_current_state, 1),
		(quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_target_center, "$current_town"),
 	  ],"Sneak into the harem.",[
			(jump_to_menu,"mnu_oim_dmitriy_alevtina_hanum"),
      ],"{!}Edit_scenes"),




      ("Edit_scenes",[
		(eq, debug_mode, 1),
  ],"{!}Edit_scenes",[
			(jump_to_menu, "mnu_oim_edit_scenes_in_this_town"),  
          ],"{!}Edit_scenes"),


      ("town_alley",
       [(party_slot_eq,"$current_town",slot_party_type, spt_town),
        (eq, "$cheat_mode", 1),
           ],"{!}CHEAT: Go to the alley.",
       [
           (party_get_slot, reg(11), "$current_town", slot_town_alley),
           (set_jump_mission, "mt_ai_training"),
           (jump_to_scene,reg(11)),
           (change_screen_mission),
        ]),
      
      ("collect_taxes_qst",[(check_quest_active, "qst_collect_taxes"),
                            (quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, "$current_town"),
                            (neg|quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 4),
                            (quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
                            (str_store_troop_name, s1, ":quest_giver_troop"),
                            (quest_get_slot, reg5, "qst_collect_taxes", slot_quest_current_state),
                            ], "{reg5?Continue collecting taxes:Collect taxes} due to {s1}.",
       [(jump_to_menu, "mnu_collect_taxes"),]),
      
		#(quest_get_slot, ":rand_town", "qst_oim_getman_voron_translate",slot_quest_target_center),

		("castle_tavern",[
          (party_slot_eq,"$current_town",slot_party_type, spt_castle),
		  #(neg|quest_slot_eq, "qst_oim_trakay_icon", slot_quest_current_state, 5),  
          ]
       ,"Visit the tavern.",
       [
            (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_horse),
		    (reset_visitors),		 
		    (assign, ":cur_entry", 17),
		    (set_jump_mission, "mt_castle_default"),
			(call_script, "script_oim_get_tavern_scene", "$current_town"), 
			(assign, ":cur_scene", reg0),
			(jump_to_scene, ":cur_scene"),
			(modify_visitors_at_site, ":cur_scene"),
			(party_get_slot, ":mercenary_troop", "$current_town", slot_center_mercenary_troop_type),
			(party_get_slot, ":mercenary_amount", "$current_town", slot_center_mercenary_troop_amount),
			(set_visitor, 9, "trp_town_5_tavernkeeper"),
			#(set_visitor, 9, "trp_castle_tavernkeeper"),
			(try_begin),
				(gt, ":mercenary_amount", 0),
				(set_visitor, ":cur_entry", ":mercenary_troop"),
				(val_add, ":cur_entry", 1),
			(try_end),
			(try_begin),
				(party_get_slot, ":ransom_broker", "$current_town", slot_center_ransom_broker),
				(gt, ":ransom_broker", 0),
				(set_visitor, ":cur_entry", ":ransom_broker"),
				(val_add, ":cur_entry", 1),
			(try_end),
			(try_begin),
				(party_get_slot, ":tavern_traveler", "$current_town", slot_center_tavern_traveler),
				(gt, ":tavern_traveler", 0),
				(set_visitor, ":cur_entry", ":tavern_traveler"),
				(val_add, ":cur_entry", 1),
			(try_end),
			(try_begin),
				(party_get_slot, ":tavern_bookseller", "$current_town", slot_center_tavern_bookseller),
				(gt, ":tavern_bookseller", 0),
				(set_visitor, ":cur_entry", ":tavern_bookseller"),
				(val_add, ":cur_entry", 1),
			(try_end),
		    (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
			(assign, "$talk_context", tc_tavern_talk),
            (change_screen_mission),
           
        ],"Visit the tavern."),	
   
		
		("castle_trade_with_merchants",
       [
           (party_slot_eq,"$current_town",slot_party_type, spt_castle)
        ],"Go to the marketplace.",
         [
           (try_begin),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (jump_to_menu,"mnu_town_trade"),
           (try_end),
          ]),
		  
	("zdat_tatarina",[
		(check_quest_active,"qst_oim_bring_tatarin_to_sich"),
		(neg|check_quest_succeeded,"qst_oim_bring_tatarin_to_sich"),
		(neg|check_quest_finished,"qst_oim_bring_tatarin_to_sich"),
		(quest_slot_eq, "qst_oim_bring_tatarin_to_sich", slot_quest_current_state, 1),
		(eq, "$g_encountered_party", "p_town_5"),
   ],"Hand over the Tatar.",
       [
			(party_get_slot, ":castle_scene", "$g_encountered_party", slot_town_castle),
			(modify_visitors_at_site, ":castle_scene"),
			(reset_visitors),
			(set_visitor,0, "trp_player"),
			(set_visitor,17, "trp_castle_17_seneschal"),
			(jump_to_scene, ":castle_scene"),
			(change_screen_map_conversation, "trp_castle_17_seneschal"),  
        ], "Hand over the Tatar."),		

      ("talk_to_borzobogataya",[
			(check_quest_active,"qst_oim_potop_volodievskiy"),
			(neg|check_quest_finished,"qst_oim_potop_volodievskiy"),
			(quest_slot_eq, "qst_oim_potop_volodievskiy", slot_quest_current_state, 3),
			(quest_slot_eq, "qst_oim_potop_volodievskiy", slot_quest_target_center, "$g_encountered_party"),
   ],"Talk to Anusia.",
       [
			(party_get_slot, ":castle_scene", "$g_encountered_party", slot_town_castle),
			(modify_visitors_at_site, ":castle_scene"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,"trp_knight_1_2_wife"),
			(jump_to_scene, ":castle_scene"),
			(change_screen_map_conversation, "trp_knight_1_2_wife"),  
        ], "Talk to Anusia."),			  
   
      ("town_leave",[],"Leave...",[
            (assign, "$g_permitted_to_center",0),
            (change_screen_return,0),
          ],"Leave the Area."),
#      ("siege_leave",[(eq, "$g_defending_against_siege", 1)],"Try to break out...",[(jump_to_menu,"mnu_siege_break_out")]),#TODO: Go to Menu here.

      ("castle_cheat_interior",[(eq, "$cheat_mode", 1)], "{!}CHEAT! Interior.",[
                                                       (set_jump_mission,"mt_ai_training"),
                                                       (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
                                                       (jump_to_scene,":castle_scene"),
                                                       (change_screen_mission)]),
      ("castle_cheat_town_exterior",[(eq, "$cheat_mode", 1)],"{!}CHEAT! Exterior.",[
                                                       (try_begin),
                                                         (party_slot_eq,"$current_town",slot_party_type, spt_castle),
                                                         (party_get_slot, ":scene", "$current_town", slot_castle_exterior),
                                                       (else_try),
                                                         (party_get_slot, ":scene", "$current_town", slot_town_center),
                                                       (try_end),
                                                       (set_jump_mission,"mt_ai_training"),
                                                       (jump_to_scene,":scene"),
                                                       (change_screen_mission)]),
      ("castle_cheat_dungeon",[(eq, "$cheat_mode", 1)],"{!}CHEAT! Prison.",[
                                                       (set_jump_mission,"mt_ai_training"),
                                                       (party_get_slot, ":castle_scene", "$current_town", slot_town_prison),
                                                       (jump_to_scene,":castle_scene"),
                                                       (change_screen_mission)]),
      ("castle_cheat_town_walls",[(eq, "$cheat_mode", 1),(party_slot_eq,"$current_town",slot_party_type, spt_town),], "{!}CHEAT! Town Walls.",[
                                                       (party_get_slot, ":scene", "$current_town", slot_town_walls),
                                                       (set_jump_mission,"mt_ai_training"),
                                                       (jump_to_scene,":scene"),
                                                       (change_screen_mission)]),

      ("cheat_town_start_siege",
       [
         (eq, "$cheat_mode", 1),
         (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
         (lt, "$g_encountered_party_2", 1),
         (call_script, "script_party_count_fit_for_battle","p_main_party"),
         (gt, reg(0), 1),
         (try_begin),
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
           (assign, reg6, 1),
         (else_try),
           (assign, reg6, 0),
         (try_end),
           ],"{!}CHEAT: Besiege the {reg6?town:castle}...",
       [
           (assign,"$g_player_besiege_town","$g_encountered_party"),
           (jump_to_menu, "mnu_castle_besiege"),
           ]),


      ("center_reports",[(eq, "$cheat_mode", 1),],"CHEAT! Show reports.",
       [(jump_to_menu,"mnu_center_reports"),
           ]),

      ("sail_from_port",[(party_slot_eq,"$current_town",slot_party_type, spt_town),
                         (eq, "$cheat_mode", 1),
#                         (party_slot_eq,"$current_town",slot_town_near_shore, 1),
                         ],"Sail from port.",
       [(assign, "$g_player_icon_state", pis_ship),
        (party_set_flags, "p_main_party", pf_is_ship, 1),
        (party_get_position, pos1, "p_main_party"),
        (map_get_water_position_around_position, pos2, pos1, 6),
        (party_set_position, "p_main_party", pos2),
        (assign, "$g_main_ship_party", -1),
        (change_screen_return),
        ]),

      ]
  ),

  (
    "town_tournament_lost",0,"You have been eliminated from the tournament.",
    "none",
    [
        ],
    [
      ("continue", [], "Continue...",
       [(jump_to_menu, "mnu_town_tournament_won_by_another"),
        ]),
    ]
  ),

  (
    "town_tournament_won",mnf_disable_all_keys,"You have won the tournament of {s3}! You are filled with pride as the crowd cheers your name. In addition to honor, fame and glory, you earn a prize of {reg9} thaler. {s8}",
    "none",
    [
        (str_store_party_name, s3, "$current_town"),
        (call_script, "script_change_troop_renown", "trp_player", 20),
        (call_script, "script_change_player_relation_with_center", "$current_town", 1),   
        (assign, reg9, 200),
        (add_xp_to_troop, 250, "trp_player"),
        (troop_add_gold, "trp_player", reg9),
        (str_clear, s8),
        (store_add, ":total_win", "$g_tournament_bet_placed", "$g_tournament_bet_win_amount"),
        (try_begin),
          (gt, "$g_tournament_bet_win_amount", 0),
          (assign, reg8, ":total_win"),
          (str_store_string, s8, "@Moreover, you earn {reg8} denars from the clever bets you placed on yourself..."),
        (try_end),
        (troop_add_gold, "trp_player", ":total_win"),
        (assign, ":player_odds_sub", 0),
        (store_div, ":player_odds_sub", "$g_tournament_bet_win_amount", 5),
        (party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
        (val_sub, ":player_odds", ":player_odds_sub"),
        (val_max, ":player_odds", 250),
        (party_set_slot, "$current_town", slot_town_player_odds, ":player_odds"),
        (call_script, "script_play_victorious_sound"),
        ],
    [
      ("continue", [], "Continue...",
       [(jump_to_menu, "mnu_town"),
        ]),
    ]
  ),
  
  (
    "town_tournament_won_by_another",mnf_disable_all_keys,"As the only {reg3?fighter:man} to remain undefeated this day, {s1} wins the lists and the glory of the tournament.",
    "none",
    [   (call_script, "script_get_num_tournament_participants"),
        (store_sub, ":needed_to_remove_randomly", reg0, 1),
        (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
        (call_script, "script_sort_tournament_participant_troops"),
        (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
        (str_store_troop_name, s1, ":winner_troop"),
        (try_begin),
          (troop_is_hero, ":winner_troop"),
          (call_script, "script_change_troop_renown", ":winner_troop", 20),
        (try_end),
        (troop_get_type, reg3, ":winner_troop"),
        ],
    [
      ("continue", [], "Continue...",
       [(jump_to_menu, "mnu_town"),
        ]),
    ]
  ),

  (
    "town_tournament",mnf_disable_all_keys,"{s1}You are at tier {reg0} of the tournament, with {reg1} participants remaining. In the next round, there will be {reg2} teams with {reg3} {reg4?fighters:fighter} each.",
    "none",
    [
        (party_set_slot, "$current_town", slot_town_has_tournament, 0), #No way to return back if this menu is left
        (call_script, "script_sort_tournament_participant_troops"),#Moving trp_player to the top of the list
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (try_begin),
          (neg|troop_slot_eq, "trp_tournament_participants", 0, 0),#Player is defeated

          (assign, ":player_odds_add", 0),
          (store_div, ":player_odds_add", "$g_tournament_bet_placed", 5),
          (party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
          (val_add, ":player_odds", ":player_odds_add"),
          (val_min, ":player_odds", 4000),
          (party_set_slot, "$current_town", slot_town_player_odds, ":player_odds"),

          (jump_to_menu, "mnu_town_tournament_lost"),
        (else_try),
          (eq, ":num_participants", 1),#Tournament won
          (jump_to_menu, "mnu_town_tournament_won"),
        (else_try),
          (try_begin),
            (le, "$g_tournament_next_num_teams", 0),
            (call_script, "script_get_random_tournament_team_amount_and_size"),
            (assign, "$g_tournament_next_num_teams", reg0),
            (assign, "$g_tournament_next_team_size", reg1),
          (try_end),
          (assign, reg2, "$g_tournament_next_num_teams"),
          (assign, reg3, "$g_tournament_next_team_size"),
          (store_sub, reg4, reg3, 1),
          (str_clear, s1),
          (try_begin),
            (eq, "$g_tournament_player_team_won", 1),
            (str_store_string, s1, "@Victory is yours! You have won this melee, but now you must prepare yourself for the next round. "),
          (else_try),
            (eq, "$g_tournament_player_team_won", 0),
            (str_store_string, s1, "@You have been bested in this melee, but the master of ceremonies declares a recognition of your skill and bravery, allowing you to take part in the next round. "),
          (try_end),
          (assign, reg1, ":num_participants"),
          (store_add, reg0, "$g_tournament_cur_tier", 1),
        (try_end),
        ],
    [
      ("tournament_view_participants", [],"View participants.",
       [(jump_to_menu, "mnu_tournament_participants"),
        ]),
      ("tournament_bet", [(neq, "$g_tournament_cur_tier", "$g_tournament_last_bet_tier")],"Place a bet on yourself.",
       [(jump_to_menu, "mnu_tournament_bet"),
        ]),
      ("tournament_join_next_fight", [],"Fight in the next round.",
       [
           (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
           (modify_visitors_at_site, ":arena_scene"),
           (reset_visitors),
           #Assuming that there are enough participants for the teams
           (val_add, "$g_tournament_cur_tier", 1),
		   
           (store_mul, "$g_tournament_num_participants_for_fight", "$g_tournament_next_num_teams", "$g_tournament_next_team_size"),
           (troop_set_slot, "trp_tournament_participants", 0, -1),#Removing trp_player from the list
           (troop_set_slot, "trp_temp_array_a", 0, "trp_player"),
           (try_for_range, ":slot_no", 1, "$g_tournament_num_participants_for_fight"),
             (call_script, "script_get_random_tournament_participant"),
             (troop_set_slot, "trp_temp_array_a", ":slot_no", reg0),
           (try_end),
           (call_script, "script_shuffle_troop_slots", "trp_temp_array_a", 0, "$g_tournament_num_participants_for_fight"),


           (try_for_range, ":slot_no", 0, 4),#shuffle teams
             (troop_set_slot, "trp_temp_array_b", ":slot_no", ":slot_no"),
           (try_end),
           (call_script, "script_shuffle_troop_slots", "trp_temp_array_b", 0, 4),

           (assign, ":cur_slot", 0),
           (try_for_range, ":cur_team_offset", 0, "$g_tournament_next_num_teams"),
             (troop_get_slot, ":cur_team", "trp_temp_array_b", ":cur_team_offset"),
           
             (try_for_range, ":slot_no", 0, 8),#shuffle entry_points
               (troop_set_slot, "trp_temp_array_c", ":slot_no", ":slot_no"),
             (try_end),
             (call_script, "script_shuffle_troop_slots", "trp_temp_array_c", 0, 8),
           
             (try_for_range, ":cur_index", 0, "$g_tournament_next_team_size"),
               (store_mul, ":cur_entry_point", ":cur_team", 8),
               (troop_get_slot, ":entry_offset", "trp_temp_array_c", ":cur_index"),
               (val_add, ":cur_entry_point", ":entry_offset"),
               (troop_get_slot, ":troop_no", "trp_temp_array_a", ":cur_slot"),
               (set_visitor, ":cur_entry_point", ":troop_no"),
               (val_add, ":cur_slot", 1),
             (try_end),
           (try_end),

           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),
           
           (assign, "$g_mt_mode", abm_tournament),

           (party_get_slot, ":town_original_faction", "$current_town", slot_center_original_faction),
           (assign, ":town_index_within_faction", 0),
           (assign, ":end_cond", towns_end),
           (try_for_range, ":cur_town", towns_begin, ":end_cond"),
             (try_begin),
               (eq, ":cur_town", "$current_town"),
               (assign, ":end_cond", 0), #break
             (else_try),
               (party_slot_eq, ":cur_town", slot_center_original_faction, ":town_original_faction"),
               (val_add, ":town_index_within_faction", 1),
             (try_end),
           (try_end),
           (try_begin),
             (eq, ":town_original_faction", "fac_kingdom_1"),
             #Swadia
             (store_mod, ":mod", ":town_index_within_faction", 4),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 100, 100, 0, 0, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
             (else_try),
               (eq, ":mod", 2),
               (call_script, "script_set_items_for_tournament", 100, 0, 100, 0, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
             (else_try),
               (eq, ":mod", 3),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 40, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
             (try_end),
           (else_try),
             (eq, ":town_original_faction", "fac_kingdom_2"),
             #Vaegirs
             (store_mod, ":mod", ":town_index_within_faction", 4),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 0, 0, 0, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 100, 50, 0, 0, 0, 20, 30, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
             (else_try),
               (eq, ":mod", 2),
               (call_script, "script_set_items_for_tournament", 100, 0, 50, 0, 0, 20, 30, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
             (else_try),
               (eq, ":mod", 3),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 30, 0, 60, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
             (try_end),
           (else_try),
             (eq, ":town_original_faction", "fac_kingdom_3"),
             #Khergit
             (store_mod, ":mod", ":town_index_within_faction", 2),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 100, 0, 0, 0, 0, 40, 60, 0, "itm_arena_tunic_red", "itm_steppe_helmet_red"),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 100, 50, 25, 0, 0, 30, 50, 0, "itm_arena_tunic_red", "itm_steppe_helmet_red"),
             (try_end),
           (else_try),
             (eq, ":town_original_faction", "fac_kingdom_4"),
             #Nords
             (store_mod, ":mod", ":town_index_within_faction", 3),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 0, 0, 0, 0, "itm_arena_armor_red", -1),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 50, 0, 0, 0, "itm_arena_armor_red", -1),
             (else_try),
               (eq, ":mod", 2),
               (call_script, "script_set_items_for_tournament", 40, 0, 0, 100, 0, 0, 0, 0, "itm_arena_armor_red", -1),
             (try_end),
           (else_try),
             #Rhodoks
             (call_script, "script_set_items_for_tournament", 25, 100, 60, 0, 30, 0, 30, 50, "itm_arena_tunic_red", "itm_arena_helmet_red"),
           (try_end),
           (set_jump_mission, "mt_arena_melee_fight"),
           (jump_to_scene, ":arena_scene"),
           (change_screen_mission),
        ]),
      ("leave_tournament",[],"Withdraw from the tournament.",
       [
           (jump_to_menu, "mnu_tournament_withdraw_verify"),
        ]),
    ]
  ),

  (
    "tournament_withdraw_verify",0,"Are you sure you want to withdraw from the tournament?",
    "none",
    [],
    [
      ("tournament_withdraw_yes", [],"Yes. This is pointless affectation.",
       [(jump_to_menu, "mnu_town_tournament_won_by_another"),
        ]),
      ("tournament_withdraw_no", [],"No, not so long as there is a chance of victory!",
       [(jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),

  (
    "tournament_bet",0,
    "The odds against you are {reg5} to {reg6}.{reg1? You have already bet {reg1} thaler on yourself, and if you win, you will earn {reg2}.:} How much do you want to bet?",
    "none",
    [
      (assign, reg1, "$g_tournament_bet_placed"),
      (store_add, reg2, "$g_tournament_bet_win_amount", "$g_tournament_bet_placed"),
      (call_script, "script_get_win_amount_for_tournament_bet"),
      (assign, ":player_odds", reg0),
      (assign, ":min_dif", 100000),
      (assign, ":min_dif_divisor", 1),
      (assign, ":min_dif_multiplier", 1),
      (try_for_range, ":cur_multiplier", 1, 50),
        (try_for_range, ":cur_divisor", 1, 50),
          (store_mul, ":result", 100, ":cur_multiplier"),
          (val_div, ":result", ":cur_divisor"),
          (store_sub, ":difference", ":player_odds", ":result"),
          (val_abs, ":difference"),
          (lt, ":difference", ":min_dif"),
          (assign, ":min_dif", ":difference"),
          (assign, ":min_dif_divisor", ":cur_divisor"),
          (assign, ":min_dif_multiplier", ":cur_multiplier"),
        (try_end),
      (try_end),
      (assign, reg5, ":min_dif_multiplier"),
      (assign, reg6, ":min_dif_divisor"),
      ],
    [
      ("bet_100_denars", [(store_troop_gold, ":gold", "trp_player"),
                          (ge, ":gold", 100)
                          ],"100 thaler.",
       [
         (assign, "$temp", 100),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_50_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 50)
                         ],"50 thaler.",
       [
         (assign, "$temp", 50),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_20_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 20)
                         ],"20 thaler.",
       [
         (assign, "$temp", 20),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_10_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 10)
                         ],"10 thaler.",
       [
         (assign, "$temp", 10),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_5_denars", [(store_troop_gold, ":gold", "trp_player"),
                        (ge, ":gold", 5)
                        ],"5 thaler.",
       [
         (assign, "$temp", 5),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("go_back_dot", [], "Go back.",
       [
         (jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),

  (
    "tournament_bet_confirm",0,"If you bet {reg1} thaler, you will earn {reg2} thaler if you win the tournament. Is that as you wish?",
    "none",
    [
      (call_script, "script_get_win_amount_for_tournament_bet"),
      (assign, ":win_amount", reg0),
      (val_mul, ":win_amount", "$temp"),
      (val_div, ":win_amount", 100),
      (assign, reg1, "$temp"),
      (assign, reg2, ":win_amount"),
      ],
    [
      ("tournament_bet_accept", [],"Absolutely.",
       [
         (call_script, "script_tournament_place_bet", "$temp"),
         (jump_to_menu, "mnu_town_tournament"),
         ]),
      ("tournament_bet_cancel", [],"No.",
       [
         (jump_to_menu, "mnu_tournament_bet"),
         ]),
    ]
  ),
  
  (
    "tournament_participants",0,"You ask one of the criers for the names of the tournament participants. They are:^{s11}",
    "none",
    [
        (str_clear, s11),
        (call_script, "script_sort_tournament_participant_troops"),
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (try_for_range, ":cur_slot", 0, ":num_participants"),
          (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
          (str_store_troop_name, s12, ":troop_no"),
          (str_store_string, s11, "@{s11}^{s12}"),
        (try_end),
        ],
    [
      ("go_back_dot", [], "Go back.",
       [(jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),


  (
    "collect_taxes",mnf_disable_all_keys,"As the best trader in the party ({reg2} trade skill), {reg3?you expect:{s1} expects} that collecting taxes here will require {reg4} days...",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
     (assign, ":max_skill", reg0),
     (assign, reg2, reg0),
     (assign, ":max_skill_owner", reg1),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (assign, ":tax_quest_expected_revenue", 3000),
     (try_begin),
       (party_slot_eq, "$current_town", slot_party_type, spt_town),
       (assign, ":tax_quest_expected_revenue", 6000),
     (try_end),

     (try_begin),
       (quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 0),
       (store_add, ":max_skill_plus_thirty", ":max_skill", 30),
       (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (store_div, "$qst_collect_taxes_total_hours", 24* 7 * 30, ":max_skill_plus_thirty"),
       (else_try),
         #Village
         (store_div, "$qst_collect_taxes_total_hours", 24 * 3 * 30, ":max_skill_plus_thirty"),
       (try_end),

       (call_script, "script_party_count_fit_for_battle", "p_main_party"),
       (val_add, reg0, 20),
       (val_mul, "$qst_collect_taxes_total_hours", 20),
       (val_div, "$qst_collect_taxes_total_hours", reg0),

     
       (quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, "$qst_collect_taxes_total_hours"),
       (store_div, ":menu_begin_time", "$qst_collect_taxes_total_hours", 20),#between %5-%25
       (store_div, ":menu_end_time", "$qst_collect_taxes_total_hours", 4),
       (assign, ":unrest_begin_time", ":menu_end_time"),#between %25-%75
       (store_mul, ":unrest_end_time", "$qst_collect_taxes_total_hours", 3),
       (val_div, ":unrest_end_time", 4),

       (val_mul, ":tax_quest_expected_revenue", 2),
       (store_div, "$qst_collect_taxes_hourly_income", ":tax_quest_expected_revenue", "$qst_collect_taxes_total_hours"),
     
       (store_random_in_range, "$qst_collect_taxes_menu_counter", ":menu_begin_time", ":menu_end_time"),
       (store_random_in_range, "$qst_collect_taxes_unrest_counter", ":unrest_begin_time", ":unrest_end_time"),
       (assign, "$qst_collect_taxes_halve_taxes", 0),
     (try_end),
     (quest_get_slot, ":target_hours", "qst_collect_taxes", slot_quest_target_amount),
     (store_div, ":target_days", ":target_hours", 24),
     (val_mul, ":target_days", 24),
     (try_begin),
       (lt, ":target_days", ":target_hours"),
       (val_add, ":target_days", 24),
     (try_end),
     (val_div, ":target_days", 24),
     (assign, reg4, ":target_days"),
     ],
    [
      ("start_collecting", [],"Start collecting.",
       [(assign, "$qst_collect_taxes_currently_collecting", 1),
        (try_begin),
          (quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 0),
          (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 1),
        (try_end),
        (rest_for_hours_interactive, 1000, 5, 0), #rest while not attackable
        (assign,"$auto_enter_town","$current_town"),
        (assign, "$g_town_visit_after_rest", 1),
        (change_screen_return),
        ]),
      ("collect_later", [],"Put it off until later.",
       [(try_begin),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
        ]),
    ]
  ),

  (
    "collect_taxes_complete",mnf_disable_all_keys,"You've collected {reg3} thaler in taxes from {s3}. You are to bring the collected amount to {s19}.",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     (quest_get_slot, ":quest_giver", "qst_collect_taxes", slot_quest_giver_troop),
     (str_store_troop_name, s19, ":quest_giver"),
     (quest_get_slot, reg3, "qst_collect_taxes", slot_quest_gold_reward),
     (try_begin),
       (eq, "$qst_collect_taxes_halve_taxes", 0),
       (call_script, "script_change_player_relation_with_center", "$current_town", -2),   
     (try_end),
     (call_script, "script_succeed_quest", "qst_collect_taxes"),
     ],
    [
      ("continue", [], "Continue...",
       [(change_screen_return),
        ]),
    ]
  ),

  (
    "collect_taxes_rebels_killed",0,"Your swift action and strong arm have successfully put down the revolt. Surely now anyone with a mind to rebel against you will think better of it.",
    "none",
    [
    ],
    [
      ("continue", [], "Continue...",
       [(change_screen_map),
        ]),
    ]
  ),

  (
    "collect_taxes_failed",mnf_disable_all_keys,"You could collect only {reg3} thaler as tax from {s3} before revolt broke out. {s1} won't be happy, but some silver is better than none at all...",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     (quest_get_slot, ":quest_giver", "qst_collect_taxes", slot_quest_giver_troop),
     (str_store_troop_name, s1, ":quest_giver"),
     (quest_get_slot, reg3, "qst_collect_taxes", slot_quest_gold_reward),
     (call_script, "script_fail_quest", "qst_collect_taxes"),
     (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
     (rest_for_hours, 0, 0, 0), #stop resting
     ],
    [
      ("continue", [], "Continue...",
       [(change_screen_map),
        ]),
    ]
  ),

  (
    "collect_taxes_revolt_warning",0,"The people of {s3} are outraged at your demands, and decry it as nothing more than extortion. They're becoming very restless, and they may react violently if you continue pressing them.",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     ],
    [
      ("continue_collecting_taxes", [],"Ignore their complaints and continue.",
       [(change_screen_return),]),
      ("halve_taxes", [(quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
                       (str_store_troop_name, s1, ":quest_giver_troop"),],"Agree to reduce your collection by half. ({s1} may be upset)",
       [(assign, "$qst_collect_taxes_halve_taxes", 1),
        (change_screen_return),
        ]),
    ]
  ),

  (
    "collect_taxes_revolt",0,"You are interrupted while collecting the taxes at {s3}. A large band of angry {reg9?peasants:townsmen} is marching nearer, shouting about the exorbitant taxes, and waving torches and weapons. It looks as though they aim to fight!",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     (assign, reg9, 0),
     (try_begin),
       (party_slot_eq, "$current_town", slot_party_type, spt_village),
       (assign, reg9, 1),
     (try_end),
     ],
    [
      ("continue", [], "Continue...",
       [(set_jump_mission,"mt_back_alley_revolt"),
        (quest_get_slot, ":target_center", "qst_collect_taxes", slot_quest_target_center),
        (try_begin),
          (party_slot_eq, ":target_center", slot_party_type, spt_town),
          (party_get_slot, ":town_alley", ":target_center", slot_town_alley),
        (else_try),
          (party_get_slot, ":town_alley", ":target_center", slot_castle_exterior),
        (try_end),
        (modify_visitors_at_site,":town_alley"),
        (reset_visitors),
        (assign, ":num_rebels", 6),
        (store_character_level, ":level", "trp_player"),
        (val_div, ":level", 5),
        (val_add, ":num_rebels", ":level"),
		(val_clamp, ":num_rebels", 0, 50),
        (set_visitors, 1, "trp_tax_rebel", ":num_rebels"),
        (jump_to_scene,":town_alley"),
        (change_screen_mission),
        ]),
    ]
  ),

# They must learn field discipline and the steadiness to follow orders in combat before they can be thought to use arms.",
  (
    "train_peasants_against_bandits",0,"As the best instructor in the party ({reg2} training skill), {reg3?you expect:{s1} expects} that getting some peasants ready for practice will take {reg4} hours.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
     (assign, ":max_skill", reg0),
     (assign, reg2, reg0),
     (assign, ":max_skill_owner", reg1),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (store_sub, ":needed_hours", 20, ":max_skill"),
     (val_mul, ":needed_hours", 3),
     (val_div, ":needed_hours", 5),
     (store_sub, reg4, ":needed_hours", "$qst_train_peasants_against_bandits_num_hours_trained"),
     ],
    [
      ("make_preparation", [],"Train them.",
       [
         (assign, "$qst_train_peasants_against_bandits_currently_training", 1),
         (rest_for_hours_interactive, 1000, 5, 0), #rest while not attackable
         (assign, "$auto_enter_town", "$current_town"),
         (assign, "$g_town_visit_after_rest", 1),
         (change_screen_return),
         ]),
      ("train_later", [],"Put it off until later.",
       [
         (jump_to_menu, "mnu_village"),
        ]),
    ]
  ), 

  (
    "train_peasants_against_bandits_ready",0,"You put the peasants through the basics of soldiering, discipline, and obedience. You believe that {reg0} of them {reg1?have:has} fully grasped the training, while {reg1?are:is} ready for some practice.",
    "none",
    [
      (store_character_level, ":level", "trp_player"),
      (val_div, ":level", 10),
      (val_add, ":level", 1),
      (quest_get_slot, ":quest_target_amount", "qst_train_peasants_against_bandits", slot_quest_target_amount),
      (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
      (val_sub, ":quest_target_amount", ":quest_current_state"),
      (assign, ":max_random", ":level"),
      (val_min, ":max_random", ":quest_target_amount"),
      (val_add, ":max_random", 1),
      (store_random_in_range, ":random_number", 1, ":max_random"),
      (assign, "$g_train_peasants_against_bandits_num_peasants", ":random_number"),
      (assign, reg0, ":random_number"),
      (store_sub, reg1, ":random_number", 1),
      (str_store_troop_name_by_count, s0, "trp_trainee_peasant", ":random_number"),
     ],
    [
      ("peasant_start_practice", [],"Begin the practice fight.",
       [
         (set_jump_mission,"mt_village_training"),
         (quest_get_slot, ":target_center", "qst_train_peasants_against_bandits", slot_quest_target_center),
         (party_get_slot, ":village_scene", ":target_center", slot_castle_exterior),
         (modify_visitors_at_site, ":village_scene"),
         (reset_visitors),
         (set_visitor, 0, "trp_player"),
         (set_visitors, 1, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
         (set_jump_entry, 11),
         (jump_to_scene, ":village_scene"),
         (jump_to_menu, "mnu_train_peasants_against_bandits_training_result"),
         (music_set_situation, 0),
         (change_screen_mission),
         ]),
      ]
    ),

  (
    "train_peasants_against_bandits_training_result",mnf_disable_all_keys,"{s0}",
    "none",
    [
      (assign, reg5, "$g_train_peasants_against_bandits_num_peasants"),
      (str_store_troop_name_by_count, s0, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
      (try_begin),
        (eq, "$g_train_peasants_against_bandits_training_succeeded", 0),
        (str_store_string, s0, "@You were beaten. The peasants are heartened by their success, but the lesson you wanted to teach them probably didn't get through..."),
      (else_try),
        (str_store_string, s0, "@After beating your last opponent, you explain to the peasants how to better defend themselves against such an attack. Hopefully they'll take the experience on board and will be prepared next time."),
        (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
        (val_add, ":quest_current_state", "$g_train_peasants_against_bandits_num_peasants"),
        (quest_set_slot, "qst_train_peasants_against_bandits", slot_quest_current_state, ":quest_current_state"),
      (try_end),
     ],
    [
      ("continue", [], "Continue...",
       [
         (try_begin),
           (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
           (quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_amount, ":quest_current_state"),
           (jump_to_menu, "mnu_train_peasants_against_bandits_attack"),
         (else_try),
           (change_screen_map),
         (try_end),
         ]),
      ]
    ),

  (
    "train_peasants_against_bandits_attack",0,"As you were training the militia, a man from the village runs up to you, shouting in alarm. The bandits have been spotted on the horizon, riding hard for {s3}. The elder begs that you organize your newly-trained militia and face them.",
    "none",
    [
	(str_store_party_name, s3, "$current_town"),
     ],
    [
      ("peasants_against_bandits_attack_resist", [],"Prepare to fight!",
       [
        (store_random_in_range, ":random_no", 0, 3),
        (try_begin),
          (eq, ":random_no", 0),
          (assign, ":bandit_troop", "trp_bandit"),
        (else_try),
          (eq, ":random_no", 1),
          (assign, ":bandit_troop", "trp_mountain_bandit"),
        (else_try),
          (assign, ":bandit_troop", "trp_forest_bandit"),
        (try_end),
        (party_get_slot, ":scene_to_use", "$g_encountered_party", slot_castle_exterior),
        (modify_visitors_at_site, ":scene_to_use"),
        (reset_visitors),
        (store_character_level, ":level", "trp_player"),
        (val_div, ":level", 2),
        (store_add, ":min_bandits", ":level", 16),
        (store_add, ":max_bandits", ":min_bandits", 6),
        (store_random_in_range, ":random_no", ":min_bandits", ":max_bandits"),
        (set_visitors, 0, ":bandit_troop", ":random_no"),
        (assign, ":num_villagers", ":max_bandits"),
        (set_visitors, 2, "trp_trainee_peasant", ":num_villagers"),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission,"mt_village_attack_bandits"),
        (jump_to_scene, ":scene_to_use"),
        (assign, "$g_next_menu", "mnu_train_peasants_against_bandits_attack_result"),
        (jump_to_menu, "mnu_battle_debrief"),
        (assign, "$g_mt_mode", vba_after_training),
        (change_screen_mission),
        ]),
      ]
    ),

  (
    "train_peasants_against_bandits_attack_result",mnf_scale_picture|mnf_disable_all_keys,"{s9}",
    "none",
    [
      (try_begin),
        (eq, "$g_battle_result", 1),
        (str_store_string, s9, "@The bandits are broken!\
 Those few who remain alive and conscious run off with their tails between their legs,\
 terrified of the peasants and their new champion."),
	(call_script, "script_succeed_quest", "qst_train_peasants_against_bandits"),
        (jump_to_menu, "mnu_train_peasants_against_bandits_success"),
      (else_try),
        (call_script, "script_fail_quest", "qst_train_peasants_against_bandits"),
        (str_store_string, s9, "@Try as you might, you could not defeat the bandits.\
 Infuriated, they raze the village to the ground to punish the peasants,\
 and then leave the burning wasteland behind to find greener pastures to plunder."),
        (set_background_mesh, "mesh_pic_looted_village"),
      (try_end),
     ],
    [
      ("continue", [], "Continue...",
       [(try_begin),
          (call_script, "script_village_set_state",  "$current_town", svs_looted),

          (party_add_particle_system, "$current_town", "psys_map_village_fire"), #new
          (party_add_particle_system, "$current_town", "psys_map_village_fire_smoke"), #new
          (party_set_icon, "$current_town", "icon_village_burnt_a"), #new
          (party_set_slot, "$current_town", slot_village_smoke_added, 1), #new
		
          (party_set_slot, "$current_town", slot_village_raid_progress, 100), #was 0
          (party_set_slot, "$current_town", slot_village_recover_progress, 0),

          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
          (call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
        (try_end),
        (change_screen_map),
	 ]),
      ]
    ),

   (
    "train_peasants_against_bandits_success",mnf_disable_all_keys,"The bandits are broken! The few who remain run off with their tails between their legs, terrified by the peasants and their new champion. The villagers have little left in the way of wealth after their ordeal, but they offer you all they can find to show their gratitude.",
    "none",
    [(party_clear, "p_temp_party"),
     (call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
     (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 4),

     (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
     (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 50),
        (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
     (try_end),
     (call_script, "script_add_log_entry", logent_helped_peasants, "trp_player",  "$current_town", -1, -1),
    ],
    [
      ("village_bandits_defeated_accept",[],"Take it as your just due.",[(jump_to_menu, "mnu_auto_return_to_map"),
                                                                         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
                                                                         (troop_sort_inventory, ":merchant_troop"),
                                                                         (change_screen_loot, ":merchant_troop"),
                                                                       ]),
      ("village_bandits_defeated_cont",[],  "Refuse, stating that they need these items more than you do.",[
	  (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
      (call_script, "script_change_player_honor", 1),
      (change_screen_map)]),
    ],
  ),


  (
    "disembark",0,"Do you wish to disembark?",
    "none",
    [],
    [
      ("disembark_yes", [], "Yes.",
       [(assign, "$g_player_icon_state", pis_normal),
        (party_set_flags, "p_main_party", pf_is_ship, 0),
        (party_get_position, pos1, "p_main_party"),
        (party_set_position, "p_main_party", pos0),
        (try_begin),
          (le, "$g_main_ship_party", 0),
          (set_spawn_radius, 0),
          (spawn_around_party, "p_main_party", "pt_none"),
          (assign, "$g_main_ship_party", reg0),
          (party_set_flags, "$g_main_ship_party", pf_is_static|pf_always_visible|pf_hide_defenders|pf_is_ship, 1),
          (str_store_troop_name, s1, "trp_player"),
          (party_set_name, "$g_main_ship_party", "@{s1}'s Ship"),
          (party_set_icon, "$g_main_ship_party", "icon_ship"),
          (party_set_slot, "$g_main_ship_party", slot_party_type, spt_ship),
        (try_end),
        (enable_party, "$g_main_ship_party"),
        (party_set_position, "$g_main_ship_party", pos0),
        (party_set_icon, "$g_main_ship_party", "icon_ship_on_land"),
        (assign, "$g_main_ship_party", -1),
        (change_screen_return),
        ]),
      ("disembark_no", [], "No.",
       [(change_screen_return),
        ]),
    ]
  ),

  (
    "ship_reembark",0,"Do you wish to embark?",
    "none",
    [],
    [
      ("reembark_yes", [],"Yes.",
       [(assign, "$g_player_icon_state", pis_ship),
        (party_set_flags, "p_main_party", pf_is_ship, 1),
        (party_get_position, pos1, "p_main_party"),
        (map_get_water_position_around_position, pos2, pos1, 6),
        (party_set_position, "p_main_party", pos2),
        (assign, "$g_main_ship_party", "$g_encountered_party"),
        (disable_party, "$g_encountered_party"),
        (change_screen_return),
        ]),
      ("reembark_no", [],"No.",
       [(change_screen_return),
        ]),
    ]
  ),

  (
    "center_reports",0,
    "Town Name: {s1}^Rent Income: {reg1} thaler^Tariff Income: {reg2} thaler^Food Stock: enough for {reg3} days",
    "none",
    [(party_get_slot, ":town_food_store", "$g_encountered_party", slot_party_food_store),
     (call_script, "script_center_get_food_consumption", "$g_encountered_party"),
     (assign, ":food_consumption", reg0),
       (store_div, reg3, ":town_food_store", ":food_consumption"),
     (str_store_party_name, s1, "$g_encountered_party"),
     (party_get_slot, reg1, "$g_encountered_party", slot_center_accumulated_rents),
     (party_get_slot, reg2, "$g_encountered_party", slot_center_accumulated_tariffs),
     ],
    [
      ("to_price_and_productions", [],"Show prices and productions.",
       [(jump_to_menu, "mnu_price_and_production"),
        ]),
      
      ("go_back_dot",[],"Go back.",
       [(try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_town"),
        (try_end),
        ]),
    ]
  ),
    
  (
    "price_and_production",0,"Productions are:^{s1}^^Price factors are:^{s2}",
    "none",
    [(str_store_string, s1, "@ "),
     (str_store_string, s2, "@ "),
     (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
       (store_sub, ":cur_good_slot", ":cur_good", trade_goods_begin),
       (val_add, ":cur_good_slot", slot_town_trade_good_productions_begin),
       (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
       (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
       (party_get_slot, ":production", "$g_encountered_party", ":cur_good_slot"),
       (party_get_slot, ":price", "$g_encountered_party", ":cur_good_price_slot"),
       (str_store_item_name, s3, ":cur_good"),
       (assign, reg1, ":production"),
       (str_store_string, s1, "@^{s3} = {reg1}{s1}"),
       (assign, reg1, ":price"),
       (str_store_string, s2, "@^{s3} = {reg1}{s2}"),
     (try_end),
     ],
    [
      ("go_back_dot",[],"Go back.",
       [(try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_town"),
        (try_end),
        ]),
    ]
  ),
  
  (
    "town_trade",0,"You head towards the marketplace.",
    "none",
    [],
    [
      ("assess_prices",
       [
         (store_faction_of_party, ":current_town_faction", "$current_town"),
         (store_relation, ":reln", ":current_town_faction", "fac_player_supporters_faction"),
         (ge, ":reln", 0),
         ],"Assess the local prices.",
       [
           (jump_to_menu,"mnu_town_trade_assessment_begin"),
        ]),
      ("trade_with_arms_merchant",[(party_slot_ge, "$current_town", slot_town_weaponsmith, 1)],"Trade with the arms merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_weaponsmith),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_armor_merchant",[(party_slot_ge, "$current_town", slot_town_armorer, 1)],"Trade with the armor merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_armorer),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_horse_merchant",[(party_slot_ge, "$current_town", slot_town_horse_merchant, 1)],"Trade with the horse merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_horse_merchant),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_goods_merchant",[(party_slot_ge, "$current_town", slot_town_merchant, 1)],"Trade with the goods merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_merchant),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("back_to_town_menu",[],"Return...",
       [
           (jump_to_menu,"mnu_town"),
        ]),
    ]
  ),

  (
   "town_trade_assessment_begin",0,"You overhear discussions about the price of trade goods across the area, hoping to work out the best deals.",
    "none",
    [],
    [
      ("continue",[],"Continue...",
       [
           (assign,"$auto_enter_town", "$current_town"),
           (assign, "$g_town_assess_trade_goods_after_rest", 1),
           (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
           (val_div, reg0, 2),
           (store_sub, ":num_hours", 6, reg0),
           (assign, "$g_last_rest_center", "$current_town"),
           (assign, "$g_last_rest_payment_until", -1),
           (rest_for_hours, ":num_hours", 5, 0), #rest while not attackable
           (change_screen_return),
        ]),
    ]
  ),

  (
    "town_trade_assessment",mnf_disable_all_keys,"As the best trader in the party ({reg2} trade skill), {reg3?you try to figure out:{s1} tries to figure out} the best goods to trade in. {s2}",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),

     (assign, ":num_best_results", 0),
     (assign, ":best_result_1_item", -1),
     (assign, ":best_result_1_town", -1),
     (assign, ":best_result_1_profit", 0),
     (assign, ":best_result_2_item", -1),
     (assign, ":best_result_2_town", -1),
     (assign, ":best_result_2_profit", 0),
     (assign, ":best_result_3_item", -1),
     (assign, ":best_result_3_town", -1),
     (assign, ":best_result_3_profit", 0),
     (assign, ":best_result_4_item", -1),
     (assign, ":best_result_4_town", -1),
     (assign, ":best_result_4_profit", 0),
     (assign, ":best_result_5_item", -1),
     (assign, ":best_result_5_town", -1),
     (assign, ":best_result_5_profit", 0),

     (store_sub, ":num_towns", walled_centers_end, walled_centers_begin),
     (store_sub, ":num_goods", trade_goods_end, trade_goods_begin),
     (store_mul, ":max_iteration", ":num_towns", ":num_goods"),
     (val_mul, ":max_iteration", ":max_skill"),
     (val_div, ":max_iteration", 20),

     (assign, ":org_encountered_party", "$g_encountered_party"),

     (try_for_range, ":unused", 0, ":max_iteration"),
       (store_random_in_range, ":random_trade_good", trade_goods_begin, trade_goods_end),

       (store_random_in_range, ":random_town", towns_begin, towns_end),

       (party_get_slot, ":cur_merchant", ":org_encountered_party", slot_town_merchant),       
	   (assign, ":num_items_in_town_inventory", 0),
       (try_for_range, ":i_slot", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
         (troop_get_inventory_slot, ":slot_item", ":cur_merchant", ":i_slot"),
         (try_begin),
           (eq, ":slot_item", ":random_trade_good"),           
		   (val_add, ":num_items_in_town_inventory", 1),
         (try_end),
       (try_end),

       (ge, ":num_items_in_town_inventory", 1),

       (assign, ":already_best", 0),
       
	   (try_begin),
         (eq, ":random_trade_good", ":best_result_1_item"),
         (eq, ":random_town", ":best_result_1_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_2_item"),
         (eq, ":random_town", ":best_result_2_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_3_item"),
         (eq, ":random_town", ":best_result_3_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_4_item"),
         (eq, ":random_town", ":best_result_4_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_5_item"),
         (eq, ":random_town", ":best_result_5_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (assign, ":pass", 0),
	   (try_begin),
         (eq, ":already_best", 0),
		 (lt, ":num_items_in_town_inventory", 5),
		 (assign, ":pass", 1),
	   (else_try),
         (le, ":already_best", 1),
		 (ge, ":num_items_in_town_inventory", 5),
		 (assign, ":pass", 1),
	   (try_end),

	   (eq, ":pass", 1),

       (store_item_value, ":random_trade_good_price", ":random_trade_good"),
       (assign, "$g_encountered_party", ":org_encountered_party"),
       (call_script, "script_game_get_item_buy_price_factor", ":random_trade_good"),
       (store_mul, ":random_trade_good_buy_price", ":random_trade_good_price", reg0),
       (val_div, ":random_trade_good_buy_price", 100),
       (val_max, ":random_trade_good_buy_price", 1),
       (assign, "$g_encountered_party", ":random_town"),
       (call_script, "script_game_get_item_sell_price_factor", ":random_trade_good"),
       (store_mul, ":random_trade_good_sell_price", ":random_trade_good_price", reg0),
       (val_div, ":random_trade_good_sell_price", 100),
       (val_max, ":random_trade_good_sell_price", 1),
       (store_sub, ":difference", ":random_trade_good_sell_price", ":random_trade_good_buy_price"),

       (try_begin),
	     (this_or_next|eq, ":best_result_1_item", ":random_trade_good"),
		 (this_or_next|eq, ":best_result_2_item", ":random_trade_good"),
		 (this_or_next|eq, ":best_result_3_item", ":random_trade_good"),
		 (this_or_next|eq, ":best_result_4_item", ":random_trade_good"),
		 (eq, ":best_result_5_item", ":random_trade_good"),

         (try_begin),
		   (eq, ":best_result_1_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_1_profit"),
           (assign, ":best_result_1_item", ":random_trade_good"),
           (assign, ":best_result_1_town", ":random_town"),
           (assign, ":best_result_1_profit", ":difference"),
         (else_try),
		   (eq, ":best_result_2_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_2_profit"),
           (assign, ":best_result_2_item", ":random_trade_good"),
           (assign, ":best_result_2_town", ":random_town"),
           (assign, ":best_result_2_profit", ":difference"),
		 (else_try),
		   (eq, ":best_result_3_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_3_profit"),
           (assign, ":best_result_3_item", ":random_trade_good"),
           (assign, ":best_result_3_town", ":random_town"),
           (assign, ":best_result_3_profit", ":difference"),
		 (else_try),
		   (eq, ":best_result_4_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":random_trade_good"),
           (assign, ":best_result_4_town", ":random_town"),
           (assign, ":best_result_4_profit", ":difference"),
		 (else_try),
		   (eq, ":best_result_5_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_5_profit"),
           (assign, ":best_result_5_item", ":random_trade_good"),
           (assign, ":best_result_5_town", ":random_town"),
           (assign, ":best_result_5_profit", ":difference"),
		 (try_end),
	   (else_try),
         (try_begin),
           (gt, ":difference", ":best_result_1_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":best_result_3_item"),
           (assign, ":best_result_4_town", ":best_result_3_town"),
           (assign, ":best_result_4_profit", ":best_result_3_profit"),
           (assign, ":best_result_3_item", ":best_result_2_item"),
           (assign, ":best_result_3_town", ":best_result_2_town"),
           (assign, ":best_result_3_profit", ":best_result_2_profit"),
           (assign, ":best_result_2_item", ":best_result_1_item"),
           (assign, ":best_result_2_town", ":best_result_1_town"),
           (assign, ":best_result_2_profit", ":best_result_1_profit"),
           (assign, ":best_result_1_item", ":random_trade_good"),
           (assign, ":best_result_1_town", ":random_town"),
           (assign, ":best_result_1_profit", ":difference"),
         (else_try),
           (gt, ":difference", ":best_result_2_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":best_result_3_item"),
           (assign, ":best_result_4_town", ":best_result_3_town"),
           (assign, ":best_result_4_profit", ":best_result_3_profit"),
           (assign, ":best_result_3_item", ":best_result_2_item"),
           (assign, ":best_result_3_town", ":best_result_2_town"),
           (assign, ":best_result_3_profit", ":best_result_2_profit"),
           (assign, ":best_result_2_item", ":random_trade_good"),
           (assign, ":best_result_2_town", ":random_town"),
           (assign, ":best_result_2_profit", ":difference"),
         (else_try),
           (gt, ":difference", ":best_result_3_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":best_result_3_item"),
           (assign, ":best_result_4_town", ":best_result_3_town"),
           (assign, ":best_result_4_profit", ":best_result_3_profit"),
           (assign, ":best_result_3_item", ":random_trade_good"),
           (assign, ":best_result_3_town", ":random_town"),
           (assign, ":best_result_3_profit", ":difference"),
         (else_try),
           (gt, ":difference", ":best_result_4_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":random_trade_good"),
           (assign, ":best_result_4_town", ":random_town"),
           (assign, ":best_result_4_profit", ":difference"),
         (else_try),
           (gt, ":difference", ":best_result_5_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
         (try_end),
	   (try_end),
     (try_end),

     (assign, "$g_encountered_party", ":org_encountered_party"),

     (str_clear, s3),
     
     (assign, reg2, ":max_skill"),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (try_begin),
       (le, ":num_best_results", 0),
       (str_store_string, s2, "@However, {reg3?You are:{s1} is} unable to find any trade goods that would bring a profit."),
     (else_try),
       (try_begin),
         (ge, ":best_result_5_item", 0),
         (assign, reg6, ":best_result_5_profit"),
         (str_store_item_name, s4, ":best_result_5_item"),
         (str_store_party_name, s5, ":best_result_5_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_4_item", 0),
         (assign, reg6, ":best_result_4_profit"),
         (str_store_item_name, s4, ":best_result_4_item"),
         (str_store_party_name, s5, ":best_result_4_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_3_item", 0),
         (assign, reg6, ":best_result_3_profit"),
         (str_store_item_name, s4, ":best_result_3_item"),
         (str_store_party_name, s5, ":best_result_3_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_2_item", 0),
         (assign, reg6, ":best_result_2_profit"),
         (str_store_item_name, s4, ":best_result_2_item"),
         (str_store_party_name, s5, ":best_result_2_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_1_item", 0),
         (assign, reg6, ":best_result_1_profit"),
         (str_store_item_name, s4, ":best_result_1_item"),
         (str_store_party_name, s5, ":best_result_1_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end), 
       (str_store_string, s2, "@{reg3?You find:{s1} finds} out the following:^{s3}"),
     (try_end),
     ],
    [
      ("continue",[],"Continue...",
       [
           (jump_to_menu,"mnu_town_trade"),
        ]),
    ]
  ),

  (
    "sneak_into_town_suceeded",0,"Disguised in the garments of a poor pilgrim, you trick the guards and make your way into town.",
    "none",
    [],
    [
      ("continue",[],"Continue...",
       [
			(try_begin),
				#(quest_get_slot, ":state", "qst_oim_alevtina_hanum", slot_quest_current_state),
				#(quest_get_slot, ":town", "qst_oim_alevtina_hanum", slot_quest_target_center),
				#(assign, reg0, ":state"),
				#(str_store_party_name, s1, ":town"),
				#(display_log_message, "@state: {reg0}, town: {s1}"),

				(check_quest_active, "qst_oim_alevtina_hanum"),
				(neg|check_quest_succeeded, "qst_oim_alevtina_hanum"),
				(neg|check_quest_finished,"qst_oim_alevtina_hanum"),
				#(quest_slot_ge, "qst_oim_alevtina_hanum", slot_quest_current_state, 1),
				(quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_target_center, "$current_town"),
				#code
				(jump_to_menu,"mnu_oim_dmitriy_alevtina_hanum"),
			(else_try), 	
           (assign, "$sneaked_into_town",1),
           (jump_to_menu,"mnu_town"),
			(end_try),	
        ]),
    ]
  ),
  (
    "sneak_into_town_caught",0,"As you attempt to sneak in, one of the guards recognizes you and raises the alarm! You must flee back through the gates before all the guards in the town come down on you!",
    "none",
    [
       (assign,"$auto_menu","mnu_captivity_start_castle_surrender"),
    ],
    [
      ("sneak_caught_fight",[],"Try to fight your way out!",
       [
           (assign,"$all_doors_locked",1),
           (party_get_slot, ":sneak_scene", "$current_town", slot_town_center), # slot_town_gate),
           (modify_visitors_at_site,":sneak_scene"),(reset_visitors),
           (set_visitor,0,"trp_player"),
           (store_faction_of_party, ":town_faction","$current_town"),
           (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
           (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           (try_begin),
             (gt, ":tier_2_troop", 0),
             (gt, ":tier_3_troop", 0),
             (assign,reg(0),":tier_3_troop"),
             (assign,reg(1),":tier_3_troop"),
             (assign,reg(2),":tier_2_troop"),
             (assign,reg(3),":tier_2_troop"),
           (else_try),  
             (assign,reg(0),"trp_swadian_skirmisher"),
             (assign,reg(1),"trp_swadian_crossbowman"),
             (assign,reg(2),"trp_swadian_infantry"),
             (assign,reg(3),"trp_swadian_crossbowman"),
           (try_end),
           #(assign,reg(4),-1),
           #(shuffle_range,0,5),
           (set_visitor,1,reg(0)),
           (set_visitor,2,reg(1)),
           (set_visitor,3,reg(2)),
           (set_visitor,4,reg(3)),
           (set_jump_mission,"mt_sneak_caught_fight"),
 #          (jump_to_menu,"mnu_captivity_start_castle_defeat"),
           (set_passage_menu,"mnu_town"),
           (jump_to_scene,":sneak_scene"),
           (change_screen_mission),
        ]),
      ("sneak_caught_surrender",[],"Surrender.",
       [
           (jump_to_menu,"mnu_captivity_start_castle_surrender"),
        ]),
    ]
  ),
  (
    "sneak_into_town_caught_dispersed_guards",0,"You drive off the guards and cover your trail as you escape, easily losing your pursuers in the maze of streets.",
    "none",
    [],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$sneaked_into_town",1),
           (assign, "$town_entered", 1),
           (jump_to_menu,"mnu_town"),
        ]),
    ]
  ),
  (
    "sneak_into_town_caught_ran_away",0,"You make your way back through the gates, quickly retreating to the safety of the hills.",
    "none",
    [],
    [      
      ("continue",[],"Continue...",
       [
           (assign,"$auto_menu",-1),
           (store_encountered_party,"$last_sneak_attempt_town"),
           (store_current_hours,"$last_sneak_attempt_time"),
           (change_screen_return),
        ]),
    ]
  ),


  (
    "enemy_offer_ransom_for_prisoner",0,"{s2} offers you a sum of {reg12} thaler in silver if you are willing to sell him {s1}.",
    "none",
    [(call_script, "script_calculate_ransom_amount_for_troop", "$g_ransom_offer_troop"),
     (assign, reg12, reg0),
     (str_store_troop_name, s1, "$g_ransom_offer_troop"),
     (store_troop_faction, ":faction_no", "$g_ransom_offer_troop"),
     (str_store_faction_name, s2, ":faction_no"),
     ],
    [
      ("ransom_accept",[],"Accept the offer.",
       [(troop_add_gold, "trp_player", reg12),
        (party_remove_prisoners, "$g_ransom_offer_party", "$g_ransom_offer_troop", 1),
        #(troop_set_slot, "$g_ransom_offer_troop", slot_troop_is_prisoner, 0),
        (call_script, "script_remove_troop_from_prison", "$g_ransom_offer_troop"),
        (change_screen_return),
        ]),
      ("ransom_reject",[],"Reject the offer.",
       [
        (call_script, "script_change_player_relation_with_troop", "$g_ransom_offer_troop", -4),
        (call_script, "script_change_player_honor", -1),
        (assign, "$g_ransom_offer_rejected", 1),
        (change_screen_return),
        ]),
    ]
  ),


  (
    "training_ground",0,"You approach a mercenary camp... Here you can hire warriors and arm your men.",
    "none",
    [
      (store_add, "$g_training_ground_melee_training_scene", "scn_training_ground_ranged_melee_1", "$g_encountered_party"),
      (val_sub, "$g_training_ground_melee_training_scene", training_grounds_begin),
      (try_begin),
        (ge, "$g_training_ground_training_count", 3),
        (assign, "$g_training_ground_training_count", 0),
        (rest_for_hours, 1, 5, 1), #rest while attackable
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
      (try_end),
      ],
    [
      ("camp_trainer",
       [(eq, 0, 1),],"Speak with the trainer.",
       [
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         (change_screen_mission),
         (music_set_situation, 0),
         ]),
	 
      ("camp_merch",
       [],"Find the mercenary captain.",
       [
         (jump_to_menu, "mnu_capitan_vid"),
         (music_set_situation, 0),
         ]),
	
	
	
      ("camp_train_melee",
       [
         (neg|troop_is_wounded, "trp_player"),
         (call_script, "script_party_count_fit_for_battle", "p_main_party"),
         (gt, reg0, 1),
		 (eq, 0, 1),
         ],"Melee.",
       [
         (assign, "$g_mt_mode", ctm_melee),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_1"),
         (music_set_situation, 0),
         ]),
      ("camp_train_archery",[(eq, 0, 1),], "Begin practice.",
       [
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_1"),
         (music_set_situation, 0),
         ]),
      ("camp_train_mounted",[(eq, 0, 1),],"Horseback practice.",
       [
         (assign, "$g_mt_mode", ctm_mounted),
         (jump_to_menu, "mnu_training_ground_selection_details_mounted"),
         (music_set_situation, 0),
         ]),

      ("go_to_track",[(eq, "$cheat_mode", 1), (eq, 0, 1),],"{!}Cheat: Go to track.",
       [
         (set_jump_mission, "mt_ai_training"),
         (store_add, ":scene_no", "scn_training_ground_horse_track_1", "$g_encountered_party"),
         (val_sub, ":scene_no", training_grounds_begin),
         (jump_to_scene, ":scene_no"),
         (change_screen_mission),
        ]
       ),
      ("go_to_range",[(eq, "$cheat_mode", 1), (eq, 0, 1),],"{!}Cheat: Go to range.",
       [
         (set_jump_mission, "mt_ai_training"),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         (change_screen_mission),
        ]
       ),
      ("leave",[],"Leave.",
       [(change_screen_return),
        ]),
    ]
  ),

  ("training_ground_selection_details_melee_1",0,"How many opponents will you battle?",
   "none",
   [
     (call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
     (troop_get_slot, "$temp", "trp_stack_selection_amounts", 1), #number of men fit
     (assign, "$temp_2", 1),
     ],
    [
      ("camp_train_melee_num_men_1",[(ge, "$temp", 1)],"One.",
       [
         (assign, "$temp", 1),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("camp_train_melee_num_men_2",[(ge, "$temp", 2)],"Two.",
       [
         (assign, "$temp", 2),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("camp_train_melee_num_men_3",[(ge, "$temp", 3)],"Three.",
       [
         (assign, "$temp", 3),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("camp_train_melee_num_men_4",[(ge, "$temp", 4)],"Four.",
       [
         (assign, "$temp", 4),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("go_back_dot",[],"Go back.",
       [
         (jump_to_menu, "mnu_training_ground"),
        ]),
      ]
  ),

  ("training_ground_selection_details_melee_2",0,"Choose your opponent #{reg1}:",
   "none",
   [
     (assign, reg1, "$temp_2"),
     (troop_get_slot, "$temp_3", "trp_stack_selection_amounts", 0), #number of slots
     ],
    [
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 1),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 1),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 2),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 2),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 3),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 3),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 4),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 4),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 5),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 5),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 6),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 6),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 7),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 7),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 8),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 8),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 9),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 9),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 10),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 10),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 11),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 11),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 12),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 12),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 13),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 13),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 14),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 14),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 15),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 15),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 16),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 16),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 17),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 17),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 18),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 18),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 19),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 19),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 20),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 20),]),
      ("training_ground_selection_details_melee_random", [],"Choose randomly.",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", -1),]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_selection_details_mounted",0,"What kind of weapon do you wish to train with?",
   "none",
   [],
    [
      ("camp_train_mounted_details_1",[],"Single-handed weapon.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_one_handed_wpn, 0),
         ]),
      ("camp_train_mounted_details_2",[],"Pole arm.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_polearm, 0),
         ]),
      ("camp_train_mounted_details_3",[],"Bow.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_bow, 0),
         ]),
      ("camp_train_mounted_details_4",[],"Thrown weapon.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_thrown, 0),
         ]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_selection_details_ranged_1",0,"What kind of ranged weapon do you wish to train with?",
   "none",
   [],
    [
      ("camp_train_ranged_weapon_bow",[],"Bow and arrows.",
       [
         (assign, "$g_mt_mode", ctm_ranged),
         (assign, "$temp", itp_type_bow),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
      ("camp_train_ranged_weapon_crossbow",[],"Crossbow",
       [
         (assign, "$g_mt_mode", ctm_ranged),
         (assign, "$temp", itp_type_crossbow),
	 (assign, "$g_flag", 0),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
	 
  ("camp_train_ranged_weapon_mushket",[],"Musket",
       [
         (assign, "$g_mt_mode", ctm_ranged),
         (assign, "$temp", itp_type_crossbow),
	 (assign, "$g_flag", 1),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
      ("camp_train_ranged_weapon_thrown",[],"Throwing Knives",
       [
         (assign, "$g_mt_mode", ctm_ranged),
         (assign, "$temp", itp_type_thrown),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_selection_details_ranged_2",0,"At what range do you wish to practice?",
   "none",
   [],
    [
      ("camp_train_ranged_details_1",[],"10 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 10),
         ]),
      ("camp_train_ranged_details_2",[],"20 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 20),
         ]),
      ("camp_train_ranged_details_3",[],"30 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 30),
         ]),
      ("camp_train_ranged_details_4",[],"40 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 40),
         ]),
      ("camp_train_ranged_details_5",[(eq, "$g_mt_mode", ctm_ranged),],"50 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 50),
         ]),
      ("camp_train_ranged_details_6",[(eq, "$g_mt_mode", ctm_ranged),],"60 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 60),
         ]),
      ("camp_train_ranged_details_7",[(eq, "$g_mt_mode", ctm_ranged),],"70 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 70),
         ]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_description",0,"{s0}",
   "none",
    [
      (str_store_string,s1,"@ " ),
	   (str_store_string,s2,"@ Continue...." ),
	     (val_add, "$g_train_count", 1),
			
	  (try_begin),
      (gt,"$g_train_count",50),
			(store_character_level,":price","trp_player"),
			(store_proficiency_level,":prof_level","trp_player", "$g_training_ground_used_weapon_proficiency"),
			(val_mul, ":price",":prof_level"),
			(val_div, ":price", 100),
			(val_sub, ":price", 15),
			(try_begin),
				(le,":price",1),
				(assign, ":price", 3),			
			(try_end),
			
			(store_troop_gold,":allgold","trp_player"),
			(assign, reg8, ":price"),
			(assign, reg9, ":allgold"),
			(try_begin),
				(lt,":allgold",":price"),
				(str_store_string,s1,"@ Ne hvataet money, nuzhno {reg8} dinarov" ),
				(str_store_string,s2,"@ Back" ),
			(else_try),
				(str_store_string,s1,"@ Stoimost {reg8} dinarov" ),
				(str_store_string,s2,"@ Continue" ),
			(try_end),
		(try_end),
   ],
    [
      ("s2_dot", [], "{s2}...",
       [
         (try_begin),
	 (gt,"$g_train_count",50),
	   (try_begin),
				(lt,reg9, reg8),
				(change_screen_return),
			(else_try),				
		    (troop_remove_gold,"trp_player",reg8),
         (set_jump_mission, "mt_training_ground_training"),
         (jump_to_scene, "$g_training_ground_training_scene"),
         (change_screen_mission),
	   (try_end),
	 (else_try),	
         (set_jump_mission, "mt_training_ground_training"),
         (jump_to_scene, "$g_training_ground_training_scene"),
         (change_screen_mission),
	 (try_end)
        ]
       ),
      ]
  ),

  ("training_ground_training_result",mnf_disable_all_keys,"{s7}{s2}",
   "none",
   [
     (store_skill_level, ":trainer_skill", "skl_trainer", "trp_player"),
     (store_add, ":trainer_skill_multiplier", 5, ":trainer_skill"),
     (call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
     (str_clear, s2),
     (troop_get_slot, ":num_fit", "trp_stack_selection_amounts", 1),
     (troop_get_slot, ":num_slots", "trp_stack_selection_amounts", 0),
     (try_begin),
       (gt, "$g_training_ground_training_success_ratio", 0),
       (store_mul, ":xp_ratio_to_add", "$g_training_ground_training_success_ratio", "$g_training_ground_training_success_ratio"),
       (try_begin),
         (eq, "$g_training_ground_training_success_ratio", 100),
         (val_mul, ":xp_ratio_to_add", 2), #2x when perfect
       (try_end),
       (try_begin),
         (eq, "$g_mt_mode", ctm_melee),
         (val_div, ":xp_ratio_to_add", 2),
       (try_end),
       (val_div, ":xp_ratio_to_add", 10), # value over 1000
       (try_begin),
         (gt, ":num_fit", 8),
         (val_mul, ":xp_ratio_to_add", 3),
         (assign, ":divisor", ":num_fit"),
         (convert_to_fixed_point, ":divisor"),
         (store_sqrt, ":divisor", ":divisor"),
         (convert_to_fixed_point, ":xp_ratio_to_add"),
         (val_div, ":xp_ratio_to_add", ":divisor"),
       (try_end),
##       (assign, reg0, ":xp_ratio_to_add"),
##       (display_message, "@xp earn ratio: {reg0}/1000"),
       (store_mul, ":xp_ratio_to_add_with_trainer_skill", ":xp_ratio_to_add", ":trainer_skill_multiplier"),
       (val_div, ":xp_ratio_to_add_with_trainer_skill", 10),
       (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
       (store_add, ":end_cond", ":num_slots", 2),
       (try_for_range, ":i_slot", 2, ":end_cond"),
         (troop_get_slot, ":amount", "trp_stack_selection_amounts", ":i_slot"),
         (troop_get_slot, ":troop_id", "trp_stack_selection_ids", ":i_slot"),
         (assign, ":end_cond_2", ":num_stacks"),
         (try_for_range, ":stack_no", 0, ":end_cond_2"),
           (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
           (eq, ":stack_troop", ":troop_id"),
           (assign, ":end_cond_2", 0), #break
           (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", ":amount", ":xp_ratio_to_add_with_trainer_skill"),
           (str_store_troop_name_by_count, s1, ":troop_id", ":amount"),
           (assign, reg1, ":amount"),
           (str_store_string, s2, "@{s2}^{reg1} {s1} earned {reg0} experience."),
         (try_end),
       (try_end),
       (try_begin),
         (eq, "$g_mt_mode", ctm_melee),
         (store_mul, ":special_xp_ratio_to_add", ":xp_ratio_to_add", 3),
         (val_div, ":special_xp_ratio_to_add", 2),
         (try_for_range, ":enemy_index", 0, "$g_training_ground_training_num_enemies"),
           (troop_get_slot, ":troop_id", "trp_temp_array_a", ":enemy_index"),
           (assign, ":end_cond_2", ":num_stacks"),
           (try_for_range, ":stack_no", 0, ":end_cond_2"),
             (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
             (eq, ":stack_troop", ":troop_id"),
             (assign, ":end_cond_2", 0), #break
             (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", 1, ":special_xp_ratio_to_add"),
             (str_store_troop_name, s1, ":troop_id"),
             (str_store_string, s2, "@{s2}^{s1} earned an additional {reg0} experience."),
           (try_end),
         (try_end),
       (try_end),
       (try_begin),
         (call_script, "script_cf_training_ground_sub_routine_for_training_result", "trp_player", -1, 1, ":xp_ratio_to_add"),
         (str_store_string, s2, "@^You earned {reg0} experience.{s2}"),
       (try_end),
     (try_end),
     (try_begin),
       (eq, "$g_training_ground_training_success_ratio", 0),
       (str_store_string, s7, "@The training didn't go well at all."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 25),
       (str_store_string, s7, "@The training didn't go well at all."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 50),
       (str_store_string, s7, "@The training didn't go very well."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 75),
       (str_store_string, s7, "@The training went quite well."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 99),
       (str_store_string, s7, "@The training went very well."),
     (else_try),
       (str_store_string, s7, "@The training went perfectly."),
     (try_end),
     
     ],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
   ),
  
  ("marshall_selection_candidate_ask",0,"{s15} will soon select a new marshal for {s23}. Some of the grandees have put forth your name as likely candidate.",
   "none",
   [
     (try_begin),
       (eq, "$g_presentation_marshall_selection_ended", 1),
       (change_screen_return),
     (try_end),
     (faction_get_slot, ":king", "$players_kingdom", slot_faction_leader),
     (str_store_troop_name, s15, ":king"),
     (str_store_faction_name, s23, "$players_kingdom"),
     ],
    [
      ("marshall_candidate_accept", [],"Come forward as a candidate for elections.",
       [
         (start_presentation, "prsnt_marshall_selection"),
        ]
       ),
      ("marshall_candidate_reject", [],"Tell everyone that you are too busy for such matters.",
       [
         (try_begin),
           (eq, "$g_presentation_marshall_selection_max_renown_2_troop", "trp_player"),
           (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_3"),
           (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_3_troop"),
         (else_try),
           (assign, "$g_presentation_marshall_selection_max_renown_1", "$g_presentation_marshall_selection_max_renown_2"),
           (assign, "$g_presentation_marshall_selection_max_renown_1_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
           (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_3"),
           (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_3_troop"),
         (try_end),
         (start_presentation, "prsnt_marshall_selection"),
        ]
       ),
      ]
  ),



  
##    [
##      ("renew_oath",[],"Renew your oath to {s1} for another month.",[
##          (store_current_day, ":cur_day"),
##          (store_add, "$g_oath_end_day", ":cur_day", 30),
##          (change_screen_return)]),
##      ("dont_renew_oath",[],"Become free of your bond.",[
##          (assign, "$players_kingdom",0),
##          (assign, "$g_player_permitted_castles", 0),
##          (change_screen_return)]),
##    ]
##  ),


#####################################################################
## Captivity....
#####################################################################
#####################################################################
#####################################################################
#####################################################################
  (
    "captivity_avoid_wilderness",0,"Suddenly all the world goes black. Many hours later, you regain consciousness and find yourself at the very spot you fell. Your enemies must have taken you up for dead and left you there. However, it seems that none of your wounds were lethal, and although your head is still reeling, you discover that you can still walk. You pick yourself up and go to look for any other survivors from your party.",
    "none",
    [
      ],
    []
  ),

  (
    "captivity_start_wilderness",0,"Stub",
    "none",
    [
          (assign, "$g_player_is_captive", 1),
          (try_begin),
            (eq,"$g_player_surrenders",1),
            (jump_to_menu, "mnu_captivity_start_wilderness_surrender"), 
          (else_try),
            (jump_to_menu, "mnu_captivity_start_wilderness_defeat"), 
          (try_end),
      ],
    []
  ),
  
  (
    "captivity_start_wilderness_surrender",0,"Stub",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1), #We need this since we may come here by something other than auto_menu
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_wilderness_taken_prisoner"),
      ],
    []
  ),
  (
    "captivity_start_wilderness_defeat",0,"You are taken prisoner.",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_wilderness_taken_prisoner"),
    ],
    []
  ),
  (
    "captivity_start_castle_surrender",0,"Stub",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
      ],
    []
  ),
  (
    "captivity_start_castle_defeat",0,"Stub",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),
	   #(call_script, "script_replace_shturm_item_end"),
       (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
      ],
    []
  ),
  (
    "captivity_start_under_siege_defeat",0,"You are taken prisoner.",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
    ],
    []
  ),
  
  (
    "captivity_wilderness_taken_prisoner",mnf_scale_picture,"You are taken prisoner.",
    "none",
    [
        (set_background_mesh, "mesh_pic_prisoner_wilderness"),
     ],
    [
      ("continue",[],"Continue...",
       [
         (try_for_range, ":npc", companions_begin, companions_end),
           (main_party_has_troop, ":npc"),
           (store_random_in_range, ":rand", 0, 100),
           (lt, ":rand", 30),
           (remove_member_from_party, ":npc", "p_main_party"),
           (troop_set_slot, ":npc", slot_troop_occupation, 0),
           (troop_set_slot, ":npc", slot_troop_playerparty_history, pp_history_scattered),
           (assign, "$last_lost_companion", ":npc"),
           (store_faction_of_party, ":victorious_faction", "$g_encountered_party"),
           (troop_set_slot, ":npc", slot_troop_playerparty_history_string, ":victorious_faction"),
           (troop_set_health, ":npc", 100),
           (store_random_in_range, ":rand_town", towns_begin, towns_end),
           (troop_set_slot, ":npc", slot_troop_cur_center, ":rand_town"),
           (assign, ":nearest_town_dist", 1000),
           (try_for_range, ":town_no", towns_begin, towns_end),
             (store_faction_of_party, ":town_fac", ":town_no"),
             (store_relation, ":reln", ":town_fac", "fac_player_faction"),
             (ge, ":reln", 0),
             (store_distance_to_party_from_party, ":dist", ":town_no", "p_main_party"),
             (lt, ":dist", ":nearest_town_dist"),
             (assign, ":nearest_town_dist", ":dist"),
             (troop_set_slot, ":npc", slot_troop_cur_center, ":town_no"),
           (try_end),
         (try_end),

         (set_camera_follow_party, "$capturer_party"),
         (assign, "$g_player_is_captive", 1),
         (store_random_in_range, ":random_hours", 18, 30),
         (call_script, "script_event_player_captured_as_prisoner"),
         (call_script, "script_stay_captive_for_hours", ":random_hours"),
         (assign,"$auto_menu","mnu_captivity_wilderness_check"),
         (change_screen_return),
         ]),
      ]
  ),
  (
    "captivity_wilderness_check",0,"stub",
    "none",
    [(jump_to_menu,"mnu_captivity_end_wilderness_escape")],
    []
  ),
  (
    "captivity_end_wilderness_escape",mnf_scale_picture,"After several painful days of being dragged about as a prisoner, you find a chance and escape from your captors!",
    "none",
    [
        (play_cue_track, "track_escape"),
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_escape_1_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_escape_1"),
        (try_end),
    ],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 0),
           (try_begin),
             (party_is_active, "$capturer_party"),
             (party_relocate_near_party, "p_main_party", "$capturer_party", 2),
           (try_end),
           (call_script, "script_set_parties_around_player_ignore_player", 2, 4),
           (assign, "$g_player_icon_state", pis_normal),
           (set_camera_follow_party, "p_main_party"),
           (rest_for_hours, 0, 0, 0), #stop resting
           (change_screen_return),
        ]),
    ]
  ),
  (
    "captivity_castle_taken_prisoner",0,"You are quickly surrounded by guards who take away your weapons. With curses and insults, they throw you into the dungeon where you shall while away the miserable days of your captivity.",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
    ],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (store_random_in_range, ":random_hours", 16, 22),
           (call_script, "script_event_player_captured_as_prisoner"),
           (call_script, "script_stay_captive_for_hours", ":random_hours"),
           (assign,"$auto_menu", "mnu_captivity_castle_check"),
           (change_screen_return)
        ]),
    ]
  ),
  (
    "captivity_rescue_lord_taken_prisoner",0,"You remain in disguise for as long as possible before your ruse is discovered. The guards are outraged, and beat you savagely before throwing you back into the cell for God knows how long...",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
   ],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (store_random_in_range, ":random_hours", 16, 22),
           (call_script, "script_event_player_captured_as_prisoner"),
           (call_script, "script_stay_captive_for_hours", ":random_hours"),
           (assign,"$auto_menu", "mnu_captivity_castle_check"),
           (change_screen_return),
        ]),
    ]
  ),
  (
    "captivity_castle_check",0,"stub",
    "none",
    [
        (store_random_in_range, reg(7), 0, 10),
        (try_begin),
          (lt, reg(7), 4),
          (store_random_in_range, "$player_ransom_amount", 3, 6),
          (val_mul, "$player_ransom_amount", 100),
          (store_troop_gold, reg(3), "trp_player"),
          (gt, reg(3), "$player_ransom_amount"),
          (jump_to_menu,"mnu_captivity_end_propose_ransom"),
        (else_try),
          (lt, reg(7), 7),
          (jump_to_menu,"mnu_captivity_end_exchanged_with_prisoner"),
        (else_try),
          (jump_to_menu,"mnu_captivity_castle_remain"),
        (try_end),
    ],
    []
  ),
  (
    "captivity_end_exchanged_with_prisoner",0,"After many days of imprisonment, you are finally set free when your captors exchange you for another prisoner.",
    "none",
    [
      (play_cue_track, "track_escape"),
      ],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 0),
           (try_begin),
             (party_is_active, "$capturer_party"),
             (party_relocate_near_party, "p_main_party", "$capturer_party", 2),
           (try_end),
           (call_script, "script_set_parties_around_player_ignore_player", 2, 12),
           (assign, "$g_player_icon_state", pis_normal),
           (set_camera_follow_party, "p_main_party"),
           (rest_for_hours, 0, 0, 0), #stop resting
           (change_screen_return),
        ]),
    ]
  ),
  (
    "captivity_end_propose_ransom",0,"You many spend long hours in the sunless dank of the dungeon, more than you can possibly count. Then, suddenly, one of your captors enters your cell with an offer; he proposes to free you in return for {reg5} thaler of your hidden wealth. You decide to...",
    "none",
    [
        (store_character_level, ":player_level", "trp_player"),
        (store_mul, "$player_ransom_amount", ":player_level", 50),
        (val_add, "$player_ransom_amount", 100),
      (assign, reg5, "$player_ransom_amount"),
    ],
    [
      ("captivity_end_ransom_accept",[(store_troop_gold,":player_gold", "trp_player"),
                                      (ge, ":player_gold","$player_ransom_amount")],"Accept the offer.",
      [
        (play_cue_track, "track_escape"),
        (assign, "$g_player_is_captive", 0),		
        (troop_remove_gold, "trp_player", "$player_ransom_amount"), 
        (try_begin),
          (party_is_active, "$capturer_party"),
          (party_relocate_near_party, "p_main_party", "$capturer_party", 1),
        (try_end),
        (call_script, "script_set_parties_around_player_ignore_player", 2, 6),
        (assign, "$g_player_icon_state", pis_normal),
        (set_camera_follow_party, "p_main_party"),
        (rest_for_hours, 0, 0, 0), #stop resting
        (change_screen_return),
      ]),
      ("captivity_end_ransom_deny",[],"Refuse him, and wait for another chance to escape.",
      [
        (assign, "$g_player_is_captive", 1),
        (store_random_in_range, reg(8), 16, 22),
        (call_script, "script_stay_captive_for_hours", reg8),
        (assign,"$auto_menu", "mnu_captivity_castle_check"),
        (change_screen_return),
      ]),
    ]
  ),
  (
    "captivity_castle_remain",mnf_scale_picture|mnf_disable_all_keys,"More days pass in the darkness of your cell. You survive them as best you can, enduring the kicks and curses of the guards, watching your underfed body waste away more and more...",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
        (store_random_in_range, ":random_hours", 16, 22),
        (call_script, "script_stay_captive_for_hours", ":random_hours"),
        (assign,"$auto_menu", "mnu_captivity_castle_check"),
        
    ],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (change_screen_return),
        ]),
    ]
  ),

  (
    "kingdom_army_quest_report_to_army",mnf_scale_picture,"{s8} sends word that he wishes you to join his military campaign. You must bring with you at least {reg13} troops, and if you do not yet have enough, you are instructed to raise a sufficient force with all due haste.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (quest_get_slot, ":quest_target_troop", "qst_report_to_army", slot_quest_target_troop),
        (quest_get_slot, ":quest_target_amount", "qst_report_to_army", slot_quest_target_amount),
        (call_script, "script_get_information_about_troops_position", ":quest_target_troop", 0),
        (str_clear, s9),
        (try_begin),
          (eq, reg0, 1), #troop is found and text is correct
          (str_store_string, s9, s1),
        (try_end),
        (str_store_troop_name, s8, ":quest_target_troop"),
        (assign, reg13, ":quest_target_amount"),
      ],
    [
      ("continue",[],"Continue...",
       [
           (quest_get_slot, ":quest_target_troop", "qst_report_to_army", slot_quest_target_troop),
           (quest_get_slot, ":quest_target_amount", "qst_report_to_army", slot_quest_target_amount),
           (str_store_troop_name_link, s13, ":quest_target_troop"),
           (assign, reg13, ":quest_target_amount"),
           (setup_quest_text, "qst_report_to_army"),
           (str_store_string, s2, "@{s13} asked you to report to him with at least {reg13} troops."),
           (call_script, "script_start_quest", "qst_report_to_army", ":quest_target_troop"),
           (call_script, "script_report_quest_troop_positions", "qst_report_to_army", ":quest_target_troop", 3),
           (change_screen_return),
        ]),
     ]
  ),

  (
    "kingdom_army_quest_messenger",mnf_scale_picture,"{s8} sends word that he wishes to speak with you about a task he needs performed. He requests you come to him as soon as possible.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
        (str_store_troop_name, s8, ":faction_marshall"),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "kingdom_army_quest_join_siege_order",mnf_scale_picture,"{s8} sends word that you are to join the siege of {s9} in preparation for a full assault. Your troops are to take {s9} at all costs.",
    "none",
    [
		(set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
        (quest_get_slot, ":quest_target_center", "qst_join_siege_with_army", slot_quest_target_center),
        (str_store_troop_name, s8, ":faction_marshall"),
        (str_store_party_name, s9, ":quest_target_center"),
      ],
    [
      ("continue",[],"Continue...",
       [
           (call_script, "script_end_quest", "qst_follow_army"),
           (quest_get_slot, ":quest_target_center", "qst_join_siege_with_army", slot_quest_target_center),
           (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
           (str_store_troop_name_link, s13, ":faction_marshall"),
           (str_store_party_name_link, s14, ":quest_target_center"),
           (setup_quest_text, "qst_join_siege_with_army"),
           (str_store_string, s2, "@{s13} ordered you to join the assault against {s14}."),
           (call_script, "script_start_quest", "qst_join_siege_with_army", ":faction_marshall"),
           (change_screen_return),
        ]),
     ]
  ),

  (
    "kingdom_army_follow_failed",mnf_scale_picture,"You have disobeyed your orders, and failed to follow {s8}. In anger, he has barred you from the army, and sends a stern warning that your actions will not be forgotten.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
        (str_store_troop_name, s8, ":faction_marshall"),
        (call_script, "script_abort_quest", "qst_follow_army", 1),
        (call_script, "script_change_player_relation_with_troop", ":faction_marshall", -3),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


  (
    "invite_player_to_faction_without_center",mnf_scale_picture,"You receive an offer of service!^^ {s8} of {s9} has sent a messenger to deliver an initiation written in his own hand. You would be granted the honor of becoming a subject of the {lord/lady} of {s9}, and in return, {s8} asks that you swear an oath of homage to him, and fight in his military campaigns. Although he offers you no lands or titles, he will nevertheless surely be offended if you do not accept his offer...",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, "$g_invite_faction_lord", "$g_invite_faction", slot_faction_leader),
        (str_store_troop_name, s8, "$g_invite_faction_lord"),
        (str_store_faction_name, s9, "$g_invite_faction"),
      ],
    [
      ("faction_accept",[],"Accept.",
       [(str_store_troop_name,s1,"$g_invite_faction_lord"),
        (setup_quest_text,"qst_join_faction"),

        (str_store_troop_name_link, s3, "$g_invite_faction_lord"),
        (str_store_faction_name_link, s4, "$g_invite_faction"),
        (quest_set_slot, "qst_join_faction", slot_quest_giver_troop, "$g_invite_faction_lord"),
        (quest_set_slot, "qst_join_faction", slot_quest_expiration_days, 30),
        (str_store_string, s2, "@Find and speak with {s3} of {s4} to give him your oath of homage."),
        (call_script, "script_start_quest", "qst_join_faction", "$g_invite_faction_lord"),
        (call_script, "script_report_quest_troop_positions", "qst_join_faction", "$g_invite_faction_lord", 3),
        (jump_to_menu, "mnu_invite_player_to_faction_accepted"),
        ]),
      ("faction_reject",[],"Decline.",
       [(call_script, "script_change_player_relation_with_troop", "$g_invite_faction_lord", -3),
        (call_script, "script_change_player_relation_with_faction", "$g_invite_faction", -10),
        (assign, "$g_invite_faction", 0),
        (assign, "$g_invite_faction_lord", 0),
        (assign, "$g_invite_offered_center", 0),
        (change_screen_return),
        ]),
     ]
  ),
  

  (
    "invite_player_to_faction",mnf_scale_picture,"You receive an offer of service!^^ {s8} of {s9} has sent a messenger to deliver an initiation written in his own hand. You are to receive the honor of becoming a subject of the {lord/lady} of {s9}, and in return, {s8} asks that you swear an oath of homage to him, and fight in his military campaigns. He offers you the fief of {s2} for your loyal service, and will surely be offended if you do not accept the offer...",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, "$g_invite_faction_lord", "$g_invite_faction", slot_faction_leader),
        (str_store_troop_name, s8, "$g_invite_faction_lord"),
        (str_store_faction_name, s9, "$g_invite_faction"),
        (str_store_party_name, s2, "$g_invite_offered_center"),
      ],
    [
      ("faction_accept",[],"Accept.",
       [(str_store_troop_name,s1,"$g_invite_faction_lord"),
        (setup_quest_text,"qst_join_faction"),

        (str_store_troop_name_link, s3, "$g_invite_faction_lord"),
        (str_store_faction_name_link, s4, "$g_invite_faction"),
        (quest_set_slot, "qst_join_faction", slot_quest_giver_troop, "$g_invite_faction_lord"),
        (quest_set_slot, "qst_join_faction", slot_quest_expiration_days, 30),
        (str_store_string, s2, "@Find and speak with {s3} of {s4} to give him your oath of homage."),
        (call_script, "script_start_quest", "qst_join_faction", "$g_invite_faction_lord"),
        (call_script, "script_report_quest_troop_positions", "qst_join_faction", "$g_invite_faction_lord", 3),
        (jump_to_menu, "mnu_invite_player_to_faction_accepted"),
        ]),
      ("faction_reject",[],"Decline.",
       [(call_script, "script_change_player_relation_with_troop", "$g_invite_faction_lord", -3),
        (assign, "$g_invite_faction", 0),
        (assign, "$g_invite_faction_lord", 0),
        (assign, "$g_invite_offered_center", 0),
        (change_screen_return),
        ]),
     ]
  ),
  
  (
    "invite_player_to_faction_accepted",0,"In order to become a vassal, you must swear an oath of homage to {s3}. You shall have to find him and give him your oath in person. {s5}",
    "none",
    [
        (call_script, "script_get_information_about_troops_position", "$g_invite_faction_lord", 0),
        (str_store_troop_name, s3, "$g_invite_faction_lord"),
        (str_store_string, s5, "@{s1}"),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "question_peace_offer",0,"You receive a Peace Offering^^{s1} offers you a peace agreement. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("peace_offer_accept",[],"Accept",
       [
         (call_script, "script_diplomacy_start_peace_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (change_screen_return),
        ]),
      ("peace_offer_reject",[],"Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -5),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "notification_player_faction_active",0,"You now possess land in your name without being tied to any nation. You are a warlord with no master, who knows no higher authority. Enjoy this freedom! -- But know that the kings of the lands will not look kindly upon you, will make every attempt to dispose of you. You may find life very difficult without the protection of a sovereign.",
    "none",
    [
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),
	],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),  
  
  (
    "notification_player_faction_deactive",0,"You no longer hold any land.",
    "none",
    [
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),  
  
  (
    "notification_center_under_siege",0,"{s1} has been besieged by {s2} of {s3}!",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),  

  (
    "notification_village_raided",0,"Enemies have laid waste to a fief^^{s1} has been raided by {s2} of {s3}!",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),  

  (
    "notification_village_raid_started",0,"Your village is under attack!^^{s2} of {s3} is laying waste to {s1}.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_one_faction_left",0,"All of eastern Europe is conquered^^{s1} has defeated all rivals, and stands as the sole sovereign.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue",[],"Continue...",
       [
		(try_begin), 
			(check_quest_active, "qst_oim_getman_last_qst"),
			(neg|check_quest_succeeded, "qst_oim_getman_last_qst"), 
			(neg|check_quest_finished,"qst_oim_getman_last_qst"),
			(call_script, "script_succeed_quest", "qst_oim_getman_last_qst"),
		(try_end), 
		(try_begin), 
			(check_quest_active, "qst_oim_black_lord"),
			(quest_slot_ge, "qst_oim_black_lord", slot_quest_current_state, 1),			
			(str_store_string, s2, "str_oim_end_dmitriy_vlastilin_end"),
            (unlock_achievement, ACHIEVEMENT_GRAND_TZAR),            
			(jump_to_menu, "mnu_oim_last_game_menu"),
		(else_try), 	
			(check_quest_active, "qst_oim_black_lord"),
			(str_store_string, s2, "str_oim_end_text_dmitriy_velikiy"),
            (unlock_achievement, ACHIEVEMENT_GRAND_TZAR),            
			(jump_to_menu, "mnu_oim_last_game_menu"),
		(else_try), 	
			(change_screen_return),
		(end_try),	
        ]),
     ]
  ),
  
  (
    "notification_oath_renounced_faction_defeated",0,"Your motherland is defeated^^You won the battle against {s1}! Thus ends the struggle which began after you renounced your oath to them.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_center_lost",0,"An estate is lost.^^You have lost {s1} to {s2}.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


  (
    "notification_troop_left_players_faction",0,"Betrayal!^^{s1} has left {s2} and joined {s3}.",
    "none",
    [
      (str_store_troop_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$players_kingdom"),
      (str_store_faction_name, s3, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 55),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
      (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_troop_joined_players_faction",0,"Good news!^^ {s1} has left {s2} and joined {s3}.",
    "none",
    [
      (str_store_troop_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (str_store_faction_name, s3, "$players_kingdom"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 55),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
      (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_war_declared",0,"Declaration of War!^^{s1} has declared war against {s2}!",
    "none",
    [
      (try_begin),
        (eq, "$g_notification_menu_var1", "fac_player_supporters_faction"),
        (str_store_faction_name, s1, "$g_notification_menu_var2"),
        (str_store_string, s2, "@you"),
      (else_try),
        (eq, "$g_notification_menu_var2", "fac_player_supporters_faction"),
        (str_store_faction_name, s1, "$g_notification_menu_var1"),
        (str_store_string, s2, "@you"),
      (else_try),
        (str_store_faction_name, s1, "$g_notification_menu_var1"),
        (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (try_end),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_peace_declared",0,"Peace Agreement!^^{s1} and {s2} have made peace!",
    "none",
    [
	  (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_faction_defeated",0,"Nation eliminated!^^{s1} is no more!",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue",[],"Continue...",
       [
         (try_begin),
           (is_between, "$supported_pretender", pretenders_begin, pretenders_end),
           (troop_slot_eq, "$supported_pretender", slot_troop_original_faction, "$g_notification_menu_var1"),
           (try_for_range, ":cur_troop", kingdom_heroes_begin, kingdom_heroes_end),
             (store_troop_faction, ":cur_faction", ":cur_troop"),
             (eq, ":cur_faction", "fac_player_supporters_faction"),
             (troop_set_faction, ":cur_troop", "$g_notification_menu_var1"),
           (try_end),
           (try_for_parties, ":cur_party"),
             (store_faction_of_party, ":cur_faction", ":cur_party"),
             (eq, ":cur_faction", "fac_player_supporters_faction"),
             (party_set_faction, ":cur_party", "$g_notification_menu_var1"),
           (try_end),
           (assign, "$players_kingdom", "$g_notification_menu_var1"),
           (call_script, "script_add_notification_menu", "mnu_notification_rebels_switched_to_faction", "$g_notification_menu_var1", "$supported_pretender"),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_state, sfs_active),
           (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
           (faction_get_slot, ":old_leader", "$g_notification_menu_var1", slot_faction_leader),
           (troop_set_slot, ":old_leader", slot_troop_change_to_faction, "fac_commoners"),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_leader, "$supported_pretender"),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_marshall, "trp_player"),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_ai_state, sfai_default),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_ai_object, -1),
           (troop_set_slot, "$supported_pretender", slot_troop_occupation, slto_kingdom_hero),
           (party_remove_members, "p_main_party", "$supported_pretender", 1),
           (call_script, "script_set_player_relation_with_faction", "$g_notification_menu_var1", 0),
           (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
             (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
             (neq, ":cur_kingdom", "$g_notification_menu_var1"),
             (store_relation, ":reln", ":cur_kingdom", "fac_player_supporters_faction"),
             (set_relation, ":cur_kingdom", "$g_notification_menu_var1", ":reln"),
           (try_end),
           (assign, "$supported_pretender", 0),
           (assign, "$g_recalculate_ais", 1),
           (assign, "$supported_pretender_old_faction", 0),
           (call_script, "script_update_all_notes"),
		   (call_script, "script_player_join_faction", "$g_notification_menu_var1"),
         (try_end),
		 
		#oim code
		(try_begin), 
		#qst_oim_na_rech_pospolitu
		   (check_quest_active, "qst_oim_na_rech_pospolitu"),
		   (neg|check_quest_succeeded, "qst_oim_na_rech_pospolitu"), 
		   (neg|check_quest_finished,"qst_oim_na_rech_pospolitu"),
		   (eq, "$g_notification_menu_var1", "fac_kingdom_1"),
		   (call_script, "script_succeed_quest", "qst_oim_na_rech_pospolitu"),
		(try_end),
		#barabash code
		(try_begin), 
		   #qst_oim_na_mc
		   (check_quest_active, "qst_oim_na_msk_tsarzd"),
		   (neg|check_quest_succeeded, "qst_oim_na_msk_tsarzd"), 
		   (neg|check_quest_finished,"qst_oim_na_msk_tsarzd"),
		   (eq, "$g_notification_menu_var1", "fac_kingdom_2"),
		   (call_script, "script_succeed_quest", "qst_oim_na_msk_tsarzd"),
		(try_end), 
		(try_begin), 
		   #qst_oim_na_mc
		   (check_quest_active, "qst_oim_getman_barabash_reb"),
		   (neg|check_quest_succeeded, "qst_oim_getman_barabash_reb"), 
		   (neg|check_quest_finished,"qst_oim_getman_barabash_reb"),
		   (eq, "$g_notification_menu_var1", "fac_kingdom_2"),
		   (call_script, "script_succeed_quest", "qst_oim_getman_barabash_reb"),
		(try_end), 
		(try_begin), 
			(check_quest_active, "qst_oim_getman_barabash_casus_beli"),
			(neg|check_quest_succeeded, "qst_oim_getman_barabash_casus_beli"), 
			(neg|check_quest_finished,"qst_oim_getman_barabash_casus_beli"),
			(eq, "$g_notification_menu_var1", "fac_kingdom_1"),
			(call_script, "script_succeed_quest", "qst_oim_getman_barabash_casus_beli"),
		(try_end), 
		(try_begin), 
		 #qst_oim_getman_hmel_casus_beli
			(check_quest_active, "qst_oim_getman_hmel_casus_beli"),
			(neg|check_quest_succeeded, "qst_oim_getman_hmel_casus_beli"), 
			(neg|check_quest_finished,"qst_oim_getman_hmel_casus_beli"),
			(eq, "$g_notification_menu_var1", "fac_kingdom_2"),
			(call_script, "script_succeed_quest", "qst_oim_getman_hmel_casus_beli"),
		(try_end), 
		(try_begin), 
			(check_quest_active, "qst_oim_getman_hmel_reb"),
			(neg|check_quest_succeeded, "qst_oim_getman_hmel_reb"), 
			(neg|check_quest_finished,"qst_oim_getman_hmel_reb"),
			(eq, "$g_notification_menu_var1", "fac_kingdom_1"),
			(call_script, "script_succeed_quest", "qst_oim_getman_hmel_reb"),
		(try_end), 
		(try_begin), 
		#qst_oim_na_rech_pospolitu
		   (check_quest_active, "qst_mest_i_zakon3"),
		   (neg|check_quest_succeeded, "qst_mest_i_zakon3"), 
		   (neg|check_quest_finished,"qst_mest_i_zakon3"),
		   (eq, "$g_notification_menu_var1", "fac_kingdom_1"),
		   (call_script, "script_end_quest", "qst_mest_i_zakon3"),
         (try_end),
         (change_screen_return),
        ]),
     ]
  ),

  
  (
    "notification_rebels_switched_to_faction",0,"Rebellion Success!^^ Your rebellion is victorious! Your nation now has the sole claim to the title of {s11}, with {s12} as the single ruler.",
    "none",
    [
      (str_store_faction_name, s11, "$g_notification_menu_var1"),
	  (try_begin), 
		(check_quest_active, "qst_oim_black_lord"),
		(str_store_troop_name, s12, "trp_player"),
	  (else_try), 
      (str_store_troop_name, s12, "$g_notification_menu_var2"),
	  (end_try), 	
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue",[],"Continue...",
       [
		 #oim code
		 (try_begin), 
			(check_quest_active, "qst_oim_black_lord"),
			#(quest_slot_eq, "qst_oim_black_lord", slot_quest_current_state, 1),
			(quest_set_slot, "qst_oim_black_lord", slot_quest_current_state, 1),
			(jump_to_menu, "mnu_oim_razin_asking_for_marshal"),
		 (else_try), 	
         (assign, "$talk_context", tc_rebel_thanks),
         (start_map_conversation, "$g_notification_menu_var2"),
         (change_screen_return),
		 (end_try), 	
        ]),
     ]
  ),


  (
    "kill_local_merchant_begin",0,"You spot your victim and follow him, watching as he turns a corner. This will surely be your best opportunity to attack him.",
    "none",
    [
    ],
    [
      ("continue",[],"Continue...",
       [(set_jump_mission,"mt_back_alley_kill_local_merchant"),
        (party_get_slot, ":town_alley", "$qst_kill_local_merchant_center", slot_town_alley),
        (modify_visitors_at_site,":town_alley"),
        (reset_visitors),
        (set_visitor, 0, "trp_player"),
        (set_visitor, 1, "trp_local_merchant"),
        (jump_to_menu, "mnu_town"),
        (jump_to_scene,":town_alley"),
        (change_screen_mission),
        ]),
     ]
  ),

  (
    "auto_return_to_map",0,"stub",
    "none",
    [(change_screen_map)],
    []
  ),

    (
    "monfor_talk",menu_text_color(0xFF000000)|mnf_disable_all_keys,"Welcome, adventurer, to Mount&Blade. Before you can begin playing the game you must create a character. First, select your character's gender.",
    "none",
    [],
    [
      ("start_male",[],"Male.", []),
      ("go_back",[],"Go back", [(change_screen_quit),]),
      ]
  ),

#OiM hacks

  ("oim_training_ground_selection_details_ranged",mnf_disable_all_keys,"What distance do you want to shoot from?",
   "none",
   [],
    [
      ("camp_train_ranged_details_1",[], "10 yards.",
       [
         (call_script, "script_oim_start_training_at_training_ground", "$temp", 10),
         ]),
      ("camp_train_ranged_details_2",[], "20 yards.",
       [
         (call_script, "script_oim_start_training_at_training_ground", "$temp", 20),
         ]),
      ("camp_train_ranged_details_3",[], "30 yards.",
       [
         (call_script, "script_oim_start_training_at_training_ground", "$temp", 30),
         ]),
      ("camp_train_ranged_details_4",[], "40 yards.",
       [
         (call_script, "script_oim_start_training_at_training_ground", "$temp", 40),
         ]),
      ("camp_train_ranged_details_5",[(eq, "$g_mt_mode", ctm_ranged),], "50 yards.",
       [
         (call_script, "script_oim_start_training_at_training_ground", "$temp", 50),
         ]),
      ("camp_train_ranged_details_6",[(eq, "$g_mt_mode", ctm_ranged),], "60 yards.",
       [
         (call_script, "script_oim_start_training_at_training_ground", "$temp", 60),
         ]),
      ("camp_train_ranged_details_7",[(eq, "$g_mt_mode", ctm_ranged),], "70 yards.",
       [
         (call_script, "script_oim_start_training_at_training_ground", "$temp", 70),
         ]),
      ("go_back_dot",[],"Go back.",
       [
		(assign, "$oim_monfor_ready_to_fire_musquet", 2),     
    (jump_to_menu, "mnu_start_phase_2"),
        ]
       ),
      ]
  ),

  ("oim_training_ground_description",mnf_disable_all_keys,"{s0}",
   "none",
   [],
    [
      ("continue", [], "Continue...",
       [
         (set_jump_mission, "mt_oim_training_ground_training"),
         (jump_to_scene, "$g_training_ground_training_scene"),
         (change_screen_mission),
        ]
       ),
      ]
  ),  

  ("oim_training_ground_training_result",mnf_disable_all_keys,"{s7}{s2}",
   "none",
   [
     (store_skill_level, ":trainer_skill", "skl_trainer", "trp_player"),
     (store_add, ":trainer_skill_multiplier", 5, ":trainer_skill"),
     (call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
     (str_clear, s2),
     (troop_get_slot, ":num_fit", "trp_stack_selection_amounts", 1),
     (troop_get_slot, ":num_slots", "trp_stack_selection_amounts", 0),
     (try_begin),
       (gt, "$g_training_ground_training_success_ratio", 0),
       (store_mul, ":xp_ratio_to_add", "$g_training_ground_training_success_ratio", "$g_training_ground_training_success_ratio"),
       (try_begin),
         (eq, "$g_training_ground_training_success_ratio", 100),
         (val_mul, ":xp_ratio_to_add", 2), #2x when perfect
       (try_end),
       (try_begin),
         (eq, "$g_mt_mode", ctm_melee),
         (val_div, ":xp_ratio_to_add", 2),
       (try_end),
       (val_div, ":xp_ratio_to_add", 10), # value over 1000
       (try_begin),
         (gt, ":num_fit", 8),
         (val_mul, ":xp_ratio_to_add", 3),
         (assign, ":divisor", ":num_fit"),
         (convert_to_fixed_point, ":divisor"),
         (store_sqrt, ":divisor", ":divisor"),
         (convert_to_fixed_point, ":xp_ratio_to_add"),
         (val_div, ":xp_ratio_to_add", ":divisor"),
       (try_end),
##       (assign, reg0, ":xp_ratio_to_add"),
##       (display_message, "@xp earn ratio: {reg0}/1000"),
       (store_mul, ":xp_ratio_to_add_with_trainer_skill", ":xp_ratio_to_add", ":trainer_skill_multiplier"),
       (val_div, ":xp_ratio_to_add_with_trainer_skill", 10),
       (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
       (store_add, ":end_cond", ":num_slots", 2),
       (try_for_range, ":i_slot", 2, ":end_cond"),
         (troop_get_slot, ":amount", "trp_stack_selection_amounts", ":i_slot"),
         (troop_get_slot, ":troop_id", "trp_stack_selection_ids", ":i_slot"),
         (assign, ":end_cond_2", ":num_stacks"),
         (try_for_range, ":stack_no", 0, ":end_cond_2"),
           (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
           (eq, ":stack_troop", ":troop_id"),
           (assign, ":end_cond_2", 0), #break
           (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", ":amount", ":xp_ratio_to_add_with_trainer_skill"),
           (str_store_troop_name_by_count, s1, ":troop_id", ":amount"),
           (assign, reg1, ":amount"),
           (str_store_string, s2, "@{s2}^{reg1} {s1} earned {reg0} experience."),
         (try_end),
       (try_end),
       (try_begin),
         (eq, "$g_mt_mode", ctm_melee),
         (store_mul, ":special_xp_ratio_to_add", ":xp_ratio_to_add", 3),
         (val_div, ":special_xp_ratio_to_add", 2),
         (try_for_range, ":enemy_index", 0, "$g_training_ground_training_num_enemies"),
           (troop_get_slot, ":troop_id", "trp_temp_array_a", ":enemy_index"),
           (assign, ":end_cond_2", ":num_stacks"),
           (try_for_range, ":stack_no", 0, ":end_cond_2"),
             (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
             (eq, ":stack_troop", ":troop_id"),
             (assign, ":end_cond_2", 0), #break
             (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", 1, ":special_xp_ratio_to_add"),
             (str_store_troop_name, s1, ":troop_id"),
             (str_store_string, s2, "@{s2}^{s1} earned an additional {reg0} experience."),
           (try_end),
         (try_end),
       (try_end),
       (try_begin),
         (call_script, "script_cf_training_ground_sub_routine_for_training_result", "trp_player", -1, 1, ":xp_ratio_to_add"),
         (str_store_string, s2, "@^You earned {reg0} experience.{s2}"),
       (try_end),
     (try_end),
     (try_begin),
       (eq, "$g_training_ground_training_success_ratio", 0),
       (str_store_string, s7, "@The training didn't go well at all."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 25),
       (str_store_string, s7, "@The training didn't go well at all."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 50),
       (str_store_string, s7, "@The training didn't go very well."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 75),
       (str_store_string, s7, "@The training went quite well."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 99),
       (str_store_string, s7, "@The training went very well."),
     (else_try),
       (str_store_string, s7, "@The training went perfectly."),
     (try_end),
     
     ],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_oim_training_ground_selection_details_ranged"),
        ]
       ),
      ("hvatit",[],"Stop training...",
       [
      (assign, "$oim_monfor_ready_to_fire_musquet", 2),  
    (jump_to_menu, "mnu_start_phase_2"),
        ]
       ),
   
      ]
   ),

   
#   mnu_captivity_castle_taken_prisoner",
  ("oim_defeated_by_monk",mnf_disable_all_keys,"You were defeated in the fight with the priest, and he ordered the guards to jail you.",
   "none",
   [
		(set_background_mesh, "mesh_pic_tavern"),
   ],
    [
      ("continue", [], "Continue...",
       [
        (assign, "$g_player_is_captive", 1),
        (assign,"$auto_menu",-1),
        (assign, "$capturer_party", "$g_encountered_party"),
		(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -5),		
		(jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
        ]
       ),
      ]
  ),  

  
  ("oim_monk_is_killed",mnf_disable_all_keys,"You managed to overcome the priest and seize the icon. The time has come to flee the city.",
   "none",
   [
   		(set_background_mesh, "mesh_pic_defeat"),
   ],
    [
      ("continue", [], "Continue...",
       [
			(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -15),
        (jump_to_menu, "mnu_auto_return_to_map"),
        ]
       ),
      ]
  ),  

  
   ("oim_tatarin_brought_to_perekop",mnf_disable_all_keys,"You have arrived in Perekop.",
   "none",
   [
   		(set_background_mesh, "mesh_pic_village_s"),   
   ],
    [
      ("continue", [(eq, "$talked_to_tatarin2", 0)], "Continue...",
       [
		(quest_set_slot, "qst_oim_bring_tatarin_to_perekop", slot_quest_current_state, 1),
		(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
        (reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,17,"trp_oim_tatarin_zolotarenko"),
        (jump_to_scene,"scn_meeting_scene_plain_forest"),
        (change_screen_map_conversation, "trp_oim_tatarin_zolotarenko"),         
        ]
       ),
   
      ("continue", [(eq, "$talked_to_tatarin2", 1),], "Continue...",
        [
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]
       ),   
      ]
  ), 
  

  ("oim_talk_to_tatarin",mnf_disable_all_keys,"{s2}",
   "none",
   [],
    [
      ("talk_to_tatarin", [(eq, "$talked_to_tatarin", 0)],"Talk to the Tatar.",
       [
		(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
        (reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,17,"trp_oim_tatarin_zolotarenko"),
        (jump_to_scene,"scn_meeting_scene_plain_forest"),
        (change_screen_map_conversation, "trp_oim_tatarin_zolotarenko"),         
        ]
       ),
   
      ("continue", [(eq, "$talked_to_tatarin", 1),
					(neg|check_quest_failed,"qst_oim_bring_tatarin_to_sich"),
					], "Continue...",
       [
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]
       ),	

      ("continue", [(eq, "$talked_to_tatarin", 1),
					(check_quest_active,"qst_oim_bring_tatarin_to_sich"),
					(check_quest_failed,"qst_oim_bring_tatarin_to_sich"),
					], "Continue...",
       [
		(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
        (reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,17,"trp_rhodok_sergeant"),
        (jump_to_scene,"scn_meeting_scene_plain_forest"),
        (change_screen_map_conversation, "trp_rhodok_sergeant"),  
        ]
       ),

      ("continue", [(eq, "$talked_to_tatarin", 2)], "Continue...",
       [
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]
       ),   
   
      ]
  ),  
  
   ("oim_fight_sem_samuraev",mnf_disable_all_keys,"{s2}",
   "none",
   [
		(set_background_mesh, "mesh_pic_kozak_army"),
   ],
    [
      ("continue", [(eq, "$oim_fight_sem_samuraev", 0),], "Continue...",
       [
		(quest_set_slot, "qst_oim_sem_samuraev", slot_quest_current_state, 1),
		(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
        (reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,17,"trp_rhodok_sergeant"),
        (jump_to_scene,"scn_meeting_scene_plain_forest"),
        (change_screen_map_conversation, "trp_rhodok_sergeant"),         
        ]
       ),
     
   ("defend_village_", [(eq, "$oim_fight_sem_samuraev", 1),],"Prepare for a fight!",
       [
        (party_get_slot, ":scene_to_use", "$g_encountered_party", slot_castle_exterior),
        (modify_visitors_at_site, ":scene_to_use"),
        (reset_visitors),
        (set_visitors, 0, "trp_rhodok_sergeant", 10),
        #(set_visitors, 2, "trp_trainee_peasant", 10),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission,"mt_oim_sem_samuraev_battle"),
        (jump_to_scene, ":scene_to_use"),
        (jump_to_menu, "mnu_oim_sem_sameraev_battle_result"),
        (assign, "$g_mt_mode", vba_after_training),
        (change_screen_mission),
        ]),
    ]), 

  ("oim_sem_sameraev_battle_result",mnf_disable_all_keys,"{s2}",
   "none",
   [
    (try_begin),
		(eq, "$g_battle_result", -1),
		(str_store_string, s2, "@OiM You ve failed to protect the village"),
		(set_background_mesh, "mesh_pic_defeat"),
    (else_try),
		(str_store_string, s2, "@OiM You ve protected the village"),
		(set_background_mesh, "mesh_pic_victory"),
    (end_try), 

   ],
    [
      ("continue", [(eq, "$g_battle_result", -1),], "Continue...",
       [
		#add code to fail and end quest
        (call_script, "script_village_set_state",  "$current_town", svs_looted),

        (party_add_particle_system, "$current_town", "psys_map_village_fire"), #new
        (party_add_particle_system, "$current_town", "psys_map_village_fire_smoke"), #new
        (party_set_icon, "$current_town", "icon_village_burnt_a"), #new
        (party_set_slot, "$current_town", slot_village_smoke_added, 1), #new
		
        (party_set_slot, "$current_town", slot_village_raid_progress, 100), #was 0
        (party_set_slot, "$current_town", slot_village_recover_progress, 0),

        (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -15),
		(call_script, "script_fail_quest", "qst_oim_sem_samuraev"),
		(call_script, "script_end_quest", "qst_oim_sem_samuraev"),
		(jump_to_menu, "mnu_auto_return_to_map"),
        ]),
		
   ("continue", [(neq, "$g_battle_result", -1),], "Continue...",
       [
		(call_script, "script_change_player_relation_with_faction", "fac_kingdom_3", 5),		
		(call_script, "script_end_quest", "qst_oim_sem_samuraev"),
		(call_script, "script_change_player_relation_with_center", "$g_encountered_party", 15),
		(jump_to_menu, "mnu_auto_return_to_map"),
		(party_get_slot, ":merchant_troop", "$g_encountered_party", slot_town_elder),
		(troop_sort_inventory, ":merchant_troop"),
		(change_screen_loot, ":merchant_troop"),
        ]),   
      ]
  ),  

	#
   ("oim_talk_to_bandits_horse",mnf_disable_all_keys,"{s2}",
   "none",
   [
		(set_background_mesh, "mesh_pic_sea_raiders"),   
		(str_store_string, s2, "str_oim_horse_ambush_text"),
   ],
    [
      ("continue", [(eq, "$oim_fight_horse", 0),], "Continue...",
       [
		(assign, "$oim_horse_ambush_dlg", 1),
		(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
        (reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,17,"trp_bandit"),
        (jump_to_scene,"scn_meeting_scene_plain_forest"),
        (change_screen_map_conversation, "trp_bandit"),         
        ]
       ),
     
 ("defend_village_", [(eq, "$oim_fight_horse", 1),], "Prepare for a fight!",
       [
		(call_script, "script_setup_random_scene"), 
		(assign, ":scene_to_use", reg0), 
        (modify_visitors_at_site, ":scene_to_use"),
        (reset_visitors),
        (set_visitors, 0, "trp_bandit", 20),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission,"mt_oim_sem_samuraev_battle"),
        (jump_to_scene, ":scene_to_use"),
        (jump_to_menu, "mnu_oim_bandits_battle_for_horse_result"),
        (assign, "$g_mt_mode", vba_after_training),
        (change_screen_mission),
        ]),
      ]
  ), 

  ("oim_bandits_battle_for_horse_result",mnf_disable_all_keys,"{s2}",
   "none",
   [
    (try_begin),
		(eq, "$g_battle_result", -1),
		(str_store_string, s2, "@OiM You ve failed to protect your horse"),
		(set_background_mesh, "mesh_pic_defeat"),   
    (else_try),
		(str_store_string, s2, "@OiM You ve protected the horse"),
		(set_background_mesh, "mesh_pic_victory"),   
    (end_try), 

   ],
    [
      ("continue", [(eq, "$g_battle_result", -1),], "Continue...",
       [
			#add code to fail and end quest
			(assign, "$oim_horse_ambush_dlg", 2),
			(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,"trp_bandit"),
			(jump_to_scene,"scn_meeting_scene_plain_forest"),
			(change_screen_map_conversation, "trp_bandit"),   
        ]),
		
   ("continue", [(neq, "$g_battle_result", -1),], "Continue...",
       [
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]),   
      ]
  ),  
  
 ("oim_invest_menu",mnf_disable_all_keys,"{s2}",
   "none",
   [
		(set_background_mesh, "mesh_pic_pergament"),   
		(str_store_string, s2, "@OiM Da takoe bivaet raz v zhizni"),
   ],
    [
      ("zabrat_dengi", [],"Take the money",
       [
			(call_script, "script_change_player_relation_with_faction", "fac_kingdom_5", -12),
			(call_script, "script_change_player_relation_with_troop", "trp_kingdom_5_lord", -24),
			(call_script, "script_change_player_honor", -2), 
			(call_script, "script_fail_quest", "qst_oim_invest_2"),
			(call_script, "script_end_quest", "qst_oim_invest_2"),
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]
       ),
     
	 ("do_not_take_", [], "Commit no such felony",
       [
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]),
      ]
  ), 
  
  ("oim_auto_talk_menu", mnf_disable_all_keys,"{s2}",
   "none",
  [
  #code
	(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
	(reset_visitors),
	(set_visitor,0,"trp_player"),
	(set_visitor,17,"$oim_auto_talk_troop"),
	(jump_to_scene,"scn_meeting_scene_plain_forest"),
	(change_screen_map_conversation, "$oim_auto_talk_troop"),   
  ], 
  []
  ), 

  
  #Potop. Defend Village agains badits
  ("oim_potop_defend_church",mnf_disable_all_keys,"You have arrived in time! The Swedes have not yet plundered the monastery. Time to teach them the lesson of Kirchholm once more!",
   "none",
   [
		(set_background_mesh, "mesh_pic_sea_raiders"),   
   ],
    [
      ("continue", [(quest_slot_eq, "qst_oim_potop_defend_church", slot_quest_current_state, 0),], "Continue...",
       [
		(quest_set_slot, "qst_oim_potop_defend_church", slot_quest_current_state, 1),
		(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
        (reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,17,"trp_nord_archer"),
        (jump_to_scene,"scn_meeting_scene_plain_forest"),
        (change_screen_map_conversation, "trp_nord_archer"),         
        ]
       ),
     
      ("defend_village_", [(quest_slot_eq, "qst_oim_potop_defend_church", slot_quest_current_state, 1),], "Prepare for a fight!",
       [
			(party_get_slot, ":scene_to_use", "p_village_66", slot_castle_exterior),
			(modify_visitors_at_site, ":scene_to_use"),
			(reset_visitors),
			(set_party_battle_mode),
			(set_battle_advantage, 0),
			#(assign, "$g_enemy_party", "p_collective_enemy"), 
			(set_spawn_radius,0),
			(spawn_around_party,"$current_town", "pt_kingdom_hero_party"),
			(assign, ":party", reg0),
			
			(party_clear, ":party"), 
			(call_script, "script_party_count_fit_for_battle", "p_main_party"), 
			(assign, ":main_party_count",reg0), 
			(assign, ":reiters_count", ":main_party_count"), 
			(assign, ":mushket_count", ":main_party_count"), 
			(assign, ":pikeman_count", ":main_party_count"), 
			(assign, ":sword_masters_count", ":main_party_count"), 
			(assign, ":dragoons_count", ":main_party_count"), 
			(val_mul, ":reiters_count", 25),
			(val_div, ":reiters_count", 100),
			(val_mul, ":mushket_count", 45),
			(val_div, ":mushket_count", 100),
			(val_mul, ":pikeman_count", 35),
			(val_div, ":pikeman_count", 100),
			(val_mul, ":sword_masters_count", 15),
			(val_div, ":sword_masters_count", 100),
			(val_add, ":sword_masters_count", 5), 
			(val_mul, ":dragoons_count", 25),
			(val_div, ":dragoons_count", 100),
			(try_begin),
				(lt, ":mushket_count", 10), 
				(assign, ":mushket_count", 10),
			(try_end),
			(try_begin),
				(lt, ":reiters_count", 5), 
				(assign, ":reiters_count", 5),
			(try_end),
			(try_begin),
				(lt, ":sword_masters_count", 5), 
				(assign, ":sword_masters_count", 5),
			(try_end),
			(try_begin),
				(lt, ":dragoons_count", 10), 
				(assign, ":dragoons_count", 10),
			(try_end),
			(try_begin),
				(lt, ":pikeman_count", 10), 
				(assign, ":pikeman_count", 10),
			(try_end),
			
			(val_clamp, ":mushket_count", 5, 25),
			(val_clamp, ":reiters_count", 5, 6),
			(val_clamp, ":dragoons_count", 5, 15),
			(val_clamp, ":pikeman_count", 5, 25),
			
			(party_add_members, ":party", "trp_nord_archer", ":mushket_count"),
			(party_add_members, ":party", "trp_nord_veteran", ":reiters_count"),
			#(party_add_members, "$g_enemy_party", "trp_sved_swordmaster", ":sword_masters_count"),
			(party_add_members, ":party", "trp_nord_warrior", ":dragoons_count"),
			(party_add_members, ":party", "trp_nord_trained_footman", ":pikeman_count"),
			#(party_get_battle_opponent, ":party_x", "p_main_party"), 
			#(party_leave_cur_battle, ":party_x"),
			#(call_script, "script_clear_party_group", "$g_encountered_party"),
			(party_clear, "$g_encountered_party"),
			(party_quick_attach_to_current_battle, ":party", 1), 
			(quest_set_slot, "qst_oim_potop_defend_church", slot_quest_target_party, ":party"),
			(assign, "$g_battle_result", 0),
			(set_jump_mission,"mt_chenstohova_lead_charge"),
			(jump_to_scene, ":scene_to_use"),
			(jump_to_menu, "mnu_oim_potop_defend_church_result"),
			(assign, "$g_mt_mode", vba_after_training),
			(change_screen_mission),
      ]),
	]  
  ), 

  ("oim_potop_defend_church_result",mnf_disable_all_keys,"{s2}",
   "none",
   [
    (quest_get_slot, ":party", "qst_oim_potop_defend_church", slot_quest_target_party),
	(try_begin),
		(eq, "$g_battle_result", -1),
		(str_store_string, s2, "str_oim_generik_death_qst"),
		(set_background_mesh, "mesh_pic_defeat"), 
		(try_begin), 
			(neq, ":party", -1),
			(remove_party, ":party"),
			(quest_set_slot, "qst_oim_potop_defend_church", slot_quest_target_party, -1),
		(end_try),
    (else_try),
		(try_begin), 
			(neq, ":party", -1),
			(call_script, "script_party_calculate_loot", ":party"),
			(gt, reg0, 0),
			(troop_sort_inventory, "trp_temp_troop"),
			(quest_set_slot, "qst_oim_potop_defend_church", slot_quest_target_party, -1),
			(remove_party, ":party"),
			(change_screen_loot, "trp_temp_troop"),
		(end_try),
		(str_store_string, s2, "@OiM You ve protected the village"),
		(set_background_mesh, "mesh_pic_victory"),   
    (end_try), 

   ],
    [
      ("continue", [(eq, "$g_battle_result", -1),], "Continue...",
       [
            (call_script, "script_village_set_state",  "$current_town", svs_looted),

            (party_add_particle_system, "$current_town", "psys_map_village_fire"), #new
            (party_add_particle_system, "$current_town", "psys_map_village_fire_smoke"), #new
            (party_set_icon, "$current_town", "icon_village_burnt_a"), #new
            (party_set_slot, "$current_town", slot_village_smoke_added, 1), #new
		
            (party_set_slot, "$current_town", slot_village_raid_progress, 100), #was 0
            (party_set_slot, "$current_town", slot_village_recover_progress, 0),

            (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -5),
			(call_script, "script_fail_quest", "qst_oim_potop_defend_church"),
			#(jump_to_menu, "mnu_auto_return_to_map"),
			(change_screen_quit),			
        ]),
		
   ("continue", [(neq, "$g_battle_result", -1),], "Continue...",
       [
			(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 5),		
			(call_script, "script_succeed_quest", "qst_oim_potop_defend_church"),
			(quest_set_slot, "qst_oim_potop_defend_church", slot_quest_current_state, 2),
			(call_script, "script_refresh_village_defenders", "$g_encountered_party"),
			(jump_to_menu, "mnu_auto_return_to_map"),
      ]),
	] 
  ),  

  ("oim_auto_message_menu",mnf_disable_all_keys,"{s2}",
   "none",
   [],
    [
      ("continue", [], "Continue...",
       [
			(jump_to_menu, "mnu_auto_return_to_map"),
       ]
  ),
    ]
  ), 

  ("oim_potop_romeo_fight",mnf_disable_all_keys,"{s2}",
   "none",
   [
    (try_begin),
		(quest_slot_eq, "qst_oim_potop_volodievskiy", slot_quest_current_state, 3), 
		(str_store_string, s2, "str_before_fight_swedish"),
		(set_background_mesh, "mesh_pic_tavern"),   
	(else_try), 
		(quest_slot_eq, "qst_oim_potop_volodievskiy", slot_quest_current_state, 4), 
		(eq, "$g_battle_result", -1),
		(str_store_string, s2, "str_before_fight_swedish_lost"),
		(set_background_mesh, "mesh_pic_defeat"),   
    (else_try),
		(set_background_mesh, "mesh_pic_victory"),   
		(str_store_string, s2, "str_before_fight_swedish_win"),
    (end_try), 

   ],
    [
	  ("continue", [(quest_slot_eq, "qst_oim_potop_volodievskiy", slot_quest_current_state, 3),], "Continue...",
       [
	        (party_get_slot, ":scene_to_use", "$g_encountered_party", slot_town_castle),
			(modify_visitors_at_site, ":scene_to_use"),
			(reset_visitors),
			(set_visitors, 17, "trp_nord_warrior", 2),
			(set_visitors, 19, "trp_nord_warrior", 2),
			(set_visitors, 20, "trp_nord_warrior", 2),
			(set_visitors, 21, "trp_nord_warrior", 2),
			(set_visitors, 22, "trp_nord_warrior", 2),
			(set_visitors, 18, "trp_oim_polish_lord", 1),
			#(set_visitors, 1, "trp_npc1", 1),
			(set_visitor, 0, "trp_player"),
			(set_party_battle_mode),
			(set_battle_advantage, 0),
			(assign, "$g_battle_result", 0),
			(set_jump_mission,"mt_oim_interior_battle"),
			(jump_to_scene, ":scene_to_use"),
			(jump_to_menu, "mnu_oim_potop_romeo_fight"),
			(assign, "$g_mt_mode", vba_after_training),
			(quest_set_slot, "qst_oim_potop_volodievskiy", slot_quest_current_state, 4), 
			(change_screen_mission),
        ]),
	
      ("continue", [(eq, "$g_battle_result", -1), (quest_slot_eq, "qst_oim_potop_volodievskiy", slot_quest_current_state, 4),], "Continue...",
       [
			#add code to fail and end quest
			(assign, "$g_player_is_captive", 1),
			(assign,"$auto_menu",-1),
			(assign, "$capturer_party", "$g_encountered_party"),
			(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -5),		
			(jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
			(quest_set_slot, "qst_oim_potop_volodievskiy", slot_quest_current_state, 3), 
        ]),
		
     ("continue", [(neq, "$g_battle_result", -1), (quest_slot_eq, "qst_oim_potop_volodievskiy", slot_quest_current_state, 4),], "Continue...",
       [
			(quest_set_slot, "qst_oim_potop_volodievskiy", slot_quest_current_state, 10), #something like the quest is ended
			(str_store_string, s5, "@OiM_Potop Pani osvobozhdena. Pora idti k volodievskomu"),	
			(add_quest_note_from_sreg, "qst_oim_potop_volodievskiy", 6, s5, 1),
			(jump_to_menu, "mnu_auto_return_to_map"),
			(party_force_add_members, "p_main_party", "trp_knight_1_2_wife", 1),			
        ]),   
      ]
  ),  
  
  
  #
   (
    "capitan_vid",mnf_disable_all_keys,"You ask the soldiers at the camp where you may find their commander, and they point out the captain.",
    "none",
    [
		(set_background_mesh, "mesh_pic_recruits"),   
	],
    [
      ("merch_tatar",
       [
			(eq, "$g_encountered_party", "p_training_ground_4"),
	   ],"Talk to the captain of the Tatar mercenaries.",
       [
	     (call_script, "script_naem_set_param", 0), 
		 (music_set_situation, 0)
       ]),
	 
	 ("merch_kozak",
        [
			(eq, "$g_encountered_party", "p_training_ground_3"),
		],"Talk to the captain of the Cossack mercenaries.",
        [
		  (call_script, "script_naem_set_param", 1), 
		  (music_set_situation, 0),
        ]),
		
	("merch_polyak",
        [
			(eq, "$g_encountered_party", "p_training_ground_5"),
		],"Talk to the captain of the Polish mercenaries.",
        [
		  (call_script, "script_naem_set_param", 2),
		  (music_set_situation, 0),
        ]),

	("merch_shved",
        [
			(eq, "$g_encountered_party", "p_training_ground_2"),
		],"Talk to the captain of the Swedish mercenaries.",
		[
		  (call_script, "script_naem_set_param", 3), 
		  (music_set_situation, 0),
        ]),

	("merch_moskov",
        [
			(eq, "$g_encountered_party", "p_training_ground_1"),
		],"Talk to the captain of the Muscovite mercenaries.",
		[
		  (call_script, "script_naem_set_param", 4), 
		  (music_set_situation, 0),
        ]),	 
                 
      ("Back_1",[],"Leave...",
	    [
	     (change_screen_return),
        ]),
    ]
  ), 

  #oim_potop_kshetuskiy
  ("oim_potop_kshetuskiy",mnf_disable_all_keys,"{s2}",
   "none",
   [
    (try_begin),
		(quest_slot_eq, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 2),
		(str_store_string, s2, "@OiM_Potop_kshetuskiy Probracco v konushnyu"), 
		(set_background_mesh, "mesh_pic_village_u"),   
	(else_try),
		(eq, "$g_battle_result", -1),
		(str_store_string, s2, "@OiM You ve failed to win battle"),
		(set_background_mesh, "mesh_pic_defeat"),   
    (else_try),
		(quest_slot_eq, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 3),
		(str_store_string, s2, "@OiM You ve got the horse. Pora idti otdavat konya"),
		(set_background_mesh, "mesh_pic_village_u"),   
    (else_try),
		(quest_slot_eq, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 4),
		(str_store_string, s2, "@Kozaki podnyali na nogi strazhu!"),		
		(set_background_mesh, "mesh_pic_kozak_army"),   
    (end_try), 

   ],
    [
      ("sneak_in", [(quest_slot_eq, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 2),],"Continue...",
       [
			#should be fixed
			(assign, ":scene_to_use", "scn_oim_potop_horse_stables"),
			(modify_visitors_at_site, ":scene_to_use"),
            (reset_visitors),
			(set_visitor, 17, "trp_reestrovuy_kozak"),
			(set_visitor, 18, "trp_reestrovuy_kozak"),
			(set_visitor, 19, "trp_reestrovuy_kozak"),
			(set_visitor, 20, "trp_reestrovuy_kozak"),
			(set_visitor, 21, "trp_reestrovuy_kozak"),
			(assign, "$g_battle_result", 0),
			(set_jump_mission,"mt_oim_steale_horse"),
			(jump_to_scene, ":scene_to_use"),
			(assign, "$g_next_menu", "mnu_oim_potop_kshetuskiy"),
			(change_screen_mission),
			(quest_set_slot, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 3),
        ]),
  
  ("continue", [(eq, "$g_battle_result", -1),], "Continue...",
       [
			#add code to fail and end quest
			#no need to it, quest failed
			##(assign, "$g_player_is_captive", 1),
			##(assign,"$auto_menu",-1),
			##(assign, "$capturer_party", "$g_encountered_party"),
			##(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -5),		
			##(jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
			##(call_script, "script_fail_quest", "qst_oim_potop_kshetuskiy"),
			##(call_script, "script_end_quest", "qst_oim_potop_kshetuskiy"),
			##(call_script, "script_fail_quest", "qst_oim_potop_main"),
			##(call_script, "script_end_quest", "qst_oim_potop_main"),
			
			(str_store_string, s2, "str_oim_generik_death_qst"),
			(jump_to_menu, "mnu_oim_last_game_menu"),

        ]),
		
   ("continue", [(quest_slot_eq, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 3),(neq, "$g_battle_result", -1),], "Continue...",
       [
			(quest_set_slot, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 10), #something like the quest is ended
			(str_store_string, s5, "@OiM_Potop Loshad teper u menya pora idti k kshetuskomu"),	
			(add_quest_note_from_sreg, "qst_oim_potop_kshetuskiy", 6, s5, 1),
			#fix it!
			(troop_add_item, "trp_player", "itm_oim_qst_horse"), 
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]),   
		
		("defend_village_", [(quest_slot_eq, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 4),(neq, "$g_battle_result", -1),], "Prepare for a fight!",
        [
			(party_get_slot, ":scene_to_use", "$g_encountered_party", slot_castle_exterior),
			#oim code to test usage
			#(party_get_slot, ":scene_to_use", "p_village_55", slot_castle_exterior),
			(modify_visitors_at_site, ":scene_to_use"),
			(reset_visitors),
			(set_party_battle_mode),
			(set_battle_advantage, 0),
			#(assign, "$g_enemy_party", "p_collective_enemy"), 
			#(party_clear, "$g_enemy_party"), 
			(set_spawn_radius,0),
			(spawn_around_party,"$current_town", "pt_kingdom_hero_party"),
			(assign, ":party", reg0),

			(call_script, "script_party_count_fit_for_battle", "p_main_party"), 
			(assign, ":main_party_count",reg0), 
			(assign, ":reiters_count", ":main_party_count"), 
			(assign, ":mushket_count", ":main_party_count"), 
			(assign, ":pikeman_count", ":main_party_count"), 
			(assign, ":sword_masters_count", ":main_party_count"), 
			(assign, ":dragoons_count", ":main_party_count"), 
			(val_mul, ":reiters_count", 25),
			(val_div, ":reiters_count", 100),
			(val_mul, ":mushket_count", 45),
			(val_div, ":mushket_count", 100),
			(val_mul, ":pikeman_count", 35),
			(val_div, ":pikeman_count", 100),
			(val_mul, ":sword_masters_count", 15),
			(val_div, ":sword_masters_count", 100),
			(val_add, ":sword_masters_count", 5), 
			(val_mul, ":dragoons_count", 25),
			(val_div, ":dragoons_count", 100),
			(try_begin),
				(lt, ":mushket_count", 10), 
				(assign, ":mushket_count", 10),
			(try_end),
			(try_begin),
				(lt, ":reiters_count", 5), 
				(assign, ":reiters_count", 5),
			(try_end),
			(try_begin),
				(lt, ":sword_masters_count", 5), 
				(assign, ":sword_masters_count", 10),
			(try_end),
			(try_begin),
				(lt, ":dragoons_count", 10), 
				(assign, ":dragoons_count", 10),
			(try_end),
			(try_begin),
				(lt, ":pikeman_count", 10), 
				(assign, ":pikeman_count", 10),
			(try_end),
			(party_add_members, ":party", "trp_rhodok_sergeant", ":mushket_count"),
			(party_add_members, ":party", "trp_rhodok_veteran_crossbowman", ":reiters_count"),
			(party_add_members, ":party", "trp_rhodok_veteran_spearman", ":sword_masters_count"),
			(party_add_members, ":party", "trp_rhodok_veteran_crossbowman", ":dragoons_count"),
			(party_add_members, ":party", "trp_rhodok_trained_spearman", ":pikeman_count"),
			(party_quick_attach_to_current_battle, ":party", 1), 
			(assign, "$g_battle_result", 0),
			(set_jump_mission,"mt_lead_charge"),
			(jump_to_scene, ":scene_to_use"),
			(jump_to_menu, "mnu_oim_potop_kshetuskiy"),
			(assign, "$g_mt_mode", vba_after_training),
			(quest_set_slot, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 3),
			(change_screen_mission),
      ]),
		
      ]
  ), 


  
  
  ( "podkup_neg",mnf_disable_all_keys,"Just as your truce envoy entered the gates with a white flag, you heard a shot -- and then saw his body being hung on the wall.^^The morale of your troops has fallen.",
    "none",
    [
	(call_script, "script_cf_party_remove_random_regular_troop", "p_main_party"),
	(party_get_morale, ":morale_value", "p_main_party"),
	(val_sub,  ":morale_value", 1),
	(try_begin),
		(ge, ":morale_value", 0),
		(party_set_morale, "p_main_party", ":morale_value"),
	(try_end),],
    [
      ("Back_2",[],"Continue...",
       [(change_screen_return),
        ]),
    ]
  ),
  
   ( "podkup_ataka",mnf_disable_all_keys,"You managed to bribe one of the fortress defenders. He has opened the gates, and now you can unleash carnage on the town.",
     "none",
    [
		(set_background_mesh, "mesh_pic_siege_sighted"),   
	],
    [
      ("Cont",[],"Continue...",
       [
		(call_script, "script_get_max_skill_of_player_party", "skl_horse_archery"),
		(assign, ":flag", reg0),
		(try_begin),
			(ge, ":flag", 5),
			(set_jump_mission,"mt_shturm_podkup_horse"),
		(else_try),
			(set_jump_mission,"mt_shturm_podkup"),
		(try_end),
		(party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_center),
        (call_script, "script_calculate_battle_advantage"),
		(assign, ":battle_advantage", reg0),
        (val_mul, ":battle_advantage", 2),
        (val_div, ":battle_advantage", 3), #scale down the advantage a bit in sieges.
        (set_battle_advantage, ":battle_advantage"),
        (set_party_battle_mode),
        (assign, "$g_siege_battle_state", 1),
		(try_begin),
			(ge, ":flag", 5),
			(set_jump_mission,"mt_shturm_podkup_horse"),
		(else_try),
			(set_jump_mission,"mt_shturm_podkup"),
		(try_end),
        (assign, "$cant_talk_to_enemy", 0),           
        (assign, "$g_siege_final_menu", "mnu_castle_besiege"),
        (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
        (assign, "$g_siege_method", 0), #reset siege timer
		(call_script, "script_ms_before_attack", "$g_encountered_party", "p_main_party", "trp_player"),
		#(call_script, "script_replace_shturm_item_begin"),
        (jump_to_scene,":battle_scene"),
        (jump_to_menu, "mnu_battle_debrief"),
        (change_screen_mission),
        ]),
    ]),
  
   ("udral_otravil",mnf_disable_all_keys,"You managed to sneak into the city and poison the well.",
    "none",
    [(call_script, "script_remove_percent_of_each_kind_of_troops", 10, "$g_encountered_party"),],
    [
      ("Cont1",[],"Continue...",
       [
            (jump_to_menu, "mnu_castle_besiege"),
       ]),
    ]),
  
  ( "vzvesili",mnf_disable_all_keys,"Failure! You were discovered and captured!",
    "none",
    [ (troop_set_health,"trp_player",0),],
    [
      ("Cont2",[],"Continue...",
       [
		(str_store_string, s2, "str_oim_was_killed_while_in_town"),
		(jump_to_menu, "mnu_oim_last_game_menu"),
		(finish_mission),
		(music_set_situation, 0),
   ]
   ),
    ]
  ),
  
  (
    "udral_neotravil",mnf_disable_all_keys,"You were discovered, but you managed to flee.",
    "none", [],
    [
      ("Cont3",[],"Continue...",
       [
             (change_screen_return),
        ]),
    ]
  ),

  (
    "neudral_otravil",mnf_disable_all_keys,"You were discovered, but you managed to poison the water. Now you shall have to make your way through the lines of defenders.",
    "none",
    [ ],
    [
           
           
    ("Cont4",[],"Continue...",
       [
		(assign,"$all_doors_locked",1),
		(party_get_slot, ":sneak_scene", "$current_town",slot_town_center), # slot_town_gate),
		(modify_visitors_at_site,":sneak_scene"),(reset_visitors),
		(set_visitor,0,"trp_player"),
		(store_faction_of_party, ":town_faction","$current_town"),
		(faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
		(faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
		(try_begin),
			(gt, ":tier_2_troop", 0),
			(gt, ":tier_3_troop", 0),
			(assign,reg(0),":tier_3_troop"),
			(assign,reg(1),":tier_3_troop"),
			(assign,reg(2),":tier_2_troop"),
			(assign,reg(3),":tier_2_troop"),
		(else_try),
			(assign,reg(0),"trp_swadian_skirmisher"),
			(assign,reg(1),"trp_swadian_crossbowman"),
			(assign,reg(2),"trp_swadian_infantry"),
			(assign,reg(3),"trp_swadian_crossbowman"),
		(try_end),
		#(assign,reg(4),-1),
		#(shuffle_range,0,5),
		(set_visitors,1,reg(0), 2),
		(set_visitors,2,reg(1), 2),
		(set_visitors,3,reg(2), 3),
		(set_visitors,4,reg(3), 4),
		(set_jump_mission,"mt_sneak_caught_fight"),
		(jump_to_menu,"mnu_captivity_start_castle_defeat"),
		(set_passage_menu,"mnu_castle_besiege"),
		#(call_script, "script_replace_shturm_item_begin"),
		(jump_to_scene,":sneak_scene"),
		(call_script, "script_remove_percent_of_each_kind_of_troops", 10, "$g_encountered_party"),
		(change_screen_mission), 
		]),
	]
  ),
  
  (
    "neudral_neotravil",mnf_disable_all_keys,"You were discovered before you could poison the water. Now you will have to flee, making your way through the lines of defenders.",
    "none",
    [ ],
    [
           
           
      ("Cont4",[],"Continue...",
       [
            
			(assign,"$all_doors_locked",1),
           (party_get_slot, ":sneak_scene", "$current_town",slot_town_center), # slot_town_gate),
           (modify_visitors_at_site,":sneak_scene"),(reset_visitors),
           (set_visitor,0,"trp_player"),
           (store_faction_of_party, ":town_faction","$current_town"),
           (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
           (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           (try_begin),
             (gt, ":tier_2_troop", 0),
             (gt, ":tier_3_troop", 0),
             (assign,reg(0),":tier_3_troop"),
             (assign,reg(1),":tier_3_troop"),
             (assign,reg(2),":tier_2_troop"),
             (assign,reg(3),":tier_2_troop"),
           (else_try),
             (assign,reg(0),"trp_swadian_skirmisher"),
             (assign,reg(1),"trp_swadian_crossbowman"),
             (assign,reg(2),"trp_swadian_infantry"),
             (assign,reg(3),"trp_swadian_crossbowman"),
           (try_end),
           #(assign,reg(4),-1),
           #(shuffle_range,0,5),
			(set_visitors,1,reg(0), 1),
			(set_visitors,2,reg(1), 2),
			(set_visitors,3,reg(2), 2),
			(set_visitors,4,reg(3), 3),
           (set_jump_mission,"mt_sneak_caught_fight"),

           (set_passage_menu,"mnu_castle_besiege"),
		   #(call_script, "script_replace_shturm_item_begin"),
           (jump_to_scene,":sneak_scene"),
	   
           (change_screen_mission), 
			
        ]),
    ]
  ),
  
  ( "sneak_into_town_caught_dispersed_guards_t",mnf_disable_all_keys,"You managed to plow through the guard lines and escape the town.",
    "none",
    [],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$sneaked_into_town",1),
           (assign, "$town_entered", 1),
           (jump_to_menu,"mnu_castle_besiege"),
        ]),
    ]
  ),
  
  (
    "sneak_into_town_caught_ran_away_t",mnf_disable_all_keys,"You managed to hide in the maze of streets and escape the town.",
    "none",
    [],
    [
      ("continue",[],"Continue...",
       [
           (assign,"$auto_menu",-1),
           (assign, "$town_entered", 1),
           (jump_to_menu,"mnu_castle_besiege"),
        ]),
    ]
  ),
  
  (
    "vorvatsya_uspeh",mnf_disable_all_keys,"You managed to sneak into the city, but part of your army remains outside the walls. You shall need to defeat no less than {reg0}% of defenders before you can open the gates.",
    "none",
    [
		(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),				
		(store_sub, ":koef", 20, reg0),
		(val_mul, ":koef", 4),
		(assign, reg0, ":koef"),
		(set_background_mesh, "mesh_pic_siege_sighted"),   
	],
    [
	("continue",[],"Continue...",
    [
		(set_jump_mission,"mt_vtorhenie"),
		(call_script, "script_get_scene_for_shturm_podkup", "$g_encountered_party"),
		(assign, ":battle_scene", reg0),
		(call_script, "script_calculate_battle_advantage"),
        (assign, ":battle_advantage", reg0),
        #(val_mul, ":battle_advantage", 2),
        (val_div, ":battle_advantage", 2), #scale down the advantage a bit in sieges.
        (set_battle_advantage, ":battle_advantage"),
        (set_party_battle_mode),
        (assign, "$g_siege_battle_state", 1),
        (set_jump_mission,"mt_vtorhenie"),
        (assign, "$g_podkup", 0), 
        (assign, "$cant_talk_to_enemy", 0),           
        (assign, "$g_siege_final_menu", "mnu_castle_besiege"),
        (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
        (assign, "$g_siege_method", 0), #reset siege timer
		(call_script, "script_ms_before_attack", "$g_encountered_party", "p_main_party", "trp_player"),
		#(call_script, "script_replace_shturm_item_begin"),
        (jump_to_scene,":battle_scene"),
        (jump_to_menu, "mnu_battle_debrief"),
        (change_screen_mission),
    ]),
    ]
  ),
  
  ("vorvatsya_proval",mnf_disable_all_keys,"You failed to sneak into the city. Worse yet, your vanguard ({s50}) was slaughtered by the city defenders, and the morale of your main forces has fallen.",
    "none",
   [
	(try_begin),
	(call_script, "script_remove_percent_of_each_kind_of_troops", 15, "p_main_party"),
	(try_end),
	(set_background_mesh, "mesh_pic_siege_sighted"),   
   ],[
		("continue",[],"Continue...",
		[
			(party_get_morale, ":morale_value", "p_main_party"),
			(val_sub,  ":morale_value", 10),
			(try_begin),
				(ge, ":morale_value", 0),
				(party_set_morale, "p_main_party", ":morale_value"),
			(try_end),
			(jump_to_menu,"mnu_castle_besiege"),
		]),
    ]
  ),
  
  (
    "podkop_uspih",mnf_disable_all_keys,"You have counted that you shall need no less than {reg4} hours to plant the explosives.",
    "none",
    [
		(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
		(set_background_mesh, "mesh_pic_siege_sighted"),   
		(assign, ":max_skill", reg0),
		(store_sub, reg4, 10, ":max_skill"),
		(val_add, reg4, 5),
		(val_mul, reg4, 3),
		(val_div, reg4, 2),
    ],[
    
		("build_podkop_min",[],"Begin the work.", [
           (assign, "$g_siege_method", 2),
           (store_current_hours, ":cur_hours"),
	   (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
           (assign, ":max_skill", reg0),
	   (store_sub, ":hours_takes", 10, ":max_skill"),
	   (val_add, ":hours_takes", 5),
	   (val_mul, ":hours_takes", 3),
           (val_div, ":hours_takes", 2),
           (store_add, "$g_siege_method_finish_hours",":cur_hours", ":hours_takes"),
           (assign,"$auto_besiege_town","$current_town"),
           (rest_for_hours_interactive, ":hours_takes", 5, 1), #rest while attackable. A trigger will divert control when attack is ready.
           (change_screen_return),
           ]),
      ("go_back_dot",[],
       "Go back.", [(jump_to_menu,"mnu_castle_besiege")]),
        ],
  ),
  
  (
    "podkop_neg",mnf_disable_all_keys,"You failed to plant the explosives. Apparently, you overestimated your knowledge of such arts.",
    "none", [],
    [
      ("go_back_dot",[],
       "Go back.", 
   [
		(jump_to_menu,"mnu_castle_besiege"),
		(assign, "$g_diversiya_proval", 0),
		(assign, "$g_siege_method", 0),
    ]),
    ],
  ),
  
  (
    "podkop_uspih_walls",mnf_disable_all_keys,"The walls of this city are too strong to be broken by such means.",
    "none",  [],
    [
      ("go_back_dot",[],
       "Go back.", [
			(jump_to_menu,"mnu_castle_besiege"),
			(assign, "$g_diversiya_proval", 0),
			(assign, "$g_siege_method", 0),
		]),
    ],
  ),
  
  
  (
    "podkop_uspih_uspih",mnf_disable_all_keys,"The explosives detonated, destroying part of the wall...",
    "none",
    [
		(set_background_mesh, "mesh_pic_siege_sighted"),   
	],
    [
      ("go_next",[],"Begin the assault!", 
   [
		(set_jump_mission,"mt_castle_attack_walls_mina"),
		#(party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_center),
		(call_script, "script_oim_get_scene_walls_destroyed", "$g_encountered_party"),
		(assign, ":battle_scene", reg0),
		(call_script, "script_calculate_battle_advantage"),
		(assign, ":battle_advantage", reg0),
        (val_mul, ":battle_advantage", 2),
        (val_div, ":battle_advantage", 3), #scale down the advantage a bit in sieges.
        (set_battle_advantage, ":battle_advantage"),
        (set_party_battle_mode),
        (assign, "$g_siege_battle_state", 1),
		(set_jump_mission,"mt_castle_attack_walls_mina"),
		(assign, "$g_podkup", 0), 
        (assign, "$cant_talk_to_enemy", 0),           
        (assign, "$g_siege_final_menu", "mnu_castle_besiege"),
        (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
        (assign, "$g_siege_method", 0), #reset siege timer
		(call_script, "script_ms_before_attack", "$g_encountered_party", "p_main_party", "trp_player"),
		#(call_script, "script_replace_shturm_item_begin"),
        (jump_to_scene,":battle_scene"),
        (jump_to_menu, "mnu_battle_debrief"),
        (change_screen_mission),
		(unlock_achievement, ACHIEVEMENT_KNOCK_KNOCK),		
   ]),
    ],
  ),
  
   (
    "podkop_uspih_neg",mnf_disable_all_keys,"The walls of this city are too strong to be broken by such means.",
    "none",
    [
		(set_background_mesh, "mesh_pic_siege_sighted"),   
		(assign, "$g_siege_method", 0),		
		(assign, "$g_siege_method_finish_hours", 0),
	],
    [
      ("go_back_dot",[],
       "Go back.", [(jump_to_menu,"mnu_castle_besiege")]),
    ],
  ),


  (
    "oim_test_menus",mnf_disable_all_keys, "{!}NOT USED",
    "none", [], [],
  ),

  
  (
    "oim_last_game_menu",mnf_disable_all_keys,"{s2}",
    "none",
    [
		(set_background_mesh, "mesh_pic_pergament"),   
	],
    [
      ("continue",[],
       "Continue...", 
   [
		(start_presentation, "prsnt_game_credits"),
		#(jump_to_menu, "mnu_oim_last_game_menu2"),
        (change_screen_quit),
   ]),
    ],
  ),

  
##
## OiM Black Getman menu section
##
  ("oim_getman_defend_village",mnf_disable_all_keys,"You arrived in time! The bandits have not yet plundered the village. However, they noticed your arrival and are preparing to attack.",
   "none",
   [
		(set_background_mesh, "mesh_pic_steppe_bandits"),   
   ],
    [
     
 ("continue", [], "Continue...",
       [
			(party_get_slot, ":scene_to_use", "$g_encountered_party", slot_castle_exterior),
			(modify_visitors_at_site, ":scene_to_use"),
			(reset_visitors),
			#(assign, "$g_enemy_party", "p_collective_enemy"), 
			#(party_clear, "p_collective_enemy"), 
			#(assign, "$g_enemy_party", "p_collective_enemy"), 
			#(party_clear, "$g_enemy_party"), 
			(set_spawn_radius,0),
			(spawn_around_party,"$current_town", "pt_kingdom_hero_party"),
			(assign, ":party", reg0),
			
	        (assign, "$g_battle_result", 0),
            (assign, "$g_engaged_enemy", 1),
			
			#(assign, "$g_encountered_party", -1),
			#(assign, "$g_encountered_party_2", -1),
			
            #(call_script, "script_calculate_renown_value"),
            (call_script, "script_calculate_battle_advantage"),
            (set_battle_advantage, reg0),
            (set_party_battle_mode),
			#(assign, ":main_party_count",reg0), 
			#(assign, ":bandits_count", ":main_party_count"), 
			#(val_mul, ":bandits_count", 140), 
			#(val_div, ":bandits_count", 100), 
			#(try_begin),
			#	(lt, ":bandits_count", 14), 
			#	(assign, ":bandits_count", 14),
			#(try_end),
			(party_add_members, ":party", "trp_bandit", 12),
			(party_add_members, ":party", "trp_nord_veteran_levelup", 2),
			(party_add_members, ":party", "trp_lisovchiki_levelup", 3),
			(party_add_members, ":party", "trp_ttr_cherkes_levelup", 2),
			#(call_script, "script_clear_party_group", "$g_encountered_party"),
			(party_clear, "$g_encountered_party"),
			(party_quick_attach_to_current_battle, ":party", 1), 
			(quest_set_slot, "qst_oim_getman_defend_villages", slot_quest_target_party, ":party"),
			(assign, "$g_battle_result", 0),
			(set_jump_mission,"mt_lead_charge"),
			(jump_to_scene, ":scene_to_use"),
			(jump_to_menu, "mnu_oim_getman_defend_village_result"),
			(assign, "$g_mt_mode", vba_after_training),
			(change_screen_mission),
      ]),
	]  
  ), 

  ("oim_getman_defend_village_result",mnf_disable_all_keys,"{s2}",
   "none",
   [
    (try_begin),
		(eq, "$g_battle_result", -1),
		(str_store_string, s2, "@OiM You ve failed to protect the village"),
		(set_background_mesh, "mesh_pic_defeat"),   
		#(quest_get_slot, ":party", "qst_oim_getman_defend_villages", slot_quest_target_party),
		#(try_begin), 
		#	(neq, ":party", -1),
		#	(remove_party, ":party"),
		#	(quest_set_slot, "qst_oim_getman_defend_villages", slot_quest_target_party, -1),
		#(end_try),
    (else_try),
		#(try_begin), 
		#	(neq, ":party", -1),
		#	(call_script, "script_party_calculate_loot", ":party"),
		#	(gt, reg0, 0),
		#	(troop_sort_inventory, "trp_temp_troop"),
		#	(quest_set_slot, "qst_oim_getman_defend_villages", slot_quest_target_party, -1),
		#	(remove_party, ":party"),
		#	(change_screen_loot, "trp_temp_troop"),
		#(end_try),
		(str_store_string, s2, "@OiM You ve protected the village"),
		(set_background_mesh, "mesh_pic_victory"),   
    (end_try), 

   ],
    [
      ("continue", [(eq, "$g_battle_result", -1),], "Continue...",
       [
            (call_script, "script_village_set_state",  "$oim_getman_target_village", svs_looted),

        (party_add_particle_system, "$oim_getman_target_village", "psys_map_village_fire"), #new
        (party_add_particle_system, "$oim_getman_target_village", "psys_map_village_fire_smoke"), #new
        (party_set_icon, "$oim_getman_target_village", "icon_village_burnt_a"), #new
        (party_set_slot, "$oim_getman_target_village", slot_village_smoke_added, 1), #new
		
        (party_set_slot, "$oim_getman_target_village", slot_village_raid_progress, 100), #was 0
        (party_set_slot, "$oim_getman_target_village", slot_village_recover_progress, 0),

            (call_script, "script_change_player_relation_with_center", "$oim_getman_target_village", -25),
			(call_script, "script_fail_quest", "qst_oim_getman_defend_villages"),
			(call_script, "script_end_quest", "qst_oim_getman_defend_villages"), 
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]),
		
   ("continue", [(neq, "$g_battle_result", -1),], "Continue...",
       [
			(call_script, "script_refresh_village_defenders", "$g_encountered_party"),
			(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,"trp_oim_old_man_qst"),
			(jump_to_scene,"scn_meeting_scene_plain_forest"),
			(change_screen_map_conversation, "trp_oim_old_man_qst"),         
      ]),
	] 
  ),  
  
  ("oim_getman_defend_village_result2",mnf_disable_all_keys,"Before the old man could finish his speech, one of the wounded bandits took a shot. Alas, the bullet found its mark... The old man can tell you nothing more.",
   "none",
   [
		(set_background_mesh, "mesh_pic_wounded"),   
   ],
    [
      ("continue", [], "Continue...",
       [
			(call_script, "script_succeed_quest", "qst_oim_getman_defend_villages"), 
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]),
	] 
  ),  

  ("oim_getman_letter_text",mnf_disable_all_keys,"To the secret service clerk, to be delivered in person. ^^Acting on your orders, I discovered that the graves of the house of Oleg were stolen from Kiev by the Lithuanian Prince Janusz Radziwill. Word as it that he has taken them to his family burial vault. So far I know nothing more. One thing is certain, however -- Radziwill is a Protestant heretic, even ready to perform witchcraft if it will bring him closer to the crown. ^I send this message with a trusty spy, may God keep him safe, while I go to Riga where the archives of the Templars may hold the secret of the Black Mace...",
   "none",
   [
		(set_background_mesh, "mesh_pic_pergament"),   
   ],
    [
      ("continue", [], "Continue...",
       [
   	(quest_get_slot, ":talk_troop", "qst_oim_getman_capture_tatarin", slot_quest_target_troop), 
			(assign, "$oim_auto_talk_troop", ":talk_troop"), 
			#(jump_to_menu, "mnu_oim_getman_letter_text"),
			(finish_mission),
			(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,":talk_troop"),
			(jump_to_scene,"scn_meeting_scene_plain_forest"),
			(change_screen_map_conversation, ":talk_troop"),         
			(music_set_situation, 0),
        ]),
	] 
  ),  

  ("oim_getman_tamplier_archives", mnf_disable_all_keys,"{s2}",
   "none",
   [
	#code to set text...
	(try_begin), 
		(store_attribute_level, ":int", "trp_player", ca_intelligence),
		(ge, ":int", 1), 
		(str_store_string, s2, "@OIM_getman_heroe_can_read_book"), 
		(set_background_mesh, "mesh_pic_pergament"),   
	(else_try), 
		(str_store_string, s2, "@OIM_getman_heroe_need_help_to_read_book"), 
		(set_background_mesh, "mesh_pic_pergament"),   
	(end_try), 
	
   ],
   [
    ("continue", [], "Continue...",
     [
		#the hero is to stupid to read the documents
		(store_attribute_level, ":int", "trp_player", ca_intelligence),
		(try_begin), 
			(ge, ":int", 1), 
			#qst_oim_getman_nesviz_grobnica_radzivilov
			(quest_set_slot, "qst_oim_getman_nesviz_grobnica_radzivilov", slot_quest_giver_troop, "$g_talk_troop"), 
			(quest_set_slot, "qst_oim_getman_nesviz_grobnica_radzivilov", slot_quest_current_state, 0),
			(setup_quest_text, "qst_oim_getman_nesviz_grobnica_radzivilov"),
			(str_store_string, s2, "@OIM_add  pora nayti grobnicu radzivillow"),
			(call_script, "script_start_quest", "qst_oim_getman_nesviz_grobnica_radzivilov", "$g_talk_troop"),
			(add_xp_as_reward, 3000),
			#(call_script, "script_succeed_quest", "qst_oim_getman_tampliers_archives"),
			(call_script, "script_end_quest", "qst_oim_getman_tampliers_archives"),
		(end_try), 
		(jump_to_menu, "mnu_auto_return_to_map"),		
     ]), 
   ]),

   #oim_potop_fight_with_king_result
   ("oim_potop_fight_with_king_result",mnf_disable_all_keys,"{s3}",
   "none",
   [
    (try_begin),
		(this_or_next|eq,"$g_player_surrenders",1), 
		(eq, "$g_battle_result", -1),
		(str_store_string, s3, "@OiM You ve failed to win the king"),
		(set_background_mesh, "mesh_pic_defeat"),   
    (else_try),
		(str_store_string, s3, "@OiM You ve wing the king"),
		(set_background_mesh, "mesh_pic_victory"),   
    (end_try), 

   ],
    [
      ("continue", [
		(this_or_next|eq,"$g_player_surrenders",1), 
		(eq, "$g_battle_result", -1),], "Continue...",
       [
			#fail
			(str_store_string, s2, "str_oim_polish_defeated_hero_dead"),
			(jump_to_menu, "mnu_oim_last_game_menu"),
			(finish_mission),
			(music_set_situation, 0),
        ]),
		
   ("continue", [
		(neq, "$g_battle_result", -1),
		(neq, "$g_player_surrenders", 1),
	], "Continue...",
       [
			#victory
			(assign, "$g_oim_fight_with_king", 0),
			(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,"trp_npc1"),
			(jump_to_scene,"scn_meeting_scene_plain_forest"),
			(change_screen_map_conversation, "trp_npc1"),         
			#(jump_to_menu, "mnu_auto_return_to_map"),
			(call_script, "script_succeed_quest", "qst_oim_potop_execute_king"),
      ]),
	] 
  ), 

  #mnu_oim_cheats_and_solving_quests_menu
   #oim_potop_fight_with_king_result
   ("oim_cheats_and_solving_quests_menu",mnf_disable_all_keys,"Not used",
   "none",
  [ ],
    [
	
   ("money_menu", [],"cheat money",
        [
			(call_script, "script_troop_add_gold", "trp_player", 1500),
        ]),

   ("exp_menu", [],"cheat experience",
        [
			(add_xp_as_reward, 2000),
        ]),
		
		#change_troop_renown
   ("exp_renown", [],"cheat fame",
        [
			(call_script, "script_change_troop_renown", "trp_player", 250),
        ]),

   ("add_relation_to_all", [],"cheat reputation",
        [
			#(call_script, "script_change_troop_renown", "trp_player", 250),
			(call_script, "script_change_player_relation_with_faction", "fac_kingdom_1", 25),	
			(call_script, "script_change_player_relation_with_faction", "fac_kingdom_2", 25),	
			(call_script, "script_change_player_relation_with_faction", "fac_kingdom_3", 25),	
			(call_script, "script_change_player_relation_with_faction", "fac_kingdom_4", 25),	
			(call_script, "script_change_player_relation_with_faction", "fac_kingdom_5", 25),	
        ]),

      ("add_zagloba", [],"cheat add zagloba",
        [
			(call_script, "script_recruit_troop_as_companion", "trp_npc1"),
        ]),		

      ("fac_kingdom_4", [],"cheat minus swedes",
        [
			(call_script, "script_change_player_relation_with_faction", "fac_kingdom_4", -50),	
        ]),				
 	#nord_archer
       ("swedish_prisoner", [],"cheat prisoner",
        [
			#(call_script, "script_change_player_relation_with_faction", "fac_kingdom_4", -50),	
			(party_force_add_prisoners, "p_main_party", "trp_nord_archer", 1),
        ]),				
		
   ("exit_menu", [],"Return.",
        [
			#(call_script, "script_change_troop_renown", "trp_player", 250),
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]),
		
	] 
  ), 

	#oim_getman_reading_book
    ("oim_getman_reading_book",mnf_disable_all_keys,"{s3}",
	"none",
    [
		#code checking int of the hero
		(try_begin),
			(store_attribute_level, ":int", "trp_player", ca_intelligence),			
			(ge, ":int", 15),
			#qst_oim_getman_kozak_legend
			(quest_set_slot, "qst_oim_getman_kozak_legend", slot_quest_giver_troop, "trp_player"), 
			(quest_set_slot, "qst_oim_getman_kozak_legend", slot_quest_current_state, 0),
			(setup_quest_text, "qst_oim_getman_kozak_legend"),
			(str_store_string, s2, "@OIM_add_getman  Da zanyatnaya knizheca"),
			(call_script, "script_start_quest", "qst_oim_getman_kozak_legend", "trp_player"),
			(str_store_string, s3, "str_getman_voron_book_full_text"),
			(set_background_mesh, "mesh_pic_books"),   
		(else_try), 
			#qst_oim_getman_voron_translate
			(quest_set_slot, "qst_oim_getman_voron_translate", slot_quest_giver_troop, "trp_player"), 
			(quest_set_slot, "qst_oim_getman_voron_translate", slot_quest_current_state, 0),
			(setup_quest_text, "qst_oim_getman_voron_translate"),
			(str_store_string, s2, "@OIM_add_getman  Knigu bez tolmacha ne perevesti. Pora iskat kto smozhet eto sdelat"),
			(call_script, "script_start_quest", "qst_oim_getman_voron_translate", "trp_player"),
			(str_store_string, s3, "str_getman_voron_book_dont_understand"),
			(set_background_mesh, "mesh_pic_books"),   
		(end_try), 
	],
    [
      ("continue", [], "Continue...",
       [
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]),
	] 
  ),  

  #getman_book_translated  
    ("getman_book_translated",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(str_store_string, s3, "str_getman_voron_book_full_text"),
		(set_background_mesh, "mesh_pic_books"),   
	],
    [
      ("continue", [], "Continue...",
       [
			(call_script, "script_end_quest", "qst_oim_getman_voron_translate"),
			(quest_set_slot, "qst_oim_getman_kozak_legend", slot_quest_giver_troop, "trp_player"), 
			(quest_set_slot, "qst_oim_getman_kozak_legend", slot_quest_current_state, 0),
			(setup_quest_text, "qst_oim_getman_kozak_legend"),
			(str_store_string, s2, "@OIM_add_getman  Da zanyatnaya knizheca"),
			(call_script, "script_start_quest", "qst_oim_getman_kozak_legend", "trp_player"),
			(jump_to_menu, "mnu_auto_return_to_map"),
        ]),
	] 
  ),    
  
  #oim_dmitriy_yevangelik
    ("oim_dmitriy_yevangelik",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(try_begin),
			(quest_slot_eq, "qst_oim_dmitriy_gerasim", slot_quest_current_state, 2),
			(str_store_string, s3, "str_dmitriy_talk_to_gerasim"),
			(set_background_mesh, "mesh_pic_village_u"),   
		(else_try),
			(quest_slot_eq, "qst_oim_dmitriy_gerasim", slot_quest_current_state, 3),
			(str_store_string, s3, "str_dmitriy_prepare_to_fight"),
			(set_background_mesh, "mesh_pic_steppe_bandits"),   
		(else_try),
			(eq, "$g_battle_result", -1),
			(quest_slot_eq, "qst_oim_dmitriy_gerasim", slot_quest_current_state, 4),
			(str_store_string, s3, "str_dmitriy_lost_batle"),
			(set_background_mesh, "mesh_pic_looted_village"),   
			(quest_get_slot, ":party", "qst_oim_dmitriy_gerasim", slot_quest_target_party),
			#(remove_party
			(try_begin), 
				(neq, ":party", -1),
				(remove_party, ":party"),
				(quest_set_slot, "qst_oim_dmitriy_gerasim", slot_quest_target_party, -1),
			(end_try),
		(else_try),
			(neq, "$g_battle_result", -1),
			(quest_slot_eq, "qst_oim_dmitriy_gerasim", slot_quest_current_state, 4),
			(str_store_string, s3, "str_dmitriy_win_batle"),
			(set_background_mesh, "mesh_pic_village_u"),   
			(quest_get_slot, ":party", "qst_oim_dmitriy_gerasim", slot_quest_target_party),
			(try_begin), 
				(neq, ":party", -1),
				(call_script, "script_party_calculate_loot", ":party"),
				(gt, reg0, 0),
				(troop_sort_inventory, "trp_temp_troop"),
				(quest_set_slot, "qst_oim_dmitriy_gerasim", slot_quest_target_party, -1),
				(remove_party, ":party"),
				(change_screen_loot, "trp_temp_troop"),
			(end_try),
		(try_end), 
	],
    [
      ("continue", [
		(quest_slot_eq, "qst_oim_dmitriy_gerasim", slot_quest_current_state, 2),
       ], "Continue...",
       [
			(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,"trp_oim_dmitriy_yevangelik"),
			(jump_to_scene,"scn_meeting_scene_plain_forest"),
			(change_screen_map_conversation, "trp_oim_dmitriy_yevangelik"),         
        ]),
	
		#fight
      ("continue", [
		(quest_slot_eq, "qst_oim_dmitriy_gerasim", slot_quest_current_state, 3),
       ], "Continue...",
       [
		#fight code
			(quest_set_slot, "qst_oim_dmitriy_gerasim", slot_quest_current_state, 4),
			(party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
			(modify_visitors_at_site, ":scene_to_use"),
			(reset_visitors),
			(set_party_battle_mode),
			(set_battle_advantage, 0),
			#(assign, "$g_enemy_party", "p_collective_enemy"), 
			(set_spawn_radius,0),
			(spawn_around_party,"$current_town", "pt_kingdom_hero_party"),
			(assign, ":party", reg0),

			(party_clear, ":party"), 
			(call_script, "script_party_count_fit_for_battle", "p_main_party"), 
			(assign, ":main_party_count",reg0), 
			(assign, ":bandits_count", ":main_party_count"), 
			(val_mul, ":bandits_count", 130), 
			(val_div, ":bandits_count", 100), 
			(try_begin),
				(lt, ":bandits_count", 14), 
				(assign, ":bandits_count", 14),
			(try_end),
			(party_add_members, ":party", "trp_bandit", ":bandits_count"),
			#(call_script, "script_clear_party_group", "$g_encountered_party"),
			(party_clear, "$g_encountered_party"),
			(party_quick_attach_to_current_battle, ":party", 1), 
			(quest_set_slot, "qst_oim_dmitriy_gerasim", slot_quest_target_party, ":party"),
			(assign, "$g_battle_result", 0),
			(set_jump_mission,"mt_lead_charge"),
			(jump_to_scene, ":scene_to_use"),
			(jump_to_menu, "mnu_oim_dmitriy_yevangelik"),
			(assign, "$g_mt_mode", vba_after_training),
			(change_screen_mission),
        ]),


     ("continue", [
		(neq, "$g_battle_result", -1),
		(quest_slot_eq, "qst_oim_dmitriy_gerasim", slot_quest_current_state, 4),
     ], "Continue...",
       [
            (party_get_slot, ":village_elder_troop", "$current_town",slot_town_elder),
			(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,":village_elder_troop"),
			(jump_to_scene,"scn_meeting_scene_plain_forest"),
			(change_screen_map_conversation, ":village_elder_troop"),  
			(call_script, "script_refresh_village_defenders", "$g_encountered_party"),			
        ]),

     ("continue", [
    (eq, "$g_battle_result", -1),
		(quest_slot_eq, "qst_oim_dmitriy_gerasim", slot_quest_current_state, 4),
  ], "Continue...",
       [
			#code to fail quest qst_oim_dmitriy_gerasim
			(call_script, "script_fail_quest", "qst_oim_dmitriy_gerasim"),
			(call_script, "script_end_quest", "qst_oim_dmitriy_gerasim"),
			(jump_to_menu, "mnu_auto_return_to_map"),
			(call_script, "script_refresh_village_defenders", "$g_encountered_party"),
   ]),
	] 
  ),    

    ("oim_getman_fight_in_nesvizh",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(try_begin), 
			(quest_slot_eq, "qst_oim_getman_nesvizh_pernach", slot_quest_current_state, 1),
			(str_store_string, s3, "str_getman_voron_nesviz_village_enter"),
			(set_background_mesh, "mesh_pic_village_p"),   
		(else_try),
			(quest_slot_eq, "qst_oim_getman_nesvizh_pernach", slot_quest_current_state, 2),
			(neq, "$g_battle_result", -1),
			(str_store_string, s3, "str_getman_nesviz_victory"),
			(set_background_mesh, "mesh_pic_victory"),   
		(else_try),
			(quest_slot_eq, "qst_oim_getman_nesvizh_pernach", slot_quest_current_state, 2),
			(eq, "$g_battle_result", -1),
			(str_store_string, s3, "str_oim_generik_death_qst"),
			(set_background_mesh, "mesh_pic_defeat"),   
		(end_try),
	], [

	("continue", [(quest_slot_eq, "qst_oim_getman_nesvizh_pernach", slot_quest_current_state, 1),], "Continue...",
       [
			#code to start usual fight
			(quest_set_slot, "qst_oim_getman_nesvizh_pernach", slot_quest_current_state, 2),
			(party_get_slot, ":scene_to_use", "p_village_53", slot_castle_exterior),
			(modify_visitors_at_site, ":scene_to_use"),
			(reset_visitors),
			(set_party_battle_mode),
			(set_battle_advantage, 0),
			(party_clear, "$g_enemy_party"), 
			(call_script, "script_oim_spawn_strong_army", "$g_enemy_party", "fac_kingdom_1"),
			(assign, "$g_enemy_party", reg0), 
			(party_quick_attach_to_current_battle, "$g_enemy_party", 1), 
			(assign, "$g_battle_result", 0),
			(set_jump_mission,"mt_lead_charge"),
			(jump_to_scene, ":scene_to_use"),
			(jump_to_menu, "mnu_oim_getman_fight_in_nesvizh"),
			(assign, "$g_mt_mode", vba_after_training),
			(change_screen_mission),
		]),
		
    ("continue", [
		(quest_slot_eq, "qst_oim_getman_nesvizh_pernach", slot_quest_current_state, 2),
		(eq, "$g_battle_result", -1),
	], "Continue...",
       [
			#code if battle lost
			(start_presentation, "prsnt_game_credits"),
			#(jump_to_menu, "mnu_oim_last_game_menu2"),
			(change_screen_quit),
        ]),
		
	("continue", [
		(quest_slot_eq, "qst_oim_getman_nesvizh_pernach", slot_quest_current_state, 2),
		(neq, "$g_battle_result", -1),
	], "Continue...",
       [
			#code battle win
			(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,"trp_swadian_man_at_arms"),
			(jump_to_scene,"scn_meeting_scene_plain_forest"),
			(change_screen_map_conversation, "trp_swadian_man_at_arms"),         
		]),
	]),  

	#oim_getman_sneack_in
    ("oim_getman_sneack_in",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(try_begin), 
			(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 0),
			(str_store_string, s3, "str_getman_radzivil_gurds"),		
		(else_try), 
			(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 1),
			(str_store_string, s3, "str_getman_radzivil_before_fght"),
		(else_try), 
			(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 2),
			(eq, "$g_battle_result", -1),
			(str_store_string, s3, "str_oim_generik_death_qst"),
		(else_try), 
			(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 2),
			(neq, "$g_battle_result", -1),
			(str_store_string, s3, "str_getman_radzivil_killled"),
		(else_try), 
			(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 3),
			(eq, "$g_battle_result", -1),
			(str_store_string, s3, "str_oim_generik_death_qst"),
		(else_try), 
			(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 3),
			(neq, "$g_battle_result", -1),
			(str_store_string, s3, "str_getman_radzivil_mamay"),
		(end_try),
	], [
	
	("continue", [(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 0),], "Continue...",
       [

			(party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
			(modify_visitors_at_site,":castle_scene"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,"trp_swadian_crossbowman"),
			(jump_to_scene,":castle_scene"),
			(change_screen_map_conversation, "trp_swadian_crossbowman"),         
		]),
	
    ("continue", [
		(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 1),
		#(eq, "$g_battle_result", -1),
	], "Continue...",
       [
			(assign, "$g_next_menu", "mnu_oim_getman_sneack_in"),
			(assign, "$talk_context", tc_court_talk),
			(party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
			(modify_visitors_at_site,":castle_scene"),
			(reset_visitors),
			#visitors
			(set_visitor, 6, "trp_nord_champion"),
			(set_visitor, 7, "trp_nord_champion"),
			(set_visitor, 16, "trp_kingdom_1_pretender"),
			(set_visitor, 17, "trp_nord_champion"),
			(set_visitor, 18, "trp_nord_champion"),
			(set_visitor, 19, "trp_nord_champion"),
			(set_visitor, 20, "trp_nord_champion"),
			(set_jump_mission,"mt_oim_simle_fight_interior"),
			(jump_to_scene,":castle_scene"),
			(scene_set_slot, ":castle_scene", slot_scene_visited, 1),
			(change_screen_mission),
    ]),

    ("continue", [
		(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 2),
		(eq, "$g_battle_result", -1),
	], "Continue...",
       [
			(start_presentation, "prsnt_game_credits"),
			(change_screen_quit),
        ]),

		
	("continue", [
		(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 2),
		(neq, "$g_battle_result", -1),
	], "Continue...",
       [
            (assign,"$all_doors_locked",1),
			(assign, "$g_next_menu", "mnu_oim_getman_sneack_in"),
			(quest_set_slot, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 3),
			(try_begin), 
				(party_slot_eq,"$g_encountered_party", slot_party_type,spt_castle),
				(assign, "$g_battle_result", 1),
				(jump_to_menu, "mnu_oim_getman_sneack_in"), 
			(else_try), 	
				(party_get_slot, ":sneak_scene", "$current_town",slot_town_center), # slot_town_gate),
				(modify_visitors_at_site,":sneak_scene"),
				(reset_visitors),
				(set_visitor,0,"trp_player"),
				(assign,reg(0),"trp_swadian_skirmisher"),
				(assign,reg(1),"trp_swadian_crossbowman"),
				(assign,reg(2),"trp_swadian_infantry"),
				(assign,reg(3),"trp_swadian_crossbowman"),
				(assign,reg(4),"trp_swadian_crossbowman"),
				(shuffle_range,0,5),
				(set_visitors,1, reg(0), 2),
				(set_visitors,2, reg(1), 1),
				(set_visitors,3, reg(2), 3),
				(set_visitors,4, reg(3), 2),
				(set_jump_mission,"mt_sneak_oim_after_radz"),
				(jump_to_scene,":sneak_scene"),
				(change_screen_mission),   
			(end_try),
		]),

    ("continue", [
		(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 3),
		(eq, "$g_battle_result", -1),
	], "Continue...",
       [
			(start_presentation, "prsnt_game_credits"),
			(change_screen_quit),
        ]),

	("continue", [
		(quest_slot_eq, "qst_oim_getman_kill_radzivill", slot_quest_current_state, 3),
		(neq, "$g_battle_result", -1),
	], "Continue...",
       [
			(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,"trp_npc4"),
			(jump_to_scene,"scn_meeting_scene_plain_forest"),
			(change_screen_map_conversation, "trp_npc4"),         
		]),
	]),  


	#oim_getman_quest_failed
    ("oim_getman_quest_failed",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(str_store_string, s3, "str_getman_radzivil_is_the_king"),
		(set_background_mesh, "mesh_pic_defeat"),   
	],
     [
      ("continue", [], "Continue...",
       [
			(call_script, "script_fail_quest", "qst_oim_getman_main"),   
			(call_script, "script_end_quest", "qst_oim_getman_main"),
			(call_script, "script_fail_quest", "qst_oim_getman_nesvizh_pernach"),   
			(call_script, "script_end_quest", "qst_oim_getman_nesvizh_pernach"),
			(try_begin), 
				(call_script, "script_fail_quest", "qst_oim_getman_kill_radzivill"),   
				(call_script, "script_end_quest", "qst_oim_getman_kill_radzivill"),
			(try_end),	
			(start_presentation, "prsnt_game_credits"),
			(change_screen_quit),
		]),
 ] 
    ),  
	
	#oim_getman_hmel_order		
    ("oim_getman_hmel_order",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(str_store_string, s3, "str_getman_hmel_rebelion"),
		(set_background_mesh, "mesh_pic_pergament"),   
	],
     [
      ("continue", [], "Continue...",
       [
		#code
			(quest_set_slot, "qst_oim_na_rech_pospolitu", slot_quest_giver_troop, "trp_player"), 
			(quest_set_slot, "qst_oim_na_rech_pospolitu", slot_quest_current_state, 0),
			(setup_quest_text, "qst_oim_na_rech_pospolitu"),
			(str_store_string, s2, "@OIM_add_getman  Prikaz Hmelya - zavoevat RP"),
			(call_script, "script_start_quest", "qst_oim_na_rech_pospolitu", "trp_player"),
			(call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_5", "fac_kingdom_1", 1),
			(jump_to_menu, "mnu_auto_return_to_map"),
		]),
	] 
    ),  
	
	#oim_getman_hmel_rebelion	
    ("oim_getman_hmel_rebelion",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(str_store_string, s3, "str_oim_smesh_down_rebelion"),
		(set_background_mesh, "mesh_pic_pergament"),   
	],
     [
      ("continue", [], "Continue...",
       [
		#code
			#qst_oim_getman_hmel_reb
			(call_script, "script_end_quest", "qst_oim_na_rech_pospolitu"), 
			(quest_set_slot, "qst_oim_getman_hmel_reb", slot_quest_giver_troop, "trp_kingdom_5_lord"), 
			(quest_set_slot, "qst_oim_getman_hmel_reb", slot_quest_current_state, 0),
			(setup_quest_text, "qst_oim_getman_hmel_reb"),
			(str_store_string, s2, "str_oim_smesh_down_rebelion"),
			(call_script, "script_start_quest", "qst_oim_getman_hmel_reb", "trp_kingdom_5_lord"),
			#script of rebelion
			(try_begin), 
				(party_count_prisoners_of_type, ":rslt", "p_main_party", "trp_kingdom_1_lord"), 
				(gt, ":rslt", 0), 
				(call_script, "script_remove_troop_from_prison", "trp_kingdom_1_lord"),
				(party_remove_prisoners, "p_main_party", "trp_kingdom_1_lord", 1),
			(end_try), 
			(call_script, "script_change_troop_faction", "trp_kingdom_1_lord", "fac_kingdom_1"), 
			(faction_set_slot, "fac_kingdom_1", slot_faction_leader, "trp_kingdom_1_lord"),
			(faction_set_slot, "fac_kingdom_1", slot_faction_state, sfs_active),
			(str_store_faction_name, s1, "fac_kingdom_1"),
			(faction_set_name, "fac_kingdom_1", "@{s1} Rebels"),
			(set_relation, "fac_kingdom_5", "fac_kingdom_1", -100), 
			(call_script, "script_give_center_to_lord", "p_town_6", "trp_kingdom_1_lord", 0),
			(call_script, "script_give_center_to_faction", "p_town_6", "fac_kingdom_1"),  
			(call_script, "script_remove_lords_from_center", "p_town_6"), 
			#lords-rebels
			(try_for_range, ":unused", 0, 6), 
				(call_script, "script_cf_get_random_lord_except_king_with_faction", "fac_kingdom_5"), 
				(assign, ":target_troop", reg0), 
				(call_script, "script_change_troop_faction", ":target_troop", "fac_kingdom_1"), 
			(end_try), 
			(assign, "$g_recalculate_ais", 1),
			(call_script, "script_update_all_notes"),
			(jump_to_menu, "mnu_auto_return_to_map"),
		]),
 ] 
    ),  
	
	#oim_getman_casus_beli_hmel
	("oim_getman_casus_beli_hmel",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(str_store_string, s3, "str_getman_hmel_rebelion_end"),
		(set_background_mesh, "mesh_pic_pergament"),   
	],
     [
      ("continue", [], "Continue...",
       [
		#qst_oim_getman_hmel_casus_beli
		(call_script, "script_end_quest", "qst_oim_getman_hmel_reb"), 
		(quest_set_slot, "qst_oim_getman_hmel_casus_beli", slot_quest_giver_troop, "trp_kingdom_5_lord"), 
		(quest_set_slot, "qst_oim_getman_hmel_casus_beli", slot_quest_current_state, 0),
		(setup_quest_text, "qst_oim_getman_hmel_casus_beli"),
		(str_store_string, s2, "@OIM_add_getman  Nuzhno vstretitsya s getmanom - obgovorit politiku..."),
		(call_script, "script_start_quest", "qst_oim_getman_hmel_casus_beli", "trp_kingdom_5_lord"),
		(jump_to_menu, "mnu_auto_return_to_map"),
		]),
 ] 
    ),  

	#oim_getman_casus_beli_hmel_war
	("oim_getman_casus_beli_hmel_war",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(try_begin),
			(quest_slot_eq, "qst_oim_getman_hmel_greate_war", slot_quest_current_state, 2),
			(str_store_string, s3, "str_casus_beli_hmel_war_message_delivered"),
			(set_background_mesh, "mesh_pic_pergament"),   
		(else_try),
			(quest_slot_eq, "qst_oim_getman_hmel_greate_war", slot_quest_current_state, 1),
			(str_store_string, s3, "str_casus_beli_hmel_war_message_intercepted"),
			(set_background_mesh, "mesh_pic_pergament"),   
		(end_try), 
	],
     [
      ("continue", [], "Continue...",
       [
			(quest_set_slot, "qst_oim_getman_hmel_greate_war", slot_quest_current_state, 3),
			#code for rebelion
			(call_script, "script_count_lords_of_faction", "fac_kingdom_5"), 
			(assign, ":count", reg0), 
			(val_mul, ":count", 100), 
			(val_div, ":count", 60), 
			(try_for_range, ":unused", 0, ":count"), 
				(call_script, "script_cf_get_random_lord_except_king_with_faction", "fac_kingdom_5"), 
				(assign, ":target_troop", reg0), 
				(call_script, "script_change_troop_faction", ":target_troop", "fac_kingdom_2"), 
			(try_end), 
			(call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_5", "fac_kingdom_2", 1),
			(jump_to_menu, "mnu_auto_return_to_map"),
			(assign, "$g_recalculate_ais", 1),
		]),
 ] 
    ), 
	
	#oim_korono_vitovta
	("oim_korono_vitovta",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(try_begin),
			(quest_slot_eq, "qst_oim_getman_korona_vitovta", slot_quest_current_state, 4),
			(str_store_string, s3, "str_korona_vitovta_target_city"),
			(set_background_mesh, "mesh_pic_pergament"),   
		(else_try),
			(quest_slot_eq, "qst_oim_getman_korona_vitovta", slot_quest_current_state, 5),
			(eq, "$g_battle_result", -1), 
			(str_store_string, s3, "str_korona_vitovta_target_city_killed"),
			(set_background_mesh, "mesh_pic_pergament"),   
		(else_try),
			(str_store_string, s3, "str_korona_vitovta_target_city_win"),
			(set_background_mesh, "mesh_pic_pergament"),   
		(end_try), 
	],
     [
      ("continue", [(quest_slot_eq, "qst_oim_getman_korona_vitovta", slot_quest_current_state, 4),], "Continue...",
       [
			(quest_set_slot, "qst_oim_getman_korona_vitovta", slot_quest_current_state, 5),
			(assign, "$g_next_menu", "mnu_oim_korono_vitovta"),
			#(assign, "$talk_context", tc_court_talk),
			(assign, ":curr_scene", "scn_oim_vitavt_dangeon"),
            (modify_visitors_at_site, ":curr_scene"),
			(reset_visitors),
			#visitors
			(set_visitor, 0, "trp_player"),
			(set_visitor, 4, "trp_swadian_sharpshooter"),
			(set_visitor, 5, "trp_nord_champion"),
			(set_visitor, 6, "trp_halberdier"),
			(set_visitor, 7, "trp_swadian_sharpshooter"),
			(set_visitor, 8, "trp_nord_champion"),
			(set_visitor, 9, "trp_swadian_sharpshooter"),
			(set_visitor, 10, "trp_swadian_sharpshooter"),
			(set_visitor, 11, "trp_swadian_sharpshooter"),
			(set_visitor, 12, "trp_halberdier"),
			(set_visitor, 13, "trp_halberdier"),
			(set_visitor, 14, "trp_halberdier"),
			(set_visitor, 15, "trp_halberdier"),
			(set_jump_mission,"mt_oim_dungeon_mission"),
			(jump_to_scene,":curr_scene"),
			(scene_set_slot, ":curr_scene", slot_scene_visited, 1),
			(change_screen_mission),
		]),
		
      ("continue", [
			(quest_slot_eq, "qst_oim_getman_korona_vitovta", slot_quest_current_state, 5),
			(eq, "$g_battle_result", -1), 
   ], "Continue...",
       [
			(str_store_string, s2, "str_oim_generik_death_qst"),
			(jump_to_menu, "mnu_oim_last_game_menu"),
		]),
		
      ("continue", [
			(quest_slot_eq, "qst_oim_getman_korona_vitovta", slot_quest_current_state, 5),
			(neq, "$g_battle_result", -1), 
   ], "Continue...",
       [
			(call_script, "script_succeed_quest", "qst_oim_getman_korona_vitovta"), 
			(jump_to_menu, "mnu_auto_return_to_map"),
		]),
		
 ] 
    ), 
	
	#oim_dmitriy_captured
	("oim_dmitriy_captured",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(try_begin),
			(quest_slot_eq, "qst_oim_dmitriy_tsar_prison", slot_quest_current_state, 0),
			(str_store_string, s3, "str_pobeg_iz_turmi_init"),
			(set_background_mesh, "mesh_pic_escape_1"),   
		(else_try),
			(quest_slot_eq, "qst_oim_dmitriy_tsar_prison", slot_quest_current_state, 1),
			(eq, "$g_battle_result", -1), 
			(str_store_string, s3, "str_pobeg_iz_turmi_init_killed"),
			(set_background_mesh, "mesh_pic_defeat"),   
		(else_try),
			(str_store_string, s3, "str_pobeg_iz_turmi_init_succeeded"),
			(set_background_mesh, "mesh_pic_escape_1"),   
		(end_try), 
	],
     [
      ("continue", [(quest_slot_eq, "qst_oim_dmitriy_tsar_prison", slot_quest_current_state, 0),], "Continue...",
       [
			(quest_set_slot, "qst_oim_dmitriy_tsar_prison", slot_quest_current_state, 1),
			(assign, "$g_next_menu", "mnu_oim_dmitriy_captured"),
			#(assign, "$talk_context", tc_court_talk),
			(assign, ":curr_scene", "scn_oim_moscow_dangeon"),
            (modify_visitors_at_site, ":curr_scene"),
			(reset_visitors),
			#visitors
			#trp_moskov_straj
			#trp_vaegir_marksman
			(set_visitor, 0, "trp_player"),
			(set_visitor, 4, "trp_vaegir_marksman"),
			(set_visitor, 5, "trp_moskov_straj"),
			(set_visitor, 6, "trp_moskov_straj"),
			(set_visitor, 7, "trp_vaegir_marksman"),
			(set_visitor, 8, "trp_moskov_straj"),
			(set_visitor, 9, "trp_vaegir_marksman"),
			(set_visitor, 10, "trp_vaegir_marksman"),
			(set_visitor, 11, "trp_vaegir_marksman"),
			(set_visitor, 12, "trp_moskov_straj"),
			(set_visitor, 13, "trp_vaegir_marksman"),
			(set_visitor, 14, "trp_vaegir_marksman"),
			(set_visitor, 15, "trp_vaegir_marksman"),
			(set_visitor, 16, "trp_moskov_straj"),
			(set_jump_mission,"mt_oim_dungeon_mission_msk"),
            #(entry_point_get_position,pos1,1),
            #(set_spawn_position, pos1),
            #(spawn_item, "itm_pistol_b"),
			#(spawn_item, "itm_cartridges"),
			(jump_to_scene,":curr_scene"),
			(scene_set_slot, ":curr_scene", slot_scene_visited, 1),
			(change_screen_mission),
		]),
		
      ("continue", [
			(quest_slot_eq, "qst_oim_dmitriy_tsar_prison", slot_quest_current_state, 1),
			(eq, "$g_battle_result", -1), 
   ], "Continue...",
       [
			(start_presentation, "prsnt_game_credits"),
			(change_screen_quit),
		]),
		
      ("continue", [
			(quest_slot_eq, "qst_oim_dmitriy_tsar_prison", slot_quest_current_state, 1),
			(neq, "$g_battle_result", -1), 
   ], "Continue...",
       [
			(troop_add_item, "trp_player", "itm_streletzkiy_mundir"),
			(call_script, "script_succeed_quest", "qst_oim_dmitriy_tsar_prison"), 
			(str_store_string, s5, "@OiM_dmitriy Teper kogda vibralsya iz turmi i vse kto videl samozvanca mertvi krome carya nuzhno sprosit kogo libo chto tovoricco..."),	
			(add_quest_note_from_sreg, "qst_oim_dmitriy_tsar_prison", 4, s5, 1),
			(jump_to_menu, "mnu_auto_return_to_map"),
		]),
		
 ] 
    ), 

	
	#oim_edit_scenes_in_this_town
	("oim_edit_scenes_in_this_town",mnf_disable_all_keys,"{!}Edit scenes",
	"none",
    [],
     [
    ("edit_slot_town_center",[],"{!}edit slot town center",
    [
	    (assign, "$talk_context", 0),
            (party_get_slot, ":town_scene", "$g_encountered_party", slot_town_center),
			#(assign, ":town_scene", "scn_oim_moscow_dangeon"),
            (modify_visitors_at_site, ":town_scene"),
            (reset_visitors),
            (assign, "$g_mt_mode", tcm_default),
            (set_jump_mission,"mt_town_center"),
			(set_visitor, "trp_player", 0),
            (jump_to_scene, ":town_scene"),
            (change_screen_mission),
        ],"{!}edit_slot_town_center"),

    ("edit_slot_town_castle",[],"{!}edit slot town castle",
    [
	    (assign, "$talk_context", 0),
            (party_get_slot, ":town_scene", "$g_encountered_party", slot_town_castle),
			#(assign, ":town_scene", "scn_oim_moscow_dangeon"),
            (modify_visitors_at_site, ":town_scene"),
            (reset_visitors),
            (assign, "$g_mt_mode", tcm_default),
            (set_jump_mission,"mt_town_center"),
			(set_visitor, "trp_player", 0),
            (jump_to_scene, ":town_scene"),
            (change_screen_mission),
        ],"{!}edit_slot_town_castle"),

    ("edit_slot_town_prison",[],"{!}edit slot town prison",
    [
	    (assign, "$talk_context", 0),
            (party_get_slot, ":town_scene", "$g_encountered_party", slot_town_prison),
			#(assign, ":town_scene", "scn_oim_moscow_dangeon"),
            (modify_visitors_at_site, ":town_scene"),
            (reset_visitors),
            (assign, "$g_mt_mode", tcm_default),
            (set_jump_mission,"mt_town_center"),
			(set_visitor, "trp_player", 0),
            (jump_to_scene, ":town_scene"),
            (change_screen_mission),
        ],"{!}edit_slot_town_prison"),		
		
    ("edit_slot_town_tavern",[],"{!}edit slot town tavern",
    [
	    (assign, "$talk_context", 0),
            (party_get_slot, ":town_scene", "$g_encountered_party", slot_town_tavern),
			#(assign, ":town_scene", "scn_oim_moscow_dangeon"),
            (modify_visitors_at_site, ":town_scene"),
            (reset_visitors),
            (assign, "$g_mt_mode", tcm_default),
            (set_jump_mission,"mt_town_center"),
			(set_visitor, "trp_player", 0),
            (jump_to_scene, ":town_scene"),
            (change_screen_mission),
        ],"{!}edit_slot_town_tavern"),		

    ("edit_slot_town_store",[],"{!}edit slot town store",
    [
	    (assign, "$talk_context", 0),
            (party_get_slot, ":town_scene", "$g_encountered_party", slot_town_store),
			#(assign, ":town_scene", "scn_oim_moscow_dangeon"),
            (modify_visitors_at_site, ":town_scene"),
            (reset_visitors),
            (assign, "$g_mt_mode", tcm_default),
            (set_jump_mission,"mt_town_center"),
			(set_visitor, "trp_player", 0),
            (jump_to_scene, ":town_scene"),
            (change_screen_mission),
        ],"{!}edit_slot_town_store"),		
		
    ("edit_slot_town_arena",[],"{!}edit slot town arena",
    [
	    (assign, "$talk_context", 0),
            (party_get_slot, ":town_scene", "$g_encountered_party", slot_town_arena),
			#(assign, ":town_scene", "scn_oim_moscow_dangeon"),
            (modify_visitors_at_site, ":town_scene"),
            (reset_visitors),
            (assign, "$g_mt_mode", tcm_default),
            (set_jump_mission,"mt_town_center"),
			(set_visitor, "trp_player", 0),
            (jump_to_scene, ":town_scene"),
            (change_screen_mission),
        ],"{!}edit_slot_town_arena"),			

    ("edit_slot_town_alley",[],"{!}edit slot town alley",
    [
	    (assign, "$talk_context", 0),
            (party_get_slot, ":town_scene", "$g_encountered_party", slot_town_alley),
			#(assign, ":town_scene", "scn_oim_moscow_dangeon"),
            (modify_visitors_at_site, ":town_scene"),
            (reset_visitors),
            (assign, "$g_mt_mode", tcm_default),
            (set_jump_mission,"mt_town_center"),
			(set_visitor, "trp_player", 0),
            (jump_to_scene, ":town_scene"),
            (change_screen_mission),
        ],"{!}edit_slot_town_alley"),	

    ("edit_slot_town_walls",[],"{!}edit slot town walls ",
    [
	    (assign, "$talk_context", 0),
            (party_get_slot, ":town_scene", "$g_encountered_party", slot_town_walls),
			#(assign, ":town_scene", "scn_oim_moscow_dangeon"),
            (modify_visitors_at_site, ":town_scene"),
            (reset_visitors),
            (assign, "$g_mt_mode", tcm_default),
            (set_jump_mission,"mt_town_center"),
			(set_visitor, "trp_player", 0),
            (jump_to_scene, ":town_scene"),
            (change_screen_mission),
        ],"{!}edit_slot_town_walls"),	

    ("edit_slot_town_walls_destroyed",[],"{!}edit slot town walls destroyed",
    [
	    (assign, "$talk_context", 0),
            #(party_get_slot, ":town_scene", "$g_encountered_party", slot_town_alley),
			(call_script, "script_oim_get_scene_walls_destroyed", "$g_encountered_party"), 
			(assign, ":town_scene", reg0),
            (modify_visitors_at_site, ":town_scene"),
            (reset_visitors),
            (assign, "$g_mt_mode", tcm_default),
            (set_jump_mission,"mt_town_center"),
			(set_visitor, "trp_player", 0),
            (jump_to_scene, ":town_scene"),
            (change_screen_mission),
        ],"edit slot town walls destroyed"),	

    ("exit_this_menu",[],"{!}exit this menu",
    [
			(jump_to_menu, "mnu_auto_return_to_map"),
        ],"{!}exit_this_menu"),	
	] 
    ), 


	("oim_dmitriy_alevtina_hanum",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(try_begin),
			(this_or_next|quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_current_state, 2),
			(quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_current_state, 1),
			(str_store_string, s3, "str_alevtina_hanum_init"),
			(set_background_mesh, "mesh_pic_village_s"),   
		(else_try),
			(quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_current_state, 3),
			(eq, "$g_battle_result", -1), 
			(str_store_string, s3, "str_alevtina_hanum_killed"),
			(set_background_mesh, "mesh_pic_defeat"),   
		(else_try),
			(str_store_string, s3, "str_alevtina_hanum_succeeded"),
			(set_background_mesh, "mesh_pic_village_s"),   
		(end_try), 
	],
     [
      
	  ("oim_walk_the_streets", [
			(this_or_next|quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_current_state, 2),
			(quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_current_state, 1),	  
		],"Leave the harem and go to the city.",
       [
			(assign, "$sneaked_into_town",1),
			(jump_to_menu,"mnu_town"),
		]),
	  
	  
	  ("continue", [
			(this_or_next|quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_current_state, 2),
			(quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_current_state, 1),	  
		], "Continue...",
       [
			(quest_set_slot, "qst_oim_alevtina_hanum", slot_quest_current_state, 3),
			(assign, "$g_next_menu", "mnu_oim_dmitriy_alevtina_hanum"),
			(assign, "$talk_context", tc_court_talk),
			(assign, ":curr_scene", "scn_oim_garem_scene"),
            (modify_visitors_at_site, ":curr_scene"),
			(reset_visitors),
			#visitors
			#trp_moskov_straj
			#trp_vaegir_marksman
			(set_visitor, 0, "trp_player"),
			(set_visitor, 6, "trp_khergit_veteran_horse_archer"),
			(set_visitor, 7, "trp_khergit_veteran_horse_archer"),
			(set_visitor, 22, "trp_khergit_lancer"),
			(set_visitor, 27, "trp_saymen"),
			(set_jump_mission,"mt_oim_simle_fight_interior_alevtina"),
			(jump_to_scene,":curr_scene"),
			(scene_set_slot, ":curr_scene", slot_scene_visited, 1),
			(change_screen_mission),
		]),
		
      ("continue", [
			(quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_current_state, 3),
	 		(eq, "$g_battle_result", -1), 
    ], "Continue...",
       [
			(start_presentation, "prsnt_game_credits"),
			(change_screen_quit),
		]),
		
      ("continue", [
			(quest_slot_eq, "qst_oim_alevtina_hanum", slot_quest_current_state, 3),
			(neq, "$g_battle_result", -1), 
    ], "Continue...",
       [
			(modify_visitors_at_site,"scn_meeting_scene_plain_forest"),
			(reset_visitors),
			(set_visitor,0,"trp_player"),
			(set_visitor,17,"trp_alevtina"),
			(jump_to_scene,"scn_meeting_scene_plain_forest"),
			(change_screen_map_conversation, "trp_alevtina"),         
		]),
		
    ] 
    ), 

	## OiM barabash code
	#oim_barabash_order_mc
    ("oim_barabash_order_mc",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(str_store_string, s3, "str_getman_barabash_rebelion"),
		(set_background_mesh, "mesh_pic_pergament"),   
	],
     [
      ("continue", [], "Continue...",
       [
			#code
			#qst_oim_na_rech_pospolitu
			(quest_set_slot, "qst_oim_na_msk_tsarzd", slot_quest_giver_troop, "trp_player"), 
			(quest_set_slot, "qst_oim_na_msk_tsarzd", slot_quest_current_state, 0),
			(setup_quest_text, "qst_oim_na_msk_tsarzd"),
			(str_store_string, s2, "@OIM_add_getman  Prikaz Barabasha - zavoevat MC"),
			(call_script, "script_start_quest", "qst_oim_na_msk_tsarzd", "trp_player"),
			(jump_to_menu, "mnu_auto_return_to_map"),
		]),
	] 
    ),  
	
	#oim_getman_barabash_rebelion	
    ("oim_getman_barabash_rebelion",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(str_store_string, s3, "str_getman_barabash_rebelion_ntf"),
		(set_background_mesh, "mesh_pic_pergament"),   
	],
     [
      ("continue", [], "Continue...",
       [
		#code
			#qst_oim_getman_barabash_reb
			(call_script, "script_end_quest", "qst_oim_na_msk_tsarzd"), 
			#qst_oim_na_msk_tsarzd_reb
			(quest_set_slot, "qst_oim_getman_barabash_reb", slot_quest_giver_troop, "trp_kingdom_5_pretender"), 
			(quest_set_slot, "qst_oim_getman_barabash_reb", slot_quest_current_state, 0),
			(setup_quest_text, "qst_oim_getman_barabash_reb"),
			(str_store_string, s2, "@OIM_add_getman  Prikaz Hmelya - zavoevat RP"),
			(call_script, "script_start_quest", "qst_oim_getman_barabash_reb", "trp_kingdom_5_pretender"),
			#script of rebelion
			(call_script, "script_change_troop_faction", "trp_kingdom_2_lord", "fac_kingdom_2"), 
			(faction_set_slot, "fac_kingdom_2", slot_faction_leader, "trp_kingdom_2_lord"),
			(faction_set_slot, "fac_kingdom_2", slot_faction_state, sfs_active),
			(str_store_faction_name, s1, "fac_kingdom_2"),
			(faction_set_name, "fac_kingdom_2", "@{s1} Rebels"),
			(set_relation, "fac_kingdom_5", "fac_kingdom_2", -100), 
			(call_script, "script_give_center_to_faction", "p_town_9", "fac_kingdom_1"),  
			(call_script, "script_give_center_to_lord", "p_town_9", "trp_kingdom_2_lord", 0),
			(call_script, "script_remove_lords_from_center", "p_town_9"), 
			#lords-rebels
			(try_for_range, ":unused", 0, 4), #change it
				(call_script, "script_cf_get_random_lord_except_king_with_faction", "fac_kingdom_5"), 
				(assign, ":target_troop", reg0), 
				(gt, ":target_troop", 0),
				(call_script, "script_change_troop_faction", ":target_troop", "fac_kingdom_2"), 
			(end_try), 
			(assign, "$g_recalculate_ais", 1),
			(call_script, "script_update_all_notes"),
			(jump_to_menu, "mnu_auto_return_to_map"),
		]),
 ] 
    ),  
	
	#oim_getman_casus_beli_barabash
	("oim_getman_casus_beli_barabash",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(str_store_string, s3, "str_getman_barabash_rebelion_end"),
		(set_background_mesh, "mesh_pic_pergament"),   
	],
     [
      ("continue", [], "Continue...",
       [
		(call_script, "script_end_quest", "qst_oim_getman_barabash_reb"), 
		#qst_oim_getman_barabash_casus_beli
		(quest_set_slot, "qst_oim_getman_barabash_casus_beli", slot_quest_giver_troop, "trp_kingdom_5_pretender"), 
		(quest_set_slot, "qst_oim_getman_barabash_casus_beli", slot_quest_current_state, 0),
		(setup_quest_text, "qst_oim_getman_barabash_casus_beli"),
		(str_store_string, s2, "@OIM_add_getman  Bunt podavlen - pora pogovorit s Barabashem..."),
		(call_script, "script_start_quest", "qst_oim_getman_barabash_casus_beli", "trp_kingdom_5_pretender"),
		(jump_to_menu, "mnu_auto_return_to_map"),
		]),
	 ] 
    ),  

	#oim_getman_casus_beli_barabash_war
	("oim_getman_casus_beli_barabash_war",mnf_disable_all_keys,"{s3}",
	"none",
    [
		(try_begin),
			(quest_slot_eq, "qst_oim_getman_barabash_greate_war", slot_quest_current_state, 2),
			(str_store_string, s3, "str_casus_beli_hmel_war_message_delivered"),
			(set_background_mesh, "mesh_pic_pergament"),   
		(else_try),
			(quest_slot_eq, "qst_oim_getman_barabash_greate_war", slot_quest_current_state, 1),
			(str_store_string, s3, "str_casus_beli_hmel_war_message_intercepted"),
			(set_background_mesh, "mesh_pic_pergament"),   
		(end_try), 
	],
     [
      ("continue", [], "Continue...",
       [
			(quest_set_slot, "qst_oim_getman_barabash_greate_war", slot_quest_current_state, 3),
			#code for rebelion
			(call_script, "script_count_lords_of_faction", "fac_kingdom_5"), 
			(assign, ":count", reg0), 
			(val_mul, ":count", 100), 
			(val_div, ":count", 60), 
			(try_for_range, ":unused", 0, ":count"), 
				(call_script, "script_cf_get_random_lord_except_king_with_faction", "fac_kingdom_5"), 
				(assign, ":target_troop", reg0), 
				(call_script, "script_change_troop_faction", ":target_troop", "fac_kingdom_1"), 
			(try_end), 
			(call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_5", "fac_kingdom_1", 1),
			(jump_to_menu, "mnu_auto_return_to_map"),
			(assign, "$g_recalculate_ais", 1),
		]),
	  ] 
    ), 	
	
	
	
	
	
	#OiM tavern code
	#oim_tavern_simple_fight	
	("oim_tavern_simple_fight",mnf_disable_all_keys,"You challenge one of the pub's patrons to a fight. Your enemy is ready and awaits you.",
	"none",
    [
		(set_background_mesh, "mesh_pic_tavern"),   
	],
     [
      ("continue", [], "Continue...",
       [
		(assign,"$all_doors_locked",1),
		#(assign, ":town_scene", "scn_town_7_center"),
		(party_get_slot, ":town_scene", "$current_town", slot_town_arena),
 		(modify_visitors_at_site,":town_scene"),
		(reset_visitors),
		(call_script, "script_oim_set_hero_hp"),
		(set_visitor, 0,"trp_player"),
		(call_script, "script_cf_oim_setup_fighter"),
		(assign, ":visitor", reg0),		
		(set_visitor, 1, ":visitor"),		
        (unlock_achievement, ACHIEVEMENT_LETS_TAKE_THIS_OUTSIDE),		
		(set_jump_mission,"mt_oim_tavern_simple_fight"),
		(jump_to_scene, ":town_scene"),
		(change_screen_mission),
		]),
	  ] 
    ), 	
	
	("oim_tavern_simple_fight_result",mnf_disable_all_keys,"{s2}",
	"none",
    [	
		(assign, reg0, "$g_oim_bet"),
		(try_begin),
			(eq, "$g_battle_result", -1),
			(assign, reg0, "$g_oim_bet"), 
			(str_store_string, s2, "@you we lost the fight. And all the bet {reg0}"),
		(else_try), 
			(val_mul, reg0, 2), 
			(str_store_string, s2, "@you won the fight. And all the bet {reg0}. Even more - you ve learned some new tricks."),
		(end_try), 
		(set_background_mesh, "mesh_pic_tavern"),   		
	],
     [
      ("continue", [(eq, "$g_battle_result", -1),], "Continue...",
       [
			(jump_to_menu, "mnu_auto_return_to_map"),
			#(store_sub, ":gold", 0, "$g_oim_bet"),			
			(troop_remove_gold, "trp_player", "$g_oim_bet"),
			#(call_script, "script_troop_add_gold", "trp_player", ":gold"), 
		]),
		
      ("continue", [(neq, "$g_battle_result", -1)], "Continue...",
       [
			#oim_tavern_fight code
			(store_mul, ":gold", 2, "$g_oim_bet"),
			(call_script, "script_troop_add_gold", "trp_player", ":gold"), 
			(add_xp_as_reward, 50), 
			(store_random_in_range, ":rand", 0, 4),  
			(troop_raise_proficiency_linear, "trp_player",wpt_one_handed_weapon,":rand"),
			(troop_raise_proficiency_linear, "trp_player",wpt_two_handed_weapon,":rand"),
			(troop_raise_proficiency_linear, "trp_player",wpt_polearm,":rand"),
			(jump_to_menu, "mnu_town"),
		]),
	  ] 
    ), 	

	#oim_duel_fight
	("oim_duel_fight",mnf_disable_all_keys,"A bad joke leads you straight into a fight. This would be a good time to recall your fencing practice, and give your foe a good dressing down.",
	"none",
    [
		(set_background_mesh, "mesh_pic_tavern"),   	
	],
     [
      ("continue", [], "Continue...",
       [
		(assign,"$all_doors_locked",1),
		#(assign, ":town_scene", "scn_town_7_center"),
		(party_get_slot, ":town_scene", "$current_town", slot_town_arena),
 		(modify_visitors_at_site,":town_scene"),
		(reset_visitors),
		(call_script, "script_oim_set_hero_hp"),
		(set_visitor, 0, "trp_player"),
		(call_script, "script_cf_oim_setup_fighter"),
		(assign, ":visitor", reg0),
		
		(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
		(try_begin),
		  (eq, ":reduce_campaign_ai", 0), #hard		  
		  (set_visitor, 1, ":visitor"),
		  (set_visitor, 2, ":visitor"),
		  (set_visitor, 3, ":visitor"), 
		(else_try),
		  (eq, ":reduce_campaign_ai", 1), #moderate		  		  
          (set_visitor, 1, ":visitor"),
          (set_visitor, 2, ":visitor"), 
		  (set_visitor, 3, -1), 
        (else_try),
          (eq, ":reduce_campaign_ai", 2), #easy		  
		  (set_visitor, 1, ":visitor"),
		  (set_visitor, 2, -1), 
		  (set_visitor, 3, -1), 
		(try_end),        

		(store_troop_faction, ":troop_faction", reg0),
		(try_begin), 
			(eq, ":troop_faction", "fac_kingdom_4"),
			(set_jump_mission,"mt_oim_tavern_duel_fight_swed"),
		(else_try), 
			(set_jump_mission,"mt_oim_tavern_duel_fight"),
		(end_try),
		(jump_to_scene, ":town_scene"),
		(change_screen_mission),
		]),
	  ] 
    ), 	
	
	#oim_tavern_duel_fight_result
	("oim_tavern_duel_fight_result",mnf_disable_all_keys,"{s2}",
	"none",
    [
		(assign, reg0, "$g_oim_bet"),
		(try_begin),
			(eq, "$g_battle_result", -1),
			(str_store_string, s2, "@you we lost the fight. And got wounds"),
		(else_try), 
			(str_store_string, s2, "@you won the fight. And some new tricks."),
		(end_try), 
		(set_background_mesh, "mesh_pic_tavern"),   
	],
     [
      ("continue", [(eq, "$g_battle_result", -1),], "Continue...",
       [
			(jump_to_menu, "mnu_auto_return_to_map"),
			#code to start quest qst_oim_duel_wound
						
			(store_troop_gold, ":gold", "trp_player"),
			(store_mul, ":lost_gold", ":gold", 5), 
			(val_div, ":lost_gold", 100), 
            (val_min, ":lost_gold", 1000),
            (val_max, ":lost_gold", 50),
            (val_min, ":lost_gold", ":gold"),
			(troop_remove_gold, "trp_player", ":lost_gold"),

			(try_begin),
			  (neg|check_quest_active, "qst_oim_duel_wound"),
              (quest_set_slot, "qst_oim_duel_wound", slot_quest_current_state, 0),
			  (quest_set_slot, "qst_oim_duel_wound", slot_quest_giver_troop, "$g_talk_troop"),  
			  (quest_set_slot, "qst_oim_duel_wound", slot_quest_expiration_days, 5),  
			  (setup_quest_text, "qst_oim_duel_wound"),	
			  (str_store_string, s2, "@You ve got wound.. It's better to have a rest"),
			  (call_script, "script_start_quest", "qst_oim_duel_wound", "$g_talk_troop"),
			  (troop_raise_attribute, "trp_player", ca_strength, -1), 
			  (troop_raise_attribute, "trp_player", ca_agility, -2), 			  
            (try_end),
			
			(troop_set_slot, "$g_talk_troop", slot_troop_last_duel_time, -1),
		]),
		
      ("continue", [(neq, "$g_battle_result", -1)], "Continue...",
       [
			#oim_tavern_fight code
			(add_xp_as_reward, 150), 
			(store_random_in_range, ":rand", 2, 7),  
			(troop_raise_proficiency_linear, "trp_player",wpt_one_handed_weapon, ":rand"),
			#getting random weapon
			(store_random_in_range, ":rand", 0, 5), 
			(try_begin), 
				(eq, ":rand", 0), 
				(troop_add_item, "trp_player", "itm_sablya_a"),
			(else_try),
				(eq, ":rand", 1), 
				(troop_add_item, "trp_player", "itm_sablya_b"),
			(else_try),
				(eq, ":rand", 2), 
				(troop_add_item, "trp_player", "itm_sablya_c"),
			(else_try), 
				(eq, ":rand", 3), 
				(store_random_in_range, ":rnd", 3, 6), 
				(val_mul, ":rnd", 100), 
				(call_script, "script_troop_add_gold", "trp_player", ":rnd"),
			(end_try),
			(jump_to_menu, "mnu_town"),
			(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),  
		]),
	  ] 
    ),
	
	#oim_tavern_ranged_fight
    #(assign, "$g_mt_mode", ctm_ranged),
    #(assign, "$temp", itp_type_bow),
    #(jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
    #(call_script, "script_start_training_at_training_ground", "$temp", 10),
	
	("oim_tavern_ranged_fight",mnf_disable_all_keys,"You prepare for a marksmanship contest. To win, you must hit as many targets as you can.",
	"none",
    [
		#oim_code
		(set_background_mesh, "mesh_pic_tavern"),   
	],
     [
      ("continue", [], "Continue...",
       [
			(modify_visitors_at_site, "scn_oim_training_ground_ranged_melee_monfor"),
			(reset_visitors),
			(set_visitor, 0, "trp_player"),
			(mission_tpl_entry_clear_override_items, "mt_oim_tavern_ranged_duel", 0),
			(store_troop_faction, ":troop_faction", "$g_talk_troop"),
			(try_begin), 
				(eq, ":troop_faction", "fac_kingdom_3"),
				(mission_tpl_entry_add_override_item, "mt_oim_tavern_ranged_duel", 0, "itm_tutorial_short_bow"),
				(mission_tpl_entry_add_override_item, "mt_oim_tavern_ranged_duel", 0, "itm_practice_arrows_10_amount"),
			(else_try), 
				(mission_tpl_entry_add_override_item, "mt_oim_tavern_ranged_duel", 0, "itm_old_musket"),
				(mission_tpl_entry_add_override_item, "mt_oim_tavern_ranged_duel", 0, "itm_steel_bolts_10"),
			(end_try),
			(set_jump_mission, "mt_oim_tavern_ranged_duel"),
			(jump_to_scene, "scn_oim_training_ground_ranged_melee_monfor"),
			(change_screen_mission),
		]),
		
	  ] 
    ),
	
	
	#oim_ranged_duel_tavern_result	
	("oim_ranged_duel_tavern_result",mnf_disable_all_keys,"{s2}",
	"none",
    [
		#main param $scene_num_total_gourds_destroyed
		#code getting amount destroyed by NPC
		(val_sub, "$scene_num_total_gourds_destroyed", 1), 
		(troop_get_slot, ":alc_count", "$g_talk_troop", slot_troop_alcohol_count), 
		(try_begin), 
			(lt, ":alc_count", 4),
			(store_random_in_range, ":npc_count", 6, 8), 
		(else_try), 
			(is_between, ":alc_count", 4, 6), 
			(store_random_in_range, ":npc_count", 3, 6), 
		(else_try), 
			(store_random_in_range, ":npc_count", 2, 5), 
		(end_try), 
		(assign, "$g_oim_npc_result", ":npc_count"),
		(try_begin), 
			(eq, "$g_oim_npc_result", "$scene_num_total_gourds_destroyed"), 
			(str_store_string, s2, "@oim the duel is over. There is draw"), 
		(else_try), 
			(gt, "$g_oim_npc_result", "$scene_num_total_gourds_destroyed"), 
			(str_store_string, s2, "@oim the duel is over. You lost the battle"), 
		(else_try), 
			(str_store_string, s2, "@oim the duel is over. You win"), 
		(end_try),	
		#(assign, reg0, "$g_oim_npc_result"), 
		#(assign, reg1, "$scene_num_total_gourds_destroyed"),
		#(display_log_message, "@p: {reg0}, p2: {reg1}"),
		(set_background_mesh, "mesh_pic_tavern"),   		
 	 ],
     [
      ("continue", [], "Continue...",
       [
			(try_begin), 
				(gt, "$g_oim_npc_result", "$scene_num_total_gourds_destroyed"), 
				#(store_sub, ":gold", 0, "$g_oim_bet"), 				
				(troop_remove_gold, "trp_player", "$g_oim_bet"), 
				#(call_script, "script_troop_add_gold", "trp_player", ":gold"), 
				(add_xp_as_reward, 10), 
				(store_random_in_range, ":rand", 0, 2),  
				(store_troop_faction, ":troop_faction", "$g_talk_troop"),
				(try_begin), 
					(eq, ":troop_faction", "fac_kingdom_3"),
					(troop_raise_proficiency_linear, "trp_player",wpt_archery, ":rand"),
				(else_try), 
					(troop_raise_proficiency_linear, "trp_player",wpt_crossbow, ":rand"),
				(end_try), 	
			(else_try), 
				(lt, "$g_oim_npc_result", "$scene_num_total_gourds_destroyed"), 
				(val_mul, "$g_oim_bet", 2), 
				(call_script, "script_troop_add_gold", "trp_player", "$g_oim_bet"), 
				(add_xp_as_reward, 50), 
				(store_random_in_range, ":rand", 2, 7),  
				(store_troop_faction, ":troop_faction", "$g_talk_troop"),
				(try_begin), 
					(eq, ":troop_faction", "fac_kingdom_3"),
					(troop_raise_proficiency_linear, "trp_player",wpt_archery, ":rand"),
				(else_try), 
					(troop_raise_proficiency_linear, "trp_player",wpt_crossbow, ":rand"),
				(end_try), 	
			(end_try),	
			(jump_to_menu, "mnu_town"),
		]),
	  ] 
    ),
	
	#oim_drunken_prison
	("oim_drunken_prison",mnf_disable_all_keys,"That last cup of wine turns out to be not such a good idea and you drift off to a drunken stupor. When you open up your eyes, you find yourself in a dark cell in the city prison.",
	"none",
    [
		(set_background_mesh, "mesh_pic_wounded"),   
	],
     [
      ("continue", [], "Continue...",
       [
			(store_troop_gold, ":gold", "trp_player"),
			(val_mul, ":gold", 5), 
			(val_div, ":gold", 100), 
			#(store_sub, ":gold", 0, ":gold"), 
			#(call_script, "script_troop_add_gold", "trp_player", ":gold"), 			
			(troop_remove_gold, "trp_player", ":gold"),
			(assign, "$g_player_is_captive", 1),
			(assign,"$auto_menu",-1),
			(assign, "$capturer_party", "$g_encountered_party"),
			(jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
		]),
	  ] 
    ), 	
	
	#oim_drunken_wound
	("oim_drunken_wound",mnf_disable_all_keys,"You wake up the devil knows where, beaten and penniless. You vaguely recall your last toast...",
	"none",
    [
		(set_background_mesh, "mesh_pic_wounded"),   	
	],
     [
      ("continue", [], "Continue...",
       [
			(store_troop_gold, ":gold", "trp_player"),
			(store_mul, ":lost_gold", ":gold", 5), 
			(val_div, ":lost_gold", 100), 
            (val_min, ":lost_gold", 1000),
            (val_max, ":lost_gold", 50),
            (val_min, ":lost_gold", ":gold"),
			(troop_remove_gold, "trp_player", ":lost_gold"),

			(try_begin),			  
			  (neg|check_quest_active, "qst_oim_duel_wound"),
			  (troop_raise_attribute, "trp_player", ca_strength, -1), 
			  (troop_raise_attribute, "trp_player", ca_agility, -2), 			  
			  (quest_set_slot, "qst_oim_duel_wound", slot_quest_current_state, 0),
			  (quest_set_slot, "qst_oim_duel_wound", slot_quest_giver_troop, "trp_player"), 
			  (quest_set_slot, "qst_oim_duel_wound", slot_quest_expiration_days, 3),  
			  (setup_quest_text, "qst_oim_duel_wound"),
			  (str_store_string, s2, "@You ve got wound.. It's better to have a rest"),
			  (call_script, "script_start_quest", "qst_oim_duel_wound", "trp_player"),
			(try_end),
			(jump_to_menu, "mnu_auto_return_to_map"), 
		]),
	  ] 
    ),
	
	#oim_alcoholic
	("oim_alcoholic",mnf_disable_all_keys,"You have become too fond of pubs. Not a day passes by without you draining a couple mugs. But once you do, your strength fails you, and your money strangely vanishes...",
	"none",
    [
		(set_background_mesh, "mesh_pic_wounded"),   	
	],
     [
      ("continue", [], "Continue...",
       [
			#qst_oim_alcoholic
			(try_begin),
			  (neg|check_quest_active, "qst_oim_alcoholic"),
			  (quest_set_slot, "qst_oim_alcoholic", slot_quest_current_state, 0),
			  (quest_set_slot, "qst_oim_alcoholic", slot_quest_giver_troop, "trp_player"),  
			  (quest_set_slot, "qst_oim_alcoholic", slot_quest_target_amount, "$g_oim_hero_global_alc_count"), 
			  (setup_quest_text, "qst_oim_alcoholic"),	
			  (str_store_string, s2, "@You ve got wound.. It's better to have a rest"),
			  (call_script, "script_start_quest", "qst_oim_alcoholic", "trp_player"),
			  (troop_raise_attribute, "trp_player", ca_strength, -1), 
			  (troop_raise_attribute, "trp_player", ca_agility, -1), 			  
			(try_end),
			(jump_to_menu, "mnu_auto_return_to_map"), 
		]),
	  ] 
    ),
	
	#oim_rich_visitor
	("oim_rich_visitor",mnf_disable_all_keys,"{s2}",
	"none",
    [
		(store_character_level, ":level", "trp_player"), 
		(try_begin),
			(eq, "$players_kingdom", 0),
			(lt, ":level", 13),  
			(str_store_string, s2, "@You sought that the visitor is alone"),
		(else_try), 
			(str_store_string, s2, "@There is gourds. It's better to return to the tavern..."),
		(end_try), 
	],
     [
      ("attack", [
  		(store_character_level, ":level", "trp_player"), 
		(eq, "$players_kingdom", 0),
		(lt, ":level", 13),
	  ],"Pursue the townsman.",
       [
			#
			(assign,"$all_doors_locked",1),
			(assign, "$g_next_menu", "mnu_oim_getman_sneack_in"),
			(party_get_slot, ":sneak_scene", "$current_town",slot_town_alley), # slot_town_gate),
			(modify_visitors_at_site,":sneak_scene"),
			(reset_visitors),
			#slot_faction_tier_3_troop
			#slot_faction_tier_4_troop
			(store_faction_of_party, ":party_faction", "$g_encountered_party"), 
			(call_script, "script_get_faction_unit_of_type", ":party_faction", 1), #pikeman
			(assign, ":tier_2_troop", reg0), 
			(call_script, "script_get_faction_unit_of_type", ":party_faction", 2), #mushketman
			(assign, ":tier_3_troop", reg0), 			
			(set_visitor, 0, "trp_player"),
			(set_visitor, 3, "trp_oim_rich_visitor"), 
			(store_random_in_range, ":rand", 0, 100),
			(try_begin), 
				(le, ":rand", 40), 
				(set_visitor, 2 ,":tier_2_troop"),
				(set_visitor, 1 ,":tier_2_troop"),
				(set_visitor, 4 ,":tier_3_troop"),
			(end_try), 	
			(set_jump_mission,"mt_oim_tavern_rich_man_hunt"),
			(jump_to_scene,":sneak_scene"),
			(change_screen_mission), 

			(assign, "$g_tavern_rest", 0),
		]),

  	  ("go_back_dot", [], "Go back.",
       [
			(jump_to_menu, "mnu_town"),
		]),

       ] 
    ),

	("oim_rich_visitor_result",mnf_disable_all_keys,"{s2}",
	"none",
    [
		(try_begin),
			(eq, "$g_battle_result", -1),
			(str_store_string, s2, "@You lost the fight. And gourds taken you as an prisoner..."),
		(else_try), 
			(str_store_string, s2, "@The man is dead... You found only a small sum of money and his weapon..."),
		(end_try), 
	],
     [
      ("continue", [(eq, "$g_battle_result", -1),], "Continue...",
       [
			(val_add, "$g_oim_crimes_counter", 1),
			(store_troop_gold, ":gold", "trp_player"),
			(val_mul, ":gold", 15), 
			(val_div, ":gold", 100), 
			#(store_sub, ":gold", 0, ":gold"), 
			#(call_script, "script_troop_add_gold", "trp_player", ":gold"), 			
			(troop_remove_gold, "trp_player", ":gold"),
			(assign, "$g_player_is_captive", 1),
			(assign,"$auto_menu",-1),
			(assign, "$capturer_party", "$g_encountered_party"),
			(try_begin), 
				(gt, "$g_oim_crimes_counter", 3),
				(str_store_string, s2, "@you were killed as crimer"), 
				(jump_to_menu, "mnu_oim_last_game_menu"),	
			(else_try), 	
				(val_add, "$g_oim_crimes_counter", 1),
				(jump_to_menu, "mnu_oim_drunken_prison"),			
			(end_try), 	
		]),

      ("continue", [(neq, "$g_battle_result", -1),], "Continue...",
       [
			(store_random_in_range, ":gold", 4, 7), 
			(val_mul, ":gold", 100), 
			(call_script, "script_troop_add_gold", "trp_player", ":gold"), 
			(store_random_in_range, ":rand", 0, 5), 
			(try_begin), 
				(eq, ":rand", 0), 
				(troop_add_item, "trp_player", "itm_sablya_a"),
			(else_try),
				(eq, ":rand", 1), 
				(troop_add_item, "trp_player", "itm_sablya_b"),
			(else_try),
				(eq, ":rand", 2), 
				(troop_add_item, "trp_player", "itm_sablya_c"),
			(else_try),
				(eq, ":rand", 3), 
				(troop_add_item, "trp_player", "itm_pistol_b"),
			(end_try), 
			(call_script, "script_change_player_honor", -1), 
			(jump_to_menu, "mnu_auto_return_to_map"),
		]),
		
	  ] 
    ),	
   (
    "captured_enemy_menu",mnf_disable_all_keys,"{s17}",
    "none",
    [],
    [
      ("continue_kill",[],"Execute the prisoners.",[
					
				(party_get_morale, ":morale","p_main_party"),
				(val_sub, ":morale", 1),
				(val_clamp,":morale",0, 101),
				(party_set_morale, "p_main_party", ":morale"),
				(call_script, "script_remove_captured_enemies"),
				(jump_to_menu,"mnu_total_victory")]),
				
	  ("continue_spawn",[],"Release the prisoners.",[
	  (assign, "$spawn_enemies_true", 1),
	  (jump_to_menu,"mnu_total_victory")]),
    ]
  ),
  
  
  
  (
    "capture_prisoners_as_guards",mnf_disable_all_keys,"{s17}",
    "none",
    [],
    [
      ("continue_guards",[],"Enlist in the garrison.",[
				(assign, "$capture_prisioners_true", 1),
				(jump_to_menu,"mnu_total_victory")]),
				
	  ("continue_spawn_prisoners",[],"Release.",[
	  (assign, "$spawn_prisioners_true", 1),
	  (jump_to_menu,"mnu_total_victory")]),
    ]
  ),

  (
    "charge_with_bunt",mnf_disable_all_keys,"Low spirits among your troops led to a riot. The rebellious demand your blood -- or gold -- ""for their labors"".",
    "none",
    [ 		
		(set_background_mesh, "mesh_pic_deserters"),   	
    ],
    [
      ("continue_bunt",[],"Continue...",[
	   (assign, "$cant_leave_encounter",1),
       (jump_to_menu, "mnu_auto_return_to_map"), 
	   				]),
	 
    ]
  ),
	
	(
    "illness_warning",mnf_disable_all_keys,"{s0} Men of wisdom say good food can help. Perhaps, {s1} or {s2} might heal the soldiers. In any case, a small rest in a pub could do no harm.",
    "none",
    [
		(str_store_troop_name,s1,"trp_npc12"),
		(str_store_troop_name,s2,"trp_npc13"),
	],
    [
      ("continue",[],"Continue...",[
	  (jump_to_menu, "mnu_auto_return_to_map"), 
	  	   				]),
	 
    ]
  ),
  
  (
    "illness_end",mnf_disable_all_keys,"Thanks to a good rest and some decent food, your soldiers have recovered from {s0}.",
    "none",
    [
	],
    [
      ("continue",[],"Continue...",[
	  (change_screen_return,0),
	  	   				]),
	 
    ]
  ),
  
  (
    "warn_taverna_morale",mnf_disable_all_keys,"Your soldiers growl at you with unceasing hunger. They grow tired of these constant marches. Displeasure spreads among your men. ^^Even your weathered fighters hint that it would be well to spend a day or two at the nearest inn...",
    "none",
    [
	],
    [
      ("continue",[],"Continue...",[
	  (change_screen_return,0),
	  	   				]),
	 
    ]
  ),
	
 
  #oim_dmitriy_razin_warn
  ("oim_dmitriy_razin_warn",mnf_disable_all_keys,"Rumors spread that Ataman Stenka Razin has stirred up another rebellion. This time -- against you.",
    "none",
    [],
    [
      ("continue", [], "Continue...",
       [
		(jump_to_menu, "mnu_auto_return_to_map"),		
	  ]),
    ]),

   #oim_razin_asking_for_marshal
  ("oim_razin_asking_for_marshal",mnf_disable_all_keys,"{s2}",
    "none",
    [
		(try_begin), 
			(quest_slot_eq, "qst_oim_black_lord", slot_quest_current_state, 1),
			(str_store_string, s2, "@Nu vow vostaniye zakoncheno. Pora pogovorit s razinim"),
		(else_try), 
			(quest_slot_eq, "qst_oim_black_lord", slot_quest_current_state, 2),
			(eq, "$g_battle_result", -1), 
			(str_store_string, s2, "str_oim_defeated_by_razin"),
		(else_try), 
			(str_store_string, s2, "@Razin now is the marshal"),
		(end_try), 
		#
	],
    [
      ("continue", [(quest_slot_eq, "qst_oim_black_lord", slot_quest_current_state, 1),], "Continue...",
       [
		(call_script, "script_get_closest_walled_center_of_faction", "fac_kingdom_2", "p_town_8"), 
		(assign, ":center_no", reg0), 		
		(try_begin), 
			(neg|is_between, ":center_no", walled_centers_begin, walled_centers_end),
			(assign, ":center_no", "p_town_8"), 		
		(end_try), 
	    (set_jump_mission,"mt_oim_simle_fight_interior"),
        (party_get_slot, ":castle_scene", ":center_no", slot_town_castle),
        (modify_visitors_at_site,":castle_scene"),
        (reset_visitors),
        (store_faction_of_party, ":center_faction", ":center_no"),
        (faction_get_slot, ":guard_troop", ":center_faction", slot_faction_guard_troop),
        (try_begin),
			(le, ":guard_troop", 0),
			(assign, ":guard_troop", "trp_swadian_sergeant"),
        (try_end),
		(set_visitor, 16, "trp_kingdom_2_pretender"),
        (set_visitor, 6, ":guard_troop"),
        (set_visitor, 7, ":guard_troop"),
        (set_visitor, 17, ":guard_troop"),
        (set_visitor, 18, ":guard_troop"),
        (jump_to_scene,":castle_scene"),
        (scene_set_slot, ":castle_scene", slot_scene_visited, 1),
		(assign, "$g_next_menu", "mnu_oim_razin_asking_for_marshal"),
		(party_relocate_near_party, "p_main_party", ":center_no", 1),
        (change_screen_mission),
		#(jump_to_menu, "mnu_auto_return_to_map"),		
		(str_store_string, s2, "str_oim_black_lord_king"),  
		(add_quest_note_from_sreg, "qst_oim_black_lord", 4, s2, 1),
	  ]),
	  
      ("continue", [
		(quest_slot_eq, "qst_oim_black_lord", slot_quest_current_state, 2),
		(eq, "$g_battle_result", -1),
	  ], "Continue...",
       [
		(start_presentation, "prsnt_game_credits"),
        (change_screen_quit),
	  ]),

      ("continue", [
  		(quest_slot_eq, "qst_oim_black_lord", slot_quest_current_state, 2),
		(neq, "$g_battle_result", -1),
	  ], "Continue...",
       [
		(jump_to_menu, "mnu_auto_return_to_map"),		
        (faction_set_slot, "fac_kingdom_2", slot_faction_leader, "trp_player"),	
		(troop_add_item, "itm_shapka_monomaha", 0), 
        (assign, "$g_recalculate_ais", 1),
        (call_script, "script_update_all_notes"),
		(quest_set_slot, "qst_oim_black_lord", slot_quest_current_state, 10),
		(call_script, "script_end_quest", "qst_rebel_against_kingdom"),
		(faction_set_slot, "fac_kingdom_2", slot_faction_marshall, -1), 
		#seems to be enogh
		(call_script, "script_oim_remove_lord", "trp_kingdom_2_pretender", "fac_kingdom_2"),
        (assign, "$g_recalculate_ais", 1),
        (call_script, "script_update_all_notes"),
		
	  ]),
    ]),

	#oim_dmitry_elected
    ("oim_dmitry_elected",mnf_disable_all_keys,"You persuaded the Boyars to support you in the election. As a result, you have become Tsar.",
    "none",
    [],
    [
      ("continue", [], "Continue...",
       [
		#code
		(assign, "$g_razin_rebellion", 1), 
		(store_current_day, "$g_razin_time_offset"),
		(val_add, "$g_razin_time_offset", 7), 
		(troop_get_slot, ":lord_party", "trp_kingdom_2_pretender", slot_troop_leaded_party),
		(call_script, "script_party_set_ai_state", ":lord_party", spai_undefined, -1),
		(jump_to_menu, "mnu_auto_return_to_map"),		
		
		(quest_set_slot, "qst_oim_black_lord", slot_quest_current_state, 0),
		(quest_set_slot, "qst_oim_black_lord", slot_quest_giver_troop, "trp_player"),  
		(setup_quest_text, "qst_oim_black_lord"),	
		(str_store_string, s2, "str_oim_black_lord_king"),
		(call_script, "script_start_quest", "qst_oim_black_lord", "trp_player"),	
		#it is simply immposible, but fixed to:
		(quest_set_slot, "qst_oim_dmitriy_elections", slot_quest_expiration_days, -1),
		(call_script, "script_end_quest", "qst_oim_dmitriy_elections"),		
        (faction_set_slot, "fac_kingdom_2", slot_faction_leader, "trp_player"),
        (faction_set_slot, "fac_kingdom_2", slot_faction_marshall, "trp_kingdom_2_pretender"),
		(troop_set_slot, "trp_kingdom_2_pretender", slot_troop_occupation, slto_kingdom_hero),
		(troop_add_item, "itm_shapka_monomaha", 0), 
        (assign, "$g_recalculate_ais", 1),
        (call_script, "script_update_all_notes"),
	  ]),
    ]),	

	#oim_dmitry_election_failed	
    ("oim_dmitry_election_failed",mnf_disable_all_keys,"You failed to draw the Boyars to your side. The Boyar Council elected Razin as Tsar.",
    "none",
    [],
    [
      ("continue", [], "Continue...",
       [
		#code
		(store_current_day, ":cur_day"),
		(quest_set_slot, "qst_oim_dmitriy_elections", slot_quest_start_time, ":cur_day"),
		(call_script, "script_fail_quest", "qst_oim_dmitriy_elections"),
		(jump_to_menu, "mnu_auto_return_to_map"),		
	  ]),
    ]),	
	
  #simle_text_message
  ("simle_text_message",mnf_disable_all_keys,"{s2}",
    "none",
    [],
    [
      ("continue", [], "Continue...",
       [
		(jump_to_menu, "mnu_auto_return_to_map"),		
	  ]),
    ]),	
	
  ("oim_diplomacy_window",mnf_disable_all_keys,"With which nation do you wish to declare war?",
    "none",
    [],
    [
      ("fac_1_continue", [
		(str_store_faction_name, s2, "fac_kingdom_1"),
		(store_relation, ":players_kingdom_relation", "$players_kingdom", "fac_kingdom_1"),
		(ge, ":players_kingdom_relation", 0),
		(neq, "$players_kingdom", "fac_kingdom_1"),
		(faction_slot_eq, "fac_kingdom_1", slot_faction_state, sfs_active),
	  ],"{s2}",
       [
		(assign, "$temp", "fac_kingdom_1"),
		(jump_to_menu, "mnu_submit_war"),		
	  ]),
	  
      ("fac_2_continue", [
		(str_store_faction_name, s2, "fac_kingdom_2"),
		(store_relation, ":players_kingdom_relation", "$players_kingdom", "fac_kingdom_2"),
		(ge, ":players_kingdom_relation", 0),
		(neq, "$players_kingdom", "fac_kingdom_2"),
		(faction_slot_eq, "fac_kingdom_2", slot_faction_state, sfs_active),
	  ],"{s2}",
       [
		(assign, "$temp", "fac_kingdom_2"),
		(jump_to_menu, "mnu_submit_war"),		
	  ]),

      ("fac_3_continue", [
		(str_store_faction_name, s2, "fac_kingdom_3"),
		(store_relation, ":players_kingdom_relation", "$players_kingdom", "fac_kingdom_3"),
		(faction_slot_eq, "fac_kingdom_3", slot_faction_state, sfs_active),
		(ge, ":players_kingdom_relation", 0),
		(neq, "$players_kingdom", "fac_kingdom_3"),
	  ],"{s2}",
       [
		(assign, "$temp", "fac_kingdom_3"),
		(jump_to_menu, "mnu_submit_war"),		
	  ]),
      ("fac_4_continue", [
		(str_store_faction_name, s2, "fac_kingdom_4"),
		(store_relation, ":players_kingdom_relation", "$players_kingdom", "fac_kingdom_4"),
		(faction_slot_eq, "fac_kingdom_4", slot_faction_state, sfs_active),
		(ge, ":players_kingdom_relation", 0),
		(neq, "$players_kingdom", "fac_kingdom_4"),
	  ],"{s2}",
       [
		(assign, "$temp", "fac_kingdom_4"),
		(jump_to_menu, "mnu_submit_war"),		
	  ]),
	  
      ("fac_5_continue", [
		(str_store_faction_name, s2, "fac_kingdom_5"),
		(store_relation, ":players_kingdom_relation", "$players_kingdom", "fac_kingdom_5"),
		(faction_slot_eq, "fac_kingdom_5", slot_faction_state, sfs_active),
		(ge, ":players_kingdom_relation", 0),
		(neq, "$players_kingdom", "fac_kingdom_5"),
	  ],"{s2}",
       [
		(assign, "$temp", "fac_kingdom_5"),
		(jump_to_menu, "mnu_submit_war"),		
	  ]),

      ("go_back_dot", [], "Go back.",
       [
			(change_screen_return),			  
		]),
	  
	  
    ]),		
	
   ("submit_war",mnf_disable_all_keys,"You really wish to start a war with {s2}?",
    "none",
    [
		(str_store_faction_name, s2, "$temp"),
	],
    [
      ("submit_war", [], "Yes",
       [
		(call_script, "script_diplomacy_start_war_between_kingdoms", "$temp", "$players_kingdom", 1),
		(change_screen_return),		
	  ]),
	  
      ("reject", [],"No",
       [
		(change_screen_return),		
	  ]),
	  
	  
    ]),		
	
	("oim_auto_talk_menu2", mnf_disable_all_keys,"none", "none",
	[
		#code
		#(party_get_slot, ":scene", "$g_encountered_party", slot_town_tavern), 
		(party_get_slot, ":scene", "$current_town", slot_town_tavern),
		(modify_visitors_at_site, ":scene"),
		(reset_visitors),
		(set_visitor,0,"trp_player"),
		(set_visitor,17,"$oim_auto_talk_troop"),
		(jump_to_scene, ":scene"),
		(change_screen_map_conversation, "$oim_auto_talk_troop"),   
	], []
	), 

	("oim_auto_message_menu2",mnf_disable_all_keys,"{s2}",
    "none",
    [
		(str_store_string, s2, "@OiM_text_for_main_qst_talk_to_king_shtirlic"), 
	],
	[
		("continue", [], "Continue...",
        [
	 		(jump_to_menu, "mnu_auto_return_to_map"),
        ]
		),
    ]
    ), 
	 
	 #Expanded management system -begin
		
		
		#MS Notification menus -begin
	(
    "notification_about_gold_usage_after_construct",0,"In {s1} {s51}.",
    "none",
    [
      (call_script, "script_ms_fill_string", "$g_notification_menu_var1", "$g_notification_menu_var2", slot_ms_script_after_construct),
	  (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
	  (str_store_party_name, s1, "$g_notification_menu_var1"),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),  
  
   (
    "notification_about_gold_usage_30_day",0,"In {s1} {s51}.",
    "none",
    [
	  (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
	  (call_script, "script_ms_get_faction_description_for_element", "$g_notification_menu_var2", ms_flag_short, "$g_notification_menu_var1"),
	  (str_store_string, s2, reg0),
      (call_script, "script_ms_fill_string", "$g_notification_menu_var1", "$g_notification_menu_var2", slot_ms_script_30_day),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
	  (str_store_party_name, s1, "$g_notification_menu_var1"),
	],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),  
  
  (
    "notification_party_under_siege_with_defence",0,"During the siege, {s2} of {s3} has lost {s50} in traps.",
    "none",
       [
      #(str_store_troop_name, s2, "$g_notification_menu_var2"),
	  
	  (party_stack_get_troop_id, ":leader_troop_no", "$g_notification_menu_var2", 0),
      (str_store_troop_name, s2, ":leader_troop_no"),
	  
      #(store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", ":leader_troop_no"),
	  (try_begin), 
		(eq, "$g_notification_menu_var2", "p_main_party"),
		(assign, ":troop_faction", "$players_kingdom"),
	  (end_try), 
      (str_store_faction_name, s3, ":troop_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
	  (call_script, "script_remove_percent_of_each_kind_of_troops", 10, "$g_notification_menu_var2"),	
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      #(str_store_party_name, s44, "$g_notification_menu_var1"),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
    ]),  
 
	(
    "notification_village_element_leave_service",0,"{s2} of {s1} has resigned from service.",
    "none",
    [
      (call_script, "script_ms_get_faction_description_for_element", "$g_notification_menu_var2", ms_flag_short, "$g_notification_menu_var1"),
	  (str_store_string, s2, reg0),	  
	  (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
	  (str_store_party_name, s1, "$g_notification_menu_var1"),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),
  
    (
    "notification_extra_good_ready",0,"{s2} was made in {s1} on your order. You may collect it.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
	  (str_store_item_name, s2, "$g_notification_menu_var2"),
	  (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),  
		#MS Notification menus -end
		
		#MS Additional menus -begin
  (
    "ms_additional_menu",0,"{s0}",
    "none",
    [
		(call_script, "script_ms_init"), 
		(try_begin),
			(call_script, "script_ms_has_party_additional_menus"),
			(try_begin),
				(troop_slot_ge, "trp_ms_temp_array_additional", 0, 2),
				(str_store_string, s0, "@Viberite nuzhnuyu vam uslugu"),
			(else_try),
				(str_store_string, s0, "@Na daniy moment eto poseleniye ne predostavlyaet dopolnitelnih vozmozhnostey"),
			(try_end),
		(try_end),
	],
    [
        ("ms_add_1",[
						(troop_slot_ge, "trp_ms_temp_array_additional", 1, 1),
						(try_begin),
							(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 1),
							(call_script, "script_ms_get_faction_description_for_element", ":temp_element", ms_flag_short, "$g_encountered_party"),
							(str_store_string, s1, reg0),
						(try_end),
						(this_or_next|party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
						(eq, ":temp_element", "trp_town_building_merchant_guild"), 
					],"{s1}.",[
								(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 1),
								(assign, "$g_ms_cur_add_menu", ":temp_element"),
								(troop_get_slot, ":menu", ":temp_element", slot_ms_additional_menu),
								(jump_to_menu, ":menu")]
							   ),
		("ms_add_2",[
						(troop_slot_ge, "trp_ms_temp_array_additional", 2, 1),
						(try_begin),
							(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 2),
							(call_script, "script_ms_get_faction_description_for_element", ":temp_element", ms_flag_short, "$g_encountered_party"),
							(str_store_string, s1, reg0),
						(try_end),
						(this_or_next|party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
						(eq, ":temp_element", "trp_town_building_merchant_guild"), 
						
					],"{s1}.",[
								(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 2),
								(assign, "$g_ms_cur_add_menu", ":temp_element"),
								(troop_get_slot, ":menu", ":temp_element", slot_ms_additional_menu),
								(jump_to_menu, ":menu")]
							   ),
		("ms_add_3",[
						(troop_slot_ge, "trp_ms_temp_array_additional", 3, 1),
						(try_begin),
							(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 3),
							(call_script, "script_ms_get_faction_description_for_element", ":temp_element", ms_flag_short, "$g_encountered_party"),
							(str_store_string, s1, reg0),
						(this_or_next|party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
						(eq, ":temp_element", "trp_town_building_merchant_guild"), 
							
						(try_end),
					],"{s1}.",[
								(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 3),
								(assign, "$g_ms_cur_add_menu", ":temp_element"),
								(troop_get_slot, ":menu", ":temp_element", slot_ms_additional_menu),
								(jump_to_menu, ":menu")]
							   ),
		("ms_add_4",[
						(troop_slot_ge, "trp_ms_temp_array_additional", 4, 1),
						(try_begin),
							(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 4),
							(call_script, "script_ms_get_faction_description_for_element", ":temp_element", ms_flag_short, "$g_encountered_party"),
							(str_store_string, s1, reg0),
						(try_end),
						(this_or_next|party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
						(eq, ":temp_element", "trp_town_building_merchant_guild"), 
						
					],"{s1}.",[
								(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 4),
								(assign, "$g_ms_cur_add_menu", ":temp_element"),
								(troop_get_slot, ":menu", ":temp_element", slot_ms_additional_menu),
								(jump_to_menu, ":menu")]
							   ),
		("ms_add_5",[
						(troop_slot_ge, "trp_ms_temp_array_additional", 5, 1),
						(try_begin),
							(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 5),
							(call_script, "script_ms_get_faction_description_for_element", ":temp_element", ms_flag_short, "$g_encountered_party"),
							(str_store_string, s1, reg0),
						(try_end),
						(this_or_next|party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
						(eq, ":temp_element", "trp_town_building_merchant_guild"), 
						
					],"{s1}.",[
								(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 5),
								(assign, "$g_ms_cur_add_menu", ":temp_element"),
								(troop_get_slot, ":menu", ":temp_element", slot_ms_additional_menu),
								(jump_to_menu, ":menu")]
							   ),
		("ms_add_6",[
						(troop_slot_ge, "trp_ms_temp_array_additional", 6, 1),
						(try_begin),
							(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 6),
							(call_script, "script_ms_get_faction_description_for_element", ":temp_element", ms_flag_short, "$g_encountered_party"),
							(str_store_string, s1, reg0),
						(try_end),
						(this_or_next|party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
						(eq, ":temp_element", "trp_town_building_merchant_guild"), 
						
					],"{s1}.",[
								(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 6),
								(assign, "$g_ms_cur_add_menu", ":temp_element"),
								(troop_get_slot, ":menu", ":temp_element", slot_ms_additional_menu),
								(jump_to_menu, ":menu")]
							   ),
		("ms_add_7",[
						(troop_slot_ge, "trp_ms_temp_array_additional", 7, 1),
						(try_begin),
							(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 7),
							(call_script, "script_ms_get_faction_description_for_element", ":temp_element", ms_flag_short, "$g_encountered_party"),
							(str_store_string, s1, reg0),
						(try_end),
						(this_or_next|party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
						(eq, ":temp_element", "trp_town_building_merchant_guild"), 
						
					],"{s1}.",[
								(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 7),
								(assign, "$g_ms_cur_add_menu", ":temp_element"),
								(troop_get_slot, ":menu", ":temp_element", slot_ms_additional_menu),
								(jump_to_menu, ":menu")]
							   ),
		("ms_add_8",[
						(troop_slot_ge, "trp_ms_temp_array_additional", 8, 1),
						(try_begin),
							(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 8),
							(call_script, "script_ms_get_faction_description_for_element", ":temp_element", ms_flag_short, "$g_encountered_party"),
							(str_store_string, s1, reg0),
						(try_end),
						(this_or_next|party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
						(eq, ":temp_element", "trp_town_building_merchant_guild"), 
						
					],"{s1}.",[
								(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 8),
								(assign, "$g_ms_cur_add_menu", ":temp_element"),
								(troop_get_slot, ":menu", ":temp_element", slot_ms_additional_menu),
								(jump_to_menu, ":menu")]
							   ),
		("ms_add_9",[
						(troop_slot_ge, "trp_ms_temp_array_additional", 9, 1),
						(try_begin),
							(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 9),
							(call_script, "script_ms_get_faction_description_for_element", ":temp_element", ms_flag_short, "$g_encountered_party"),
							(str_store_string, s1, reg0),
						(try_end),
						(this_or_next|party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
						(eq, ":temp_element", "trp_town_building_merchant_guild"), 
						
					],"{s1}.",[
								(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 9),
								(assign, "$g_ms_cur_add_menu", ":temp_element"),
								(troop_get_slot, ":menu", ":temp_element", slot_ms_additional_menu),
								(jump_to_menu, ":menu")]
							   ),
		("ms_add_10",[
						(troop_slot_ge, "trp_ms_temp_array_additional", 10, 1),
						(try_begin),
							(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 10),
							(call_script, "script_ms_get_faction_description_for_element", ":temp_element", ms_flag_short, "$g_encountered_party"),
							(str_store_string, s1, reg0),
						(try_end),
						(this_or_next|party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
						(eq, ":temp_element", "trp_town_building_merchant_guild"), 
						
					],"{s1}.",[
								(troop_get_slot, ":temp_element", "trp_ms_temp_array_additional", 10),
								(assign, "$g_ms_cur_add_menu", ":temp_element"),
								(troop_get_slot, ":menu", ":temp_element", slot_ms_additional_menu),
								(jump_to_menu, ":menu")]
							   ),					   
		("ms_back",[],"Return...",[(jump_to_menu, "$g_next_menu")]),
    ],
    ),
	
	(
    "ms_additional_school",0,"{s2}",
    "none",
    [
		(try_begin),
			(str_store_string, s2, "@V vashem otryade netu kompanionov."),
			(call_script, "script_ms_player_has_any_companion"),
			(try_begin),
				(eq, "$g_ms_temp", 1),
				(str_store_string, s2, "@V vashem otryade imeyutsya companioni, kotorih mozhno obuchit"),
			(try_end),
		(try_end),
	],
    [
        ("ms_see_npc_list",[
								(eq, "$g_ms_temp", 1),
							],"See companion list.",
							[
								(party_get_slot, ":elder_troop", "$g_encountered_party", slot_town_elder),
								(modify_visitors_at_site, "scn_meeting_scene_plain_forest"),
								(reset_visitors),
								(set_visitor,0,"trp_player"),
								(set_visitor,17, ":elder_troop"),
								(jump_to_scene,"scn_meeting_scene_plain_forest"),
								(change_screen_map_conversation, ":elder_troop"), 
								(assign, "$g_is_npc_dialog", 1),
	   ]),
		("ms_back",[],"Return...",[(jump_to_menu, "mnu_ms_additional_menu")]),
    ],
    ),
	  
	(
    "ms_additional_merchant_guild",0,"Choose an action.",
    "none",
    [],
       [
        ("ms_guild_deposit",[
								(party_slot_eq, "$g_encountered_party", slot_ms_party_operation_type, ms_flag_none),
								(party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
								(try_begin),
									(call_script, "script_ms_get_deposit_percent"),
									(store_troop_gold, ":gold", "trp_player"),
								(try_end),
								(ge, ":gold", 4000),
							],"Deposit money for {reg0}% monthly.",
							[
								(assign, "$g_guild_flag", ms_flag_deposit),
								(store_troop_gold, ":max_depozit_value", "trp_player"),
								(party_set_slot,  "$g_encountered_party", slot_ms_party_main_balance, ":max_depozit_value"),
								(jump_to_menu, "mnu_ms_guild_get_value")
							]),
		("ms_guild_credit",[
								(party_slot_eq, "$g_encountered_party", slot_ms_party_operation_type, ms_flag_none),
								(party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),								
								(try_begin),
									(call_script, "script_ms_get_credit_percent"),
								(try_end),
							],"Take a loan for one month with {reg0}%.",
							[
								(assign, "$g_guild_flag",ms_flag_credit),
								(store_character_level, ":level", "trp_player"),
								(store_mul, ":max_value", ":level", 950),
								(val_min, ":max_value", 3000),
								(party_set_slot,  "$g_encountered_party", slot_ms_party_main_balance, ":max_value"),
								(jump_to_menu, "mnu_ms_guild_get_value")
							]),
		("ms_guild_deposit_out",[
									(party_slot_eq, "$g_encountered_party", slot_ms_party_operation_type, ms_flag_deposit),
									(party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),									
									(try_begin),
										(call_script, "script_ms_get_deposit_value"),
									(try_end),
								],"Take back the deposit ({reg0} thaler)",
								[
									(assign, "$g_guild_flag", ms_flag_deposit),
									(jump_to_menu, "mnu_ms_guild_get_out")
								]),
		("ms_guild_credit_out",[
									(party_slot_eq, "$g_encountered_party", slot_ms_party_operation_type, ms_flag_credit),
									(party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),									
									(try_begin),
										(call_script, "script_ms_get_credit_value"),
									(try_end),
								],"Repay the loan ({reg0} thaler)",
								[
									(store_troop_gold, ":gold", "trp_player"),
									(assign, "$g_guild_flag", ms_flag_credit),
									(try_begin),
										(party_slot_ge, "$g_encountered_party", slot_ms_party_percent_balance, ":gold"),
										(neg|party_slot_eq, "$g_encountered_party", slot_ms_party_percent_balance, ":gold"),
										(jump_to_menu, "mnu_ms_guild_not_enough_money"),
									(else_try),
										(jump_to_menu, "mnu_ms_guild_get_out"),
									(try_end),
								]),
		("ms_back",[],"Return...",[(jump_to_menu, "mnu_ms_additional_menu")]),
    ],
    ),
	
	(
    "ms_guild_get_value",0,"Select a sum {s0}. Currently the sum {s0} is equal to {reg5}.",
    "none",
    [
		(call_script, "script_ms_get_value_with_corrections"),
	],
    [
        ("ms_guild_500_minus", [
			(party_get_slot, ":value", "$g_encountered_party", slot_ms_party_main_balance),
			(val_sub, ":value", 500), 
			(ge, ":value", 1000), 
		],"-500 thaler",
								[
									(call_script, "script_ms_correct_balance", -500),
									(jump_to_menu, "mnu_ms_guild_get_value"),
								]),
		("ms_guild_500_plus", [
			(try_begin),
				(eq, "$g_guild_flag", ms_flag_deposit),
				(store_troop_gold, ":max_depozit_value", "trp_player"),
			(else_try),
				(eq, "$g_guild_flag", ms_flag_credit),
				(assign, ":max_depozit_value", 1000000),
			(try_end),
			(party_get_slot, ":value", "$g_encountered_party", slot_ms_party_main_balance),
			(store_character_level, ":level", "trp_player"),
			(store_mul, ":max_value", ":level", 350),
			(val_min, ":max_value", ":max_depozit_value"),
			(val_add, ":value", 500), 
			(try_begin), 
				(eq, "$g_guild_flag", ms_flag_deposit),
				(store_troop_gold, ":max_value", "trp_player"),
			(end_try), 
			(ge, ":max_value", ":value"), 
		],"+500 thaler",
								[
									(call_script, "script_ms_correct_balance", 500),
									(jump_to_menu, "mnu_ms_guild_get_value"),
								]),
		("ms_guild_1000_minus", [
			(party_get_slot, ":value", "$g_encountered_party", slot_ms_party_main_balance),
			(val_sub, ":value", 1000), 
			(ge, ":value", 1000), 
		],"-1000 thaler",
								[
									(call_script, "script_ms_correct_balance", -1000),
									(jump_to_menu, "mnu_ms_guild_get_value")
								]),
		("ms_guild_1000_plus", [
			(try_begin),
				(eq, "$g_guild_flag", ms_flag_deposit),
				(store_troop_gold, ":max_depozit_value", "trp_player"),
			(else_try),
				(eq, "$g_guild_flag", ms_flag_credit),
				(assign, ":max_depozit_value", 1000000),
			(try_end),
			(party_get_slot, ":value", "$g_encountered_party", slot_ms_party_main_balance),
			(store_character_level, ":level", "trp_player"),
			(store_mul, ":max_value", ":level", 350),
			(val_min, ":max_value", ":max_depozit_value"),
			(val_add, ":value", 1000), 
			(try_begin), 
				(eq, "$g_guild_flag", ms_flag_deposit),
				(store_troop_gold, ":max_value", "trp_player"),
			(end_try), 
			(ge, ":max_value", ":value"), 
		],"+1000 thaler",
								[
									(call_script, "script_ms_correct_balance", 1000),
									(jump_to_menu, "mnu_ms_guild_get_value")
								]),
		("ms_guild_1500_minus", [
			(party_get_slot, ":value", "$g_encountered_party", slot_ms_party_main_balance),
			(val_sub, ":value", 500), 
			(ge, ":value", 1500), 
		],"-1500 thaler",
								[
									(call_script, "script_ms_correct_balance", -1500),
									(jump_to_menu, "mnu_ms_guild_get_value")
								]),
		("ms_guild_1500_plus", [
			(try_begin),
				(eq, "$g_guild_flag", ms_flag_deposit),
				(store_troop_gold, ":max_depozit_value", "trp_player"),
			(else_try),
				(eq, "$g_guild_flag", ms_flag_credit),
				(assign, ":max_depozit_value", 1000000),
			(try_end),
			(party_get_slot, ":value", "$g_encountered_party", slot_ms_party_main_balance),
			(store_character_level, ":level", "trp_player"),
			(store_mul, ":max_value", ":level", 350),
			(val_min, ":max_value", ":max_depozit_value"),
			(val_add, ":value", 1500), 
			(try_begin), 
				(eq, "$g_guild_flag", ms_flag_deposit),
				(store_troop_gold, ":max_value", "trp_player"),
			(end_try), 
			(ge, ":max_value", ":value"), 
		],"+1500 thaler",
								[
									(call_script, "script_ms_correct_balance", 1500),
									(jump_to_menu, "mnu_ms_guild_get_value")
								]),
		("ms_guild_2000_minus", [
			(party_get_slot, ":value", "$g_encountered_party", slot_ms_party_main_balance),
			(val_sub, ":value", 500), 
			(ge, ":value", 1000), 
		],"-2000 thaler",
								[
									(call_script, "script_ms_correct_balance", -2000),
									(jump_to_menu, "mnu_ms_guild_get_value")
								]),
		("ms_guild_2000_plus", [
			(try_begin),
				(eq, "$g_guild_flag", ms_flag_deposit),
				(store_troop_gold, ":max_depozit_value", "trp_player"),
			(else_try),
				(eq, "$g_guild_flag", ms_flag_credit),
				(assign, ":max_depozit_value", 1000000),
			(try_end),
			(party_get_slot, ":value", "$g_encountered_party", slot_ms_party_main_balance),
			(store_character_level, ":level", "trp_player"),
			(store_mul, ":max_value", ":level", 350),
			(val_min, ":max_value", ":max_depozit_value"),
			(val_add, ":value", 2000), 
			(try_begin), 
				(eq, "$g_guild_flag", ms_flag_deposit),
				(store_troop_gold, ":max_value", "trp_player"),
			(end_try), 
			(ge, ":max_value", ":value"), 
		],"+2000 thaler",
								[
									(call_script, "script_ms_correct_balance", 2000),
									(jump_to_menu, "mnu_ms_guild_get_value")
								]),
		("ms_continue",[],"Complete the transaction",[
												(call_script, "script_ms_make_deal"),
												(jump_to_menu, "mnu_ms_additional_merchant_guild")
											 ]),
		("ms_back",[],"Return...",[(jump_to_menu, "mnu_ms_additional_merchant_guild")]),
    ],
    ),
	
	(
    "ms_guild_get_out",0,"Do you wish to carry out this transaction?",
    "none",
    [],
    [
        ("ms_guild_break", [],"Yes",
								[
									(call_script, "script_ms_end_deal"),
									(jump_to_menu, "mnu_ms_additional_merchant_guild")
								]),
		("ms_guild_back", [],"No",
								[
									(jump_to_menu, "mnu_ms_additional_merchant_guild")
								]),
	],
    ),
	
	(
    "ms_guild_not_enough_money",0,"You do not have enough money for that!",
    "none",
    [],
    [
		("ms_guild_back", [],"No",
									[
										(jump_to_menu, "mnu_ms_additional_merchant_guild")
									]),
	],
    ),
	
	(
    "ms_credit_fight",0,"You have not returned the monies due in time, so the bankers have decided to collect by force.",
    "none",
    [],
    [
		("ms_credit_fight_continue", [],"Continue...",
									[
										   (assign,"$all_doors_locked",1),
										   (store_character_level, ":level", "trp_player"),
										   (val_mul, ":level", 4),
										   (val_div, ":level", 10),
										   (val_clamp, ":level", 4, 17),
										   (party_get_slot, ":sneak_scene", "$current_town",slot_town_center),
										   (modify_visitors_at_site,":sneak_scene"),(reset_visitors),
										   #(set_visitor,1,"trp_player"),
										   (store_faction_of_party, ":town_faction","$current_town"),
										   (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_3_troop),
										   (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_4_troop),
										   (try_begin),
											 (gt, ":tier_2_troop", 0),
											 (gt, ":tier_3_troop", 0),
											 (assign,reg(0),":tier_3_troop"),
											 (assign,reg(1),":tier_3_troop"),
											 (assign,reg(2),":tier_2_troop"),
											 (assign,reg(3),":tier_2_troop"),
										   (else_try),
											 (assign,reg(0),"trp_swadian_skirmisher"),
											 (assign,reg(1),"trp_swadian_crossbowman"),
											 (assign,reg(2),"trp_swadian_infantry"),
											 (assign,reg(3),"trp_swadian_crossbowman"),
										   (try_end),
										   #(assign,reg(4),-1),
										   #(shuffle_range,0,5),
										   (store_div, ":amount", ":level", 3),
										   (val_clamp, ":amount", 4, 10),
										   (set_party_battle_mode),
										   (try_begin), 
												(party_slot_eq,"$current_town", slot_party_type, spt_castle),
												(set_visitor, 1, "trp_player"),
												(set_visitors, 3, reg(0), ":amount"),
												(set_visitors, 4, reg(1), ":amount"),
												(set_visitors, 5, reg(2), ":amount"),
												(set_visitors, 6, reg(3), ":amount"),
												(set_jump_mission,"mt_credit_fight"),
										   (else_try), 
												(set_visitor, 1, "trp_player"),
												(set_visitors, 3, reg(0), ":amount"),
												(set_visitors, 4, reg(1), ":amount"),
												(set_visitors, 5, reg(2), ":amount"),
												(set_visitors, 6, reg(3), ":amount"),
												(set_jump_mission,"mt_credit_fight_town"),
										   (end_try), 
										   (set_passage_menu,"mnu_castle_besiege"),
										   #(call_script, "script_replace_shturm_item_begin"),
										   (jump_to_scene,":sneak_scene"),
										   (change_screen_mission), 
									]),
	],
    ),
	
	(
    "ms_additional_extra_goods",0,"{s0}",
    "none",
    [
		(try_begin),
			(call_script, "script_ms_fill_category_array"),
		(try_end),
	],
    [
        ("ms_extra_goods_next",[
									(neg|troop_slot_eq, "trp_ms_temp_array_extra_category", 101, 1),
								],"Continue...",
								[
									(modify_visitors_at_site, "scn_meeting_scene_plain_forest"),
									(reset_visitors),
									(set_visitor,0, "trp_player"),
									(call_script, "script_ms_get_armorer_troop", "$g_ms_cur_add_menu", "$g_encountered_party"), 
									(assign, ":troop_no", reg0),
									#(set_visitor,17, "$g_ms_cur_add_menu"),
									(set_visitor,17, ":troop_no"),
									(assign, "$g_select_extra_good_dialog", 1),
									(jump_to_scene,"scn_meeting_scene_plain_forest"),
									(change_screen_map_conversation, ":troop_no"), 
								]),
		("ms_back",[],"Return...",[(jump_to_menu, "mnu_ms_additional_menu")]),
    ],
    ),
	
	(
    "ms_additional_adviser",0,"{s0}",
    "none",
    [
		(try_begin),
			(call_script, "script_ms_check_for_any_additional_adviser_menu"),
			(try_begin),
				(troop_slot_eq, "trp_ms_temp_extra_adviser_menu", 0, 1),
				(str_store_string, s0,"@Prosmotret spisok gorodov, gde vi imeete pomoschnikov i kotoriye ne v osade"),
			(else_try),
				(str_store_string, s0,"@U vas net gorodov, gde vi imeete pomoschnikov i kotoriye ne v osade"),
			(try_end),
		(try_end),
	],
    [
        ("ms_extra_adviser_continue",[
										(troop_slot_eq, "trp_ms_temp_extra_adviser_menu", 0, 1),
									 ],"Continue...",
										[
											(store_troop_faction, ":faction", "trp_player"),
											(party_get_slot, ":messenger_troop", ":faction", slot_faction_messenger_troop),
											(modify_visitors_at_site, "scn_meeting_scene_plain_forest"),
											(reset_visitors),
											(set_visitor,0, "trp_player"),
											(set_visitor,17, ":messenger_troop"),
											(assign, "$g_ms_extra_adviser_dialog", 1),
											(jump_to_scene,"scn_meeting_scene_plain_forest"),
											(change_screen_map_conversation, ":messenger_troop"), 
										]),
		("ms_back",[],"Return...",[
									(assign, "$g_ms_extra_adviser_dialog", 0),
									(jump_to_menu, "mnu_camp")
								]),
    ],
    ),
		#MS Additional menus -end
	#Expanded management system -end
		
	(
    "notification_change_diplomatic_capital",0,"Now the ambassadors can always be found in {s1}.",
    "none",
    [
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
	  (str_store_party_name, s1, "$g_notification_menu_var1"),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),
  
  (
    "messenger_for_capital",0,"{s0}",
    "none",
    [
		(try_begin),
			(call_script, "script_check_potential_faction_diplomatic_capital"),
			(try_begin),
				(troop_slot_eq, "trp_diplomatic_array", 0, 1),
				(str_store_string, s0,"@Vam nuzhno poslat gonca i vibrat diplomaticheskuyu stolicu."),
			(else_try),
				(troop_slot_eq, "trp_diplomatic_array", 0, 2),
				(str_store_string, s0,"@Vibor stolici proshel uspeshno."),
			(else_try),	
				(str_store_string, s0,"@Vam nuzhno vibrat diplomaticheskuyu stolicu, no v vashey frakcii seychas net gorodov."),
			(try_end),
		(try_end),
	],
    [
		("continue",[],"Continue...",[
											(try_begin),
												(troop_slot_eq, "trp_diplomatic_array", 0, 1),
												#(store_troop_faction, ":faction", "trp_player"),
												#(party_get_slot, ":messenger_troop", ":faction", slot_faction_messenger_troop),
												(faction_get_slot, ":messenger_troop", "$players_kingdom", slot_faction_messenger_troop),
												(modify_visitors_at_site, "scn_meeting_scene_plain_forest"),
												(reset_visitors),
												(set_visitor,0, "trp_player"),
												(set_visitor,17, ":messenger_troop"),
												(assign, "$g_select_capital_dialog", 1),
												(jump_to_scene,"scn_meeting_scene_plain_forest"),
												(change_screen_map_conversation, ":messenger_troop"), 
											(else_try),
												 (try_begin),
													(eq, "$g_diplomatic_capital", -1),
													(assign, "$g_diplomatic_capital", 0),
												 (try_end),
												 (change_screen_map),
											(try_end),
										]),
    ],
    ),
	
	(
    "select_ambassador",0,"Pick an ambassador:",
    "none",
    [],
    [
		
		("ambassador_fac1",[
							(try_begin),
								(call_script, "script_get_ambassador_name_condition", "fac_kingdom_1"),
							(try_end),
							(eq, reg0, 1),
						],"{s0}",[
										(call_script, "script_ambassador_dialog", "fac_kingdom_1"),
									]),
		("ambassador_fac2",[
							(try_begin),
								(call_script, "script_get_ambassador_name_condition", "fac_kingdom_2"),
							(try_end),
							(eq, reg0, 1),
						],"{s0}",[
										(call_script, "script_ambassador_dialog", "fac_kingdom_2"),
									]),
		("ambassador_fac3",[
							(try_begin),
								(call_script, "script_get_ambassador_name_condition", "fac_kingdom_3"),
							(try_end),
							(eq, reg0, 1),
						],"{s0}",[
										(call_script, "script_ambassador_dialog", "fac_kingdom_3"),
									]),
		("ambassador_fac4",[
							(try_begin),
								(call_script, "script_get_ambassador_name_condition", "fac_kingdom_4"),
							(try_end),
							(eq, reg0, 1),
						],"{s0}",[
										(call_script, "script_ambassador_dialog", "fac_kingdom_4"),
									]),
		("ambassador_fac5",[
							(try_begin),
								(call_script, "script_get_ambassador_name_condition", "fac_kingdom_5"),
							(try_end),
							(eq, reg0, 1),
						],"{s0}",[
										(call_script, "script_ambassador_dialog", "fac_kingdom_5"),
									]),
		("back",[],"Return...",[(jump_to_menu, "$g_next_menu")]),
    ],
    ),
	
	(
    "ms_additional_officer",0,"Here you can talk to the garrison commander and hire forces.",
    "none",
    [],
    [
        ("ms_additional_officer_next",[],"Speak with the garrison commander.",
										[
											(modify_visitors_at_site, "scn_meeting_scene_plain_forest"),
											(call_script, "script_ms_init"), 
											(reset_visitors),
											(set_visitor,0, "trp_player"),
											(call_script, "script_ms_get_commander_troop", "$g_encountered_party"),
											(assign, ":troop_no", reg0),
											#(set_visitor,17, "trp_town_upgrade_garrison_commander"),
											(set_visitor,17, ":troop_no"),
											(assign, "$g_select_extra_officer_dialog", 1),
											(jump_to_scene,"scn_meeting_scene_plain_forest"),
											#(change_screen_map_conversation, "trp_town_upgrade_garrison_commander"), 
											(change_screen_map_conversation, ":troop_no"), 
										]),
		("ms_back",[],"Return...",[(jump_to_menu, "mnu_ms_additional_menu")]),
    ],
    ),
	
	
	#oim_cravan_delivered
	
  (
    "oim_caravan_delivered",0,"All the caravan goods have been sold. After calculating all your expenses, you count a profit of {reg1} thaler.",
    "none",
    [
			#code
			(quest_get_slot, ":goods", "qst_oim_deliver_caravan", slot_quest_target_item), 
			(str_store_item_name, s2, ":goods"),
			(quest_get_slot, ":count", "qst_oim_deliver_caravan", slot_quest_target_amount),
			(quest_get_slot, ":party", "qst_oim_deliver_caravan", slot_quest_target_center),
			(call_script, "script_oim_get_item_base_price", ":goods"), 
			(assign, ":price", reg0),
			(assign, ":base_price", reg0),
			(try_begin), 
			    (ge, ":base_price", 150), 
				(neg|check_quest_active, "qst_oim_trade_pantent"), 
				(neg|quest_slot_eq, "qst_oim_trade_pantent", slot_quest_current_state, 2),
				(quest_set_slot, "qst_oim_trade_pantent", slot_quest_current_state, 1),
				(quest_set_slot, "qst_oim_trade_pantent", slot_quest_giver_troop, "trp_player"),  
				(setup_quest_text, "qst_oim_trade_pantent"),	
				(str_store_string, s2, "str_trade_patent_text"),
				(call_script, "script_start_quest", "qst_oim_trade_pantent", "trp_player"),	
				(assign, "$g_notification_menu_var1", "str_oim_trade_troubles_descr"),
				(assign, "$g_notification_menu_var2", "mnu_oim_caravan_delivered"),
				(jump_to_menu, "mnu_notification_simple_str"),
			(else_try), 			
			  (call_script, "script_oim_game_get_item_buy_price_factor", ":goods", ":party"), 
			  (assign, ":price_factor", reg0),
			  (val_mul, ":price", ":price_factor"), 
			  (val_div, ":price", 100),			

			  (val_mul, ":price", ":count"), #count

			  (store_sub, ":profit", ":price", "$g_total_caravan_cost_pure"),
			  (try_begin),
			    (get_achievement_stat, ":total_profit_till_now", ACHIEVEMENT_TRADER, 0),
				(val_add, ":total_profit_till_now", ":profit"),
				(set_achievement_stat, ACHIEVEMENT_TRADER, 0, ":total_profit_till_now"),
				(try_begin),
				  (ge, ":total_profit_till_now", 100000),
				  (unlock_achievement, ACHIEVEMENT_TRADER),				  
				(try_end),

				(try_begin),
				  (ge, ":total_profit_till_now", 1000000),
				  (unlock_achievement, ACHIEVEMENT_GREAT_TRADER),				  
				(try_end),

				(try_begin),
			      (ge, ":profit", 3000),
				  (unlock_achievement, ACHIEVEMENT_WHEELER_DEALER),				
				(try_end),
			  (try_end),

			  (try_begin), 
			    (ge, ":base_price", 300), #if base price is more than 300 and trade patent is not yet taken, 10% of payment is taken as tax.
				(this_or_next|quest_slot_eq, "qst_oim_trade_pantent", slot_quest_current_state, 0),
				(quest_slot_eq, "qst_oim_trade_pantent", slot_quest_current_state, 1),				
				(assign, ":initial_price", ":price"),
				(val_mul, ":price", 90),
				(val_div, ":price", 100), 				
				(store_sub, reg2, ":initial_price", ":price"),
				(str_store_string, s3, "str_percent_10_tax_is_paid"),
				
				(display_message, s3), 
			  (else_try), 
			    (ge, ":base_price", 150), #if base price is more than 200 and trade patent is not yet taken, 5% of payment is taken as tax.
				(this_or_next|quest_slot_eq, "qst_oim_trade_pantent", slot_quest_current_state, 0),
				(quest_slot_eq, "qst_oim_trade_pantent", slot_quest_current_state, 1),				
				(assign, ":initial_price", ":price"),
				(val_mul, ":price", 95),
				(val_div, ":price", 100),				
				(store_sub, reg2, ":initial_price", ":price"),
				(str_store_string, s3, "str_percent_5_tax_is_paid"),
				(display_message, s3), 
			  (end_try), 
			
			  (call_script, "script_troop_add_gold", "trp_player", ":price"),
			  (assign, reg1, ":price"),
			
			  (call_script, "script_oim_change_price_factors", ":party", ":goods", "$oim_count_to_deliver", 1),

			  (assign, "$oim_count_to_deliver", 0),
            (try_end),
	],
    [
		("continue",[],"Continue...",[
			(call_script, "script_end_quest", "qst_oim_deliver_caravan"),
			(quest_set_slot, "qst_oim_deliver_caravan", slot_quest_target_center, -1),  
			(quest_set_slot, "qst_oim_deliver_caravan", slot_quest_target_item, -1),  
			(quest_set_slot, "qst_oim_deliver_caravan", slot_quest_target_amount, -1),  
			(quest_get_slot, ":party_no", "qst_oim_deliver_caravan", slot_quest_target_party),  
			(try_begin),
			  (party_is_active, ":party_no"),
			  (remove_party, ":party_no"),
            (try_end),
			(quest_set_slot, "qst_oim_deliver_caravan", slot_quest_target_party, -1),  
			(change_screen_return),
			#(jump_to_menu, "mnu_castle_outside"),
		]),
    ],
    ),	
	
	
	#notification_simple_str
  (
    "notification_simple_str",0,"{s2}",
    "none",
    [
	  (str_store_string, s2, "$g_notification_menu_var1"),
      ],
    [
      ("continue",[],"Continue...",
       [
	    (try_begin), 
			(eq, "$g_notification_menu_var2", "mnu_oim_caravan_delivered"),
			(assign, "$g_notification_menu_var2", -1),
			(jump_to_menu, "mnu_oim_caravan_delivered"),
		(else_try), 
			(change_screen_return),
		(end_try), 
        ]),
     ]
  ),	

  (
    "notification_tax_collected",0,"{s2}",
    "none",
    [
	  (str_store_party_name, s2, "$g_notification_menu_var2"),
	  (assign, reg0, "$g_notification_menu_var1"),
	  (str_store_string, s2, "str_tax_collected"),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),	

	#banks_report  
  (
    "banks_report",0,"{s2}",
    "none",
    [
		(assign, ":credit_count", 0), 
		(assign, ":deposit_count", 0), 
		(try_for_range, ":cur_center", ms_parties_start, villages_begin),
			(party_is_active, ":cur_center"),			
			(try_begin), 
				(party_slot_eq, ":cur_center", slot_ms_party_operation_type, ms_flag_credit),
				(call_script, "script_ms_get_credit_value_of_party", ":cur_center"),
				(assign, ":value", reg0),				
				(try_begin), 
					(gt, ":value", 0),
					(party_get_slot, ":time", ":cur_center", slot_ms_party_operation_time),
					(store_sub, ":time", 31, ":time"),
					(try_begin), 
						(ge, ":time", 0), 
						(assign, reg1, ":time"),
						(str_store_string, s4, "str_time_credit"),
					(else_try), 
						(str_store_string, s4, "str_time_credit_zero"),
					(end_try), 
					(str_store_party_name, s3, ":cur_center"),
					(assign, reg1, ":value"),
					(str_store_string, s5, "str_credit_report"),
					(try_begin), 
						(eq, ":credit_count", 0),  
						(str_store_string, s6, "@{s5}"), 
					(else_try), 
						(str_store_string, s6, "@{s6} ^{s5}"), 
					(end_try), 
					(val_add, ":credit_count", 1),  
				(end_try), 
			(else_try),
				(party_slot_eq, ":cur_center", slot_ms_party_operation_type, ms_flag_deposit),
				(str_store_party_name, s3, ":cur_center"),
				(call_script, "script_ms_get_deposit_value_of_party", ":cur_center"),
				#(assign, ":value", reg0),				
				(str_store_string, s7, "str_deposit"), 
				(try_begin), 
					(eq, ":deposit_count", 0),  
					(str_store_string, s8, "@{s7}"), 
				(else_try), 
					(str_store_string, s8, "@{s8} ^{s7}"), 
				(end_try), 
				(val_add, ":deposit_count", 1),  
			(end_try), 
		(try_end),    
		(try_begin), 
			(eq, ":deposit_count", 0),  
			(str_store_string, s8, "str_no_deposit"), 
		(end_try), 
		(try_begin), 
			(eq, ":credit_count", 0),  
			(str_store_string, s6, "str_no_credit"), 
		(end_try), 
		(str_store_string, s2, "str_banks_full_report_str"),
	],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   (
    "notification_about_gold_usage_7_day",0,"In {s1} {s51}.",
    "none",
    [
	  (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
	  (call_script, "script_ms_get_faction_description_for_element", "$g_notification_menu_var2", ms_flag_short, "$g_notification_menu_var1"),
	  (str_store_string, s2, reg0),
      (call_script, "script_ms_fill_string", "$g_notification_menu_var1", "$g_notification_menu_var2", slot_ms_script_7_day),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
	  (str_store_party_name, s1, "$g_notification_menu_var1"),
	],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ), 
  

  (
    "meeting_with_thieves",0,"{s1}",
    "none",
    [
	  (str_store_string, s1, "str_meeting_with_thieves"),
	],
    [
	("continue",[],"Continue...",
	[
      (party_get_slot, ":cur_scene", "$current_town", slot_castle_exterior),

      (modify_visitors_at_site, ":cur_scene"),
      (reset_visitors),      	  
	  	  
      #(assign, ":bandit_troop", "trp_bandit"),

      #(store_character_level, ":level", "trp_player"),

      (set_jump_mission, "mt_bandits_at_night"),

      #(assign, ":spawn_amount", 2),
      #(store_div, ":level_fac",  ":level", 10),
      #(val_add, ":spawn_amount", ":level_fac"),
      #(try_for_range, ":unused", 0, 3),
      #  (gt, ":level", 10),
      #  (store_random_in_range, ":random_no", 0, 100),
      #  (lt, ":random_no", ":level"),
      #  (val_add, ":spawn_amount", 1),
      #(try_end),
      #(set_visitors, 4, ":bandit_troop", ":spawn_amount"),
      #(assign, "$num_center_bandits", ":spawn_amount"),
      (set_jump_entry, 2),

      (jump_to_scene, ":cur_scene"),
      (change_screen_mission),	  
	]),
    ],
    ),	


	("oim_rich_visitor_meal",mnf_disable_all_keys,"After spending 25 thaler on a satisfying meal, you decide to have a rest.",
	"none",
    [
	],
     [
      ("start_resting", [
	  ],"Start resting.",
       [
		(assign, "$g_tavern_rest", 1),
		(change_screen_map),		

        (assign, "$auto_enter_town", "$current_town"),
        (assign, "$g_town_visit_after_rest", 1),
        (assign, "$g_last_rest_center", "$current_town"),
        (assign, "$g_last_rest_payment_until", -1),

        (rest_for_hours_interactive, 24 * 7, 5, 0), #rest while not attackable	
		]),
    ],
    ),	

]