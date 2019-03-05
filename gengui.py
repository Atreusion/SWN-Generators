import random
import PySimpleGUI as sg

sg.SetOptions(text_element_background_color='#D5D5D5', button_color=("#FFFFFF", "#6D7993"), background_color="#9099A2")
  
generator_column = [[sg.Text('Choose generator:'), sg.InputCombo(('NPC', 'Problem', 'Place', 'Urban', 'Wilderness', 'One-roll NPC', 'One-roll Patron', 'Beast Style'), auto_size_text=True, key='_GENIN_', readonly=True)],
                    [sg.Multiline('Generator info', size=(80,14), key='_GENOUTPUT_', do_not_clear=True)],
                    [sg.Button('Generate')]]

weapon_column = [[sg.Text('Weapon:'), sg.InputCombo(('Primitive Bow', 'Advanced Bow', 'Conversion Bow', 'Grenade', 'Crude Pistol', 'Musket', 'Revolver', 'Rifle', 'Shotgun', 'Semi-Auto Pistol', 'Submachine Gun', 'Combat Rifle', 'Combat Shotgun', 'Sniper Rifle', 'Void Carbine', 'Mag Pistol', 'Mag Rifle', 'Spike Thrower', 'Laser Pistol', 'Laser Rifle', 'Thermal Pistol', 'Plasma Projector', 'Shear Rifle', 'Thunder Gun', 'Distortion Cannon', 'Small primitive weapon', 'Medium primitive weapon', 'Large primitive weapon', 'Small advanced weapon', 'Medium advanced weapon', 'Large advanced weapon', 'Stun baton', 'Suit ripper', 'Unarmed attack'), auto_size_text=True, key='_WEAPONIN_', readonly=True, change_submits=True)],
                 [sg.Multiline('Weapon info', size=(80,7), key='_WEAPONOUTPUT_', do_not_clear=True)],
                 [sg.Text("* Can be first in burst mode (3 rounds, +2 hit/+2 dmg). @ Two main actions to reload.")]]
roller_column = [[sg.Text('Dice Roller:'), sg.InputText(size = (2, 1), do_not_clear=True, key = "_ROLLSINPUT_"), sg.Text("d"), sg.InputText(size = (5, 1), do_not_clear=True, key = "_SIDESINPUT_")],
                 [sg.Multiline("Rolls and total", size=(80,5), key = "_ROLLSOUTPUT_", do_not_clear=True)],
                 [sg.Button("Roll"), sg.Text("Limit of 20 dice and 10,000 sides.")]]

beastinfo_column = [[sg.Text('Beast:'), sg.InputCombo(("Small Vicious Beast", "Small Pack Hunter", "Large Pack Hunter", "Large Aggresive Prey Animal", "Lesser Lone Predator", "Greater Lone Predator", "Terrifying Apex Predator", "Gengineered Murder Beast"), auto_size_text=True, key='_BEASTINFOINPUT_', readonly=True, change_submits=True)],
                    [sg.Multiline('Beast info', size=(80,9), key='_BEASTINFOOUTPUT_', do_not_clear=True)],
                    [sg.Text("")]]

npcinfo_column = [[sg.Text('NPC:'), sg.InputCombo(("Peaceful Human","Martial Human","Veteran Fighter","Elite Fighter","Heroic Fighter","Barbarian Hero","Barbarian Tribal","Gang Boss","Gang Member","Gengineered Killer","Legendary Fighter","Military Elite","Military Soldier","Normal Human","Pirate King","Police Officer","Serial Killer","Skilled Professional","Warrior Tyrant"), auto_size_text=True, key='_NPCINFOINPUT_', readonly=True, change_submits=True)],
                    [sg.Multiline('NPC info', size=(80,9), key='_NPCINFOOUTPUT_', do_not_clear=True)],
                    [sg.Text("")]]

layout = [[sg.Column(generator_column, background_color="#D5D5D5"), sg.Column(roller_column, background_color="#D5D5D5")],
          [sg.Column(weapon_column, background_color="#D5D5D5")],
          [sg.Column(beastinfo_column, background_color="#D5D5D5"), sg.Column(npcinfo_column, background_color="#D5D5D5")]]
  
window = sg.Window('SWN Generator').Layout(layout)

def get_reaction():
    reaction_roll = random.random()
    if reaction_roll < 0.027777: reaction = "Hostile, reacting as negatively as is plausible"
    elif 0.027777 < reaction_roll < 0.277777: reaction = "Negative, unfriendly and unhelpful"
    elif 0.277777 < reaction_roll < 0.722222: reaction = "Neutral, reacting predictably or warily"
    elif 0.722222 < reaction_roll < 0.972222: reaction = "Positive, potentially cooperative with PCs"
    else: reaction = "Friendly, helpful as is plausible to be"
    return reaction

def placegen():
    reward = ["Large cache of credits",
              "Precious cultural artifact",
              "Vital data on the party’s goal",
              "Missing or kidnapped",
              "Advanced pretech artifact",
              "Key to some guarded location",
              "Ancient treasure object",
              "Recently-stolen goods",
              "High-tech robotic servitor",
              "Token item of ruling legitimacy",
              "Juicy blackmail material",
              "History-rewriting evidence",
              "Alien artifact of great power",
              "Precious megacorp data files",
              "Map to some valuable thing",
              "Forbidden but precious drug",
              "Legal title to important land",
              "Awful secret of local government",
              "Cache of precious goods",
              "Stock of valuable weaponry"]
    civilized = ["Local festival going on",
                 "Angry street protests",
                 "Minor fire or other disorder",
                 "VIP Merchants and peddlers active",
                 "Tourists from another country",
                 "Building repair or maintenance",
                 "Recent vehicle crash",
                 "Public art performance",
                 "Angry traffic jam",
                 "Missionaries for a local religion",
                 "Loud advertising campaign",
                 "Memorial service ongoing",
                 "Road work halting traffic",
                 "Power outage in the area",
                 "Police chasing criminals",
                 "Annoying drunks being loud",
                 "Beggars seeking alms",
                 "Constructing a new building",
                 "Local thugs swaggering around",
                 "Aerial light display"]
    wilderness = ["Bandits have moved in",
                  "Flooding swept through",
                  "Part of it has collapsed",
                  "Refugees are hiding here",
                  "Dangerous animals lair here",
                  "A rebel cell uses it for a base",
                  "Smugglers have landed here",
                  "Foreign agents meet here",
                  "A hermit has taken up residence",
                  "A toxic plant is growing wild",
                  "An artist seeks inspiration here",
                  "An ancient structure was dug out",
                  "The weather has turned savage",
                  "A vehicle crashed nearby",
                  "Some locals are badly lost",
                  "Religious pilgrims come here",
                  "Locals fight over control of it",
                  "Nature threatens to wipe it out",
                  "An old shrine was raised here",
                  "A shell of a building remains"]

