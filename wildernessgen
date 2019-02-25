import random

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

def main():
    encounter_range = random.choice(enc_range)
    encounter_range = encounter_range.replace("1d4", str(random.randint(1,4)))
    encounter_range = encounter_range.replace("1d6", str(random.randint(1,6)))
    print(\
    random.choice(weather) + "\n" + \
    random.choice(nature) + "\n" + \
    random.choice(friendly) + "\n" + \
    encounter_range + "\n" + \
    random.choice(hostile) + "\n" + \
    random.choice(features))
    
main()
