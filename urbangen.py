import random

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

def main():
    print(\
    random.choice(venue) + "\n" + \
    random.choice(pc_involvment) + "\n" + \
    random.choice(nature) + "\n" + \
    random.choice(conflict) + "\n" + \
    random.choice(antagonists) + "\n" + \
    random.choice(features))
    
main()