def npcinfogen(npc):
    npcs = {"Peaceful Human":"HD: 1\nAC: 10\nAtk: +0\nDmg.: Unarmed\nMove: 10m\nML: 6\nSkills: +1\nSaves: 15+",
            "Martial Human":"HD: 1\nAC: 10\nAtk: +1\nDmg.: By weapon\nMove: 10m\nML: 8\nSkills: +1\nSaves: 15+",
            "Veteran Fighter":"HD: 2\nAC: 14\nAtk: +2\nDmg.: By weapon +1\nMove: 10m\nML: 9\nSkills: +1\nSaves: 14+",
            "Elite Fighter":"HD: 3\nAC: 16 (combat)\nAtk: +4\nDmg.: By weapon +1\nMove: 10m\nML: 10\nSkills: +2\nSaves: 14+",
            "Heroic Fighter":"HD: 6\nAC: 16 (combat)\nAtk: +8\nDmg.: By weapon +3\nMove: 10m\nML: 11\nSkills: +3\nSaves: 12+",
            "Barbarian Hero":"HD: 6\nAC: 16 (primitive)\nAtk: +8\nDmg.: By weapon +3\nMove: 10m\nML: 11\nSkills: +3\nSaves: 12+",
            "Barbarian Tribal":"HD: 1\nAC: 12 (primitive)\nAtk: +2\nDmg.: By weapon\nMove: 10m\nML: 8\nSkills: +1\nSaves: 15+",
            "Gang Boss":"HD: 3\nAC: 14\nAtk: +4\nDmg.: By weapon +1\nMove: 10m\nML: 9\nSkills: +2\nSaves: 14+",
            "Gang Member":"HD: 1\nAC: 12\nAtk: +1\nDmg.: By weapon\nMove: 10m\nML: 7\nSkills: +1\nSaves: 15+",
            "Gengineered Killer":"HD: 4\nAC: 16\nAtk: +5\nDmg.: By weapon +1\nMove: 15m\nML: 10\nSkills: +2\nSaves: 13+",
            "Legendary Fighter":"HD: 10\nAC: 20 (powered)\nAtk: +12x2\nDmg.: By weapon +4\nMove: 10m\nML: 12\nSkills: +5\nSaves: 10+",
            "Military Elite":"HD: 3\nAC: 16 (combat)\nAtk: +4\nDmg.: By weapon +1\nMove: 10m\nML: 10\nSkills: +2\nSaves: 14+",
            "Military Soldier":"HD: 1\nAC: 16 (combat)\nAtk: +1\nDmg.: By weapon\nMove: 10m\nML: 9\nSkills: +1\nSaves: 15+",
            "Normal Human":"HD: 1\nAC: 10\nAtk: +0\nDmg.: Unarmed\nMove: 10m\nML: 6\nSkills: +1\nSaves: 15+",
            "Pirate King":"HD: 7\nAC: 18 (powered)\nAtk: +9\nDmg.: By weapon +2\nMove: 10m\nML: 11\nSkills: +3\nSaves: 12+",
            "Police Officer":"HD: 1\nAC: 14\nAtk: +1\nDmg.: By weapon\nMove: 10m\nML: 8\nSkills: +1\nSaves: 15+",
            "Serial Killer":"HD: 6\nAC: 12\nAtk: +8\nDmg.: By weapon +3\nMove: 10m\nML: 12\nSkills: +3\nSaves: 12+",
            "Skilled Professional":"HD: 1\nAC: 10\nAtk: +0\nDmg.: By weapon\nMove: 10m\nML: 6\nSkills: +2\nSaves: 15+",
            "Warrior Tyrant":"HD: 8\nAC: 20 (powered)\nAtk: +10\nDmg.: By weapon +3\nMove: 10m\nML: 11\nSkills: +3\nSaves: 11+"}
    output = npcs[npc]
    return output

def beastinfogen(beast):
    beasts = {"Small Vicious Beast":"HD: 1 HP\nAC: 14\nAtk.: +1\nDmg.: 1d2\nMove: 10m\nML: 7\nSkills: +1\nSaves: 15+",
              "Small Pack Hunter":"HD: 1\nAC: 13\nAtk.: +1\nDmg.: 1d4\nMove: 15m\nML: 8\nSkills: +1\nSaves: 15+",
              "Large Pack Hunter":"HD: 2\nAC: 14\nAtk.: +2\nDmg.: 1d6\nMove: 15m\nML: 9\nSkills: +1\nSaves: 14+",
              "Large Aggresive Prey Animal":"HD: 5\nAC: 13\nAtk.: +4\nDmg.: 1d10\nMove: 15m\nML: 8\nSkills: +1\nSaves: 12+",
              "Lesser Lone Predator":"HD: 3\nAC: 14\nAtk.: +4x2\nDmg.: 1d8 each\nMove: 15m\nML: 8\nSkills: +2\nSaves: 14+",
              "Greater Lone Predator":"HD: 5\nAC: 15\nAtk.: +6x2\nDmg.: 1d10 each\nMove: 10m\nML: 9\nSkills: +2\nSaves: 12+",
              "Terrifying Apex Predator":"HD: 8\nAC: 16\nAtk.: +8x2\nDmg.: 1d10 each\nMove: 20m\nML: 9\nSkills: +2\nSaves: 11+",
              "Gengineered Murder Beast":"HD: 10\nAC: 18\nAtk.: +10x4\nDmg.: 1d10 each\nMove: 20m\nML: 11\nSkills: +3\nSaves: 10+"}
    output = beasts[beast]
    return output

def beaststylegen():
    featurelist = ['Amphibian: froggish or newtlike',
                   'Bird: winged and feathered',
                   'Fish: scaled and torpedo-bodied',
                   'Insect: beetle-like or fly-winged',
                   'Mammal: hairy and fanged',
                   'Reptile: lizardlike and long-bodied',
                   'Spider: many-legged and fat',
                   'Exotic: made of wholly alien elements']
    if random.random() > 0.8:
        choice_one = random.choice(featurelist)
        featurelist.remove(choice_one)
        choice_two = random.choice(featurelist)
        features = f"Features: {choice_one} and {choice_two}"
    else:
        features = f"Feature: {random.choice(featurelist)}"
    bodylist = ["Humanoid", "Quadruped", "Many-legged", "Bulbous", "Amorphous"]
    if random.random() > 0.8333:
        choice_one = random.choice(bodylist)
        bodylist.remove(choice_one)
        choice_two = random.choice(bodylist)
        body = f"Body: {choice_one} and {choice_two}"
    else:
        body = f"Body: {random.choice(bodylist)}"
    limbs = random.choice(["Wings", "Many joints", "Tentacles", "Opposable thumbs", "Retractable", "Varying Size"])
    skin = random.choice(["Hard shell", "Exoskeleton", "Odd texture", "Molts regularly", "Harmful to touch", "Wet or slimy"])
    weapon = random.choice(["Teeth or mandibles", "Claws", "Poison", "Harmful discharge", "Pincers", "Horns"])
    size = random.choice(["Cat-sized", "Wolf-sized", "Calf-sized", "Bull-sized", "Hippo-sized", "Elephant-sized"])
    predator = random.choice(["Hunts in kin-group packs",
                              "Favors ambush attacks",
                              "Cripples prey and waits for death",
                              "Pack supports alpha-beast attack",
                              "Lures or drives prey into danger",
                              "Hunts as a lone, powerful hunter",
                              "Only is predator at certain times",
                              "Mindlessly attacks humans"])
    prey = random.choice(["Moves in vigilant herds",
                          "Exists in small family groups",
                          "They all team up on a single foe",
                          "They go berserk when near death",
                          "They’re violent in certain seasons",
                          "They’re vicious if threatened",
                          "Symbiotic creature protects them",
                          "Breeds at tremendous rates"])
    scavenger = random.choice(["Never attacks unwounded prey",
                               "Uses other beasts as harriers",
                               "Always flees if significantly hurt",
                               "Poisons prey, waits for it to die",
                               "Disguises itself as its prey",
                               "Remarkably stealthy",
                               "Summons predators to weak prey",
                               "Steals prey from weaker predator"])
    discharge = random.choice(["Acidic spew doing its damage on a hit",
                               "Toxic spittle or cloud, use adjacent chart",
                               "Super-heated or super-chilled spew",
                               "Sonic drill or other disabling noise",
                               "Natural laser or plasma discharge",
                               "Nauseating stench or disabling chemical",
                               "Equipment-melting corrosive",
                               "Explosive pellets or chemical catalysts"])
    poison = random.choice(["Death",
                            "Paralysis",
                            "1d4 dmg per onset interval",
                            "Convulsions",
                            "Blindness",
                            "Hallucinations"])
    onset = random.choice(["Instant",
                           "1 round",
                           "1d6 rounds",
                           "1 minute",
                           "1d6 minutes",
                           "1 hour"])
    duration = random.choice(["1d6 rounds",
                              "1 minute",
                              "10 minutes",
                              "1 hour",
                              "1d6 hours",
                              "1d6 days"])
    output = (f"{features}\n"
              f"{body}\n"
              f"Limbs: {limbs}\n"
              f"Skin: {skin}\n"
              f"Weapon: {weapon}\n"
              f"Size: {size}\n"
              f"Predator trait: {predator}\n"
              f"Prey trait: {prey}\n"
              f"Scavenger trait: {scavenger}\n"
              f"Discharges: {discharge}\n"
              f"Poison: {poison}\n"
              f"Onset: {onset}\n"
              f"Duration: {duration}")
    output = output.replace("1d4", str(random.randint(1,4)))
    output = output.replace("1d6", str(random.randint(1,6)))
    return output

