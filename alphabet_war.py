# -*- coding: utf-8 -*-
"""
   Author:  Adam Blanchette
    Email:  tablanch@ncsu.edu
 Unity ID:  tablanch
    Class:  CSC111, Spring 2018
      Lab:  N/A

  Program:  [Name of the project or file]

  Purpose:  [Purpose of the program]

   "Bugs":  None

#== WORKLOG ==================================================================
           Date          | Time | Computer Name | Location | Notes |
Thu Jan 17 11:56:48 2019 | 2230 |   My Laptop   |          |       |


#=============================================================================

#== AKNOWLEDGEMENTS ==========================================================
Note any and all help you received on this program module, including class
notes, Piazza, etc.

#=============================================================================

"""
#==============================================================================
# IMPORT STATEMENTS
#==============================================================================





#==============================================================================
#  MODULE-LEVEL VARIABLES
#  module_level_variable2 = 98765
#  """int: Module level variable documented inline."""
#==============================================================================





#==============================================================================
# FUNCTIONS/METHODS
#==============================================================================

    
def alphabet_war1(fight):
    war = {'w':4, 'p':3, 'b':2, 's':1, 
          'm':-4, 'q':-3, 'd':-2, 'z':-1,
          '_':0, '*':0}
    fight = list(fight)
    fight = ['_' if letter not in war else letter for letter in fight ]
    bomb = [i for i, letter in enumerate(fight) if letter == '*']
    for i in bomb:
        if i == 0:
            fight[:i+2] = '_','_'
        else:
            fight[i-1:i+2] = '_','_','_'

    if sum([war[letter] for letter in fight]) > 0:
        return "Left side wins!"
    elif sum([war[letter] for letter in fight]) < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"



def alphabet_war(reinforce, airstrike):
    r = [[troop for troop in troops] for troops in reinforce]
    for ix in range(len(airstrike)):
        for jx, bomb in enumerate(airstrike[ix]):
            if bomb == '*':
                if jx == 0:
                    r[0][:jx+2] = '_','_'
                elif jx == len(r[0])-1:
                    r[0][jx-1:] = '_','_'
                else:
                    r[0][jx-1:jx+2] = '_','_','_'

        for j in range(len(r[0])):
            if '_' not in r[0]:
                break
            try:
                for i in range(len(r)):
                    if r[i][j] == '_':
                        r[i][j] = r[i+1][j]
                        r[i+1][j] = '_'
            except IndexError:
                    r[i][j] = '_'
            
    return ''.join(r[0])


#==============================================================================
# for j in range(len(lst[0])):
#     try:
#         for i in range(len(lst)):
#             lst[i][j] = lst[i+1][j]
#     except IndexError:
#         lst[i][j] = None
#==============================================================================
reinforces=["g964xxxxxxxx",
            "myjinxin2015",
            "steffenvogel",
            "smile67xxxxx",
            "giacomosorbi",
            "freywarxxxxx",
            "bkaesxxxxxxx",
            "vadimbxxxxxx",
            "zozofouchtra",
            "colbydauphxx" ]

airstrikes=["* *** ** ***",
            " ** * * * **",
            " * *** * ***",
            " **  * * ** ",
            "* ** *   ***",
            "***   ",
            "**",
            "*",
            "*" ]

re = ["abcdefg","hijklmn"]
air = ["   *   ", "*  *   "]
#==============================================================================
# MAIN METHOD & TESTING AREA
#==============================================================================
def main():
    '''Inside main()'''
    print alphabet_war(re, air)
    
    
if __name__ == "__main__":
    main()
