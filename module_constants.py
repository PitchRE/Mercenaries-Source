from ID_items import *
from ID_quests import *
from ID_factions import *
##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

########################################################
##  ITEM SLOTS             #############################
########################################################
warcry_cooldown = 25
warcry_active_time = 10



slot_item_is_checked               = 0
slot_item_food_bonus               = 1
slot_item_book_reading_progress    = 2
slot_item_book_read                = 3
slot_item_intelligence_requirement = 4

#slot_item_base_price              = 35
slot_item_base_trust_dmg          = 36
slot_item_base_swing_dmg          = 37
slot_item_base_armor              = 38
slot_item_base_weight             = 39

slot_item_amount_available         = 7

slot_item_urban_demand             = 11 #consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
slot_item_rural_demand             = 12 #consumer demand in villages, measured in abstract units
slot_item_desert_demand            = 13 #consumer demand in villages, measured in abstract units

slot_item_production_slot          = 14 
slot_item_production_string        = 15 

slot_item_tied_to_good_price       = 20 #ie, weapons and metal armor to tools, padded to cloth, leather to leatherwork, etc

slot_item_num_positions            = 22
slot_item_positions_begin          = 23 #reserve around 5 slots after this


slot_item_multiplayer_faction_price_multipliers_begin = 30 #reserve around 10 slots after this

slot_item_primary_raw_material    		= 50
slot_item_is_raw_material_only_for      = 51
slot_item_input_number                  = 52 #ie, how many items it takes to produce the finished product
slot_item_base_price                    = 53

slot_item_multiplayer_item_class   = 60 #temporary, can be moved to higher values
slot_item_multiplayer_availability_linked_list_begin = 61 #temporary, can be moved to higher values


########################################################
##  AGENT SLOTS            #############################
########################################################

slot_agent_target_entry_point     = 0
slot_agent_target_x_pos           = 1
slot_agent_target_y_pos           = 2
slot_agent_is_alive_before_retreat= 3
slot_agent_is_in_scripted_mode    = 4
slot_agent_is_not_reinforcement   = 5
slot_agent_tournament_point       = 6
slot_agent_arena_team_set         = 7
slot_agent_spawn_entry_point      = 8
slot_agent_target_prop_instance   = 9
slot_agent_map_overlay_id         = 10
slot_agent_target_entry_point     = 11
slot_agent_initial_ally_power     = 12
slot_agent_initial_enemy_power    = 13
slot_agent_enemy_threat           = 14
slot_agent_is_running_away        = 15
slot_agent_courage_score          = 16
slot_agent_is_respawn_as_bot      = 17
slot_agent_cur_animation          = 18
slot_agent_next_action_time       = 19
slot_agent_state                  = 20
slot_agent_is_old                 = 21
slot_agent_ladder                 = 22

slot_agent_in_duel_with           = 23
slot_agent_duel_start_time        = 24


slot_agent_walker_occupation      = 25
slot_agent_courage_score_fading_out = 26

slot_agent_siege_state             = 126
slot_agent_target_ladder           = 127
slot_agent_time_since_last_command = 128

    
########################################################
##  FACTION SLOTS          #############################
########################################################
slot_faction_ai_state                   = 4
slot_faction_ai_object                  = 5
slot_faction_ai_last_offensive_time   = 6
slot_faction_marshall= 7
slot_faction_ai_offensive_max_followers = 8

slot_faction_culture              = 9
slot_faction_leader               = 10
##slot_faction_vassal_of            = 11
slot_faction_banner                     = 15

slot_faction_number_of_parties    = 20
slot_faction_state                = 21

slot_faction_player_alarm         		= 30
slot_faction_last_mercenary_offer_time 	= 31
slot_faction_recognized_player    		= 32

#overriding troop info for factions in quick start mode.
slot_faction_quick_battle_tier_1_infantry      = 41
slot_faction_quick_battle_tier_2_infantry      = 42
slot_faction_quick_battle_tier_1_archer        = 43
slot_faction_quick_battle_tier_2_archer        = 44
slot_faction_quick_battle_tier_1_cavalry       = 45
slot_faction_quick_battle_tier_2_cavalry       = 46

slot_faction_tier_1_troop         = 41
slot_faction_tier_2_troop         = 42
slot_faction_tier_3_troop         = 43
slot_faction_tier_4_troop         = 44
slot_faction_tier_5_troop         = 45
slot_faction_deserter_troop       = 48
slot_faction_guard_troop          = 49
slot_faction_messenger_troop      = 50
slot_faction_prison_guard_troop   = 51
slot_faction_castle_guard_troop   = 52

slot_faction_has_rebellion_chance = 60


#Rebellion changes
#slot_faction_rebellion_target                     = 65
#slot_faction_inactive_leader_location         = 66
#slot_faction_support_base                     = 67
#Rebellion changes



#slot_faction_deserter_party_template       = 62

slot_faction_reinforcements_a        = 77
slot_faction_reinforcements_b        = 78
slot_faction_reinforcements_c        = 79

slot_faction_num_armies              = 80
slot_faction_num_castles             = 81
slot_faction_num_towns               = 82

slot_faction_trade_deal              = 83

slot_faction_num_routed_agents       = 90

slot_faction_respawning_frequency    = 91
########################################################
##  PARTY SLOTS            #############################
########################################################
slot_party_type                = 0  #spt_caravan, spt_town, spt_castle

slot_party_retreat_flag        = 2
slot_party_ignore_player_until = 3
slot_party_ai_state            = 4
slot_party_ai_object           = 5

slot_town_belongs_to_kingdom   = 6
slot_town_lord                 = 7
slot_party_ai_substate         = 8
slot_town_claimed_by_player    = 9

slot_cattle_driven_by_player = slot_town_lord #hack

slot_town_center        = 10
slot_town_castle        = 11
slot_town_prison        = 12
slot_town_tavern        = 13
slot_town_store         = 14
slot_town_arena         = 16
slot_town_alley         = 17
slot_town_walls         = 18
slot_center_culture     = 19

slot_town_tavernkeeper  = 20
slot_town_weaponsmith   = 21
slot_town_armorer       = 22
slot_town_merchant      = 23
slot_town_horse_merchant= 24
slot_town_elder         = 25
slot_center_player_relation = 26

slot_center_siege_with_belfry = 27
slot_center_last_taken_by_troop = 28

# party will follow this party if set:
slot_party_commander_party = 30 #default -1
slot_party_following_player    = 31
slot_party_follow_player_until_time = 32
slot_party_dont_follow_player_until_time = 33

slot_village_raided_by        = 34
slot_village_state            = 35 #svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted
slot_village_raid_progress    = 36
slot_village_recover_progress = 37
slot_village_smoke_added      = 38

slot_village_infested_by_bandits   = 39

slot_center_last_player_alarm_hour = 42

slot_village_land_quality          = 44
slot_village_number_of_cattle      = 45
slot_village_player_can_not_steal_cattle = 46

slot_center_accumulated_rents      = 47
slot_center_accumulated_tariffs    = 48
slot_town_wealth        = 49
slot_town_prosperity    = 50
slot_town_player_odds   = 51


slot_party_last_toll_paid_hours = 52
slot_party_food_store           = 53 #used for sieges
slot_center_is_besieged_by      = 54 #used for sieges
slot_center_last_spotted_enemy  = 55

slot_party_cached_strength        = 56
slot_party_nearby_friend_strength = 57
slot_party_nearby_enemy_strength  = 58
slot_party_follower_strength      = 59

