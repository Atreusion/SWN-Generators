import random

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

def main():
    conflict = random.choice(list(conflict_dict.items()))
    focus = random.choice(conflict[1]["Focus"])
    situation = random.choice(conflict[1]["Situation"])
    restraint = random.choice(restraint_list)
    twist = random.choice(twist_list)
    print(\
    conflict[0] + " Situation: " + situation + "\n" + \
    conflict[0] + " Focus: " + focus + "\n\
    Restraint: " + restraint + "\n\
    Twist: " + twist)
    
main()