def onerollnpcgen():
    age = random.choice(["Age: Unusually young or old for their role",
                         "Age: Young adult",
                         "Age: Mature prime",
                         "Age: Middle-aged or elderly"])
    background = random.choice(["Background: The local underclass or poorest natives",
                                "Background: Common laborers or cube workers",
                                "Background: Aspiring bourgeoise or upper clas",
                                "Background: The elite of this society",
                                "Background: Minority or foreigners",
                                "Background: Offworlders or exotics"])
    role = random.choice(["Role in society: Criminal, thug, thief, swindler",
                          "Role in society: Menial, cleaner, retail worker, servant",
                          "Role in society: Unskilled heavy labor, porter, construction",
                          "Role in society: Skilled trade, electrician, mechanic, pilot",
                          "Role in society: Idea worker, programmer, writer",
                          "Role in society: Merchant, business owner, trader, banker",
                          "Role in society: Official, bureaucrat, courtier, clerk",
                          "Role in society: Military, soldier, enforcer, law office"])
    desire = random.choice(["Greatest desire: They want a particular romantic partner",
                            "Greatest desire: They want money for them or a loved one",
                            "Greatest desire: They want a promotion in their job",
                            "Greatest desire: They want answers about a past trauma",
                            "Greatest desire: They want revenge on an enemy",
                            "Greatest desire: They want to help a beleaguered friend",
                            "Greatest desire: They want an entirely different job",
                            "Greatest desire: They want protection from an enemy",
                            "Greatest desire: They want to leave their current life",
                            "Greatest desire: They want fame and glory",
                            "Greatest desire: They want power over those around them",
                            "Greatest desire: They have everything they want from life"])
    problem = random.choice(["Biggest Problem: They have significant debt or money woes",
                             "Biggest Problem: A loved one is in trouble; reroll for it",
                             "Biggest Problem: Romantic failure with a desired person",
                             "Biggest Problem: Drug or behavioral addiction",
                             "Biggest Problem: Their superior dislikes or resents them",
                             "Biggest Problem: They have a persistent sickness",
                             "Biggest Problem: They hate their job or life situation",
                             "Biggest Problem: Someone dangerous is targeting them",
                             "Biggest Problem: They’re pursuing a disastrous purpose",
                             "Biggest Problem: They have no problems worth mentioning"])
    trait = random.choice(["Most obvious character trait: Ambition",
                           "Most obvious character trait: Avarice",
                           "Most obvious character trait: Bitterness",
                           "Most obvious character trait: Courage",
                           "Most obvious character trait: Cowardice",
                           "Most obvious character trait: Curiosity",
                           "Most obvious character trait: Deceitfulness",
                           "Most obvious character trait: Determination",
                           "Most obvious character trait: Devotion to a cause",
                           "Most obvious character trait: Filiality",
                           "Most obvious character trait: Hatred",
                           "Most obvious character trait: Honesty",
                           "Most obvious character trait: Hopefulness",
                           "Most obvious character trait: Love of a person",
                           "Most obvious character trait: Nihilism",
                           "Most obvious character trait: Paternalism",
                           "Most obvious character trait: Pessimism",
                           "Most obvious character trait: Protectiveness",
                           "Most obvious character trait: Resentment",
                           "Most obvious character trait: Shame"])
    reaction = get_reaction()
    output = f"{age}\n{background}\n{role}\n{desire}\n{problem}\n{trait}\nReaction: {reaction}"
    return output

def onerollpatrongen():
    eagerness = random.choice(["Eagerness to hire: Cautious, but can be convinced to hire",
                               "Eagerness to hire: Willing to promise standard rates",
                               "Eagerness to hire: Eager, willing to offer a bonus",
                               "Eagerness to hire: Desperate, might offer what they can’t pay"])
    trustworthiness = random.choice(["Trustworthiness: They intend to totally screw the PCs",
                                     "Trustworthiness: They won’t pay unless forced to do so",
                                     "Trustworthiness: They’ll pay slowly or reluctantly",
                                     "Trustworthiness: They’ll pay, but discount for mistakes",
                                     "Trustworthiness: They’ll pay without quibbling",
                                     "Trustworthiness: They’ll pay more than they promised"])
    noncash = random.choice(["Non-cash rewards: Government official favors owed",
                             "Non-cash rewards: Property in the area",
                             "Non-cash rewards: An item very valuable on another world",
                             "Non-cash rewards: Pretech mod components",
                             "Non-cash rewards: Useful pretech artifact",
                             "Non-cash rewards: Information the PCs need",
                             "Non-cash rewards: Membership in a powerful group",
                             "Non-cash rewards: Black market access",
                             "Non-cash rewards: Use of restricted facilities or shipyards",
                             "Non-cash rewards: Shares in a profitable business",
                             "Non-cash rewards: Maps to a hidden or guarded treasure",
                             "Non-cash rewards: Illegal but valuable weapons or gear"])
    challenge = random.choice(["Challenge: Kill somebody who might deserve it",
                               "Challenge: Kidnap someone dangerous",
                               "Challenge: Steal a well-guarded object",
                               "Challenge: Arson or sabotage on a place",
                               "Challenge: Get proof of some misdeed",
                               "Challenge: Protect someone from an immediate threat",
                               "Challenge: Transport someone through danger",
                               "Challenge: Guard an object being transported"])
    counter = random.choice(["Counterforce: A treacherous employer or subordinate",
                             "Counterforce: An open and known enemy of the patron",
                             "Counterforce: Official governmental meddling",
                             "Counterforce: An unknown rival of the patron",
                             "Counterforce: The macguffin itself opposes them",
                             "Counterforce: Very short time frame allowed",
                             "Counterforce: The job is spectacularly illegal",
                             "Counterforce: A participant would profit by their failure",
                             "Counterforce: The patron is badly wrong about a thing",
                             "Counterforce: The locals are against the patron"])
    complication = random.choice(["Complication: An ambush is laid somewhere",
                                  "Complication: PC involvement is leaked to the enemy",
                                  "Complication: The patron gives faulty aid somehow",
                                  "Complication: Failing would be extremely unhealthy",
                                  "Complication: The job IDs them as allies of a local faction",
                                  "Complication: The macguffin is physically dangerous",
                                  "Complication: An important location is hard to get into",
                                  "Complication: Succeeding would be morally distasteful",
                                  "Complication: A supposed ally is very unhelpful or stupid",
                                  "Complication: The patron badly misunderstood the PCs",
                                  "Complication: The job changes suddenly partway through",
                                  "Complication: An unexpected troublemaker is involved",
                                  "Complication: Critical gear will fail partway through",
                                  "Complication: An unrelated accident complicates things",
                                  "Complication: Payment comes in a hard-to-handle form",
                                  "Complication: Someone is turning traitor on the patron",
                                  "Complication: A critical element has suddenly moved",
                                  "Complication: Payment is in avidly-pursued hot goods",
                                  "Complication: The true goal is a subsidiary part of the job",
                                  "Complication: No complications; it’s just as it seems to be"])
    reaction = get_reaction()
    output = f"{eagerness}\n{trustworthiness}\n{noncash}\n{challenge}\n{counter}\n{complication}\nReaction: {reaction}"
    return output

def roller(rolls, sides):
    rolls = int(rolls)
    sides = int(sides)
    if rolls < 21 and sides < 10001:
        rolllist = []
        for i in range(1, rolls+1): rolllist.append(random.randint(1, sides))
        return rolllist