slot_town_reinforcement_party_template = 60
slot_center_original_faction           = 61
slot_center_ex_faction                 = 62

slot_party_follow_me                   = 63
slot_center_siege_begin_hours          = 64 #used for sieges
slot_center_siege_hardness             = 65
slot_spawn_party_is_control       = 66
slot_spawn_party_main_object      = 67
slot_spawn_party_attack           = 68

slot_castle_exterior    = slot_town_center

#slot_town_rebellion_contact   = 76
#trs_not_yet_approached  = 0
#trs_approached_before   = 1
#trs_approached_recently = 2

argument_none         = 0
argument_claim   = 1
argument_ruler   = 2
argument_benefit = 3
argument_victory      = 4

slot_town_rebellion_readiness = 77
#(readiness can be a negative number if the rebellion has been defeated)

slot_town_arena_melee_mission_tpl = 78
slot_town_arena_torny_mission_tpl = 79
slot_town_arena_melee_1_num_teams = 80
slot_town_arena_melee_1_team_size = 81
slot_town_arena_melee_2_num_teams = 82
slot_town_arena_melee_2_team_size = 83
slot_town_arena_melee_3_num_teams = 84
slot_town_arena_melee_3_team_size = 85
slot_town_arena_melee_cur_tier    = 86
##slot_town_arena_template	  = 87

slot_center_npc_volunteer_troop_type   = 90
slot_center_npc_volunteer_troop_amount = 91
slot_center_mercenary_troop_type  = 90
slot_center_mercenary_troop_amount= 91
slot_center_volunteer_troop_type  = 92
slot_center_volunteer_troop_amount= 93

#slot_center_companion_candidate   = 94
slot_center_ransom_broker         = 95
slot_center_tavern_traveler       = 96
slot_center_traveler_info_faction = 97
slot_center_tavern_bookseller     = 98
slot_center_tavern_minstrel       = 99

num_party_loot_slots    = 5
slot_party_next_looted_item_slot  = 109
slot_party_looted_item_1          = 110
slot_party_looted_item_2          = 111
slot_party_looted_item_3          = 112
slot_party_looted_item_4          = 113
slot_party_looted_item_5          = 114
slot_party_looted_item_1_modifier = 115
slot_party_looted_item_2_modifier = 116
slot_party_looted_item_3_modifier = 117
slot_party_looted_item_4_modifier = 118
slot_party_looted_item_5_modifier = 119

slot_village_bound_center         = 120
slot_village_market_town          = 121
slot_village_farmer_party         = 122
slot_party_home_center            = 123

slot_center_current_improvement   = 124
slot_center_improvement_end_hour  = 125

slot_center_has_manor            = 130 #village
slot_center_has_fish_pond        = 131 #village
slot_center_has_watch_tower      = 132 #village
slot_center_has_school           = 133 #village
slot_center_has_messenger_post   = 134 #town, castle, village
slot_center_has_prisoner_tower   = 135 #town, castle

village_improvements_begin = slot_center_has_manor
village_improvements_end          = 135

walled_center_improvements_begin = slot_center_has_messenger_post
walled_center_improvements_end               = 136

slot_center_has_bandits                        = 149
slot_town_has_tournament                     = 150
slot_town_tournament_max_teams               = 151
slot_town_tournament_max_team_size           = 152

slot_center_faction_when_oath_renounced      = 155

slot_center_walker_0_troop                   = 160
slot_center_walker_1_troop                   = 161
slot_center_walker_2_troop                   = 162
slot_center_walker_3_troop                   = 163
slot_center_walker_4_troop                   = 164
slot_center_walker_5_troop                   = 165
slot_center_walker_6_troop                   = 166
slot_center_walker_7_troop                   = 167
slot_center_walker_8_troop                   = 168
slot_center_walker_9_troop                   = 169

slot_center_walker_0_dna                     = 170
slot_center_walker_1_dna                     = 171
slot_center_walker_2_dna                     = 172
slot_center_walker_3_dna                     = 173
slot_center_walker_4_dna                     = 174
slot_center_walker_5_dna                     = 175
slot_center_walker_6_dna                     = 176
slot_center_walker_7_dna                     = 177
slot_center_walker_8_dna                     = 178
slot_center_walker_9_dna                     = 179

slot_center_walker_0_type                    = 180
slot_center_walker_1_type                    = 181
slot_center_walker_2_type                    = 182
slot_center_walker_3_type                    = 183
slot_center_walker_4_type                    = 184
slot_center_walker_5_type                    = 185
slot_center_walker_6_type                    = 186
slot_center_walker_7_type                    = 187
slot_center_walker_8_type                    = 188
slot_center_walker_9_type                    = 189

slot_town_trade_route_1           = 190
slot_town_trade_route_2           = 191
slot_town_trade_route_3           = 192
slot_town_trade_route_4           = 193
slot_town_trade_route_5           = 194
slot_town_trade_route_6           = 195
slot_town_trade_route_7           = 196
slot_town_trade_route_8           = 197
slot_town_trade_route_9           = 198
slot_town_trade_route_10          = 199
slot_town_trade_route_11          = 200
slot_town_trade_route_12          = 201
slot_town_trade_route_13          = 202
slot_town_trade_route_14          = 203
slot_town_trade_route_15          = 204
slot_town_trade_routes_begin = slot_town_trade_route_1
slot_town_trade_routes_end = slot_town_trade_route_15 + 1


num_trade_goods = itm_siege_supply - itm_spice
slot_town_trade_good_productions_begin       = 205
slot_town_trade_good_prices_begin            = slot_town_trade_good_productions_begin + num_trade_goods + 1


slot_party_ladders_count          = 300

slot_ms_party_operation_type      = 301
slot_ms_party_operation_time      = 302
slot_ms_party_deposit_percent     = 303
slot_ms_party_credit_percent      = 304
slot_ms_party_main_balance        = 305
slot_ms_party_percent_balance     = 306
slot_ms_party_armourer_time       = 307
slot_ms_party_armourer_element    = 308
slot_ms_party_protection_time     = 309
slot_ms_party_protection_element  = 310
slot_ms_party_messenger_to_adviser = 311

slot_ms_officer_lower_level_trp        = 312
slot_ms_officer_infantry_trp           = 313
slot_ms_officer_cavalry_trp            = 314
slot_ms_officer_infantry_guard_trp     = 315
slot_ms_officer_cavalry_guard_trp      = 316
slot_ms_officer_elite_guard_trp        = 317
slot_ms_officer_mercenary_trp          = 318

slot_ms_officer_lower_level_timer        = 319
slot_ms_officer_infantry_timer           = 320
slot_ms_officer_cavalry_timer            = 321
slot_ms_officer_infantry_guard_timer     = 322
slot_ms_officer_cavalry_guard_timer      = 323
slot_ms_officer_elite_guard_timer        = 324
slot_ms_officer_mercenary_timer          = 325

slot_ms_officer_lower_level_amount        = 326
slot_ms_officer_infantry_amount           = 327
slot_ms_officer_cavalry_amount            = 328
slot_ms_officer_infantry_guard_amount     = 329
slot_ms_officer_cavalry_guard_amount      = 330
slot_ms_officer_elite_guard_amount        = 331
slot_ms_officer_mercenary_amount          = 332

