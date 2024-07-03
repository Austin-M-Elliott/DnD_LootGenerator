#ROLL SPELL SCROLL
import random

chestinput = 5
scrollinput = "y"
scrolltotalcost = 500000

scrollnamelist = []
scrollvaluelist = []
scrolllevelprintlist = []
scrollnumberlist = []

if scrollinput == "y":
    for scroll in range(0,100):
        scrollvalue = 0
        
        if chestinput == 1:
            scrolllevelweight = [0.9,0.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        if chestinput == 2:
            scrolllevelweight = [0.9,0.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        if chestinput == 3:
            scrolllevelweight = [0.9,0.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        if chestinput == 4:
            scrolllevelweight = [0.9,0.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        if chestinput == 5:
            scrolllevelweight = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
        if chestinput == 6:
            scrolllevelweight = [0.9,0.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        if chestinput == 7:
            scrolllevelweight = [0.9,0.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        if chestinput == 8:
            scrolllevelweight = [0.9,0.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        if chestinput == 9:
            scrolllevelweight = [0.9,0.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        if chestinput == 10:
            scrolllevelweight = [0.9,0.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        
        scrolllevellist = ["Cantrip","1","2","3","4","5","6","7","8","9"]
            
        scrolllevel = random.choices(scrolllevellist,scrolllevelweight)
        
        if scrolllevel[0] == "Cantrip":
            scrolllist = ['Acid Splash','Blade Ward','Chill Touch','Control Flames','Create Bonfire','Dancing Lights','Druidcraft','Eldritch Blast','Fire Bolt','Friends','Frostbite','Guidance','Gust','Light','Mage Hand','Magic Stone','Mending','Message','Minor Illusion','Mold Earth','Poison Spray','Prestidigitation','Produce Flame','Ray Of Frost','Resistance','Sacred Flame','Shape Water','Shillelagh','Shocking Grasp','Spare The Dying','Thaumaturgy','Thorn Whip','Thunderclap','True Strike','Vicious Mockery']
            scrollvalue = scrollvalue + 50
        if scrolllevel[0] == "1":
            scrolllist = ['Absorb Elements','Alarm','Animal Friendship','Armor Of Agathys','Arms Of Hadar','Bane','Beast Bond','Bless','Burning Hands','Catapult','Charm Person','Chromatic Orb','Color Spray','Command','Compelled Duel','Comprehend Languages','Create Or Destroy Water','Cure Wounds','Detect Evil And Good','Detect Magic','Detect Poison And Disease','Disguise Self','Dissonant Whispers','Divine Favor','Earth Tremor','Ensnaring Strike','Entangle','Expeditious Retreat','Faerie Fire','False Life','Feather Fall','Find Familiar','Floating Disk','Fog Cloud','Goodberry','Grease','Guiding Bolt','Hail Of Thorns','Healing Word','Hellish Rebuke','Heroism','Hex','Hideous Laughter','Hunters Mark','Ice Knife','Identify','Illusory Script','Inflict Wounds','Jump','Longstrider','Mage Armor','Magic Missile','Protection From Evil And Good','Purify Food And Drink','Ray Of Sickness','Sanctuary','Searing Smite','Shield','Shield Of Faith','Silent Image','Sleep','Speak With Animals','Thunderous Smite','Thunderwave','Unseen Servant','Witch Bolt','Wrathful Smite']
            scrollvalue = scrollvalue + 75
        if scrolllevel[0] == "2":
            scrolllist = ['Acid Arrow','Aganazzars Scorcher','Aid','Alter Self','Animal Messenger','Arcane Lock','Arcanists Magic Aura','Augury','Bane','Barkskin','Beast Sense','Blindness/Deafness','Blur','Branding Smite','Calm Emotions','Cloud Of Daggers','Continual Flame','Cordon Of Arrows','Crown Of Madness','Darkness','Darkvision','Detect Thoughts','Dust Devil','Earthbind','Earthen Grasp','Enhance Ability','Enlarge/Reduce','Enthrall','Find Steed','Find Traps','Flame Blade','Flaming Sphere','Gentle Repose','Gust Of Wind','Heat Metal','Hold Person','Invisibility','Knock','Lesser Restoration','Levitate','Locate Animals Or Plants','Locate Object','Magic Mouth','Magic Weapon','Mirror Image','Misty Step','Moonbeam','Pass Without Trace','Phantasmal Force','Prayer Of Healing','Protection From Poison','Pyrotechnics','Ray Of Enfeeblement','Rope Trick','Scorching Ray','See Invisibility','Shatter','Silence','Skywrite','Snowball Swarm','Spider Climb','Spike Growth','Spiritual Weapon','Suggestion','Warding Bond','Warding Wind','Web','Zone Of Truth']
            scrollvalue = scrollvalue + 200    
        if scrolllevel[0] == "3":
            scrolllist = ['Animate Dead','Aura Of Vitality','Beacon Of Hope','Bestow Curse','Blinding Smite','Blink','Call Lightning','Clairvoyance','Conjure Animals','Conjure Barrage','Counterspell','Create Food And Water','Crusaders Mantle','Daylight','Dispel Magic','Elemental Weapon','Erupting Earth','Fear','Feign Death','Fireball','Flame Arrows','Fly','Gaseous Form','Glyph Of Warding','Haste','Hunger Of Horror','Hypnotic Pattern','Lightning Arrow','Lightning Bolt','Magic Circle','Major Image','Mass Healing Word','Meld Into Stone','Minute Meteors','Nondetection','Phantom Steed','Plant Growth','Protection From Energy','Remove Curse','Revivify','Sending','Sleet Storm','Slow','Speak With Dead','Speak With Plants','Spirit Guardians','Stinking Cloud','Tidal Wave','Tiny Hut','Tongues','Vampiric Touch','Wall of Sand','Wall of Water','Water Breathing','Water Walk','Wind Wall']
            scrollvalue = scrollvalue + 400    
        if scrolllevel[0] == "4":
            scrolllist = ['Arcane Eye','Aura Of Life','Aura Of Purity','Banishment','Black Tentacles','Blight','Compulsion','Confusion','Conjure Minor Elementals','Conjure Woodland Beings','Control Water','Death Ward','Dimension Door','Divination','Dominate Beast','Elemental Bane','Fabricate','Faithful Hound','Fire Shield','Freedom Of Movement','Giant Insect','Grasping Vine','Greater Invisibility','Guardian Of Faith','Hallucinatory Terrain','Ice Storm','Locate Creature','Phantasmal Killer','Polymorph','Private Sanctum','Resilient Sphere','Secret Chest','Staggering Smite','Stone Shape','Stoneskin','Storm Sphere','Vitriolic Sphere','Wall Of Fire','Watery Sphere']
            scrollvalue = scrollvalue + 1000    
        if scrolllevel[0] == "5":
            scrolllist = ['Animate Objects','Antilife Shell','Arcane Hand','Awaken','Banishing Smite','Circle Of Power','Cloudkill','Commune','Commune With Nature','Cone Of Cold','Conjure Elemental','Conjure Volley','Contact Other Plane','Contagion','Control Winds','Creation','Destructive Wave','Dispel Evil And Good','Dominate Person','Dream','Flame Strike','Geas','Greater Restoration','Hallow','Hold Monster','Immolation','Insect Plague','Legend Lore','Maelstrom','Mass Cure Wounds','Mislead','Modify Memory','Passwall','Planar Binding','Raise Dead','Reincarnate','Scrying','Seeming','Swift Quiver','Telekinesis','Telepathic Bond','Teleportation Circle','Transmute Rock','Tree Stride','Wall Of Force','Wall Of Stone']
            scrollvalue = scrollvalue + 3000    
        if scrolllevel[0] == "6":
            scrolllist = ['Arcane Gate','Blade Barrier','Bones of the Earth','Chain Lightning','Circle Of Death','Conjure Fey','Contingency','Create Undead','Disintegrate','Eyebite','Find The Path','Flesh To Stone','Forbiddance','Freezing Sphere','Globe Of Invulnerability','Guards And Wards','Harm','Heal','Heroes Feast','Instant Summons','Investiture of Flame','Investiture of Ice','Investiture of Stone','Investiture of Wind','Irresistible Dance','Magic Jar','Mass Suggestion','Move Earth','Planar Ally','Primordial Ward','Programmed Illusion','Sunbeam','Transport Via Plants','True Seeing','Wall Of Ice','Wall Of Thorns','Wind Walk','Word Of Recall']
            scrollvalue = scrollvalue + 6000    
        if scrolllevel[0] == "7":
            scrolllist = ['Arcane Sword','Conjure Celestial','Delayed Blast Fireball','Divine Word','Etherealness','Finger Of Death','Fire Storm','Forcecage','Magnificent Mansion','Mirage Arcane','Plane Shift','Prismatic Spray','Project Image','Regenerate','Resurrection','Reverse Gravity','Sequester','Simulacrum','Symbol','Teleport','Whirlwind']
            scrollvalue = scrollvalue + 15000    
        if scrolllevel[0] == "8":
            scrolllist = ['Animal Shapes','Antimagic Field','Antipathy/sympathy','Clone','Control Weather','Demiplane','Dominate Monster','Earthquake','Feeblemind','Glibness','Holy Aura','Horrid Wilting','Incendiary Cloud','Maze','Mind Blank','Power Word Stun','Sunburst','Telepathy','Tsunami']
            scrollvalue = scrollvalue + 30000    
        if scrolllevel[0] == "9":
            scrolllist = ['Astral Projection','Foresight','Gate','Imprisonment','Mass Heal','Meteor Swarm','Power Word Heal','Power Word Kill','Prismatic Wall','Shapechange','Storm Of Vengeance','Time Stop','True Polymorph','True Resurrection','Weird','Wish']
            scrollvalue = scrollvalue + 50000    

        
        scrollname = random.choice(scrolllist)
        scrollnamelist.append(scrollname)
        scrolllevelprintlist.append(scrolllevel)
        scrollvaluelist.append(scrollvalue)
        print(scrollvaluelist)
        remainingvalue = scrolltotalcost-sum(scrollvaluelist)
        if remainingvalue < 0:
            break
        elif remainingvalue > 0:
            next
try:
    del scrollnamelist[-1]
    del scrollvaluelist[-1]
except:
    next

for scroll in range(0,len(scrollvaluelist)):
    print(scrollnamelist[scroll],"at level",scrolllevelprintlist[scroll])