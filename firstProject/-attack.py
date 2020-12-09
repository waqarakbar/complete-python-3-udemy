import random


class Enemy:

    def __init__(self, atkL, atkH):
        self.atkL = atkL
        self.atkH = atkH

    def getAtk(self):
        print(self.atkL)


ene1 = Enemy(20, 34)
ene1.getAtk()

ene2 = Enemy(45, 76)
ene2.getAtk()

'''
playerHp = 260
enemyAttackL = 30
enemyAttackH = 60

while playerHp > 0:
    dmg = random.randrange(enemyAttackL, enemyAttackH)
    playerHp = playerHp - dmg

    #if playerHp <= 0:
    #    playerHp = 0

    if playerHp <= 30:
        playerHp = 30

    print('you have received', dmg, 'damage, your new HP is', playerHp)

    if playerHp == 30:
        print('You are out of the game')
        break
'''
