import numpy
import random

print("What level chest 1-10, 10 being high level?")
chestinput = input()
chestinput = int(chestinput)
print("Enable jewlery? y/n")
jewleryinput = input()


if chestinput == 1:
    rollcoinsg = random.randint(8,15)
    rollcoinss = random.randint(20,40)
    rollcoinsc = random.randint(40,100)
    totalgoldroll = (rollcoinsg)+(rollcoinss/10)+(rollcoinsc/100)
    jewlerylevelweight = [0.8,0.2,0.0]
    jewlerymetalweight = [0.7,0.25,0.05]
    jewlerystonerarity = [0.9,0.1,0.0,0.0]
if chestinput == 2:
    rollcoinsg = random.randint(16,30)
    rollcoinss = random.randint(40,80)
    rollcoinsc = random.randint(80,200)
    totalgoldroll = (rollcoinsg)+(rollcoinss/10)+(rollcoinsc/100)
    jewlerylevelweight = [0.75,0.2,0.05]
    jewlerymetalweight = [0.6,0.3,0.1]
if chestinput == 3:
    rollcoinsg = random.randint(40,75)
    rollcoinss = random.randint(100,200)
    rollcoinsc = random.randint(200,500)
    totalgoldroll = (rollcoinsg)+(rollcoinss/10)+(rollcoinsc/100)
    jewlerylevelweight = [0.6,0.3,0.1]
    jewlerymetalweight = [0.5,0.4,0.1]
if chestinput == 4:
    rollcoinsg = random.randint(100,188)
    rollcoinss = random.randint(250,500)
    rollcoinsc = random.randint(500,1250)
    totalgoldroll = (rollcoinsg)+(rollcoinss/10)+(rollcoinsc/100)
    jewlerylevelweight = [0.5,0.35,0.15]
    jewlerymetalweight = [0.45,0.45,0.1]
if chestinput == 5:
    rollcoinsg = random.randint(200,375)
    rollcoinss = random.randint(500,1000)
    rollcoinsc = random.randint(1000,50)
    totalgoldroll = (rollcoinsg)+(rollcoinss/10)+(rollcoinsc/100)
    jewlerylevelweight = [0.8,0.2,0.0]
    jewlerymetalweight = [0.7,0.25,0.05]
if chestinput == 6:
    rollcoinsg = random.randint(480,900)
    rollcoinss = random.randint(1200,2400)
    rollcoinsc = random.randint(2400,6000)
    totalgoldroll = (rollcoinsg)+(rollcoinss/10)+(rollcoinsc/100)
    jewlerylevelweight = [0.2,0.4,0.4]
    jewlerymetalweight = [0.1,0.6,0.3]
    jewlerystonerarityweight = [0.2,0.2,0.4,0.2]
if chestinput == 7:
    rollcoinsg = random.randint(1000,1875)
    rollcoinss = random.randint(2500,5000)
    rollcoinsc = random.randint(5000,12500)
    totalgoldroll = (rollcoinsg)+(rollcoinss/10)+(rollcoinsc/100)
    jewlerylevelweight = [0.8,0.2,0.0]
    jewlerymetalweight = [0.7,0.25,0.05]
if chestinput == 8:
    rollcoinsg = random.randint(2000,3750)
    rollcoinss = random.randint(5000,10000)
    rollcoinsc = random.randint(10000,25000)
    totalgoldroll = (rollcoinsg)+(rollcoinss/10)+(rollcoinsc/100)
    jewlerylevelweight = [0.8,0.2,0.0]
    jewlerymetalweight = [0.7,0.25,0.05]
if chestinput == 9:
    rollcoinsg = random.randint(4800,9000)
    rollcoinss = random.randint(12000,24000)
    rollcoinsc = random.randint(24000,60000)
    totalgoldroll = (rollcoinsg)+(rollcoinss/10)+(rollcoinsc/100)
    jewlerylevelweight = [0.8,0.2,0.0]
    jewlerymetalweight = [0.05,0.25,0.05]
if chestinput == 10:
    rollcoinsg = random.randint(12000,22500)
    rollcoinss = random.randint(30000,60000)
    rollcoinsc = random.randint(60000,150000)
    totalgoldroll = (rollcoinsg)+(rollcoinss/10)+(rollcoinsc/100)
    jewlerylevelweight = [0.0,0.2,0.8]
    jewlerymetalweight = [0.0,0.2,0.8]

jewlerytypelist = ["ring","necklace","amulet","bracelet","earrings"]
jewlerylevellist = ["cheap","average","ornate"]
jewlerymetallist = ["stainless steel","silver","gold"]
jewlerystoneraritylist = ["none", "common","uncommon","rare"]
jewlerystonerarity = random.choices(jewlerystoneraritylist,jewlerystonerarityweight)

