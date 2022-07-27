
import random
import sys
MaxHP = 10
CHP = MaxHP
Att = 2
Shield = 2
Armor = 0
Cxp = 0
XP = 10
AD = 0
help1 = 0
from random import*
seed = []
while (len(seed)) < 10:
   a = round(randint(0,9))
   seed.append(a)
print("seed:" ,seed)
def Stats():
    global MaxHP
    global CHP
    global Att
    global Shield
    global Armor
    global Cxp
    global XP
    print("You have",CHP,"/" , MaxHP ,"Hp.")
    print("Your Shield is",Shield)
    print("Your armor is",Armor)
    print("You have" ,Cxp,"/" ,XP ,"Xp.")
def Frog():
    global EnemyHP
    global EAtt
    global xpg
    global Enemy
    EnemyHP = 4
    EAtt = 1
    xpg = 2
    Enemy = 'frog'
    print("A frog attacks you")
    Combat()
def wolf():
    global EnemyHP
    global EAtt
    global xpg
    global Enemy
    EnemyHP = 6
    EAtt = 3
    xpg = 6
    Enemy = 'frog'
    print("A frog attacks you")
    Combat()
def Chest():
    while help1 == 0:
        act = input("You found a chest. Type open to open it:")
        if act == 'open':
            act = input("You found a wooden sword. Type equip to equip it:")
            if act == 'equip':
                print("You equip the sword.")
                Att = 4
            help1 == 1
    while act != 'Confirm':
        act = input("Type Confirm to continue:")


def Combat():
    global MaxHP
    global CHP
    global Att
    global Shield
    global Armor
    global Cxp
    global XP
    global EnemyHP
    global EAtt
    global xpg
    global Enemy
    global AD
    global help1
    print("It's has ",EnemyHP,"hp and it has is " ,EAtt,"attack")
    while EnemyHP >= 1:
        act = input("What do you do:")
        if act == 'attack':
            EnemyHP = EnemyHP - Att
            print("You attack.")
        elif act == 'shield':
            AD = Shield
            print("You raise your shield.")
        elif act == 'stats':
                Stats()
        elif act == 'help':
            print("help, attack , shield , stats")
            help1 = 1
        else:
             print("unknown command please try again or type help for list of commands")
             help1 = 1
        if help1 == 0:
            print("The" ,Enemy, "attacks")
            FDam = EAtt - (AD + Armor)
            if FDam > 0:
                CHP = CHP - FDam
            print("Your hp is",CHP,"/" , MaxHP)
            print("It's hp is",EnemyHP,)
        help1 = 0

        if CHP < 0:
            print("Game Over")
            sys.exit()
    Cxp = Cxp + xpg
    print("You have Beaten the",Enemy,".")
    print("You have" ,Cxp,"/" ,XP ,"Xp")
    while act != 'Confirm':
        act = input("Type Confirm to continue:")


Stats()
print("You enter the forest")
Frog()
Chest()
help1 = 0
wolf()
