import random as rand
import streamlit as st

# used chatgpt to get links to all of the images in the PKMIMAGE dict and
# create the NEW_POKEMONS as well as NEW_MOVES dict
# which are required for the evolution of many of the orginally given pokemon

PKMIMAGE = {
    'Pikachu': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png',
    'Charizard': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png',
    'Squirtle': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png',
    'Jigglypuff': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png',
    'Gengar': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png',
    'Magnemite': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/81.png',
    'Bulbasaur': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png',
    'Charmander': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png',
    'Beedrill': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/15.png',
    'Golem': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/76.png',
    'Dewgong': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/87.png',
    'Hypno': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/97.png',
    'Cleffa': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/173.png',
    'Cutiefly': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/742.png',
    'Raichu': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/26.png',
    'Charmeleon': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/5.png',
    'Wartortle': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/8.png',
    'Blastoise': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png',
    'Wigglytuff': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/40.png',
    'Gastly': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/92.png',
    'Haunter': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/93.png',
    'Magneton': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/82.png',
    'Ivysaur': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/2.png',
    'Venusaur': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/3.png',
    'Weedle': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/13.png',
    'Kakuna': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/14.png',
    'Geodude': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/74.png',
    'Graveler': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/75.png',
    'Seel': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/86.png',
    'Drowzee': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/96.png',
    'Clefairy': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/35.png',
    'Clefable': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/36.png'
}


