from character import Character

for x in range(10):
    #random
    a = Character(stat_generation='random',
                  batch=1,
                  tags=["random"])
    a.create_character_folder()
    #default
    b = Character(stat_info=5,
                  batch=2,
                  tags=["default"])
    b.create_character_folder()
    #distributed
    c = Character(stat_generation='distributed',
                  stat_info=25,
                  batch=3,
                  tags=["distributed","25"])
    c.create_character_folder()
    #triangular
    d = Character(stat_generation='triangular',
                  stat_info=5,
                  batch=4,
                  tags=["Triangle"])
    d.create_character_folder()
    #list
    e = Character(stat_generation='list',
                  stat_info=[1,2,3,4,5],
                  batch=5,
                  tags=["list"])
    e.create_character_folder()