slot_ms_officer_ai_slot_1                 = 333
slot_ms_officer_ai_slot_2                 = 334
slot_ms_officer_ai_slot_3                 = 335
slot_ms_officer_ai_slot_4                 = 336
slot_ms_officer_ai_slot_5                 = 337
slot_ms_officer_ai_slot_6                 = 338
slot_ms_officer_ai_slot_7                 = 339
slot_ms_officer_ai_slot_8                 = 340
slot_ms_officer_ai_slot_9                 = 341
slot_ms_officer_ai_slot_10                = 342

slot_ms_party_horse_time  = 343
slot_ms_party_horse_element = 344

slot_center_last_recruting_time	= 345

#slot_party_type values
##spt_caravan            = 1
spt_castle             = 2
spt_town               = 3
spt_village            = 4
##spt_forager            = 5
##spt_war_party          = 6
##spt_patrol             = 7
##spt_messenger          = 8
##spt_raider             = 9
##spt_scout              = 10
spt_kingdom_caravan    = 11
##spt_prisoner_train     = 12
spt_kingdom_hero_party = 13
##spt_merchant_caravan   = 14
spt_village_farmer     = 15
spt_ship               = 16
spt_cattle_herd        = 17
#spt_deserter           = 20

kingdom_party_types_begin = spt_kingdom_caravan
kingdom_party_types_end = spt_kingdom_hero_party + 1

#slot_faction_state values
sfs_active                     = 0
sfs_defeated                   = 1
sfs_inactive                   = 2
sfs_inactive_rebellion         = 3
sfs_beginning_rebellion        = 4


#slot_faction_ai_state values
sfai_default                   = 0
sfai_gathering_army            		 = 1
sfai_attacking_center          		 = 2
sfai_raiding_village           		 = 3
sfai_attacking_enemy_army      		 = 4
sfai_attacking_enemies_around_center = 5
#Rebellion system changes begin
sfai_nascent_rebellion          = 6
#Rebellion system changes end

#slot_party_ai_state values
spai_undefined                  = -1
spai_besieging_center           = 1
spai_patrolling_around_center   = 4
spai_raiding_around_center      = 5
##spai_raiding_village            = 6
spai_holding_center             = 7
##spai_helping_town_against_siege = 9
spai_engaging_army              = 10
spai_accompanying_army          = 11
spai_trading_with_town          = 13
spai_retreating_to_center       = 14
##spai_trading_within_kingdom     = 15
spai_recruiting_troops          = 16

#slot_village_state values
svs_normal                      = 0
svs_being_raided                = 1
svs_looted                      = 2
svs_recovering                  = 3
svs_deserted                    = 4
svs_under_siege                 = 5

#$g_player_icon_state values
pis_normal                      = 0
pis_camping                     = 1
pis_ship                        = 2


########################################################
##  SCENE SLOTS            #############################
########################################################
slot_scene_visited              = 0
slot_scene_belfry_props_begin   = 10


########################################################
##  TROOP SLOTS            #############################
########################################################
#slot_troop_role         = 0  # 10=Kingdom Lord

slot_troop_occupation          = 2  # 0 = free, 1 = merchant
#slot_troop_duty               = 3  # Kingdom duty, 0 = free
slot_troop_state               = 3  
slot_troop_last_talk_time      = 4
slot_troop_met                 = 5
slot_troop_party_template      = 6
#slot_troop_kingdom_rank        = 7

slot_troop_renown              = 7

##slot_troop_is_prisoner         = 8  # important for heroes only
slot_troop_prisoner_of_party   = 8  # important for heroes only
#slot_troop_is_player_companion = 9  # important for heroes only:::USE  slot_troop_occupation = slto_player_companion

slot_troop_leaded_party         = 10 # important for kingdom heroes only
slot_troop_wealth               = 11 # important for kingdom heroes only
slot_troop_cur_center           = 12 # important for royal family members only (non-kingdom heroes)

slot_troop_banner_scene_prop    = 13 # important for kingdom heroes and player only

slot_troop_original_faction     = 14 # for pretenders
slot_troop_loyalty              = 15
slot_troop_player_order_state   = 16
slot_troop_player_order_object  = 17

#slot_troop_present_at_event    = 19 #defined below

slot_troop_does_not_give_quest = 20
slot_troop_player_debt         = 21
slot_troop_player_relation     = 22
#slot_troop_player_favor        = 23
slot_troop_last_quest          = 24
slot_troop_last_quest_betrayed = 25
slot_troop_last_persuasion_time= 26
slot_troop_last_comment_time   = 27
slot_troop_spawned_before      = 28

#Post 0907 changes begin
slot_troop_last_comment_slot   = 29
slot_troop_present_at_event    = 19
#Post 0907 changes end

slot_troop_spouse              = 30
slot_troop_father              = 31
slot_troop_mother              = 32
slot_troop_daughter            = 33
slot_troop_son                 = 34
slot_troop_sibling             = 35
slot_troop_lover               = 36

slot_troop_trainer_met                       = 30
slot_troop_trainer_waiting_for_result        = 31
slot_troop_trainer_training_fight_won        = 32
slot_troop_trainer_num_opponents_to_beat     = 33
slot_troop_trainer_training_system_explained = 34
slot_troop_trainer_opponent_troop            = 35
slot_troop_trainer_training_difficulty       = 36
slot_troop_trainer_training_fight_won        = 37


slot_troop_family_begin        = 30
slot_troop_family_end          = 36

slot_troop_enemy_1             = 40
slot_troop_enemy_2             = 41
slot_troop_enemy_3             = 42
slot_troop_enemy_4             = 43
slot_troop_enemy_5             = 44

slot_troop_enemies_begin       = 40
slot_troop_enemies_end         = 45

slot_troop_honorable          = 50
#slot_troop_merciful          = 51
slot_lord_reputation_type     		  = 52

slot_troop_change_to_faction          = 55
slot_troop_readiness_to_join_army     = 57
slot_troop_readiness_to_follow_orders = 58

# NPC-related constants

#NPC companion changes begin
slot_troop_first_encountered          = 59
slot_troop_home                       = 60

slot_troop_morality_state       = 61
tms_no_problem         = 0
tms_acknowledged       = 1
tms_dismissed          = 2

slot_troop_morality_type = 62
tmt_aristocratic = 1
tmt_egalitarian = 2
tmt_humanitarian = 3
tmt_honest = 4
tmt_pious = 5

slot_troop_morality_value = 63

slot_troop_2ary_morality_type  = 64
slot_troop_2ary_morality_state = 65
slot_troop_2ary_morality_value = 66

slot_troop_morality_penalties =  69 ### accumulated grievances from morality conflicts


slot_troop_personalityclash_object     = 71
#(0 - they have no problem, 1 - they have a problem)
slot_troop_personalityclash_state    = 72 #1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,
pclash_penalty_to_self  = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both  = 3
#(a string)
slot_troop_personalityclash2_object   = 73
slot_troop_personalityclash2_state    = 74

slot_troop_personalitymatch_object   =  75
slot_troop_personalitymatch_state   =  76

slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash

slot_troop_home_speech_delivered = 78

#NPC history slots

slot_troop_met_previously        = 80
slot_troop_turned_down_twice     = 81
slot_troop_playerparty_history   = 82

pp_history_scattered         = 1
pp_history_dismissed         = 2
pp_history_quit              = 3
pp_history_indeterminate     = 4

slot_troop_playerparty_history_string   = 83
slot_troop_return_renown        = 84