def weapongen(weapon):
    weapondict = {'Primitive Bow':'Dmg: 1d6\nRange: 50/75\nCost: 15\nMag: 1\nAtr: Dex\nEnc: 2\nTL: 1',
                  'Advanced Bow':'Dmg: 1d6\nRange: 100/150\nCost: 50\nMag: 1\nAtr: Dex\nEnc: 2\nTL: 3',
                  'Conversion Bow':'Dmg: 1d8\nRange: 150/300\nCost: 500\nMag: 1\nAtr: Dex\nEnc: 2\nTL: 4',
                  'Grenade':'Dmg: 2d6\nRange: 10/30\nCost: 25\nMag: N/A\nAtr: Dex\nEnc: 1\nTL: 3',
                  'Crude Pistol':'Dmg: 1d6\nRange: 5/15\nCost: 20\nMag: 1@\nAtr: Dex\nEnc: 1\nTL: 2',
                  'Musket':'Dmg: 1d12\nRange: 25/50\nCost: 30\nMag: 1@\nAtr: Dex\nEnc: 2\nTL: 2',
                  'Revolver':'Dmg: 1d8\nRange: 30/100\nCost: 50\nMag: 6\nAtr: Dex\nEnc: 1\nTL: 2',
                  'Rifle':'Dmg: 1d10+2\nRange: 200/400\nCost: 75\nMag: 6\nAtr: Dex\nEnc: 2\nTL: 2',
                  'Shotgun':'Dmg: 3d4\nRange: 10/30\nCost: 50\nMag: 2\nAtr: Dex\nEnc: 2\nTL: 2',
                  'Semi-Auto Pistol':'Dmg: 1d6+1\nRange: 30/100\nCost: 75\nMag: 12\nAtr: Dex\nEnc: 1\nTL: 3',
                  'Submachine Gun':'Dmg: 1d8*\nRange: 30/100\nCost: 200\nMag: 20\nAtr: Dex\nEnc: 1\nTL: 3',
                  'Combat Rifle':'Dmg: 1d12*\nRange: 100/300\nCost: 300\nMag: 30\nAtr: Dex\nEnc: 2\nTL: 3',
                  'Combat Shotgun':'Dmg: 3d4*\nRange: 10/30\nCost: 300\nMag: 12\nAtr: Dex\nEnc: 2\nTL: 3',
                  'Sniper Rifle':'Dmg: 2d8\nRange: 1,000/2,000\nCost: 400\nMag: 1\nAtr: Dex\nEnc: 2\nTL: 3',
                  'Void Carbine':'Dmg: 2d6\nRange: 100/300\nCost: 400\nMag: 10\nAtr: Dex\nEnc: 2\nTL: 4',
                  'Mag Pistol':'Dmg: 2d6+2\nRange: 100/300\nCost: 400\nMag: 6\nAtr: Dex\nEnc: 1\nTL: 4',
                  'Mag Rifle':'Dmg: 2d8+2\nRange: 300/600\nCost: 500\nMag: 10\nAtr: Dex\nEnc: 2\nTL: 4',
                  'Spike Thrower':'Dmg: 3d8*\nRange: 20/40\nCost: 600\nMag: 15\nAtr: Dex\nEnc: 2\nTL: 4',
                  'Laser Pistol':'Dmg: 1d6\nRange: 100/300\nCost: 200\nMag: 10\nAtr: Dex\nEnc: 1\nTL: 4',
                  'Laser Rifle':'Dmg: 1d10*\nRange: 300/500\nCost: 300\nMag: 20\nAtr: Dex\nEnc: 2\nTL: 4',
                  'Thermal Pistol':'Dmg: 2d6\nRange: 25/50\nCost: 300\nMag: 5\nAtr: Dex\nEnc: 1\nTL: 4',
                  'Plasma Projector':'Dmg: 2d8\nRange: 50/100\nCost: 400\nMag: 6\nAtr: Dex\nEnc: 2\nTL: 4',
                  'Shear Rifle':'Dmg: 2d8*\nRange: 100/300\nCost: 600\nMag: 10\nAtr: Dex\nEnc: 2\nTL: 5',
                  'Thunder Gun':'Dmg: 2d10\nRange: 100/300\nCost: 1000\nMag: 6\nAtr: Dex\nEnc: 2\nTL: 5',
                  'Distortion Cannon':'Dmg: 2d12\nRange: 100/300\nCost: 1250\nMag: 6\nAtr: Dex\nEnc: 2\nTL: 5',
                  'Small primitive weapon':'Dmg: 1d4\nShock: 1 point/AC 15\nAtr: Str/Dex\nCost: 0\nEnc: 1\nTL: 0',
                  'Medium primitive weapon':'Dmg: 1d6+1\nShock: 2 points/AC 13\nAtr: Str/Dex\nCost: 20\nEnc: 1\nTL: 0',
                  'Large primitive weapon':'Dmg: 1d8+1\nShock: 2 points/AC 15\nAtr: Str\nCost: 30\nEnc: 2\nTL: 0',
                  'Small advanced weapon':'Dmg: 1d6\nShock: 1 point/AC 15\nAtr: Str/Dex\nCost: 40\nEnc: 1\nTL: 4',
                  'Medium advanced weapon':'Dmg: 1d8+1\nShock: 2 points/AC 13\nAtr: Str/Dex\nCost: 60\nEnc: 1\nTL: 4',
                  'Large advanced weapon':'Dmg: 1d10+1\nShock: 2 points/AC 15\nAtr: Str\nCost: 80\nEnc: 2\nTL: 4',
                  'Stun baton':'Dmg: 1d8\nShock: 1 point/AC 15\nAtr: Str/Dex\nCost: 50\nEnc: 1\nTL: 4',
                  'Suit ripper':'Dmg: 1d6\nShock: None\nAtr: Str/Dex\nCost: 75\nEnc: 1\nTL: 4',
                  'Unarmed attack':'Dmg: 1d2\nShock: None\nAtr: Str/Dex\nCost: -\nEnc: -\nTL: -'}
    return weapondict[weapon]


