import random
import string
import math
import warnings
import copy
import os
import shutil

class Character:
    
    def __init__(self, name=None, gender=None, stat_generation=None, stat_info=None, batch=None, tags=None):
        #stats
        self.stats = {
            'luck' : 1,
            'skill' : 1,
            'endurance' : 1,
            'agility' : 1,
            'strength' : 1
            }
        #stats - random
        if stat_generation == 'random':
            self.stats = self.generate_stats_with_random()
        #stats - distributed
        elif stat_generation == 'distributed':
            self.stats = self.generate_stats_with_distributed(stat_info)
        #stats - triangular
        elif stat_generation == 'triangular' or stat_generation == 'random triangular':
            self.stats = self.generate_stats_with_random_triangular(stat_info)
        #stats - list
        elif stat_generation == 'list':
            self.stats = self.generate_skills_from_list(stat_info)
        #stats - default
        else:
            if stat_info == None:
                default_stat_value = 1
                warnings.warn(f'Insufficient stats info. Using default of {default_stat_value}!')
                self.stats = self.default_stats(default_stat_value)
            else:
                self.stats = self.default_stats(stat_info)  
        #gender
        if gender == None:
            self.gender = self.generate_gender()
        else:
            self.gender = gender
        #name
        if name == None:
            self.name = self.generate_name()
        else:
            self.name = str(name)
        #image
        self.image = f'{self.name}.png'
        #colors
        self.colors = self.generate_colors()
        #tags
        if tags != None:
                self.tags = ','.join(tags)
        else:
            self.tags=None
        #batch
        if batch == None:
            self.creator = 1234.5
        else:
            self.creator = batch

    def generate_name(self):
        """Generates a name for the character"""
        name = ''.join([random.choice('BCDGHJKLMNPRSTVWYZ'),
                        random.choice('aeiou'),
                        random.choice('bcfhjklmnprstvwxyz'),
                        random.choice('aiouy'),
                        random.choice('abcdefghijklmnopqrstuvwxyz')])
        name_len = random.choices([2,3,4,5],weights=(1,4,5,2))[0]
        name = name[0:name_len]
        return name
    

    def generate_gender(self, male_chance=None, female_chance=None, other_chance=None):
        """Generates gender for character"""
        if male_chance == None:
            m = 33.33
        if female_chance == None:
            f = 33.33
        if other_chance == None:
            o = 33.33
        gender = random.choices([0.0,1.0,2.0],weights=(m,f,o))[0]
        return gender


    def generate_stats_with_distributed(self, points):
        """Generates stats by distributing points"""
        if points == None:
            warnings.warn(f'No point pool allocated!')
            return dict.fromkeys(self.stats, 1)
        stat_max = 45
        if points > stat_max:
            warnings.warn(f'{points} is greater than maximum allowed {stat_max} points per character!')
            return dict.fromkeys(self.stats, 10)
        stats = copy.copy(self.stats)
        options = list(stats.keys())
        for x in range(0,points):
            #grab a random stat
            stat = random.choice(options)
            #allocate a point
            stats[stat] += 1.0
            #remove the stat from next round if it is maxed
            if stats[stat] == 10.0:
                options.remove(stat)
        return stats

    def default_stats(self, default_stat):
        return dict.fromkeys(self.stats, float(default_stat))


    def generate_skills_from_list(self, skill_list):
        if skill_list == None or len(skill_list) != 5:
            default_skill_list = [1.0,1.0,1.0,1.0,1.0]
            warnings.warn(f'{skill_list} is an invalid skill_list! Defaulting to {default_skill_list}')
            skill_list = default_skill_list
        stats = {}
        index = 0
        for k in self.stats.keys():
            stats[k] = float(skill_list[index])
            index += 1
        return stats
    
        
    def generate_stats_with_random(self):
        """Generates stats randomly"""
        stats = {}
        for k in self.stats.keys():
            stats[k] = float(random.randint(1,10))
        return stats
    

    def generate_stats_with_random_triangular(self, mode):
            """Generates stats randomly waited around the given mode"""
            if mode == None:
                warnings.warn(f'No mode defined! Defaulting to 5')
                mode = 5
            elif mode > 10:
                warning.warn(f'mode entered for random triangular stat distrubution {mode} is higher than maximum of 10!')
                mode = 10
            stats = {}
            for k in self.stats.keys():
                stats[k] = float(round(random.triangular(1,10,mode)))
            return stats
        

    def generate_colors(self):
        """Randomly generate hue, saturation, and color values"""
        colors = {
            'colorr' : float(round(random.randint(0,255))),
            'colorg' : float(round(random.randint(0,255))),
            'colorb' : float(round(random.randint(0,255)))
            }
        return colors


    def create_character_folder(self, tags=None):
        """creates character folder for use in Ultimate Arena"""
        #characters directory
        if not os.path.exists("characters"):
            try:
                os.makedirs("characters")
            except FileExistsError:
                warning.warn("characters directory created during script runtime!")
                pass

        #individual character directory
        break_loop = False
        while break_loop == False:
            char_dir = os.path.join('characters',self.name)
            if not os.path.exists(char_dir):
                break_loop = True
                try:
                    os.makedirs(char_dir)
                except FileExistsError:
                    warning.warn("character directory created during script runtime!")
                    pass
            else:
                filename = os.path.join('characters',self.name, f'{self.name}.ini')
                with open (filename, 'r') as char_file:
                    #check if we just made the conflicting character
                    if str(f'creator="{self.creator}"') in char_file.read():
                        #change the name and continue
                        self.name = self.generate_name()
                        self.image = f'{self.name}.png'
                    else:
                        overwrite_permission = input(f'{self.name} already exists. Would you like to overwrite them?[Y/n]')
                        if overwrite_permission != 'Y':
                            return True
                        else:
                            break_loop = True
        
        filename = os.path.join('characters',self.name, f'{self.name}.ini')
        with open (filename, 'w+') as char_file:
            #header
            char_file.write('[character]\n')
            #creator
            char_file.write(f'creator="{self.creator}"\n')
            #tags
            if self.tags != None:
                tag_string = self.tags
                char_file.write(f'tags="{tag_string}"\n')
            #name
            char_file.write(f'name="{self.name}"\n')
            #pic
            char_file.write(f'image="{self.image}"\n')
            #gender
            gen_string = str(self.gender)#.ljust(8,"0")
            char_file.write(f'gender="{gen_string}"\n')
            #stats
            for stat_name, stat_val in self.stats.items():
                stat_string = str(stat_val)#.ljust(8,"0")
                char_file.write(f'{stat_name}="{stat_string}"\n')
            #colors
            for color_name, color_val in self.colors.items():
                col_string = str(color_val)#.ljust(8,"0")
                char_file.write(f'{color_name}="{col_string}"\n')
        #copy image
        image_file = os.path.join('characters',self.name, f'{self.name}.png')
        shutil.copy('default.png',image_file)
        print(self.name)
        return True