slot_troop_custom_banner_bg_color_1      = 85
slot_troop_custom_banner_bg_color_2      = 86
slot_troop_custom_banner_charge_color_1  = 87
slot_troop_custom_banner_charge_color_2  = 88
slot_troop_custom_banner_charge_color_3  = 89
slot_troop_custom_banner_charge_color_4  = 90
slot_troop_custom_banner_bg_type         = 91
slot_troop_custom_banner_charge_type_1   = 92
slot_troop_custom_banner_charge_type_2   = 93
slot_troop_custom_banner_charge_type_3   = 94
slot_troop_custom_banner_charge_type_4   = 95
slot_troop_custom_banner_flag_type       = 96
slot_troop_custom_banner_num_charges     = 97
slot_troop_custom_banner_positioning     = 98
slot_troop_custom_banner_map_flag_type   = 99

#conversation strings -- must be in this order!
slot_troop_intro 						= 101

slot_troop_intro_response_1 			= 102
slot_troop_intro_response_2 			= 103

slot_troop_backstory_a 					= 104
slot_troop_backstory_b 					= 105
slot_troop_backstory_c 					= 106

slot_troop_backstory_delayed 			= 107

slot_troop_backstory_response_1 		= 108
slot_troop_backstory_response_2 		= 109

slot_troop_signup   					= 110
slot_troop_signup_2 					= 111

slot_troop_signup_response_1 			= 112
slot_troop_signup_response_2 			= 113

slot_troop_mentions_payment 			= 114 #Not actually used
slot_troop_payment_response 			= 115 #Not actually used
slot_troop_morality_speech   			= 116
slot_troop_2ary_morality_speech 		= 117
slot_troop_personalityclash_speech 		= 118
slot_troop_personalityclash_speech_b 	= 119
slot_troop_personalityclash2_speech 	= 120
slot_troop_personalityclash2_speech_b 	= 121
slot_troop_personalitymatch_speech 		= 122
slot_troop_personalitymatch_speech_b 	= 123
slot_troop_retirement_speech 			= 124
slot_troop_rehire_speech 				= 125
slot_troop_home_intro           		= 126
slot_troop_home_description    			= 127
slot_troop_home_description_2 			= 128
slot_troop_home_recap         			= 129
slot_troop_honorific   					= 130
slot_troop_strings_end = 131
slot_troop_payment_request = 132

#Rebellion changes begin
slot_troop_discussed_rebellion = 140
slot_troop_support_base = 141

#OiM troop slots

slot_troop_support_hero = 142
slot_troop_weapon_backup = 143
slot_troop_weapon_to_remove = 144
slot_troop_is_studing = 145
slot_troop_studing_profile = 146
slot_troop_studing_count = 147
slot_troop_studing_war = 148
slot_troop_studing_medicine = 149
slot_troop_studing_war_work = 150
#oim tavern slots
#uses range 85-99
#oim_duels_cnt
#oim_simple_fights group
#oim_ranged_fights_group

slot_troop_duels_count = 171
slot_troop_simple_fights_count = 172
slot_troop_ranged_fights_count = 173
slot_troop_alcohol_count = 174
slot_troop_rich_people_cought = 175
slot_troop_last_duel_time = 176
slot_troop_fights_count = 177

#Number of routed agents after battle ends.
slot_troop_player_routed_agents                 = 178
slot_troop_ally_routed_agents                   = 179
slot_troop_enemy_routed_agents                  = 180

slot_troop_mp_squad_price                       = 181
slot_troop_mp_squad_type                        = 182
#slot_troop_upgrade_cost                  = 181
#slot_troop_upgrade_exp                  = 182



tro_failed_to_join_army                    = 1
tro_failed_to_support_colleague            = 2

#CONTROVERSY
#This is used to create a more "rational choice" model of faction politics, in which lords pick fights with other lords for gain, rather than simply because of clashing personalities
#It is intended to be a limiting factor for players and lords in their ability to intrigue against each other. It represents the embroilment of a lord in internal factional disputes. In contemporary media English, a lord with high "controversy" would be described as "embattled."
#The main effect of high controversy is that it disqualifies a lord from receiving a fief or an appointment
#It is a key political concept because it provides incentive for much of the political activity. For example, Lord Red Senior is worried that his rival, Lord Blue Senior, is going to get a fied which Lord Red wants. So, Lord Red turns to his protege, Lord Orange Junior, to attack Lord Blue in public. The fief goes to Lord Red instead of Lord Blue, and Lord Red helps Lord Orange at a later date.


slot_troop_will_join_prison_break      = 161

slot_troop_last_recruting_time = 162

troop_slots_reserved_for_relations_start        = 165 #this is based on id_troops, and might change

slot_troop_relations_begin				= 0 #this creates an array for relations between troops
											#Right now, lords start at 165 and run to around 290, including pretenders
											
											
											
########################################################
##  PLAYER SLOTS           #############################
########################################################

slot_player_spawned_this_round                 = 0
slot_player_last_rounds_used_item_earnings     = 1
slot_player_selected_item_indices_begin        = 2
slot_player_selected_item_indices_end          = 11
slot_player_cur_selected_item_indices_begin    = slot_player_selected_item_indices_end
slot_player_cur_selected_item_indices_end      = slot_player_selected_item_indices_end + 9
slot_player_join_time                          = 21
slot_player_button_index                       = 22 #used for presentations
slot_player_can_answer_poll                    = 23
slot_player_first_spawn                        = 24
slot_player_spawned_at_siege_round             = 25
slot_player_poll_disabled_until_time           = 26
slot_player_total_equipment_value              = 27
slot_player_last_team_select_time              = 28
slot_player_death_pos_x                        = 29
slot_player_death_pos_y                        = 30
slot_player_death_pos_z                        = 31
slot_player_damage_given_to_target_1           = 32 #used only in destroy mod
slot_player_damage_given_to_target_2           = 33 #used only in destroy mod
slot_player_last_bot_count                     = 34
slot_player_bot_type_1_wanted                  = 35
slot_player_bot_type_2_wanted                  = 36
slot_player_bot_type_3_wanted                  = 37
slot_player_bot_type_4_wanted                  = 38
slot_player_spawn_count                        = 39
slot_player_captain_bot_data_begin             = 40
slot_player_captain_bot_data_end               = slot_player_captain_bot_data_begin + 12 # there are 12 bot types for each faction
slot_player_reload_disabled_until_time           = 99
slot_player_warcry_cooldown = 100
slot_player_warcry_active_time = 101


#Illuminati

slot_player_experience = 80 #his experience
slot_player_level = 81 #his level
slot_player_this_game_points = 82 #is the value which gives players ability to play hero
slot_player_this_round_points = 83 #is the value which calculates earnings | 1 = kill - 2 = capture - 3 = hero kill - 2 = win - loose = 1   ###   players*points = gold
slot_player_experience_to_next_level = 84 #is the amount of EXP which is needed to level up
slot_player_this_round_kills = 85
slot_player_this_round_deaths = 86
slot_player_data_was_loaded = 87
slot_player_data_troop_id = 88

slot_player_we1 = 89
slot_player_we2 = 90
slot_player_we3 = 91
slot_player_we4 = 92
slot_player_head = 93
slot_player_body = 94
slot_player_foot = 95
slot_player_gloves = 96
slot_player_horse = 97
slot_player_equip_end = 98

information_chat_color                      = 0xFFFFDD8A
important_chat_color                = 0xFFFF8C27
admin_chat_color                      = 0xFFFF00FF

#Illuminati

########################################################
##  TEAM SLOTS             #############################
########################################################

slot_team_flag_situation                       = 0