def npcgen():
    manner = ["Ingratiating and cloying",
              "Grim suspicion of the PCs or their backers",
              "Xenophilic interest in the novelty of the PCs",
              "Pragmatic and businesslike",
              "Romantically interested in one or more PCs",
              "A slimy used-gravcar dealer’s approach",
              "Wide-eyed awe at the PCs",
              "Cool and superior attitude toward PC \"hirelings\"",
              "Benevolently patronizing toward outsiders",
              "Sweaty-palmed need or desperation",
              "Xenophobic mistrust of the PCs",
              "Idealistic enthusiasm for a potentially shared cause",
              "Somewhat intoxicated by recent indulgence",
              "Smoothly persuasive and reasonable",
              "Visibly uncomfortable with the PCs",
              "Grossly overconfident in PC abilities",
              "Somewhat frightened by the PCs",
              "Deeply misunderstanding the PCs’ culture",
              "Extremely well-informed about the PCs’ past",
              "Distracted by their current situation"]
    outcome = ["They’ll screw the PCs over even at their own cost",
               "They firmly intend to actively betray the PCs",
               "They won’t keep the deal unless driven to it",
               "They plan to twist the deal to their own advantage",
               "They won’t keep their word unless it’s profitable",
               "They’ll flinch from paying up when the time comes",
               "They mean to keep the deal, but are reluctant",
               "They’ll keep most of the deal, but not all of it",
               "They’ll keep the deal slowly and grudgingly",
               "They’ll keep the deal but won’t go out of their way",
               "They’ll be reasonably punctual about the deal",
               "They’ll want a further small favor to pay up on it",
               "They’ll keep the deal in a way that helps them",
               "They’ll keep the deal if it’s still good for them",
               "They’ll offer a bonus for an additional favor",
               "Trustworthy as long as the deal won’t hurt them",
               "Trustworthy, with the NPC following through",
               "They’ll be very fair in keeping to their agreements",
               "They’ll keep bargains even to their own cost",
               "Complete and righteous integrity to the bitter end"]
    motivation = ["An ambition for greater social status",
                  "Greed for wealth and indulgent riches",
                  "Protect a loved one who is somehow imperiled",
                  "A sheer sadistic love of inflicting pain and suffering",
                  "Hedonistic enjoyment of pleasing company",
                  "Searching out hidden knowledge or science",
                  "Establishing or promoting a cultural institution",
                  "Avenging a grievous wrong to them or a loved one",
                  "Promoting their religion and living out their faith",
                  "Winning the love of a particular person",
                  "Winning glory and fame in their profession",
                  "Dodging an enemy who is pursuing them",
                  "Driving out or killing an enemy group",
                  "Deposing a rival to them in their line of work",
                  "Getting away from this world or society",
                  "Promote a friend or offspring’s career or future",
                  "Taking control of a property or piece of land",
                  "Building a structure or a complex prototype tech",
                  "Perform or create their art to vast acclaim",
                  "Redeem themselves from a prior failure"]
    want =["Bring them an exotic piece of tech",
           "Convince someone to meet with the NPC",
           "Kill a particular NPC",
           "Kidnap or non-fatally eliminate a particular NPC",
           "Pay them a large amount of money",
           "Take a message to someone hard to reach",
           "Acquire a tech component that’s hard to get",
           "Find proof of a particular NPC’s malfeasance",
           "Locate a missing NPC",
           "Bring someone to a destination via dangerous travel",
           "Retrieve a lost or stolen object",
           "Defend someone from an impending attack",
           "Burn down or destroy a particular structure",
           "Explore a dangerous or remote location",
           "Steal something from a rival NPC or group",
           "Intimidate a rival into ceasing their course of action",
           "Commit a minor crime to aid the NPC",
           "Trick a rival into doing something",
           "Rescue an NPC from a dire situation",
           "Force a person or group to leave an area"]
    power = ["They’re just really appealing and sympathetic to PCs",
             "They have considerable liquid funds",
             "They control the use of large amounts of violence",
             "They have a position of great social status",
             "They’re a good friend of an important local leader",
             "They have blackmail info on the PCs",
             "They have considerable legal influence here",
             "They have tech the PCs might reasonably want",
             "They can get the PCs into a place they want to go",
             "They know where significant wealth can be found",
             "They have information about the PCs’ current goal",
             "An NPC the PCs need has implicit trust in them",
             "The NPC can threaten someone the PCs like",
             "They control a business relevant to PC needs",
             "They have considerable criminal contacts",
             "They have pull with the local religion",
             "They know a great many corrupt politicians",
             "They can alert the PCs to an unexpected peril",
             "They’re able to push a goal the PCs currently have",
             "They can get the PCs useful permits and rights"]
    hook = ["A particular odd style of dress",
            "An amputation or other maiming",
            "Visible cyberware or prosthetics",
            "Unusual hair, skin, or eye colors",
            "Scarring, either intentional or from old injuries",
            "Tic-like overuse of a particular word or phrase",
            "Specific unusual fragrance or cologne",
            "Constant fiddling with a particular item",
            "Visible signs of drug use",
            "Always seems to be in one particular mood",
            "Wears badges or marks of allegiance to a cause",
            "Extremely slow or fast pace of speech",
            "Constantly with a drink to hand",
            "Always complaining about a group or organization",
            "Paranoid, possibly for justifiable reasons",
            "Insists on a particular location for all meetings",
            "Communicates strictly through a third party",
            "Abnormally obese, emaciated, tall, or short",
            "Always found with henchmen or friends"]
    arabic_male = ["Aamir", "Ayub", "Binyamin", "Efraim", "Ibrahim", "Ilyas",
                   "Ismail", "Jibril", "Jumanah", "Kazi", "Lut", "Matta",
                   "Mohammed", "Mubarak", "Mustafa", "Nazir", "Rahim", "Reza",
                   "Sharif", "Taimur", "Usman", "Yakub", "Yusuf", "Zakariya",
                   "Zubair"]
    arabic_female = ["Aisha", "Alimah", "Badia", "Bisharah", "Chanda",
                     "Daliya", "Fatimah", "Ghania", "Halah", "Kaylah",
                     "Khayrah", "Layla", "Mina", "Munisa", "Mysha", "Naimah",
                     "Nissa", "Nura", "Parveen", "Rana", "Shalha", "Suhira",
                     "Tahirah", "Yasmin", "Zulehka"]
    arabic_surname = ["Abdel", "Awad", "Dahhak", "Essa", "Hanna", "Harbi",
                      "Hassan", "Isa", "Kasim", "Katib", "Khalil", "Malik",
                      "Mansoor", "Mazin", "Musa", "Najeeb", "Namari", "Naser",
                      "Rahman", "Rasheed", "Saleh", "Salim", "Shadi",
                      "Sulaiman", "Tabari"]
    chinese_male = ["Aiguo", "Bohai", "Chao", "Dai", "Dawei", "Duyi", "Fa",
                    "Fu", "Gui", "Hong", "Jianyu", "Kang", "Li", "Niu", "Peng",
                    "Quan", "Ru", "Shen", "Shi", "Song", "Tao", "Xue", "Yi",
                    "Yuan", "Zian"]  
    chinese_female = ["Biyu", "Changying", "Daiyu", "Huidai", "Huiliang",
                      "Jia", "Jingfei", "Lan", "Liling", "Liu", "Meili", "Niu",
                      "Peizhi", "Qiao", "Qing", "Ruolan", "Shu", "Suyin",
                      "Ting", "Xia", "Xiaowen", "Xiulan", "Ya", "Ying",
                      "Zhilan"]
    chinese_surname = ["Bai", "Cao", "Chen", "Cui", "Ding", "Du", "Fang", "Fu",
                       "Guo", "Han", "Hao", "Huang", "Lei", "Li", "Liang",
                       "Liu", "Long", "Song", "Tan", "Tang", "Wang", "Wu",
                       "Xing", "Yang", "Zhang"]  
    english_male = ["Adam", "Albert", "Alfred", "Allan", "Archibald", "Arthur",
                    "Basil", "Charles", "Colin", "Donald", "Douglas", "Edgar",
                    "Edmund", "Edward", "George", "Harold", "Henry", "Ian",
                    "James", "John", "Lewis", "Oliver", "Philip", "Richard",
                    "William"]
    english_female = ["Abigail", "Anne", "Beatrice", "Blanche", "Catherine",
                      "Charlotte", "Claire", "Eleanor", "Elizabeth", "Emily",
                      "Emma", "Georgia", "Harriet", "Joan", "Judy", "Julia",
                      "Lucy", "Lydia", "Margaret", "Mary", "Molly", "Nora",
                      "Rosie", "Sarah", "Victoria"]    
    english_surname = ["Barker", "Brown", "Butler", "Carter", "Chapman",
                       "Collins", "Cook", "Davies", "Gray", "Green", "Harris",
                       "Jackson", "Jones", "Lloyd", "Miller", "Roberts",
                       "Smith", "Taylor", "Thomas", "Turner", "Watson",
                       "White", "Williams", "Wood", "Young"]  
    greek_male = ["Alexander", "Alexius", "Anastasius", "Christodoulos",
                  "Christos", "Damian", "Dimitris", "Dysmas", "Elias",
                  "Giorgos", "Ioannis", "Konstantinos", "Lambros", "Leonidas",
                  "Marcos", "Miltiades", "Nestor", "Nikos", "Orestes",
                  "Petros", "Simon", "Stavros", "Theodore", "Vassilios",
                  "Yannis"]
    greek_female = ["Alexandra", "Amalia", "Callisto", "Charis", "Chloe",
                    "Dorothea", "Elena", "Eudoxia", "Giada", "Helena",
                    "Ioanna", "Lydia", "Melania", "Melissa", "Nika",
                    "Nikolina", "Olympias", "Philippa", "Phoebe", "Sophia",
                    "Theodora", "Valentina", "Valeria", "Yianna", "Zoe"]
    greek_surname = ["Andreas", "Argyros", "Dimitriou", "Floros", "Gavras",
                     "Ioannidis", "Katsaros", "Kyrkos", "Leventis", "Makris",
                     "Metaxas", "Nikolaidis", "Pallis", "Pappas", "Petrou",
                     "Raptis", "Simonides", "Spiros", "Stavros", "Stephanidis",
                     "Stratigos", "Terzis", "Theodorou", "Vasiliadis",
                     "Yannakakis"]  
    indian_male = ["Amrit", "Ashok", "Chand", "Dinesh", "Gobind", "Harinder",
                   "Jagdish", "Johar", "Kurien", "Lakshman", "Madhav",
                   "Mahinder", "Mohal", "Narinder", "Nikhil", "Omrao",
                   "Prasad", "Pratap", "Ranjit", "Sanjay", "Shankar", "Thakur",
                   "Vijay", "Vipul", "Yash"]  
    indian_female = ["Amala", "Asha", "Chandra", "Devika", "Esha", "Gita",
                     "Indira", "Indrani", "Jaya", "Jayanti", "Kiri", "Lalita",
                     "Malati", "Mira", "Mohana", "Neela", "Nita", "Rajani",
                     "Sarala", "Sarika", "Sheela", "Sunita", "Trishna", "Usha",
                     "Vasanta"]
    indian_surname = ["Achari", "Banerjee", "Bhatnagar", "Bose", "Chauhan",
                      "Chopra", "Das", "Dutta", "Gupta", "Johar", "Kapoor",
                      "Mahajan", "Malhotra", "Mehra", "Nehru", "Patil", "Rao",
                      "Saxena", "Shah", "Sharma", "Singh", "Trivedi",
                      "Venkatesan", "Verma", "Yadav"]    
    japanese_male = ["Akira", "Daisuke", "Fukashi", "Goro", "Hiro", "Hiroya",
                     "Hotaka", "Katsu", "Katsuto", "Keishuu", "Kyuuto",
                     "Mikiya", "Mitsunobu", "Mitsuru", "Naruhiko", "Nobu",
                     "Shigeo", "Shigeto", "Shou", "Shuji", "Takaharu",
                     "Teruaki", "Tetsushi", "Tsukasa", "Yasuharu"] 
    japanese_female = ["Aemi", "Airi", "Ako", "Ayu", "Chikaze", "Eriko",
                       "Hina", "Kaori", "Keiko", "Kyouka", "Mayumi", "Miho",
                       "Namiko", "Natsu", "Nobuko", "Rei", "Ririsa", "Sakimi",
                       "Shihoko", "Shika", "Tsukiko", "Tsuzune", "Yoriko",
                       "Yorimi", "Yoshiko"]   
    japanese_surname = ["Abe", "Arakaki", "Endo", "Fujiwara", "Goto", "Ito",
                        "Kikuchi", "Kinjo", "Kobayashi", "Koga", "Komatsu",
                        "Maeda", "Nakamura", "Narita", "Ochi", "Oshiro",
                        "Saito", "Sakamoto", "Sato", "Suzuki", "Takahashi",
                        "Tanaka", "Watanabe", "Yamamoto", "Yamasaki"]   
    latin_male = ["Agrippa", "Appius", "Aulus", "Caeso", "Decimus", "Faustus",
                  "Gaius", "Gnaeus", "Hostus", "Lucius", "Mamercus", "Manius",
                  "Marcus", "Mettius", "Nonus", "Numerius", "Opiter", "Paulus",
                  "Proculus", "Publius", "Quintus", "Servius", "Tiberius",
                  "Titus", "Volescus"]   
    latin_female = ["Appia", "Aula", "Caesula", "Decima", "Fausta", "Gaia",
                    "Gnaea", "Hosta", "Lucia", "Maio", "Marcia", "Maxima",
                    "Mettia", "Nona", "Numeria", "Octavia", "Postuma", "Prima",
                    "Procula", "Septima", "Servia", "Tertia", "Tiberia",
                    "Titia", "Vibia"]
    latin_surname = ["Antius", "Aurius", "Barbatius", "Calidius", "Cornelius",
                     "Decius", "Fabius", "Flavius", "Galerius", "Horatius",
                     "Julius", "Juventius", "Licinius", "Marius", "Minicius",
                     "Nerius", "Octavius", "Pompeius", "Quinctius", "Rutilius",
                     "Sextius", "Titius", "Ulpius", "Valerius", "Vitellius"]
    nigerian_male = ["Adesegun", "Akintola", "Amabere", "Arikawe", "Asagwara",
                     "Chidubem", "Chinedu", "Chiwetei", "Damilola",
                     "Esangbedo", "Ezenwoye", "Folarin", "Genechi", "Idowu",
                     "Kelechi", "Ketanndu", "Melubari", "Nkanta", "Obafemi",
                     "Olatunde", "Olumide", "Tombari", "Udofia", "Uyoata",
                     "Uzochi"]   
    nigerian_female = ["Abike", "Adesuwa", "Adunola", "Anguli", "Arewa",
                       "Asari", "Bisola", "Chioma", "Eduwa", "Emilohi",
                       "Fehintola", "Folasade", "Mahparah", "Minika",
                       "Nkolika", "Nkoyo", "Nuanae", "Obioma", "Olafemi",
                       "Shanumi", "Sominabo", "Suliat", "Tariere", "Temedire",
                       "Yemisi"]   
    nigerian_surname = ["Adegboye", "Adeniyi", "Adeyeku", "Adunola", "Agbaje",
                        "Akpan", "Akpehi", "Aliki", "Asuni", "Babangida",
                        "Ekim", "Ezeiruaku", "Fabiola", "Fasola", "Nwokolo",
                        "Nzeocha", "Ojo", "Okonkwo", "Okoye", "Olaniyan",
                        "Olawale", "Olumese", "Onajobi", "Soyinka", "Yamusa"]    
    russian_male = ["Aleksandr", "Andrei", "Arkady", "Boris", "Dmitri",
                    "Dominik", "Grigory", "Igor", "Ilya", "Ivan", "Kiril",
                    "Konstantin", "Leonid", "Nikolai", "Oleg", "Pavel", "Petr",
                    "Sergei", "Stepan", "Valentin", "Vasily", "Viktor",
                    "Yakov", "Yegor", "Yuri"]  
    russian_female = ["Aleksandra", "Anastasia", "Anja", "Catarina", "Devora",
                      "Dima", "Ekaterina", "Eva", "Irina", "Karolina",
                      "Katlina", "Kira", "Ludmilla", "Mara", "Nadezdha",
                      "Nastassia", "Natalya", "Oksana", "Olena", "Olga",
                      "Sofia", "Svetlana", "Tatyana", "Vilma", "Yelena"]    
    russian_surname = ["Abelev", "Bobrikov", "Chemerkin", "Gogunov", "Gurov",
                       "Iltchenko", "Kavelin", "Komarov", "Korovin",
                       "Kurnikov", "Lebedev", "Litvak", "Mekhdiev", "Muraviov",
                       "Nikitin", "Ortov", "Peshkov", "Romasko", "Shvedov",
                       "Sikorski", "Stolypin", "Turov", "Volokh", "Zaitsev",
                       "Zhukov"]  
    spanish_male = ["Alejandro", "Alonso", "Amelio", "Armando", "Bernardo",
                    "Carlos", "Cesar", "Diego", "Emilio", "Estevan", "Felipe",
                    "Francisco", "Guillermo", "Javier", "Jose", "Juan",
                    "Julio", "Luis", "Pedro", "Raul", "Ricardo", "Salvador",
                    "Santiago", "Valeriano", "Vicente"]    
    spanish_female = ["Adalina", "Aleta", "Ana", "Ascencion", "Beatriz",
                      "Carmela", "Celia", "Dolores", "Elena", "Emelina",
                      "Felipa", "Inez", "Isabel", "Jacinta", "Lucia", "Lupe",
                      "Maria", "Marta", "Nina", "Paloma", "Rafaela", "Soledad",
                      "Teresa", "Valencia", "Zenaida"]  
    spanish_surname = ["Arellano", "Arispana", "Borrego", "Carderas",
                       "Carranzo", "Cordova", "Enciso", "Espejo", "Gavilan",
                       "Guerra", "Guillen", "Huertas", "Illan", "Jurado",
                       "Moretta", "Motolinia", "Pancorbo", "Paredes",
                       "Quesada", "Roma", "Rubiera", "Santoro", "Torrillas",
                       "Vera", "Vivero"]
    namegen = {"Arabic": {"male_names":arabic_male, "female_names":arabic_female, "surnames":arabic_surname},
               "Chinese": {"male_names":chinese_male, "female_names":chinese_female, "surnames":chinese_surname},
               "English": {"male_names":english_male, "female_names":english_female, "surnames":english_surname},
               "Greek": {"male_names":greek_male, "female_names":greek_female, "surnames":greek_surname},
               "Indian": {"male_names":indian_male, "female_names":indian_female, "surnames":indian_surname},
               "Japanese": {"male_names":japanese_male, "female_names":japanese_female, "surnames":japanese_surname},
               "Latin": {"male_names":latin_male, "female_names":latin_female, "surnames":latin_surname},
               "Nigerian": {"male_names":nigerian_male, "female_names":nigerian_female, "surnames":nigerian_surname},
               "Russian": {"male_names":russian_male, "female_names":russian_female, "surnames":russian_surname},
               "Spanish": {"male_names":spanish_male, "female_names":spanish_female, "surnames":spanish_surname}}
    culture = random.choice(list(namegen.items()))
    culture_name = culture[0]
    gender = random.choice(["Male", "Female"])
    if gender == "Male":
        first_name = random.choice(list(culture[1]["male_names"]))
    else:
        first_name = random.choice(list(culture[1]["female_names"]))
    last_name = random.choice(list(culture[1]["surnames"]))
    age = str(random.randint(18,200))
    npc_manner = random.choice(list(manner))
    npc_outcome = random.choice(list(outcome))
    npc_motivation = random.choice(list(motivation))
    npc_want = random.choice(list(want))
    npc_power = random.choice(list(power))
    npc_hook = random.choice(list(hook))
    reaction = get_reaction()
    output = (f"NPC Name: {first_name} {last_name}\n"
              f"Age: {age}\n"
              f"Gender: {gender}\n"
              f"Culture: {culture_name}\n"
              f"Manner: {npc_manner}\n"
              f"Outcome: {npc_outcome}\n"
              f"Motivation: {npc_motivation}\n"
              f"Want: {npc_want}\n"
              f"Power: {npc_power}\n"
              f"Hook: {npc_hook}\n"
              f"Reaction: {reaction}")
    return output