POKEMONS = {
    'Pikachu': {'Type': ['Electric'], 'HP': 35, 'Moves': ['Thunder Shock', 'Double Kick', 'Thunderbolt'], 'Attack': 55, 'Defense': 40, 'Speed': 90, 'evo_path': ['Raichu']},
    'Charizard': {'Type': ['Fire', 'Flying'], 'HP': 78, 'Moves': ['Crunch', 'Ember', 'Scratch', 'Wing Attack'], 'Attack': 84, 'Defense': 78, 'Speed': 100, 'evo_path': None},
    'Squirtle': {'Type': ['Water'], 'HP': 44, 'Moves': ['Tackle', 'Bubble', 'Bite'], 'Attack': 48, 'Defense': 65, 'Speed': 43, 'evo_path': ['Wartortle']},
    'Jigglypuff': {'Type': ['Normal', 'Fairy'], 'HP': 115, 'Moves': ['Pound', 'Body Slam', 'Double Slap'], 'Attack': 45, 'Defense': 20, 'Speed': 20, 'evo_path': ['Wigglytuff']},
    'Gengar': {'Type': ['Ghost', 'Poison'], 'HP': 60, 'Moves': ['Lick', 'Smog', 'Dream Eater', 'Shadow Ball'], 'Attack': 65, 'Defense': 60, 'Speed': 110, 'evo_path': None},
    'Magnemite': {'Type': ['Electric', 'Steel'], 'HP': 25, 'Moves': ['Tackle', 'Flash Cannon', 'Thunder Shock', 'Thunderbolt'], 'Attack': 35, 'Defense': 70, 'Speed': 45, 'evo_path': ['Magneton']},
    'Bulbasaur': {'Type': ['Grass', 'Poison'], 'HP': 45, 'Moves': ['Tackle', 'Vine Whip', 'Razor Leaf'], 'Attack': 49, 'Defense': 49, 'Speed': 45, 'evo_path': ['Ivysaur']},
    'Charmander': {'Type': ['Fire'], 'HP': 39, 'Moves': ['Scratch', 'Ember', 'Fire Spin'], 'Attack': 52, 'Defense': 43, 'Speed': 65, 'evo_path': ['Charmeleon']},
    'Beedrill': {'Type': ['Bug', 'Poison'], 'HP': 65, 'Moves': ['Peck', 'Twineedle', 'Rage', 'Fury Attack', 'Outrage'], 'Attack': 90, 'Defense': 40, 'Speed': 75, 'evo_path': None},
    'Golem': {'Type': ['Rock', 'Ground'], 'HP': 80, 'Moves': ['Tackle', 'Rock Throw', 'Rock Slide', 'Earthquake'], 'Attack': 120, 'Defense': 130, 'Speed': 45, 'evo_path': None},
    'Dewgong': {'Type': ['Water', 'Ice'], 'HP': 90, 'Moves': ['Aqua Jet', 'Ice Shard', 'Headbutt'], 'Attack': 70, 'Defense': 80, 'Speed': 70, 'evo_path': None},
    'Hypno': {'Type': ['Psychic'], 'HP': 85, 'Moves': ['Pound', 'Confusion', 'Dream Eater'], 'Attack': 73, 'Defense': 70, 'Speed': 67, 'evo_path': None},
    'Cleffa': {'Type': ['Fairy'], 'HP': 50, 'Moves': ['Pound', 'Magical Leaf'], 'Attack': 25, 'Defense': 28, 'Speed': 15, 'evo_path': ['Clefairy']},
    'Cutiefly': {'Type': ['Fairy', 'Bug'], 'HP': 40, 'Moves': ['Absorb', 'Fairy Wind', 'Struggle Bug', 'Draining Kiss'], 'Attack': 45, 'Defense': 40, 'Speed': 84, 'evo_path': ['Ribombee']},
    'Raichu': {'Type': ['Electric'], 'HP': 60, 'Moves': ['Thunderbolt', 'Quick Attack', 'Thunder Punch'], 'Attack': 90, 'Defense': 55, 'Speed': 110, 'evo_path': None},
    'Charmeleon': {'Type': ['Fire'], 'HP': 58, 'Moves': ['Scratch', 'Ember', 'Flamethrower'], 'Attack': 64, 'Defense': 58, 'Speed': 80, 'evo_path': ['Charizard']},
    'Wartortle': {'Type': ['Water'], 'HP': 59, 'Moves': ['Tackle', 'Bubble', 'Water Gun'], 'Attack': 63, 'Defense': 80, 'Speed': 58, 'evo_path': ['Blastoise']},
    'Blastoise': {'Type': ['Water'], 'HP': 79, 'Moves': ['Tackle', 'Hydro Pump', 'Bite'], 'Attack': 83, 'Defense': 100, 'Speed': 78, 'evo_path': None},
    'Wigglytuff': {'Type': ['Normal', 'Fairy'], 'HP': 140, 'Moves': ['Pound', 'Body Slam', 'Sing'], 'Attack': 70, 'Defense': 45, 'Speed': 45, 'evo_path': None},
    'Gastly': {'Type': ['Ghost', 'Poison'], 'HP': 30, 'Moves': ['Lick', 'Smog', 'Night Shade'], 'Attack': 35, 'Defense': 30, 'Speed': 80, 'evo_path': ['Haunter']},
    'Haunter': {'Type': ['Ghost', 'Poison'], 'HP': 45, 'Moves': ['Lick', 'Shadow Ball', 'Night Shade'], 'Attack': 50, 'Defense': 45, 'Speed': 95, 'evo_path': ['Gengar']},
    'Magneton': {'Type': ['Electric', 'Steel'], 'HP': 50, 'Moves': ['Tackle', 'Thunderbolt', 'Zap Cannon'], 'Attack': 60, 'Defense': 95, 'Speed': 70, 'evo_path': ['Magnezone']},
    'Ivysaur': {'Type': ['Grass', 'Poison'], 'HP': 60, 'Moves': ['Tackle', 'Vine Whip', 'Razor Leaf'], 'Attack': 62, 'Defense': 63, 'Speed': 60, 'evo_path': ['Venusaur']},
    'Venusaur': {'Type': ['Grass', 'Poison'], 'HP': 80, 'Moves': ['Tackle', 'Vine Whip', 'Solar Beam'], 'Attack': 82, 'Defense': 83, 'Speed': 80, 'evo_path': None},
    'Weedle': {'Type': ['Bug', 'Poison'], 'HP': 40, 'Moves': ['Poison Sting', 'String Shot'], 'Attack': 35, 'Defense': 30, 'Speed': 50, 'evo_path': ['Kakuna']},
    'Kakuna': {'Type': ['Bug', 'Poison'], 'HP': 45, 'Moves': ['Harden'], 'Attack': 25, 'Defense': 50, 'Speed': 35, 'evo_path': ['Beedrill']},
    'Geodude': {'Type': ['Rock', 'Ground'], 'HP': 40, 'Moves': ['Tackle', 'Rock Throw', 'Magnitude'], 'Attack': 80, 'Defense': 100, 'Speed': 20, 'evo_path': ['Graveler']},
    'Graveler': {'Type': ['Rock', 'Ground'], 'HP': 55, 'Moves': ['Tackle', 'Rock Throw', 'Earthquake'], 'Attack': 95, 'Defense': 115, 'Speed': 35, 'evo_path': ['Golem']},
    'Seel': {'Type': ['Water'], 'HP': 65, 'Moves': ['Aqua Jet', 'Headbutt', 'Ice Beam'], 'Attack': 45, 'Defense': 55, 'Speed': 45, 'evo_path': ['Dewgong']},
    'Drowzee': {'Type': ['Psychic'], 'HP': 60, 'Moves': ['Pound', 'Confusion', 'Hypnosis'], 'Attack': 48, 'Defense': 45, 'Speed': 42, 'evo_path': ['Hypno']},
    'Clefairy': {'Type': ['Fairy'], 'HP': 70, 'Moves': ['Pound', 'Magical Leaf', 'Sing'], 'Attack': 45, 'Defense': 48, 'Speed': 35, 'evo_path': ['Clefable']},
    'Clefable': {'Type': ['Fairy'], 'HP': 95, 'Moves': ['Pound', 'Magical Leaf', 'Metronome'], 'Attack': 70, 'Defense': 73, 'Speed': 60, 'evo_path': None}
}


