import random


#TEXT COLOR FUNCTIONS
def prBlue(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 
def prOrange(skk): print("\033[93m {}\033[00m" .format(skk)) 


#MAIN
print("What level chest 1-10, 10 being high level?")
chestinput = input()
chestinput = int(chestinput)
print("Enable jewlery? y/n")
jewleryinput = input()
print("Max percent jewlery? 0.x")
jewlerypercentinput = input()
jewlerypercentinput = float(jewlerypercentinput)

if chestinput == 1:
    rollcoinsg = random.randint(8,15)
    rollcoinss = random.randint(20,40)
    rollcoinsc = random.randint(40,100)

if chestinput == 2:
    rollcoinsg = random.randint(16,30)
    rollcoinss = random.randint(40,80)
    rollcoinsc = random.randint(80,200)

if chestinput == 3:
    rollcoinsg = random.randint(40,75)
    rollcoinss = random.randint(100,200)
    rollcoinsc = random.randint(200,500)

if chestinput == 4:
    rollcoinsg = random.randint(100,188)
    rollcoinss = random.randint(250,500)
    rollcoinsc = random.randint(500,1250)

if chestinput == 5:
    rollcoinsg = random.randint(200,375)
    rollcoinss = random.randint(500,1000)
    rollcoinsc = random.randint(1000,50)

if chestinput == 6:
    rollcoinsg = random.randint(480,900)
    rollcoinss = random.randint(1200,2400)
    rollcoinsc = random.randint(2400,6000)

if chestinput == 7:
    rollcoinsg = random.randint(1000,1875)
    rollcoinss = random.randint(2500,5000)
    rollcoinsc = random.randint(5000,12500)

if chestinput == 8:
    rollcoinsg = random.randint(2000,3750)
    rollcoinss = random.randint(5000,10000)
    rollcoinsc = random.randint(10000,25000)

if chestinput == 9:
    rollcoinsg = random.randint(4800,9000)
    rollcoinss = random.randint(12000,24000)
    rollcoinsc = random.randint(24000,60000)

if chestinput == 10:
    rollcoinsg = random.randint(12000,22500)
    rollcoinss = random.randint(30000,60000)
    rollcoinsc = random.randint(60000,150000)

totalgoldroll = (rollcoinsg)+(rollcoinss/10)+(rollcoinsc/100)
totalgoldpercentg = (rollcoinsg/totalgoldroll)
totalgoldpercents = (rollcoinss/totalgoldroll)
totalgoldpercentc = (rollcoinsc/totalgoldroll)

#JEWLERY
jewlerytypelist = ["ring","necklace","amulet","bracelet","earrings"]
jewlerylevellist = ["Poor","Average","Ornate"]
jewlerymetallist = ["stainless steel","silver","gold"]
jewlerystoneraritylist = ["none", "common","uncommon","rare"]


jewlerytotalcost = random.uniform(0.0,jewlerypercentinput)*int(totalgoldroll)

jewlerynamelist = []
jewleryvaluelist = []
if jewleryinput == "y":
    for jewlery in range(0,100):
        jewleryvalue = 0
        
        if chestinput == 1:
            jewlerystonerarityweight = [0.9,0.1,0.0,0.0]
            jewlerylevelweight = [0.8,0.2,0.0]
            jewlerymetalweight = [0.7,0.25,0.05]
        if chestinput == 2:
            jewlerystonerarityweight = [0.7,0.25,0.05,0.0]
            jewlerylevelweight = [0.6,0.4,0.0]
            jewlerymetalweight = [0.65,0.3,0.05]
        if chestinput == 3:
            jewlerystonerarityweight = [0.6,0.3,0.1,0.0]
            jewlerylevelweight = [0.5,0.4,0.1]
            jewlerymetalweight = [0.6,0.3,0.1]
        if chestinput == 4:
            jewlerystonerarityweight = [0.4,0.3,0.25,0.05]
            jewlerylevelweight = [0.4,0.5,0.1]
            jewlerymetalweight = [0.4,0.4,0.2]
        if chestinput == 5:
            jewlerystonerarityweight = [0.2,0.4,0.3,0.1]
            jewlerylevelweight = [0.3,0.5,0.2]
            jewlerymetalweight = [0.3,0.4,0.3]
        if chestinput == 6:
            jewlerystonerarityweight = [0.2,0.3,0.4,0.1]
            jewlerylevelweight = [0.2,0.5,0.3]
            jewlerymetalweight = [0.2,0.4,0.4]
        if chestinput == 7:
            jewlerystonerarityweight = [0.1,0.2,0.5,0.2]
            jewlerylevelweight = [0.1,0.6,0.3]
            jewlerymetalweight = [0.1,0.5,0.4]
        if chestinput == 8:
            jewlerystonerarityweight = [0.0,0.2,0.45,0.35]
            jewlerylevelweight = [0.0,0.6,0.4]
            jewlerymetalweight = [0.0,0.5,0.5]
        if chestinput == 9:
            jewlerystonerarityweight = [0.0,0.1,0.4,0.5]
            jewlerylevelweight = [0.0,0.5,0.5]
            jewlerymetalweight = [0.0,0.4,0.6]
        if chestinput == 10:
            jewlerystonerarityweight = [0.0,0.0,0.4,0.6]
            jewlerylevelweight = [0.0,0.4,0.6]
            jewlerymetalweight = [0.0,0.3,0.7]
            
        jewlerylevel = random.choices(jewlerylevellist,jewlerylevelweight)
        jewlerymetal = random.choices(jewlerymetallist,jewlerymetalweight)
        jewlerytype = random.choice(jewlerytypelist)            
        jewlerystonerarity = random.choices(jewlerystoneraritylist,jewlerystonerarityweight)
        
        if jewlerystonerarity[0] == "none":
            jewlerystonelist = [""]
        if jewlerystonerarity[0] == "common":
            jewlerystonelist = ["","jade","garnet","sunstone","tiger eye","onyx","amethyst"]
        if jewlerystonerarity[0] == "uncommon":
            jewlerystonelist = ["","jade","garnet","sunstone","tiger eye","amethyst", "aquamarine", "citrine", "tanzanite", "topaz", "tourmaline","onyx"]
        if jewlerystonerarity[0] == "rare":
            jewlerystonelist = ["","jade","garnet","sunstone","tiger eye","amethyst", "aquamarine", "citrine", "tanzanite", "topaz", "tourmaline","onyx","diamond","sapphire","emerald","ruby"]
        
        jewlerystone = random.choice(jewlerystonelist)
                
        
        jewleryname=(jewlerylevel[0]+" "+jewlerymetal[0]+" "+jewlerytype +" with " + jewlerystone)
        if jewleryname.endswith(" "):
            jewleryname = jewleryname[:-6]
        
        jewlerynamelist.append(jewleryname)
        
        if jewlerymetal[0] == "stainless steel":
            jewleryvalue = jewleryvalue + 5
        if jewlerymetal[0] == "silver":
            jewleryvalue = jewleryvalue + 25
        if jewlerymetal[0] == "gold":
            jewleryvalue = jewleryvalue + 50
            
        if jewlerystone == "jade":
            jewleryvalue = jewleryvalue + 50
        if jewlerystone == "garnet":
            jewleryvalue = jewleryvalue + 60
        if jewlerystone == "sunstone":
            jewleryvalue = jewleryvalue + 60
        if jewlerystone == "tiger eye":
            jewleryvalue = jewleryvalue + 50
        if jewlerystone == "amethyst":
            jewleryvalue = jewleryvalue + 60
        if jewlerystone == "aquamarine":
            jewleryvalue = jewleryvalue + 90
        if jewlerystone == "citrine":
            jewleryvalue = jewleryvalue + 80
        if jewlerystone == "tanzanite":
            jewleryvalue = jewleryvalue + 80
        if jewlerystone == "topaz":
            jewleryvalue = jewleryvalue + 80
        if jewlerystone == "tourmaline":
            jewleryvalue = jewleryvalue + 90
        if jewlerystone == "onyx":
            jewleryvalue = jewleryvalue + 60
        if jewlerystone == "diamond":
            jewleryvalue = jewleryvalue + 120
        if jewlerystone == "sapphire":
            jewleryvalue = jewleryvalue + 110
        if jewlerystone == "emerald":
            jewleryvalue = jewleryvalue + 110
        if jewlerystone == "ruby":
            jewleryvalue = jewleryvalue + 110
        
        if jewlerylevel[0] == "Poor":
            jewleryvalue = jewleryvalue * .8
        if jewlerylevel[0] == "Average":
            jewleryvalue = jewleryvalue * 3
        if jewlerylevel[0] == "Ornate":
            jewleryvalue = jewleryvalue * 7
        
        jewleryvaluelist.append(jewleryvalue)
        remainingvalue = jewlerytotalcost-sum(jewleryvaluelist)
        if remainingvalue < 0:
            break
try:
    del jewlerynamelist[-1]
    del jewleryvaluelist[-1]
except:
    next

remaininggold = totalgoldroll-sum(jewleryvaluelist)

rollcoinsg = round(remaininggold*totalgoldpercentg)
rollcoinss = round(remaininggold*totalgoldpercents)
rollcoinsc = round(remaininggold*totalgoldpercentc)

print(jewlerytotalcost)
print("This chest contains " + str(rollcoinsg) + " gold, "+ str(rollcoinss) +" silver, "+str(rollcoinsc) +" copper.")
for jewlery in range(0,len(jewleryvaluelist)):
    
    jewleryprint = str(str(jewlerynamelist[jewlery])+" (expected value is "+str(round(jewleryvaluelist[jewlery]))+" gold)")
    if int(jewleryvaluelist[jewlery]) >= 50:
        prGreen(jewleryprint)
    if int(jewleryvaluelist[jewlery]) >= 300:
        prBlue(jewleryprint)
    if int(jewleryvaluelist[jewlery]) >= 500:
        prPurple(jewleryprint)
    if int(jewleryvaluelist[jewlery]) <= 50:
        prLightGray(jewleryprint)