def problemgen():
    money = {"Situation":["Money is owed to a ruthless creditor","Money was stolen from someone","A sudden profit opportunity arises","There’s a hidden stash of wealth","Money is offered from an evil source"],
             "Focus":["Organized crime wants it","Corrupt officials want it","A sympathetic NPC needs it","The PCs are owed it","It will disappear very soon"]}
    revenge = {"Situation":["Someone was murdered","Someone was stripped of rank","Someone lost all their wealth","Someone lost someone’s love","Someone was framed for a crime"],
               "Focus":["It was wholly justified","The wrong person is targeted","The reaction is excessive","The PCs are somehow blamed","Both sides were wronged"]}
    power = {"Situation":["An influential political leader","A stern community elder","A ruling patriarch of a large family","A star expert in a particular industry","A criminal boss or outcast leader"],
             "Focus":["They’ve betrayed their own","Someone’s gunning for them","They made a terrible choice","They usurped their position","They’re oppressing their own"]}
    natural_danger = {"Situation":["A cyclical planetary phenomenon","A sudden natural disaster","Sudden loss of vital infrastructure","Catastrophe from outside meddling","Formerly unknown planetary peril"],
                      "Focus":["Anti-helpful bureaucrats","Religious zealots panic","Bandits and looters strike","The government hushes it up","There’s money in exploiting it"]}
    religion = {"Situation":["Sects that hate each other bitterly","Zealot reformers forcing new things","Radical traditionalists fighting back","Ethnic religious divisions","Corrupt and decadent institutions"],
                "Focus":["Charismatic new leader","Mandatory state religion","Heavy foreign influence","Religious purging underway","Fighting for holy ground"]}
    ideology = {"Situation":["A universally-despised fringe group","Terrorists with widespread support","A political party’s goon squads","Dead-end former regime supporters","Ruthless ascendant political group"],
                "Focus":["Terrorist attack","Street rioting","Police state crackdown","Forced expulsions","Territory under hostile rule"]}
    ethnicity = {"Situation":["A traditionally subordinate group","An ethnic group from offworld","A dominant caste or ethnicity","An alien or transhuman group","Two groups that hate each other"],
                 "Focus":["Forced immigration","Official ethnic ghettos","Rigid separation of groups","Group statuses have changed","Rising ethnic violence"]}
    resources = {"Situation":["There’s a cache of illegal materials","A hidden strike of rare resources","Cargo has been abandoned as lost","Land ownership is disputed","A resource is desperately necessary"],
                 "Focus":["Someone thinks they own it","The state is looking for it","It has its own protectors","Rights to it were stolen","Offworlders want it badly"]}
    conflict_dict = {"Money":money, "Revenge":revenge, "Power":power, "Natural Danger":natural_danger, "Religion":religion, "Ideology":ideology, "Ethnicity":ethnicity, "Resources":resources}
    restraint_list = ["The government is cracking down on the conflict",
                      "One side seems invincibly stronger to the other",
                      "Both sides have \"doomsday\" info or devices",
                      "A prior conflict ended horribly for both of them",
                      "Foreign participants are keeping things tamped",
                      "Elements of both sides seek accommodation",
                      "The conflict is only viable in a narrow location",
                      "Catastrophic cost of losing a direct showdown",
                      "Each thinks they’ll win without further exertion",
                      "They expect a better opening to appear soon",
                      "Former ties of friendship or family restrain them",
                      "Religious principles are constraining them",
                      "One side’s still licking their wounds after a failure",
                      "They’re building up force to make sure they win",
                      "Their cultural context makes open struggle hard",
                      "They expect an outside power to hand them a win",
                      "They’re still searching for a way to get at their goal",
                      "One side mistakenly thinks they’ve already won",
                      "A side is busy integrating a recent success",
                      "An outside power threatens both sides"]
    twist_list = ["There’s a very sharp time limit for any resolution",
                  "The sympathetic side is actually a bunch of bastards",
                  "There’s an easy but very repugnant solution to hand",
                  "PC success means a big benefit to a hostile group",
                  "The real bone of contention is hidden from most",
                  "A sympathetic figure’s on an unsympathetic side",
                  "There’s a profitable chance for PCs to turn traitor",
                  "The \"winner\" will actually get in terrible trouble",
                  "There’s a very appealing third party in the mix",
                  "The PCs could really profit off the focus of the strife",
                  "The PCs are mistaken for an involved group",
                  "Somebody plans on screwing over the PCs",
                  "Both sides think the PCs are working for them",
                  "A side wants to use the PCs as a distraction for foes",
                  "The PCs’ main contact is mistrusted by their allies",
                  "If the other side can’t get it, they’ll destroy it",
                  "The focus isn’t nearly as valuable as both sides think",
                  "The focus somehow has its own will and goals",
                  "Victory will drastically change one of the sides",
                  "Actually, there is no twist. It’s all exactly as it seems."]
    conflict = random.choice(list(conflict_dict.items()))
    focus = random.choice(conflict[1]["Focus"])
    situation = random.choice(conflict[1]["Situation"])
    restraint = random.choice(restraint_list)
    twist = random.choice(twist_list)
    output = (f"{conflict[0]} Siutation: {situation}\n"
              f"{conflict[0]} Focus: {focus}\nRestraint: {restraint}\n"
              f"Twist: {twist}")
    return output