MOVES_DICTIONARY = {
    'Scratch': {'name': 'Scratch', 'power': 40, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Tackle': {'name': 'Tackle', 'power': 40,  'type': 'Normal',  'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Pound': {'name': 'Pound', 'power': 40, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Rage': {'name': 'Rage', 'power': 20, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Fury Attack': {'name': 'Fury Attack', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Ember': {'name': 'Ember', 'power': 40, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']},
    'Fire Spin': {'name': 'Fire Spin', 'power': 35, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']},
    'Bubble': {'name': 'Bubble', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']},
    'Aqua Jet': {'name': 'Aqua Jet', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']},
    'Thunder Shock': {'name': 'Thunder Shock', 'power': 40, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']},
    'Thunderbolt': {'name': 'Thunderbolt', 'power': 90, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']},
    'Vine Whip': {'name': 'Vine Whip', 'power': 45, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Magical Leaf': {'name': 'Magical Leaf', 'power': 60, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Ice Shard': {'name': 'Ice Shard', 'power': 40, 'type': 'Ice', 'super effective against': ['Grass', 'Ground', 'Flying', 'Dragon'], 'not very effective against': ['Fire', 'Water', 'Ice', 'Steel']},
    'Double Kick': {'name': 'Double Kick', 'power': 30, 'type': 'Fighting', 'super effective against': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'], 'not very effective against': ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy']},
    'Earthquake': {'name': 'Earthquake', 'power': 100, 'type': 'Ground', 'super effective against': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], 'not very effective against': ['Grass', 'Bug']},
    'Wing Attack': {'name': 'Wing Attack', 'power': 60, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']},
    'Peck': {'name': 'Peck', 'power': 35, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']},
    'Confusion': {'name': 'Confusion', 'power': 50, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']},
    'Twineedle': {'name': 'Twineedle', 'power': 25, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']},
    'Rock Throw': {'name': 'Rock Throw', 'power': 50, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']},
    'Rock Slide': {'name': 'Rock Slide', 'power': 75, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']},
    'Lick': {'name': 'Lick', 'power': 30, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']},
    'Outrage': {'name': 'Outrage', 'power': 120, 'type': 'Dragon', 'super effective against': ['Dragon'], 'not very effective against': ['Steel']},
    'Crunch': {'name': 'Crunch', 'power': 80, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']},
    'Bite': {'name': 'Bite', 'power': 60, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']},
    'Flash Cannon': {'name': 'Flash Cannon', 'power': 80, 'type': 'Steel', 'super effective against': ['Ice', 'Rock', 'Fairy'], 'not very effective against': ['Fire', 'Water', 'Electric', 'Steel']},
    'Smog': {'name': 'Smog', 'power': 30, 'type': 'Poison', 'super effective against': ['Grass', 'Fairy'], 'not very effective against': ['Poison', 'Ground', 'Rock', 'Ghost']},
    'Dream Eater': {'name': 'Dream Eater', 'power': 100, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']},
    'Body Slam': {'name': 'Body Slam', 'power': 85, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Double Slap': {'name': 'Double Slap', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Razor Leaf': {'name': 'Razor Leaf', 'power': 55, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Headbutt': {'name': 'Headbutt', 'power': 70, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Absorb': {'name': 'Absorb', 'power': 20, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Fairy Wind': {'name': 'Fairy Wind', 'power': 40, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']},
    'Struggle Bug': {'name': 'Struggle Bug', 'power': 50, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']},
    'Draining Kiss': {'name': 'Draining Kiss', 'power': 50, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']},
    'Shadow Ball': {'name': 'Shadow Ball', 'power': 80, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']},
    'Quick Attack': {'name': 'Quick Attack', 'power': 40, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']},
    'Thunder Punch': {'name': 'Thunder Punch', 'power': 75, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']},
    'Flamethrower': {'name': 'Flamethrower', 'power': 90, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']},
    'Water Gun': {'name': 'Water Gun', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']},
    'Hydro Pump': {'name': 'Hydro Pump', 'power': 110, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']},
    'Sing': {'name': 'Sing', 'power': 0, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['N/A']}, 
    'Night Shade': {'name': 'Night Shade', 'power': 60, 'type': 'Ghost', 'super effective against': ['N/A'], 'not very effective against': ['Normal']}, 
    'Zap Cannon': {'name': 'Zap Cannon', 'power': 120, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']},
    'Solar Beam': {'name': 'Solar Beam', 'power': 120, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']},
    'Poison Sting': {'name': 'Poison Sting', 'power': 15, 'type': 'Poison', 'super effective against': ['Grass', 'Fairy'], 'not very effective against': ['Poison', 'Ground', 'Rock', 'Ghost']},
    'String Shot': {'name': 'String Shot', 'power': 0, 'type': 'Bug', 'super effective against': ['N/A'], 'not very effective against': ['N/A']},
    'Harden': {'name': 'Harden', 'power': 0, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['N/A']},  
    'Magnitude': {'name': 'Magnitude', 'power': 70, 'type': 'Ground', 'super effective against': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], 'not very effective against': ['Grass', 'Bug']},
    'Ice Beam': {'name': 'Ice Beam', 'power': 90, 'type': 'Ice', 'super effective against': ['Grass', 'Ground', 'Flying', 'Dragon'], 'not very effective against': ['Fire', 'Water', 'Ice', 'Steel']},
    'Hypnosis': {'name': 'Hypnosis', 'power': 0, 'type': 'Psychic', 'super effective against': ['N/A'], 'not very effective against': ['N/A']}, 
    'Metronome': {'name': 'Metronome', 'power': 0, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['N/A']} 
}

# CLASSES

# Class to define a Pokemon's attributes and battle logic
class Pokemon():
    'A class that defines the attributes and behaviors of a Pokemon.'
    def __init__(self, name, EXP, Level):
        '''
        Initializes the Pokemon object with specified name, EXP, and level
        '''
        self.name = name
        self.type_ = POKEMONS.get(name)['Type']
        self.HP = POKEMONS.get(name)['HP']
        self.attack = POKEMONS.get(name)['Attack']
        self.defense = POKEMONS.get(name)['Defense']
        self.speed = POKEMONS.get(name)['Speed']
        self.EXP = EXP
        self.moves = POKEMONS.get(name)['Moves']
        self.level = Level


    def Choose_move(self):
        '''
        Chooses the most powerful move for the Opponent to use in battle. written by Cooper
        '''
        usable_moves = [move for move in self.moves if move in MOVES_DICTIONARY]
        strongest = -1
        indexes = ''
        for i in usable_moves:
            if MOVES_DICTIONARY.get(i)['power'] > strongest:
                strongest = MOVES_DICTIONARY.get(i)['power']
                indexes = i
        return int(self.moves.index(indexes))

    def Battle_turn(self):
        '''
        Runs a single battle turn where the player selects a move, and the opponent chooses one automatically.
        This function also updates the battle log and alternates turns by Cooper
        '''
        player = self
        opponent = st.session_state.opponent
        if st.session_state.turn_counter == 0:
            # Opens a form for user input of attack, adds to battle log and switches turns as well as rerunning on completion
            with st.form(key=f'Chose_move_form_{player.HP}_{opponent.HP}'):
                chosen_move = st.text_input(f'Chose your move from {player.moves}')
                submitted = st.form_submit_button("Attack")
                if submitted:
                    if chosen_move.title() in [i.title() for i in player.moves]:
                        move_index = player.moves.index(chosen_move.title())
                        damage = opponent.Calculate_damage(move_index, player)
                        st.session_state.battle_log.append(f"{player.name} used {chosen_move}, it dealt {damage} damage.")
                        st.session_state.battle_log.append(f"{opponent.name}'s HP: {opponent.HP}")
                        st.session_state.turn_counter = 1
                        st.rerun()
                    else:
                        st.write('That is not a valid move')
                        st.stop()
        # Gives the opponent a turn and displays information abotu what they did as well as chnaging turns and rerunning
        elif st.session_state.turn_counter == 1:
            st.write('Opponents Turn')
            move_index = opponent.Choose_move()
            st.write(f'Opponent used {opponent.moves[move_index]}')
            damage = player.Calculate_damage(move_index, opponent)
            st.session_state.battle_log.append(f"{opponent.name} used {opponent.moves[move_index]}, it dealt {damage} damage.")
            st.session_state.battle_log.append(f"{player.name}'s HP: {player.HP}")
            st.session_state.turn_counter = 0
            st.rerun()

    def Battle(self, opponent):
        '''
        Creates a battle between the player and the opponent until one Pokemon's HP reaches zero. The battle alternates turns 
        between the player and the opponent. If the player wins, the player's Pokemon gains exp.
        Takes in the players pokemon and the opponent they are facing By Cooper
        '''
        # Checks of battle has started and intializes varibles in st.session_state
        if 'battle' not in st.session_state or st.session_state.battle is False:
            if 'battle_log' not in st.session_state:
                st.session_state.battle_log = []
            st.session_state.battle = True
            if self.speed >= opponent.speed:
                st.session_state.turn_counter = 0
            else:
                st.session_state.turn_counter = 1
            st.session_state.player = self
            st.session_state.opponent = opponent

        # creates columns and creates images and wiritng in them 
        column0, column1 = st.columns(2)
        with column0:
            st.image(PKMIMAGE[opponent.name])
            st.write(f'{opponent.name} HP: {opponent.HP}')
        with column1:
            st.image(PKMIMAGE[self.name])
            st.write(f'{self.name} HP: {self.HP} EXP: {self.EXP}/{self.level*50}')  

        #displays the battle log
        st.text_area("Battle Log", "\n".join(st.session_state.battle_log), height=300)

        # Checks if the battle is over and clears old varibles as well as allowing capture of opponent with a 50% chnace
        if st.session_state.player.HP <= 0:
            st.session_state.player.HP = 0
            st.write('Your Pokemon fainted!')
            st.session_state.battle = False
            del st.session_state.player
            del st.session_state.opponent
            del st.session_state.battle_log
            del st.session_state.turn_counter
            return 0
        elif st.session_state.opponent.HP <= 0:
            st.session_state.opponent.HP = 0
            st.write('Opponent has fainted!')
            if opponent.name not in [pokemon.name for pokemon in st.session_state.yr_pokedex.pokemons]:
                if opponent.capture(st.session_state.yr_pokedex):
                    st.write(f'You captured {opponent.name}!')
                else:
                    st.write(f'You did not capture {opponent.name}.')
            st.session_state.battle = False
            del st.session_state.player
            del st.session_state.opponent
            del st.session_state.battle_log
            del st.session_state.turn_counter
            self.EXP += int(opponent.HP + opponent.attack + opponent.defense + opponent.speed)/10
            return 1
        if st.session_state.battle is True:
            st.session_state.player.Battle_turn()

    def Calculate_damage(self, index, opponent):
        '''
        Calculates the damage taken from a move and subtratcs it from the HP
        Self is the one taking damage
        index is the index of the move
        Opponent is using the move
        written by Louis
        '''
        index = int(index)
        eff = 1
        rd = rand.uniform(0.85, 1)
        rd2 = rand.randint(0, 511)
        crit = 1
        if rd2 < opponent.speed:
            crit = 2
        #Checks if move are not very or super effective for modifiers
        for i in self.type_:
            if i in MOVES_DICTIONARY.get(opponent.moves[index])['super effective against']:
                st.write('Its Super Effective!')
                eff *= 2
            elif i in MOVES_DICTIONARY.get(opponent.moves[index])['not very effective against']:
                st.write('Its Not Very Effective')
                eff *= 0.5
        mod = eff*rd*crit
        damage = int(((((opponent.level*2)/5+2)*MOVES_DICTIONARY.get(opponent.moves[index])['power']*(opponent.attack/self.defense))/25)*mod)
        self.HP -= damage
        return damage

    def Level_up(self):
        '''
        Levels up the pokemon based on if they have enough exp, written by Louis
        '''
        if self.EXP >= self.level*50:
            self.level += 1
            self.HP *= 1.1
            self.attack *= 1.1
            self.defense *= 1.1
            self.speed *= 1.1
            st.write(f'You have leveled up to level {self.level}')

    def stat_total(self):
        '''
        gets the total stats of a pokemon (for balancing) by Cooper
        '''
        return self.HP + self.attack + self.defense + self.speed
  
    def capture(self, pokedex):
        '''
        Captures the  opponent and adds it to the players pokedex by Louis + Cooper
        '''
        capture_chance = rand.uniform(0, 1)
        if capture_chance > 0.5:
            pokedex.add(self)
            return True
        return False




class pokedex():
    '''
    Class containing all the pokemon a user has
    '''
    def __init__(self):
        '''
        Intializes the class
        '''
        self.pokemons = []

    def add(self, pokemon):
        '''
        Adds a pokemon by Louis
        '''
        self.pokemons.append(pokemon)
        st.write(f'{pokemon.name} has been added to your pokedex')

    def __repr__(self):
        '''
        Repr to display pokemon by Louis
        '''
        return f'{self.pokemons}'

    def get_info(self, index):
        '''
        Gives info on a Pokemon by Louis
        '''
        p = self.pokemons[index]
        return f'{p.name} is level {p.level}'

    def evolve(self, index):
        '''
        Evolves a Pokemon with enough exo by Louis and Cooper
        '''
        pkm = self.pokemons[index]
        evo = POKEMONS.get(pkm.name)['evo_path']
        if evo is None:
            return 'Nothing to Evolve to'
        elif pkm.level//4 >= 1:
            pkm.name = evo[0]
            pkm.type_ = POKEMONS.get(evo[0])['Type']
            pkm.HP = POKEMONS.get(evo[0])['HP']
            pkm.attack = POKEMONS.get(evo[0])['Attack']
            pkm.defense = POKEMONS.get(evo[0])['Defense']
            pkm.speed = POKEMONS.get(evo[0])['Speed']
            pkm.moves = POKEMONS.get(evo[0])['Moves']
            return f'{pkm.name} has evolved'
        else:
            return 'Insufficient level to evolve'

    def __len__(self):
        '''
        gives the length of pokemon in the pokedex class
        '''
        return len(self.pokemons)


# FUNCTIONS


def valid_opponents(pokemon):
    '''
    finds opponets with an appropriate base stat total to battle against
    input is the players pokemon 
    returns a list of valid pokemon to fight
    '''
    valid = []
    stattotal = pokemon.stat_total()
    index = 0
    for i in POKEMONS.keys():
        x = Pokemon(i, 1, 0)
        index += 1
        if x.stat_total() in range(int(stattotal*.75), int(stattotal*1.25)):
            valid.append(i)
    return valid


# Start of real game

# displays image

st.image('https://pbs.twimg.com/media/GMl6ZquXoAA0mwA.jpg', use_column_width=True)

# Asks for the trainers name using a form and updates it in session_state
if 'trainer_name' not in st.session_state:
    with st.form(key='name_form'):
        trainer = st.text_input('Enter your name')
        submitted = st.form_submit_button("Enter")
        if submitted:
            if trainer != '':
                st.session_state.trainer_name = trainer
              
            else:
                st.error("Please enter a valid name")
                st.stop()

# When streamlit runs, it skips over forms so using this if statement it is forced to wait
if 'trainer_name' not in st.session_state:
    st.stop()

# creates 3 columns to display 3 images of the strater pokemon
column0, column1, column2 = st.columns(3)
with column0:
    st.image(PKMIMAGE['Bulbasaur'])

with column1:
    st.image(PKMIMAGE['Charmander'])

with column2:
    st.image(PKMIMAGE['Squirtle'])


# Opens a form and asks the user to choose a starter Pokemon stopping the program if there is no input or it is not a valiud choice
if 'starter_pkm' not in st.session_state:
    with st.form(key='starter_choice_form'):
        starter_choice = st.text_input(f'Hello {st.session_state.trainer_name}, Choose your first pokemon(1 Bulbasaur, 2 Charmander, 3 Squirtle)')
        submitted = st.form_submit_button("Enter")
        if submitted:
            try:
                starter_choice = int(starter_choice)
                if starter_choice == 1:
                    starter_choice = 'Bulbasaur'

                elif starter_choice == 2:
                    starter_choice = 'Charmander'

                elif starter_choice == 3:
                    starter_choice = 'Squirtle'  

                else:
                    st.error('That is not a valid choice')
                    st.stop()

                st.session_state.starter_pkm = Pokemon(starter_choice, 0, 1)
                starter_pkm = Pokemon(starter_choice, 0, 1)
                st.success(f'You chose {starter_choice}')

            except ValueError:
                st.error('Enter 1, 2, or 3')
                st.stop()
        else:
            st.stop()


starter_pkm = st.session_state.starter_pkm

#Checks to see if important variables are in st.session_state and defines them
if 'form_counter' not in st.session_state:
    st.session_state.form_counter = 0

if 'again' not in st.session_state:
    st.session_state.again = 'y'

if 'yr_pokedex' not in st.session_state:
    st.session_state.yr_pokedex = pokedex()
    st.session_state.yr_pokedex.add(starter_pkm)
    st.session_state.yr_pokedex.add(Pokemon('Pikachu', 0, 0))

# IF the user wants to battle they get to chose a pokemon if they have more then one using a form and then they battle an opponet that is scaled to them
if st.session_state.again == 'y':
    if len(st.session_state.yr_pokedex.pokemons) > 1:
        if 'chose_pokemon' not in st.session_state:
            with st.form(key=f'pokemon_choice_form_{st.session_state.form_counter}'):
                pokemons_list = [pokemon.name.title() for pokemon in st.session_state.yr_pokedex.pokemons]
                choice = st.text_input(f'choose pokemon: your current pokemons-{pokemons_list}')
                submitted = st.form_submit_button("Enter")
                if submitted:
                    if choice.title() in [i.title() for i in pokemons_list]:
                        st.session_state.chose_pokemon = st.session_state.yr_pokedex.pokemons[pokemons_list.index(choice.title())]
                    else:
                        st.write("Please enter a valid option")
                        st.stop()
       
        if 'chose_pokemon' not in st.session_state:
            st.stop()
        chosen_pokemon = st.session_state.get("chose_pokemon", None)
    else:
        chosen_pokemon = starter_pkm
    if 'opponent' not in st.session_state:
        opponent = Pokemon(rand.choice(valid_opponents(chosen_pokemon)), 0, 1)
        st.session_state.opponent = opponent
# Starts the battle then checks for evolution and leveling up
    winner = chosen_pokemon.Battle(st.session_state.opponent)
    if winner in [0, 1]:
        chosen_pokemon.Level_up()
        index = st.session_state.yr_pokedex.pokemons.index(chosen_pokemon)
        evo_result = st.session_state.yr_pokedex.evolve(index)
        if 'temp_again' in st.session_state:
            del st.session_state.temp_again
        if 'opponent' in st.session_state:
            del st.session_state.opponent
        if 'chose_pokemon' in st.session_state:
            del st.session_state.chose_pokemon
        for i in st.session_state.yr_pokedex.pokemons:
            i.HP = int(POKEMONS.get(i.name)['HP']*(i.level**1.1))

# Sets up a placeholder to prvent streamlit from skipping past user inputs. This also allows the user to battle again or end the game
    if 'temp_again' not in st.session_state and st.session_state.battle is False:
        with st.form(key=f'battle_again_{st.session_state.form_counter}'):
            st.session_state.temp_again = st.text_input('Do you want to battle again? (y/n)')
            submitted = st.form_submit_button("Enter")
            if submitted:
                if st.session_state.temp_again == 'y':
                    if 'chose_pokemon' in st.session_state:
                        del st.session_state.chose_pokemon
                    st.rerun()
                elif st.session_state.temp_again == 'n':
                    st.write(f"Congratualions, you reached level {chosen_pokemon.level} and collected {len(st.session_state.yr_pokedex)} Pokemon")
                    st.stop()    
                else:
                    st.error("Invalid, please respond w/ y or n")
                    st.stop()
# Form counter so that the forms have unique keys
    st.session_state.form_counter += 1
