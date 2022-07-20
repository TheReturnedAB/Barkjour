import random
import sys
MaxHP = 10
CHP = MaxHP
Att = 2
Shield = 2
Armor = 0
Cxp = 0
XP = 10
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
    print("It's has ",EnemyHP,"hp and it has is " ,EAtt,"attack")
    while EnemyHP >= 1:
        act = input("What do you do:")
        if act == 'attack':
            CHP = CHP - EAtt
            EnemyHP = EnemyHP - Att
            print("Your hp is",CHP,"/" , MaxHP)
            print("It's hp is",EnemyHP,)
        elif act == 'shield':
            CHP = CHP - (EAtt-Shield)
            print("Your hp is",CHP,"/" , MaxHP)
            print("It's hp is",EnemyHP,)
        elif act == 'stats':
                Stats()
        elif act == 'help':
            print("help, attack , shield , stats")
        else:
             print("unknown command please try again or type help for list of commands")
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
wolf()