if jewlerystonerarity[0] == "none":
    jewlerystonelist = [""]
if jewlerystonerarity[0] == "common":
    jewlerystonelist = ["","jade","garnet","sunstone","tiger eye","onyx","amethyst"]
if jewlerystonerarity[0] == "uncommon":
    jewlerystonelist = ["","jade","garnet","sunstone","tiger eye","amethyst", "aquamarine", "citrine", "tanzanite", "topaz", "tourmaline","onyx"]
if jewlerystonerarity[0] == "rare":
    jewlerystonelist = ["","jade","garnet","sunstone","tiger eye","amethyst", "aquamarine", "citrine", "tanzanite", "topaz", "tourmaline","onyx","diamond","sapphire","emerald","ruby"]



jewlerytotalcost = random.uniform(0.0,0.8)*int(totalgoldroll)
goldafterjewlery = totalgoldroll-jewlerytotalcost
percentgoldafterjewlery = goldafterjewlery/totalgoldroll

jewlerynamelist = []
jewleryvaluelist = []
if jewleryinput == "y":
    for jewlery in range(0,100):
        jewleryvalue = 0
        jewlerylevel = random.choices(jewlerylevellist,jewlerylevelweight)
        jewlerymetal = random.choices(jewlerymetallist,jewlerymetalweight)
        jewlerystone = random.choice(jewlerystonelist)
        jewlerytype = random.choice(jewlerytypelist)
        
        jewleryname=(jewlerylevel[0]+" "+jewlerymetal[0]+" "+jewlerytype +" with " + jewlerystone)
        if jewleryname.endswith(" "):
            jewleryname = jewleryname[:-6]
        
        jewlerynamelist.append(jewleryname)
        
        if jewlerymetal[0] == "stainless steel":
            jewleryvalue = jewleryvalue + 5
        if jewlerymetal[0] == "silver":
            jewleryvalue = jewleryvalue + 15
        if jewlerymetal[0] == "gold":
            jewleryvalue = jewleryvalue + 30
            
        if jewlerystone == "jade":
            jewleryvalue = jewleryvalue + 20
        if jewlerystone == "garnet":
            jewleryvalue = jewleryvalue + 30
        if jewlerystone == "sunstone":
            jewleryvalue = jewleryvalue + 30
        if jewlerystone == "tiger eye":
            jewleryvalue = jewleryvalue + 20
        if jewlerystone == "amethyst":
            jewleryvalue = jewleryvalue + 30
        if jewlerystone == "aquamarine":
            jewleryvalue = jewleryvalue + 60
        if jewlerystone == "citrine":
            jewleryvalue = jewleryvalue + 50
        if jewlerystone == "tanzanite":
            jewleryvalue = jewleryvalue + 50
        if jewlerystone == "topaz":
            jewleryvalue = jewleryvalue + 50
        if jewlerystone == "tourmaline":
            jewleryvalue = jewleryvalue + 60
        if jewlerystone == "onyx":
            jewleryvalue = jewleryvalue + 30
        if jewlerystone == "diamond":
            jewleryvalue = jewleryvalue + 90
        if jewlerystone == "sapphire":
            jewleryvalue = jewleryvalue + 80
        if jewlerystone == "emerald":
            jewleryvalue = jewleryvalue + 80
        if jewlerystone == "ruby":
            jewleryvalue = jewleryvalue + 80
        
        if jewlerylevel[0] == "cheap":
            jewleryvalue = jewleryvalue * .8
        if jewlerylevel[0] == "average":
            jewleryvalue = jewleryvalue * 2
        if jewlerylevel[0] == "ornate":
            jewleryvalue = jewleryvalue * 4
        
        jewleryvaluelist.append(jewleryvalue)
        remainingvalue = jewlerytotalcost-sum(jewleryvaluelist)
        if remainingvalue < 0:
            break
try:
    del jewlerynamelist[-1]
    del jewleryvaluelist[-1]
except:
    next
    
rollcoinsg = round(rollcoinsg*percentgoldafterjewlery,0)
rollcoinss = round(rollcoinss*percentgoldafterjewlery,0)
rollcoinsc = round(rollcoinsc*percentgoldafterjewlery,0)

print(jewlerytotalcost)
print("this chest contains " + str(rollcoinsg) + " gold, "+ str(rollcoinss) +" silver, "+str(rollcoinsc) +" copper.")
print(jewlerynamelist,jewleryvaluelist)