#Rebellion changes end
# character backgrounds
cb_noble = 1
cb_merchant = 2
cb_guard = 3
cb_forester = 4
cb_nomad = 5
cb_thief = 6
cb_priest = 7

cb2_page = 0
cb2_apprentice = 1
cb2_urchin  = 2
cb2_steppe_child = 3
cb2_merchants_helper = 4

cb3_poacher = 3
cb3_craftsman = 4
cb3_peddler = 5
cb3_troubadour = 7
cb3_squire = 8
cb3_lady_in_waiting = 9
cb3_student = 10

cb4_revenge = 1
cb4_loss    = 2
cb4_wanderlust =  3
cb4_disown  = 5
cb4_greed  = 6

#NPC system changes end
#Encounter types
enctype_fighting_against_village_raid = 1
enctype_catched_during_village_raid   = 2


### Troop occupations slot_troop_occupation
##slto_merchant           = 1
slto_kingdom_hero       = 2
slto_player_companion   = 3
slto_kingdom_lady       = 4
slto_kingdom_seneschal  = 5
slto_robber_knight      = 6

stl_unassigned          = -1
stl_reserved_for_player = -2
stl_rejected_by_player  = -3

#NPC changes begin
slto_retirement      = 11
slto_at_univesity    = 12
#slto_retirement_medium    = 12
#slto_retirement_short     = 13
#NPC changes end

########################################################
##  QUEST SLOTS            #############################
########################################################

slot_quest_target_center            = 1
slot_quest_target_troop             = 2
slot_quest_target_faction           = 3
slot_quest_object_troop             = 4
##slot_quest_target_troop_is_prisoner = 5
slot_quest_giver_troop              = 6
slot_quest_object_center            = 7
slot_quest_target_party             = 8
slot_quest_target_party_template    = 9
slot_quest_target_amount            = 10
slot_quest_current_state            = 11
slot_quest_giver_center             = 12
slot_quest_target_dna               = 13
slot_quest_target_item              = 14
slot_quest_object_faction           = 15

slot_quest_convince_value           = 19
slot_quest_importance               = 20
slot_quest_xp_reward                = 21
slot_quest_gold_reward              = 22
slot_quest_expiration_days          = 23
slot_quest_dont_give_again_period   = 24
slot_quest_dont_give_again_remaining_days = 25
#OiM code 
slot_quest_start_time = 26
slot_quest_is_active = 27
slot_quest_buy_price = 28


########################################################
##  PARTY TEMPLATE SLOTS   #############################
########################################################

# Ryan BEGIN
slot_party_template_num_killed   = 1
# Ryan END


########################################################
##  SCENE PROP SLOTS       #############################
########################################################

scene_prop_open_or_close_slot       = 1
scene_prop_smoke_effect_done        = 2
scene_prop_number_of_agents_pushing = 3 #for belfries only
scene_prop_next_entry_point_id      = 4 #for belfries only
scene_prop_belfry_platform_moved    = 5 #for belfries only
scene_prop_slots_end                = 6

########################################################
rel_enemy   = 0
rel_neutral = 1
rel_ally    = 2


#Talk contexts
tc_town_talk                  = 0
tc_court_talk   	      	  = 1
tc_party_encounter            = 2
tc_castle_gate                = 3
tc_siege_commander            = 4
tc_join_battle_ally           = 5
tc_join_battle_enemy          = 6
tc_castle_commander           = 7
tc_hero_freed                 = 8
tc_hero_defeated              = 9
tc_entering_center_quest_talk = 10
tc_back_alley                 = 11
tc_siege_won_seneschal        = 12
tc_ally_thanks                = 13
tc_tavern_talk                = 14
tc_rebel_thanks               = 15
tc_bandit_talk                = 16

#Troop Commentaries begin
#Log entry types
#civilian
logent_village_raided            = 1
logent_village_extorted          = 2
logent_caravan_accosted          = 3
logent_helped_peasants           = 4 

logent_castle_captured_by_player              = 10
logent_lord_defeated_by_player                = 11
logent_lord_captured_by_player                = 12
logent_lord_defeated_but_let_go_by_player     = 13
logent_player_defeated_by_lord                = 14
logent_player_retreated_from_lord             = 15
logent_player_retreated_from_lord_cowardly    = 16
logent_lord_helped_by_player                  = 17
logent_player_participated_in_siege           = 18
logent_player_participated_in_major_battle    = 19

logent_pledged_allegiance          = 21
logent_fief_granted_village      = 22
logent_renounced_allegiance      = 23 

logent_game_start                           = 31 
logent_poem_composed                        = 32 ##Not added
logent_tournament_distinguished             = 33 ##Not added
logent_tournament_won                       = 34 ##Not added


#lord reputation type, for commentaries
#"Martial" will be twice as common as the other types
lrep_none           = 0 
lrep_martial        = 1 #chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
lrep_quarrelsome   = 2 #spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, Shakespeare's Richard III
lrep_selfrighteous = 3 #coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he borders on upstanding)
lrep_cunning        = 4 #coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
lrep_debauched     = 5 #spiteful, amoral, sadistic, - eg Caligula, Tuchman's Charles of Navarre
lrep_goodnatured   = 6 #chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein, poss Ranjit Singh (although roguish), Humayun
lrep_upstanding    = 7 #moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Sher Shah Suri

#Troop Commentaries end

#Walker types: 
walkert_default            = 0
walkert_needs_money        = 1
walkert_needs_money_helped = 2
walkert_spy                = 3
num_town_walkers = 8
town_walker_entries_start = 32

reinforcement_cost            = 400

merchant_toll_duration        = 72 #Tolls are valid for 72 hours

hero_escape_after_defeat_chance = 80


raid_distance = 4

surnames_begin = "str_surname_1"
surnames_end = "str_surnames_end"
names_begin = "str_name_1"
names_end = surnames_begin
countersigns_begin = "str_countersign_1"
countersigns_end = names_begin
secret_signs_begin = "str_secret_sign_1"
secret_signs_end = countersigns_begin

kingdoms_begin = "fac_player_supporters_faction"
kingdoms_end = "fac_kingdoms_end"

npc_kingdoms_begin = "fac_kingdom_1"
npc_kingdoms_end = kingdoms_end

kingdom_ladies_begin = "trp_knight_1_1_wife"
kingdom_ladies_end = "trp_heroes_end"



kings_begin = "trp_kingdom_1_lord"
kings_end = "trp_knight_1_1"

kingdom_heroes_begin = "trp_kingdom_1_lord"
kingdom_heroes_end = kingdom_ladies_begin

heroes_begin = kingdom_heroes_begin
heroes_end = kingdom_ladies_end

companions_begin = "trp_npc1"
companions_end = "trp_kingdom_heroes_including_player_begin"

soldiers_begin = "trp_farmer"
soldiers_end = "trp_town_walker_1"

#Rebellion changes

##rebel_factions_begin = "fac_kingdom_1_rebels"
##rebel_factions_end =   "fac_kingdoms_end"

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = kingdom_heroes_end
#Rebellion changes

tavern_minstrels_begin = "trp_tavern_minstrel_1"
tavern_minstrels_end   = companions_begin

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end   = tavern_minstrels_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end   = tavern_booksellers_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end   = tavern_travelers_begin

mercenary_troops_begin = "trp_watchman"
mercenary_troops_end = "trp_mercenaries_end"

multiplayer_troops_begin = "trp_swadian_crossbowman_multiplayer"
multiplayer_troops_end = "trp_multiplayer_end"