def urbangen():
    venue = ["Venue: In the middle of the street",
             "Venue: In a public plaza",
             "Venue: Down a side alley",
             "Venue: Inside a local business",
             "Venue: Next to or in a public park",
             "Venue: At a mass-transit station"]
    pc_involvment = ["Why PCs are involved: A sympathetic participant appeals to them",
                     "Why PCs are involved: Ways around it are all dangerous/blocked",
                     "Why PCs are involved: It happens immediately around them",
                     "Why PCs are involved: A valuable thing looks snatchable amid it",
                     "Why PCs are involved: A participant offers a reward for help",
                     "Why PCs are involved: Someone mistakenly involves the PCs in it",
                     "Why PCs are involved: The seeming way out just leads deeper in",
                     "Why PCs are involved: Responsibility is somehow pinned on them"]
    nature = ["Nature of event: A parade or festival is being disrupted",
              "Nature of event: Innocents are being assaulted",
              "Nature of event: An establishment is being robbed",
              "Nature of event: A disturbance over local politics happens",
              "Nature of event: Someone is being blamed for something",
              "Nature of event: Fires or building collapses are happening",
              "Nature of event: A medical emergency is happening",
              "Nature of event: Someone’s trying to cheat the PCs",
              "Nature of event: A vehicle accident is happening",
              "Nature of event: A religious ceremony is being disrupted"]
    conflict = ["Conflict about: Money, extortion, payment due, debts",
                "Conflict about: Respect, submission to social authority",
                "Conflict about: Grudges, ethnic resentment, gang payback",
                "Conflict about: Politics, religion, or other ideology"]
    antagonists = ["Antagonists: A local bully and their thugs",
                   "Antagonists: A ruthless political boss and their zealots",
                   "Antagonists: Violent criminals",
                   "Antagonists: Religious fanatics",
                   "Antagonists: A blisteringly obnoxious offworlder",
                   "Antagonists: Corrupt or over-strict government official",
                   "Antagonists: A mob of intoxicated locals",
                   "Antagonists: A ranting demagogue and their followers",
                   "Antagonists: A stupidly bull-headed local grandee",
                   "Antagonists: A very capable assassin or strong-arm",
                   "Antagonists: A self-centered local scion of power",
                   "Antagonists: A confused foreigner or backwoodsman"]
    features = ["Revelant urban features:Heavy traffic running through the place",
                "Revelant urban features: Music blaring at deafening volumes",
                "Revelant urban features: Two groups present that detest each other",
                "Revelant urban features: Large delivery taking place right there",
                "Revelant urban features: Swarm of schoolkids or feral youth",
                "Revelant urban features: Insistent soapbox preacher here",
                "Revelant urban features: Several pickpockets working the crowd",
                "Revelant urban features: A kiosk is tipping over and spilling things",
                "Revelant urban features: Streetlights are out or visibility is low",
                "Revelant urban features: A cop patrol is here and reluctant to act",
                "Revelant urban features: PC-hostile reporters are recording here",
                "Revelant urban features: Someone’s trying to sell something to PCs",
                "Revelant urban features: Feral dogs or other animals crowd here",
                "Revelant urban features: Unrelated activists are protesting here",
                "Revelant urban features: Street kids are trying to steal from the PCs",
                "Revelant urban features: GPS maps are dangerously wrong here",
                "Revelant urban features: Downed power lines are a danger here",
                "Revelant urban features: Numerous open manholes and utility holes",
                "Revelant urban features: The street’s blockaded by something",
                "Revelant urban features: Crowds so thick one can barely move"]
    output = (f"{random.choice(venue)}\n{random.choice(pc_involvment)}\n"
              f"{random.choice(nature)}\n{random.choice(conflict)}\n"
              f"{random.choice(antagonists)}\n{random.choice(features)}")
    return output

