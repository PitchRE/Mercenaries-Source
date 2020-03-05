python process_init.py
python process_global_variables.py
python process_strings.py
python process_skills.py
python process_music.py
python process_animations.py
python process_meshes.py
python process_sounds.py
python process_skins.py
python process_map_icons.py
python process_factions.py
python process_items.py
python process_scenes.py
python process_troops.py
python process_particle_sys.py
python process_scene_props.py
python process_tableau_materials.py
python process_presentations.py
python process_party_tmps.py
python process_parties.py
python process_quests.py
python process_info_pages.py
python process_scripts.py
python process_mission_tmps.py
python process_game_menus.py
python process_simple_triggers.py
python process_dialogs.py
python process_global_variables_unused.py
python process_postfx.py
rm *.pyc


cd '/home/pitch/Desktop/Mercenaries Project/MS/compiled'
cp *.txt '/home/pitch/.local/share/Steam/steamapps/common/Mount & Blade With Fire and Sword/Modules/Mercenaries/'
cp *.txt '/home/pitch/Desktop/Mercenaries Project/Server/Modules/Mercenaries/'
echo Updated Server Files.
echo Updated Client Files.
echo Compiling was successful!