multiplayer_ai_troops_begin = "trp_swadian_crossbowman_multiplayer_ai"
multiplayer_ai_troops_end   = multiplayer_troops_begin

captain_multiplayer_troops_begin = "trp_mp_swadian_militia"
captain_multiplayer_troops_end = "trp_new_multiplayer_troops_end"

captain_multiplayer_new_troops_begin = "trp_mp_rhodok_trained_spearman"
captain_multiplayer_new_troops_end = "trp_coop_moscovite_watchmen"

captain_multiplayer_coop_new_troops_begin = "trp_coop_moscovite_watchmen"
captain_multiplayer_coop_new_troops_end = "trp_coop_troops_end"

multiplayer_scenes_begin = "scn_multi_scene_1"
multiplayer_scenes_end = "scn_multiplayer_maps_end"

multiplayer_new_scenes_begin = "scn_mp_new_1"
multiplayer_new_scenes_end = "scn_mp_new_4"

multiplayer_scene_names_begin = "str_multi_scene_1"
multiplayer_scene_names_end = "str_multi_scene_end"

multiplayer_new_scene_names_begin = "str_mp_new_1"
multiplayer_new_scene_names_end = "str_mp_new_end"

multiplayer_flag_projections_begin = "mesh_flag_project_nd"
multiplayer_flag_projections_end = "mesh_flag_projects_end"

multiplayer_flag_taken_projections_begin = "mesh_flag_project_nd_miss"
multiplayer_flag_taken_projections_end = "mesh_flag_project_misses_end"

multiplayer_game_type_names_begin = "str_multi_game_type_1"
multiplayer_game_type_names_end = "str_multi_game_types_end"

quick_battle_troops_begin = "trp_quick_battle_troop_1"
quick_battle_troops_end = "trp_quick_battle_troops_end"

quick_battle_troop_texts_begin = "str_quick_battle_troop_1"
quick_battle_troop_texts_end = "str_quick_battle_troops_end"

quick_battle_scenes_begin = "scn_quick_battle_scene_1"
quick_battle_scenes_end = "scn_quick_battle_maps_end"

quick_battle_scene_images_begin = "mesh_cb_ui_maps_scene_01"

quick_battle_battle_scenes_begin = quick_battle_scenes_begin
quick_battle_battle_scenes_end = "scn_quick_battle_scene_4"

quick_battle_siege_scenes_begin = quick_battle_battle_scenes_end
quick_battle_siege_scenes_end = quick_battle_scenes_end

quick_battle_scene_names_begin = "str_quick_battle_scene_1"

lord_quests_begin = "qst_deliver_message"
lord_quests_end   = "qst_follow_army"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end   = lord_quests_end

village_elder_quests_begin = "qst_deliver_grain"
village_elder_quests_end = "qst_eliminate_bandits_infesting_village"

mayor_quests_begin  = "qst_move_cattle_herd"
mayor_quests_end    = village_elder_quests_begin

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end   = mayor_quests_begin

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end   = lady_quests_begin

all_items_begin = 0
all_items_end = "itm_items_end"

all_quests_begin = 0
all_quests_end = "qst_quests_end"

towns_begin = "p_town_1"
castles_begin = "p_castle_1"
villages_begin = "p_village_1"

towns_end = castles_begin
castles_end = villages_begin
villages_end   = "p_salt_mine"

walled_centers_begin = towns_begin
walled_centers_end   = castles_end

centers_begin = towns_begin
centers_end   = villages_end

training_grounds_begin   = "p_training_ground_1"
training_grounds_end     = "p_Bridge_1"

scenes_begin = "scn_town_1_center"
scenes_end = "scn_castle_1_exterior"

spawn_points_begin = "p_zendar"
spawn_points_end = "p_spawn_points_end"

regular_troops_begin       = "trp_novice_fighter"
regular_troops_end         = "trp_tournament_master"

swadian_merc_parties_begin = "p_town_1_mercs"
swadian_merc_parties_end   = "p_town_8_mercs"

vaegir_merc_parties_begin  = "p_town_8_mercs"
vaegir_merc_parties_end    = "p_zendar"

arena_masters_begin    = "trp_town_1_arena_master"
arena_masters_end      = "trp_town_1_armorer"

training_gound_trainers_begin    = "trp_trainer_1"
training_gound_trainers_end      = "trp_ransom_broker_1"

town_walkers_begin = "trp_rich_baba_pol"
town_walkers_end = "trp_village_walker_1"

village_walkers_begin = "trp_rich_baba_pol"
village_walkers_end   = "trp_spy_walker_1"

spy_walkers_begin = "trp_spy_walker_1"
spy_walkers_end = "trp_tournament_master"

walkers_begin = town_walkers_begin
walkers_end   = spy_walkers_end

armor_merchants_begin  = "trp_town_1_armorer"
armor_merchants_end    = "trp_town_1_weaponsmith"

weapon_merchants_begin = "trp_town_1_weaponsmith"
weapon_merchants_end   = "trp_town_1_tavernkeeper"

tavernkeepers_begin    = "trp_town_1_tavernkeeper"
tavernkeepers_end      = "trp_town_1_merchant"

goods_merchants_begin  = "trp_town_1_merchant"
goods_merchants_end    = "trp_town_1_horse_merchant"

horse_merchants_begin  = "trp_town_1_horse_merchant"
horse_merchants_end    = "trp_town_1_mayor"

mayors_begin           = "trp_town_1_mayor"
mayors_end             = "trp_village_1_elder"

village_elders_begin   = "trp_village_1_elder"
village_elders_end     = "trp_merchants_end"

num_max_items = 10000 #used for multiplayer mode

average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

village_prod_min = -5
village_prod_max = 25

trade_goods_begin = "itm_spice"
trade_goods_end = "itm_siege_supply"
food_begin = "itm_wine"
food_end = "itm_siege_supply"
reference_books_begin = "itm_book_wound_treatment_reference"
reference_books_end   = trade_goods_begin
readable_books_begin = "itm_book_tactics"
readable_books_end   = reference_books_begin
books_begin = readable_books_begin
books_end = reference_books_end
horses_begin = "itm_sumpter_horse"
horses_end = "itm_arrows"
weapons_begin = "itm_wooden_stick"
weapons_end = "itm_wooden_shield"
ranged_weapons_begin = "itm_jarid"
ranged_weapons_end = "itm_torch"
armors_begin = "itm_leather_gloves"
armors_end = "itm_wooden_stick"
shields_begin = "itm_wooden_shield"
shields_end = "itm_jarid"

# Banner constants

banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end_minus_one = "mesh_banner_f21"

arms_meshes_begin = "mesh_arms_a01"
arms_meshes_end_minus_one = "mesh_arms_f21"

custom_banner_charges_begin = "mesh_custom_banner_charge_01"
custom_banner_charges_end = "mesh_tableau_mesh_custom_banner"

custom_banner_backgrounds_begin = "mesh_custom_banner_bg"
custom_banner_backgrounds_end = custom_banner_charges_begin

custom_banner_flag_types_begin = "mesh_custom_banner_01"
custom_banner_flag_types_end = custom_banner_backgrounds_begin

custom_banner_flag_map_types_begin = "mesh_custom_map_banner_01"
custom_banner_flag_map_types_end = custom_banner_flag_types_begin

custom_banner_flag_scene_props_begin = "spr_custom_banner_01"
custom_banner_flag_scene_props_end = "spr_banner_a"