def wildernessgen():
    weather = ["Weather and Lighting: Takes place in daylight and clear weather",
               "Weather and Lighting: Daylight, but fog, mist, rain or the like",
               "Weather and Lighting: Daylight, but harsh seasonal weather",
               "Weather and Lighting: Night encounter, but clear weather",
               "Weather and Lighting: Night, with rain or other obscuring effects",
               "Weather and Lighting: Night, with terrible weather and wind"]
    nature = ["Nature of encounter: Attack by pack of hostiles",
              "Nature of encounter: Ambush by single lone hostile",
              "Nature of encounter: Meet people who don’t want to be met",
              "Nature of encounter: Encounter people in need of aid",
              "Nature of encounter: Encounter hostile creatures",
              "Nature of encounter: Nearby feature is somehow dangerous",
              "Nature of encounter: Nearby feature promises useful loot",
              "Nature of encounter: Meet hostiles that aren’t immediately so"]
    friendly = ["Friendly creature(s): Affable but reclusive hermit",
                "Friendly creature(s): Local herd animal let loose to graze",
                "Friendly creature(s): Government ranger or circuit judge",
                "Friendly creature(s): Curious local animal",
                "Friendly creature(s): Remote homesteader and family",
                "Friendly creature(s): Working trapper or hunter",
                "Friendly creature(s): Back-country villager or native",
                "Friendly creature(s): Hiker or wilderness tourist",
                "Friendly creature(s): Religious recluse or holy person",
                "Friendly creature(s): Impoverished social exile"]
    enc_range = ["Encounter Range: Visible from a long distance away",
                 "Encounter Range: Noticed 1d4 hundred meters away",
                 "Encounter Range: Noticed only within 1d60 meters",
                 "Encounter Range: Noticed only when adjacent to the event"]
    hostile = ["Hostile creature(s): Bandits in their wilderness hideout",
               "Hostile creature(s): Dangerous locals looking for easy marks",
               "Hostile creature(s): Rabid or diseased large predator",
               "Hostile creature(s): Pack of hungry hunting beasts",
               "Hostile creature(s): Herd of potentially dangerous prey animals",
               "Hostile creature(s): Swarm of dangerous vermin",
               "Hostile creature(s): Criminal seeking to evade the law",
               "Hostile creature(s): Brutal local landowner and their men",
               "Hostile creature(s): Crazed hermit seeking enforced solitude",
               "Hostile creature(s): Friendly-seeming guide into lethal danger",
               "Hostile creature(s): Harmless-looking but dangerous beast",
               "Hostile creature(s): Confidence man seeking to gull the PCs"]
    features = ["Nearby feature: Overgrown homestead",
                "Nearby feature: Stream prone to flash-flooding",
                "Nearby feature: Narrow bridge or beam over deep cleft",
                "Nearby feature: Box canyon with steep sides",
                "Nearby feature: Unstable hillside that slides if disturbed",
                "Nearby feature: Long-lost crash site of a gravflyer",
                "Nearby feature: Once-inhabited cave or tunnel",
                "Nearby feature: Steep and dangerous cliff",
                "Nearby feature: Quicksand-laden swamp or dust pit",
                "Nearby feature: Ruins of a ghost town or lost hamlet",
                "Nearby feature: Hunting cabin with necessities",
                "Nearby feature: Ill-tended graveyard of a lost family stead",
                "Nearby feature: Narrow pass that’s easily blocked",
                "Nearby feature: Dilapidated resort building",
                "Nearby feature: Remote government monitoring outpost",
                "Nearby feature: Illicit substance farm or processing center",
                "Nearby feature: Old and forgotten battleground",
                "Nearby feature: Zone overrun by dangerous plants",
                "Nearby feature: Thick growth that lights up at a spark",
                "Nearby feature: Abandoned vehicle"]
    encounter_range = random.choice(enc_range)
    encounter_range = encounter_range.replace("1d4", str(random.randint(1,4)))
    encounter_range = encounter_range.replace("1d6", str(random.randint(1,6)))
    output = (f"{random.choice(weather)}\n{random.choice(nature)}\n"
              f"{random.choice(friendly)}\n{encounter_range}\n"
              f"{random.choice(hostile)}\n{random.choice(features)}")
    return output

while True: 
    event, values = window.Read()
#    print(event)
#    print(values)
    output = ""
    if event is None or event == 'Exit':
        break
    if event == 'Generate' and values['_GENIN_'] == 'NPC':
        output = npcgen()
        window.FindElement('_GENOUTPUT_').Update(output)
    if event == 'Generate' and values['_GENIN_'] == 'Problem':
        output = problemgen()
        window.FindElement('_GENOUTPUT_').Update(output)
    if event == 'Generate' and values['_GENIN_'] == 'Urban':
        output = urbangen()
        window.FindElement('_GENOUTPUT_').Update(output)
    if event == 'Generate' and values['_GENIN_'] == 'Wilderness':
        output = wildernessgen()
        window.FindElement('_GENOUTPUT_').Update(output)
    if event == 'Generate' and values['_GENIN_'] == 'One-roll NPC':
        output = onerollnpcgen()
        window.FindElement('_GENOUTPUT_').Update(output)
    if event == 'Generate' and values['_GENIN_'] == 'One-roll Patron':
        output = onerollpatrongen()
        window.FindElement('_GENOUTPUT_').Update(output)
    if event == 'Generate' and values['_GENIN_'] == 'Beast Style':
        output = beaststylegen()
        window.FindElement('_GENOUTPUT_').Update(output)
    if event == '_WEAPONIN_':
        output = weapongen(values['_WEAPONIN_'])
        window.FindElement('_WEAPONOUTPUT_').Update(output)
    if event == '_BEASTINFOINPUT_':
        output = beastinfogen(values['_BEASTINFOINPUT_'])
        window.FindElement('_BEASTINFOOUTPUT_').Update(output)
    if event == '_NPCINFOINPUT_':
        output = npcinfogen(values['_NPCINFOINPUT_'])
        window.FindElement('_NPCINFOOUTPUT_').Update(output)
    if event == "Roll" and values["_ROLLSINPUT_"] and values["_SIDESINPUT_"]:
        try:
            rolloutput = roller(values["_ROLLSINPUT_"], values["_SIDESINPUT_"])
            total = sum(rolloutput)
            output = f'You rolled {values["_ROLLSINPUT_"]}d{values["_SIDESINPUT_"]}. Total: {total}\nRolls: {rolloutput}'
            window.FindElement('_ROLLSOUTPUT_').Update(output)
        except:
            pass

window.Close()
