from character import Character

for x in range(10):
    #random
    Character(stat_generation='random',
              batch=1,
              tags=["random"]).create_character_folder()
    #default
    Character(stat_info=5,
              batch=2,
              tags=["default"]).create_character_folder()
    #distributed
    Character(stat_generation='distributed',
              stat_info=25,
              batch=3,
              tags=["distributed","25"]).create_character_folder()
    #triangular
    Character(stat_generation='triangular',
              stat_info=5,
              batch=4,
              tags=["Triangle"]).create_character_folder()
    #list
    Character(stat_generation='list',
              stat_info=[1,2,3,4,5],
              batch=5,
              tags=["list"]).create_character_folder()
