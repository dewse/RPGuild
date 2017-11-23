import fileinput
import dictio
from dictio import fullDict
import json
import pprint
from sortedcontainers import SortedDict
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

'''
Store player data as indexes in the playerDatabase.json that gets translated from the 
player class lists (i.e.[0][1]=Blood DK). 
'''
class player:

    def __init__(self, name, spec):
        '''Return a new Player object'''  
        self.name = name
        # self.cls = cls
        self.spec = spec
        # self.race = race 
    
    # def 
    
    # name(self, name)
    # cls = ('Death Knight','Druid','Hunter','Mage','Monk','Paladin','Priest','Rogue','Shaman','Warlock','Warrior')
    # clsIndex = self.name.index
    def spec(c,s):
        specLists = (
        ['Blood','Frost','Unholy'],                  #0  DK     [0][0],[0][1],[0][2]
        ['Balance','Feral','Guardian','Resto'],      #1  Druid  [1][0],[1][1],[1][2],[1][3]
        ['Beast Master','Marksmanship','Surival'],   #2  Hunter [2][0],[2][1],[2][2]
        ['Arcane','Fire','Frost'],                   #3  Mage   [3][0],[3][1],[3][2]
        ['Brewmaster','Mistwalker','Windwalker'],    #4  Monk   [4][0],[4][1],[4][2]
        ['Holy','Protection','Retribution'],         #5  Paladin[5][0],[5][1],[5][2]
        ['Disciple','Holy','Shadow'],                #6  Priest [6][0],[6][1],[6][2]
        ['Assassination','Outlaw','Subtlety'],       #7  Rogue  [7][0],[7][1],[7][2]
        ['Elemental','Enhancement','Restoration'],   #8  Shaman [8][0],[8][1],[8][2]
        ['Affliction','Demonology','Destruction'],   #9  Warlock[9][0],[9][1],[9][2]
        ['Arms','Fury','Protection'])                #10 Warrior[10][0],[10][1],[10][2] 
        return specLists[c][s]
# print(player.spec(0,2))
    # race = ('Blood Elf','Draenei','Dwarf','Gnome','Goblin','Human','Night Elf','Orc','Pandaren','Tauren','Troll','Undead','Worgen')

    # def playerInfo(inputSearch):
        # print('Name: ',inputSearch.name+'\n'+'Class: ',inputSearch.cls+'\n'+'Spec: ',inputSearch.spec+'\n'+'Race: ',inputSearch.race+'\n\n')
        # name = player.name
        # cls = player.cls
        # spec = player.spec
        # race = player.race
        # print('Name: ',name+'\n'+'Class: ',cls+'\n'+'Spec: ',spec+'\n'+'Race: ',race+'\n\n')
        # print('Name: ',Kepryx.name+'\n'+'Class: ',Kepryx.cls+'\n'+'Spec: ',Kepryx.spec+'\n'+'Race: ',Kepryx.race+'\n\n')
        # return "Hello!"
        
Jaike = player('Jaike',player.spec(2,1))
# Kepryx = player('Kepryx',player.cls[0],player.spec(0,0),player.race[0])
''' Format of instantiated playerInfo.'''
print('Name: ',Jaike.name+'\n'+'Spec: ',Jaike.spec+'\n\n')
# print('Name: ',Kepryx.name+'\n'+'Class: ',Kepryx.cls+'\n'+'Spec: ',Kepryx.spec+'\n\n')
## Unique ID -- Create ID serialization for each new player.
## Look up database and if doesn't exist, offer to create ID. Every player has unique ID.
## Create return from main function that generates all vars to give feed into the print.

# def playerToIndex():
'''passes Player name to retrieve all the indexes of its description (i.e. Race, Class,
Spec) to that can be used to call the player class.'''


# inputSearch = input("Write something: ")    
# while True:
    # try:
        # inputSearch = input("Write something: ")
        # inputSearchQuery = player.playerInfo(inputSearch)
        # print(player.playerInfo(inputSearch))
    # except:
        # print("Nothing here")
