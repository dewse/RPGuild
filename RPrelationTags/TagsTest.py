import string
import fileinput
import json
import pprint
from sortedcontainers import SortedDict
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from ast import literal_eval

"""
Passing 
"""
''' Test: Creating tags that will explain relations between players.
class player will hold structure to a player's information such as
Classes, Specs, GuildRank, Faction, EyeColor,
Const ClassArr = [Hunter]
Example character(in this case Jaike, Suri, Dolrok, and Yoda.
Unique ID -- Create ID serialization for each new player.
'''
class player:
    def __init__(self, name, spec):
        '''Return a new Player object'''  
        self.name = name
        # self.cls = cls
        self.spec = spec
        # self.race = race 

    # race = ('Blood Elf','Draenei','Dwarf','Gnome','Goblin',
    # 'Human','Night Elf','Orc','Pandaren','Tauren','Troll','Undead','Worgen')
        
    cls = ('Death Knight','Druid','Hunter','Mage','Monk',
    'Paladin','Priest','Rogue','Shaman','Warlock','Warrior')

    def spec(c,s):
        specList = (
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
        return specList[c][s]
        
    def def1():
        defA = "printed defA"
        def def2():
            defB = (['A1','A2','A3'],['B1','B2','B3'])
    
    
    defB = ('Death Knight','Druid')

###_________↓TEMP DATABASE↓___Main's player template(internal)
def playerLib(y):
    Jaike = player('Jaike',player.cls[2],player.spec(2,1))
    Surinya = player('Surinya',player.cls[1],playey.spec(2,1))
    # y = "Jaike"
    # e2 = "Surynia"
 
def playerConstruct(y):
    y = inputSearch
    x = str("player('{}',player.spec(2,1))".format(y))
    # print(x)
    return x

# print(player.spec.specList(0,0))
# print(player.def1.def2.defB(0,0))
# print(player.def11.defaa)
print(player.defB[0])

# inputSearch = input("Write something: ")
# playerConstructed = playerConstruct(inputSearch)
# print("")
# Jaike = player('Jaike',player.spec(2,1))
# print('Name: ',Jaike.name+'\n'+'Spec: ',Jaike.spec+'\n\n')

# setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.


# player = eval(playerConstructed)
# print('Name: ',exec(inputSearch).name+'\n'+'Spec: ',exec(inputSearch).spec+'\n\n')
# print('Name: ',Jaike.name+'\n'+'Spec: ',Jaike.spec+'\n\n')


"""Jaike = player('Jaike',player.spec(2,1))
print('Name: ',Jaike.name+'\n'+'Spec: ',Jaike.spec+'\n\n')"""

    # def playerInfo(inputSearchQuery): ############################
        # pl = "player"
        # me = string(inputSearch)
        # print("playerInfo function")
        # print("Printing me value :",me)
        # 'Name: ',inputSearch.name+'\n'+
        # 'Class: ',inputSearch.cls+'\n'+
        # 'Spec: ',inputSearch.spec+'\n'+
        # 'Race: ',inputSearch.race+'\n\n')
        # return "{} = player({},player.cls[2],player.spec(2,1),player.race[6])" % (inputSearch,inputSearch))

# print('Name: ',Jaike.name+'\n'+'Spec: ',Jaike.spec+'\n\n')
# player.x()

# while True:
    # try:
        # inputSearch = input("Write something: ")
        # test1 = (str(playerLib(inputSearch)))
        # print(test1)
    # except:
        # print("Nothing here")

# print(
# 'Name: ',Jaike.name+'\n'+
# 'Class: ',Jaike.cls+'\n'+
# 'Spec: ',Jaike.spec+'\n'+
# 'Race: ',Jaike.race+'\n\n')

# DK = 'DeathKnight'
# DRU = 'Druid'
# HNT = 'Hunter'
# MGE = 'Mage'
# MNK = 'Monk'
# PAL = 'Paladin'
# PRI = 'Priest'
# ROG = 'Rogue'
# SHM = 'Shaman'
# LCK = 'Warlock'
# WAR = 'Warrior'

'''Iferror exception as valuerror, search above accronym,spelling variation to replace invalid
 value with full name for proper function input
'''