import random

npcs = []
class NPC:
    stats = { 'str' : 0, 'int' : 0, 'pie' : 0, 'agi' : 0, 'stm' : 0, 'cha' : 0 }
    randlist = [1,1,1,1,2,2,2,3,3,4]
    level =0
    hp=0
    gold = 0
    silver = 0
    copper = 0
    wealth =0
    
    def __init__(self,name):
        self.name = name
        self.level = random.choice(self.randlist)
        self.hp = random.randrange(1,10)  
        for j in self.stats:
            dieA = random.randint(1,6)
            dieB = random.randint(1,6)
            dieC = random.randint(1,6)
            self.stats[j] = dieA+dieB+dieC

        if random.randint(1,100) < 30:
            self.gold = random.randint(0,6)
        if random.randint(1,100) < 50:
            self.silver = random.randint(3,12)
        if self.gold == 0:
            if random.randint(1,100) < 75:
                self.copper = random.randint(4,20)
        self.wealth += self.gold*100
        self.wealth+= self.silver*10
        self.wealth += self.copper
        return

for i in range(1000):
    npcs.append(NPC(i))
    #print(npcs[i].level)

def lvls(lis):
    #Generate a report that shows the distribution of NPC's by level
    w=0
    x=0
    y=0
    z=0
    for i in lis:
        if i.level == 1: w+=1
        elif i.level == 2: x+=1
        elif i.level == 3: y+=1
        elif i.level == 4: z+=1


    print(f'there are {w} NPC with level 1, {round(100*(w/len(lis)))}% are like this')
    print(f'there are {x} NPC with level 2, {round(100*(x/len(lis)))}% are like this')
    print(f'there are {y} NPC with level 3, {round(100*(y/len(lis)))}% are like this')
    print(f'there are {z} NPC with level 4, {round(100*(z/len(lis)))}% are like this')


def meanhp(lis):
    tally = 0
    for i in lis:
        tally += i.hp
    final = tally/len(lis)
    return round(final,2)
def meanwealth(lis):
    tally = 0
    for i in lis:
        tally += i.wealth
    final = tally/len(lis)
    return round(final,2)


def sdhp(lis):
    avg = meanhp(lis)
    difs = []
    squares = []
    num = 0
    for i in lis:
        difs.append(i.hp-avg)
    for i in difs:
        squares.append(i**2)
    for i in squares:
        num += i
    return round(((num/len(lis))**0.5),2)
def sdwealth(lis):
    avg = meanwealth(lis)
    difs = []
    squares = []
    num = 0
    for i in lis:
        difs.append(i.wealth-avg)
    for i in difs:
        squares.append(i**2)
    for i in squares:
        num += i
    return round(((num/len(lis))**0.5),2)


def report():
    lvls(npcs)
    print(f'For the HP, the mean value is {meanhp(npcs)} and the standard deviation is {sdhp(npcs)}')
    print(f'For the wealth, the mean value is {meanwealth(npcs)} and the standard deviation is {sdwealth(npcs)}')
report()
