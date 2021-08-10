# Ultimate_Arena_Mass_Character_Generator
A tool for creating large numbers of Ultimate Arena Characters quickly and easily

Basic use:
	Character().create_character_folder()
This will generate a random character with a randomized name, gender, and color.
Their stats will all be set to 1.0

Use with arguments:
	Character() can take the following arguments:
	- name				str
	- gender			float / int
	- stat_generation	str
	- stat_info			float / int / list[float] / list[int]
	- tags				list[str]
	- batch				float / int
	
See test.py if you are unfamiliar with Python syntax

Argument details:
	name:
		Takes a string and uses it to name the character, character folder, and image
		ex: Character(name="Simon").create_character_folder()
	
	gender:
		Ultimate Arena uses the following codes for gender:
			male = 0.0
			female = 1.0
			other = 2.0
		The generator randomly assigns a gender if none is specified in the arguments
		ex: Character(gender=2).create_character_folder()

	stat_generation:
		The following string arguments may be passed:
			random:
				Each stat is randomly assigned a value in range 1-10
				ex: Character(stat_generation="random").create_character_folder()
			distributed:
				Stats are randomly determined using a pool of points passed in stat_info
				Failure to pass a pool of points results in a default pool of 0
				ex: Character(stat_generation="distributed", stat_info=21).create_character_folder()
			triangular:
				Stats are randomly determined but weighted around the mode passed in stat_info
				Failure to pass a mode results in a default mode of 5
				ex: Character(stat_generation='triangular', stat_info=4).create_character_folder()
			list:
				Stats are assigned based on the list of values passed in stat_info
				stat_info must be passed a 5 element array of integers or floats.
				The stat order is as follows:
					luck, skill, endurance, agility, strength
				ex: Character(stat_generation="list", stat_info=[4,6,5,4,6]).create_character_folder()
			default:
				By default all stats will be set to 1
				The default can be changed by passing a float value in stat_info
				ex: Character(stat_generation="default").create_character_folder()
	
	stat_info:
		stat_info is used in conjunction with stat_generation. 
		See stat_generation for more info.
		Passing a value to stat_info only will make that value the default stat value
		ex: Character(stat_info=7).create_character_folder()

	tags:
		Ultimate Arena uses a tagging system to organize characters.
		passing a list of strings in the tags argument will assign those tags to the character
		ex: Character(tags=["generated","default"]).create_character_folder()
		
	batch:
		Ultimate Area stores a datapoint in each character sheet called "creator"
		The batch argument can be used to set a specific creator but it is also used by the generator
		If the generator creates two characters with the same name it will check the creator id
			If the creator ID is the same,
				The generator will randomly generate a new name.
			If the creator ID is different,
				the generator will request permission to overwrite the existing character.
		The generator will default to a creator ID of 1.2345 if none is provided.
		It is recommended that the batch be set when creating large numbers of characters	
		ex: Character(batch=6.7891).create_character_folder()

Examples:
1) I want 1 character named Robot with a 10 in every stat
Character(name="Robot", stat_info=10).create_character_folder()
	
2) I want 1 character named Unlucky Robot with a luck of 1 and 10 in every other stat
Character(name="Unlucky Robot", stat_generation="list", stat_info=[1,10,10,10,10]).create_character_folder()

3) I want 100 characters with random names and stats but they must all have a gender of "other"
for x in range(100):
	Character(gender=2, stat_generation="random", batch=1).create_character_folder()
	
4) I want 549 characters all named Bob with low stats but occasionally I want a superior Bob
for x in range(549):
	bob_name = "Bob" + str(x)
	Character(name=bob_name,
              gender=0,
              stat_generation="triangular",
              stat_info=2,tags=["The Bobening", "episode 1"],
              batch=808).create_character_folder()
										
5) I want 20 mostly random characters with stats built from a pool of 20 points
for x in range(20):
	Character(stat_generation="distributed",stat_info=20).create_character_folder()
	
Hit me up with questions, concerns, or bugs. I'll fix what I can.