custom_banner_map_icons_begin = "icon_custom_banner_01"
custom_banner_map_icons_end = "icon_banner_01"

banner_map_icons_begin = "icon_banner_01"
banner_map_icons_end_minus_one = "icon_banner_126"

banner_scene_props_begin = "spr_banner_a"
banner_scene_props_end_minus_one = "spr_banner_f21"

khergit_banners_begin_offset = 63
khergit_banners_end_offset = 84

# Some constants for merchant invenotries
merchant_inventory_space = 30
num_merchandise_goods = 40

num_max_river_pirates = 25
num_max_zendar_peasants = 25
num_max_zendar_manhunters = 10

num_max_dp_bandits = 10
num_max_refugees = 10
num_max_deserters = 10

num_max_militia_bands = 15
num_max_armed_bands = 12

num_max_vaegir_punishing_parties = 20
num_max_rebel_peasants = 25

num_max_frightened_farmers = 50
num_max_undead_messengers  = 20

num_forest_bandit_spawn_points = 1
num_mountain_bandit_spawn_points = 1
num_steppe_bandit_spawn_points = 1
num_black_khergit_spawn_points = 1
num_sea_raider_spawn_points = 2

peak_prisoner_trains = 4
peak_kingdom_caravans = 12
peak_kingdom_messengers = 3


# Note positions
note_troop_location = 3

#battle tactics
btactic_hold = 1
btactic_follow_leader = 2
btactic_charge = 3
btactic_stand_ground = 4

#default right mouse menu orders
cmenu_move = -7
cmenu_follow = -6

# Town center modes
tcm_default 		= 0
tcm_disguised 		= 1

# Arena battle modes
#abm_fight = 0
abm_training = 1
abm_visit = 2
abm_tournament = 3

# Camp training modes
ctm_melee    = 1
ctm_ranged   = 2
ctm_mounted  = 3
ctm_training = 4

# Village bandits attack modes
vba_normal          = 1
vba_after_training  = 2

arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 5
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 10
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 25
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 60
arena_grand_prize = 250


#oim consts
oim_tavern_visitors_begin = "trp_oim_tavern_visitor_rp"
oim_tavern_visitors_end = "trp_eleonora"

oim_pol_begin = "trp_swadian_recruit"
oim_pol_end = "trp_vaegir_recruit"

oim_mos_begin = "trp_vaegir_recruit"
oim_mos_end = "trp_khergit_tribesman"

oim_tat_begin = "trp_khergit_tribesman"
oim_tat_end = "trp_nord_recruit"

oim_shv_begin = "trp_nord_recruit"
oim_shv_end = "trp_rhodok_tribesman"

oim_koz_begin = "trp_rhodok_tribesman"
oim_koz_end = "trp_looter"

tatar_nation = 0
kozak_nation = 1
polyak_nation = 2
shved_nation = 3
moskov_nation = 4

nation_begin = 0
nation_end = 5

merch_begin = "trp_tatar_merch_novice_infantry"
merch_capitan_begin = "trp_mercanary_captain_tatars"

merch_str_begin = "str_merch_t_1"

#Expanded management system -begin
	#MS Description slots -begin
slot_ms_short_descr_fac1              = 0
slot_ms_short_descr_fac2              = 1
slot_ms_short_descr_fac3              = 2
slot_ms_short_descr_fac4              = 3
slot_ms_short_descr_fac5              = 4

slot_ms_long_descr_fac1               = 5
slot_ms_long_descr_fac2               = 6
slot_ms_long_descr_fac3               = 7
slot_ms_long_descr_fac4               = 8
slot_ms_long_descr_fac5               = 9

slot_ms_remour_descr_fac1             = 10
slot_ms_remour_descr_fac2             = 11
slot_ms_remour_descr_fac3             = 12
slot_ms_remour_descr_fac4             = 13
slot_ms_remour_descr_fac5             = 14
	#MS Description slots -end

	#MS Parameter slots -begin
slot_ms_construct_requirements        = 15
slot_ms_construct_requirements_p1     = 16
slot_ms_construct_requirements_p2     = 17
slot_ms_construct_requirements_p3     = 18
slot_ms_ai_requirements               = 19
slot_ms_ai_requirements_p1            = 20
slot_ms_ai_requirements_p2            = 21
slot_ms_ai_requirements_p3            = 22
slot_ms_ai_priority                   = 23

slot_ms_price                         = 24
slot_ms_construct_time                = 25
slot_ms_additional_menu               = 26
slot_ms_additional_menu_p1            = 27
	#MS Parameter slots -end

	#MS Flag slots -begin
slot_ms_was_used                      = 28
	#MS Flag slots -end	
	#MS Event triger slots -begin
slot_ms_script_after_construct        = 29
slot_ms_script_after_construct_p1     = 30
slot_ms_script_after_construct_p2     = 31
slot_ms_script_after_construct_p3     = 32	
slot_ms_script_after_construct_p4     = 33
slot_ms_script_after_construct_p5     = 34
slot_ms_script_after_construct_p6     = 35

slot_ms_script_before_attack          = 36
slot_ms_script_before_attack_p1       = 37
slot_ms_script_before_attack_p2       = 38
slot_ms_script_before_attack_p3       = 39

slot_ms_script_looted                 = 40
slot_ms_script_looted_p1              = 41
slot_ms_script_looted_p2              = 42
slot_ms_script_looted_p3              = 43

slot_ms_script_captured               = 44
slot_ms_script_captured_p1            = 45
slot_ms_script_captured_p2            = 46
slot_ms_script_captured_p3            = 47

slot_ms_script_unsieged               = 48
slot_ms_script_unsieged_p1            = 49
slot_ms_script_unsieged_p2            = 50
slot_ms_script_unsieged_p3            = 51
	#MS Event triger slots -end
	
	#MS Officer slots -begin
slot_ms_officer_lower_level_count        = 52
slot_ms_officer_kostyak_count            = 53
slot_ms_officer_elementar_cavalry_count  = 54
slot_ms_officer_elite_infantry_count     = 55
slot_ms_officer_elite_cavalry_count      = 56
slot_ms_officer_uniq_count               = 57
slot_ms_officer_region_count             = 58
slot_ms_officer_militiaman_count         = 59
slot_ms_officer_mercenary_count          = 60

slot_ms_officer_lower_level_time        = 61
slot_ms_officer_kostyak_time            = 62
slot_ms_officer_elementar_cavalry_time  = 63
slot_ms_officer_elite_infantry_time     = 64
slot_ms_officer_elite_cavalry_time      = 65
slot_ms_officer_uniq_time               = 66
slot_ms_officer_region_time             = 67
slot_ms_officer_militiaman_time         = 68
slot_ms_officer_mercenary_time          = 69
	#MS Officer slots -end
	
	#MS Time triger slots -begin
slot_ms_script_24_hour                = 70
slot_ms_script_24_hour_p1             = 71
slot_ms_script_24_hour_p2             = 72
slot_ms_script_24_hour_p3             = 73
slot_ms_script_24_hour_p4             = 74
slot_ms_script_24_hour_p5             = 75

slot_ms_script_7_day                  = 76
slot_ms_script_7_day_p1               = 77
slot_ms_script_7_day_p2               = 78
slot_ms_script_7_day_p3               = 79
slot_ms_script_7_day_p4               = 80
slot_ms_script_7_day_p5               = 81

slot_ms_script_30_day                 = 82
slot_ms_script_30_day_p1              = 83
slot_ms_script_30_day_p2              = 84
slot_ms_script_30_day_p3              = 85
slot_ms_script_30_day_p4              = 86
slot_ms_script_30_day_p5              = 87
slot_ms_script_30_day_p6              = 88
slot_ms_script_30_day_p7              = 89
	#MS Time triger slots -end
	
	#MS Party constants -begin
ms_party_has_element_start_slot       = slot_ms_script_30_day_p7 + 1
ms_flag_none                   = 0
ms_flag_deposit                = 1
ms_flag_credit                 = 2
ms_flag_medicine               = 0
ms_flag_war_work               = 1
ms_flag_war_prepare            = 2
ms_flag_short                  = 0
ms_flag_long                   = 1
ms_flag_remour                 = 2
ms_flag_building               = 0
ms_flag_upgrade                = 1
ms_flag_already_was_used       = 1
ms_flag_empty                  = 0
ms_flag_is_building            = 1
ms_flag_already_builded        = 2
ms_flag_temporary_inactive     = 3
ms_flag_all                    = 0
ms_flag_horsed                 = 1
ms_flag_infantry               = 0
ms_flag_cavalry                = 1
ms_flag_lower_lewel_1          = 0
ms_flag_lower_lewel_2          = 1
ms_flag_lower_lewel_3          = 2
ms_flag_kostyak_1              = 3
ms_flag_kostyak_2              = 4
ms_flag_kostyak_3              = 5
ms_flag_elementar_cavalry_1    = 6
ms_flag_elementar_cavalry_2    = 7
ms_flag_elementar_cavalry_3    = 8
ms_flag_elite_infantry_1       = 9
ms_flag_elite_infantry_2       = 10
ms_flag_elite_infantry_3       = 11
ms_flag_elite_cavalry_1        = 12
ms_flag_elite_cavalry_2        = 13
ms_flag_elite_cavalry_3        = 14
ms_flag_uniq_1                 = 15
ms_flag_uniq_2                 = 16
ms_flag_uniq_3                 = 17 
ms_flag_region_1               = 18
ms_flag_region_2               = 19
ms_flag_region_3               = 20
ms_flag_militiaman_1           = 21
ms_flag_militiaman_2           = 22
ms_flag_militiaman_3           = 23
ms_flag_mercenary_1            = 24
ms_flag_mercenary_2            = 25
ms_flag_mercenary_3            = 26
ms_flag_troop_none             = 0
ms_flag_troop_infantry         = 1
ms_flag_troop_cavalry          = 2
ms_flag_troop_elite_infantry   = 3
ms_flag_troop_elite_cavalry    = 4
ms_flag_troop_mercenary_infantry = 5
ms_flag_troop_mercenary_cavalry  = 6
ms_flag_troop_uniq             = 7
slot_ms_inf_limit              = 0
slot_ms_kav_limit              = 1
slot_ms_elit_limit             = 2
slot_ms_merc_limit             = 3
slot_ms_inf_chance_factor      = 4
slot_ms_cav_chance_factor      = 5
slot_ms_elit_chance_factor     = 6
slot_ms_merc_chance_factor     = 7
slot_ms_officer_troops_start   = 8
ms_flag_simple                 = 0
ms_flag_random                 = 1
ms_flag_with_element_name      = 3
ms_towns_number                = 58
ms_villages_number             = 90
ms_parties_start               = towns_begin
ms_towns_elements_start        = "trp_town_building_arsenal"
ms_towns_upgrade_start         = "trp_town_upgrade_armourer"
ms_village_elements_start      = "trp_village_building_mill"
ms_village_upgrade_start       = "trp_village_upgrade_judge"
ms_elenents_start              = ms_towns_elements_start
ms_elements_end                = "trp_ms_end"
ms_towns_elements_end          = ms_towns_upgrade_start
ms_village_upgrade_end         = ms_elements_end
ms_village_elements_end        = ms_village_upgrade_start
ms_towns_upgrade_end           = ms_village_elements_start
ms_descr_strings_start         = "str_ms_t_arsenal_short_descr_fac1"
ms_time_to_build_start_slot    = ms_party_has_element_start_slot + ms_towns_number + ms_villages_number
	#MS Party constants -end
#Expanded management system -end

flag_mounted = 0
flag_ranged = 1
flag_horse_archer = 2


flag_no = 0
flag_choose = 1
flag_notify = 2

ambassador_start = "trp_polsk_ambassador"

flag_peace = 0
flag_war = 1
flag_trade = 2

flag_give_one_town = 0
flag_give_two_town = 1
flag_give_nothing = 2
flag_give_money = 3

castle_mayors_begin = "trp_castle_1_elder"
castle_mayors_end = "trp_town_1_trade_guild_master"

granades_begin = "itm_granata"
granades_end = "itm_luk"

tutorial_fighters_begin = "trp_tutorial_fighter_1"
tutorial_fighters_end   = "trp_tutorial_archer_1"

#sound 

#all_orders_begin = snd_order_all_back_10
#archer_oders_shift = snd_order_archers_back_10 - all_orders_begin
#infantry_oders_shift = snd_order_infantry_back_10 - all_orders_begin
#cavalry_oders_shift = snd_order_cavalry_back_10 - all_orders_begin
#inf_cav_oders_shift = snd_order_inf_cav_back_10 - all_orders_begin
#inf_arch_oders_shift = snd_order_inf_arch_back_10 - all_orders_begin
#arch_cav_oders_shift = snd_order_cav_arch_back_10 - all_orders_begin

#incom multipliers

tax_town_multiplier    = 7
tax_castle_multiplier  = 14
tax_village_multiplier = 6

time_multiplier    = 1
debug_mode = 0
town_assault_chanse = 20
oim_mp_troop_begin = "trp_mp_swadian_militia"
oim_mp_troop_end = "trp_nurse"
multiplayer_granade_damage_to_scene_prop_ex = 17
is_steam_version = 0
oim_horses_begin = "itm_very_bad_horse"
oim_horses_end = "itm_bad_arrows"
time_force_rethink = 2
tw_verision = 1 

#NORMAL ACHIEVEMENTS
ACHIEVEMENT_FIRST_STEPS = 1,
ACHIEVEMENT_DRESS_UP = 2,
ACHIEVEMENT_LETS_TAKE_THIS_OUTSIDE = 3,
ACHIEVEMENT_NA_ZDOROVIE = 4,
ACHIEVEMENT_HUNKER_DOWN = 5,
ACHIEVEMENT_WHEELER_DEALER = 6,
ACHIEVEMENT_TRADER = 7,
ACHIEVEMENT_GREAT_TRADER = 8,
ACHIEVEMENT_VELVET_COMMANDER = 9,
ACHIEVEMENT_SUMMER_FEST = 10,
ACHIEVEMENT_KNOCK_KNOCK = 11,
ACHIEVEMENT_CITY_PLANNER = 12,
ACHIEVEMENT_DONT_DIE_OF_DYSENTERY = 13,
ACHIEVEMENT_BLACK_MACE = 14,
ACHIEVEMENT_POLISH_DRAMA = 15,
ACHIEVEMENT_GRAND_TZAR = 16,
ACHIEVEMENT_RETURN_OF_THE_HORDE = 17,
ACHIEVEMENT_SWEDISH_SCOURGE = 18,
ACHIEVEMENT_POWER_SHIFT = 19,
ACHIEVEMENT_BOMBERMAN = 20,
ACHIEVEMENT_LOCK_STOCK_AND_3_SMOKING_BARRELS = 21,
