import sys
import random
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
  
layout = [[sg.Text('Choose generator:'), sg.InputCombo(('NPC', 'Problem', 'Urban', 'Wilderness'), size=(20, 1), key='_IN_')],
          [sg.Multiline('Generator info', size=(45,10), key='_OUTPUT_')],
          [sg.Button('Roll'), sg.Button('Exit')]]
  
window = sg.Window('SWN Generator').Layout(layout)
  
while True: 
    event, values = window.Read()
    print(event)
    print(values)
    output = ""
    if event is None or event == 'Exit':
        break
    if event == 'Roll' and values['_IN_'] == 'NPC':
        print("NPC")
        output = npcgen()
    if event == 'Roll' and values['_IN_'] == 'Problem':
        output = "Problem"
    if event == 'Roll' and values['_IN_'] == 'Urban':
        output = "Urban"
    if event == 'Roll' and values['_IN_'] == 'Wilderness':
        output = "Wilderness"
    window.FindElement('_OUTPUT_').Update(output)

window.Close()

def npcgen():
    manner = ["Ingratiating and cloying", "Grim suspicion of the PCs or their backers", "Xenophilic interest in the novelty of the PCs", "Pragmatic and businesslike", "Romantically interested in one or more PCs", "A slimy used-gravcar dealer’s approach", "Wide-eyed awe at the PCs", "Cool and superior attitude toward PC \"hirelings\"", "Benevolently patronizing toward outsiders", "Sweaty-palmed need or desperation", "Xenophobic mistrust of the PCs", "Idealistic enthusiasm for a potentially shared cause", "Somewhat intoxicated by recent indulgence", "Smoothly persuasive and reasonable", "Visibly uncomfortable with the PCs", "Grossly overconfident in PC abilities", "Somewhat frightened by the PCs", "Deeply misunderstanding the PCs’ culture", "Extremely well-informed about the PCs’ past", "Distracted by their current situation"]
    outcome = ["They’ll screw the PCs over even at their own cost", "They firmly intend to actively betray the PCs", "They won’t keep the deal unless driven to it", "They plan to twist the deal to their own advantage", "They won’t keep their word unless it’s profitable", "They’ll flinch from paying up when the time comes", "They mean to keep the deal, but are reluctant", "They’ll keep most of the deal, but not all of it", "They’ll keep the deal slowly and grudgingly", "They’ll keep the deal but won’t go out of their way", "They’ll be reasonably punctual about the deal", "They’ll want a further small favor to pay up on it", "They’ll keep the deal in a way that helps them", "They’ll keep the deal if it’s still good for them", "They’ll offer a bonus for an additional favor", "Trustworthy as long as the deal won’t hurt them", "Trustworthy, with the NPC following through", "They’ll be very fair in keeping to their agreements", "They’ll keep bargains even to their own cost", "Complete and righteous integrity to the bitter end"]
    motivation = ["An ambition for greater social status", "Greed for wealth and indulgent riches", "Protect a loved one who is somehow imperiled", "A sheer sadistic love of inflicting pain and suffering", "Hedonistic enjoyment of pleasing company", "Searching out hidden knowledge or science", "Establishing or promoting a cultural institution", "Avenging a grievous wrong to them or a loved one", "Promoting their religion and living out their faith", "Winning the love of a particular person", "Winning glory and fame in their profession", "Dodging an enemy who is pursuing them", "Driving out or killing an enemy group", "Deposing a rival to them in their line of work", "Getting away from this world or society", "Promote a friend or offspring’s career or future", "Taking control of a property or piece of land", "Building a structure or a complex prototype tech", "Perform or create their art to vast acclaim", "Redeem themselves from a prior failure"]
    want =["Bring them an exotic piece of tech", "Convince someone to meet with the NPC", "Kill a particular NPC", "Kidnap or non-fatally eliminate a particular NPC", "Pay them a large amount of money", "Take a message to someone hard to reach", "Acquire a tech component that’s hard to get", "Find proof of a particular NPC’s malfeasance", "Locate a missing NPC", "Bring someone to a destination via dangerous travel", "Retrieve a lost or stolen object", "Defend someone from an impending attack", "Burn down or destroy a particular structure", "Explore a dangerous or remote location", "Steal something from a rival NPC or group", "Intimidate a rival into ceasing their course of action", "Commit a minor crime to aid the NPC", "Trick a rival into doing something", "Rescue an NPC from a dire situation", "Force a person or group to leave an area"]
    power = ["They’re just really appealing and sympathetic to PCs", "They have considerable liquid funds", "They control the use of large amounts of violence", "They have a position of great social status", "They’re a good friend of an important local leader", "They have blackmail info on the PCs", "They have considerable legal influence here", "They have tech the PCs might reasonably want", "They can get the PCs into a place they want to go", "They know where significant wealth can be found", "They have information about the PCs’ current goal", "An NPC the PCs need has implicit trust in them", "The NPC can threaten someone the PCs like", "They control a business relevant to PC needs", "They have considerable criminal contacts", "They have pull with the local religion", "They know a great many corrupt politicians", "They can alert the PCs to an unexpected peril", "They’re able to push a goal the PCs currently have", "They can get the PCs useful permits and rights"]
    hook = ["A particular odd style of dress", "An amputation or other maiming", "Visible cyberware or prosthetics", "Unusual hair, skin, or eye colors", "Scarring, either intentional or from old injuries", "Tic-like overuse of a particular word or phrase", "Specific unusual fragrance or cologne", "Constant fiddling with a particular item", "Visible signs of drug use", "Always seems to be in one particular mood", "Wears badges or marks of allegiance to a cause", "Extremely slow or fast pace of speech", "Constantly with a drink to hand", "Always complaining about a group or organization", "Paranoid, possibly for justifiable reasons", "Insists on a particular location for all meetings", "Communicates strictly through a third party", "Abnormally obese, emaciated, tall, or short", "Always found with henchmen or friends"]
    arabic_male = ["Aamir", "Ayub", "Binyamin", "Efraim", "Ibrahim", "Ilyas", "Ismail", "Jibril", "Jumanah", "Kazi", "Lut", "Matta", "Mohammed", "Mubarak", "Mustafa", "Nazir", "Rahim", "Reza", "Sharif", "Taimur", "Usman", "Yakub", "Yusuf", "Zakariya", "Zubair"]
    arabic_female = ["Aisha", "Alimah", "Badia", "Bisharah", "Chanda", "Daliya", "Fatimah", "Ghania", "Halah", "Kaylah", "Khayrah", "Layla", "Mina", "Munisa", "Mysha", "Naimah", "Nissa", "Nura", "Parveen", "Rana", "Shalha", "Suhira", "Tahirah", "Yasmin", "Zulehka"]
    arabic_surname = ["Aisha", "Alimah", "Badia", "Bisharah", "Chanda", "Daliya", "Fatimah", "Ghania", "Halah", "Kaylah", "Khayrah", "Layla", "Mina", "Munisa", "Mysha", "Naimah", "Nissa", "Nura", "Parveen", "Rana", "Shalha", "Suhira", "Tahirah", "Yasmin", "Zulehka"]
    chinese_male = ["Aiguo", "Bohai", "Chao", "Dai", "Dawei", "Duyi", "Fa", "Fu", "Gui", "Hong", "Jianyu", "Kang", "Li", "Niu", "Peng", "Quan", "Ru", "Shen", "Shi", "Song", "Tao", "Xue", "Yi", "Yuan", "Zian"]
    chinese_female = ["Biyu", "Changying", "Daiyu", "Huidai", "Huiliang", "Jia", "Jingfei", "Lan", "Liling", "Liu", "Meili", "Niu", "Peizhi", "Qiao", "Qing", "Ruolan", "Shu", "Suyin", "Ting", "Xia", "Xiaowen", "Xiulan", "Ya", "Ying", "Zhilan"]
    chinese_surname = ["Bai", "Cao", "Chen", "Cui", "Ding", "Du", "Fang", "Fu", "Guo", "Han", "Hao", "Huang", "Lei", "Li", "Liang", "Liu", "Long", "Song", "Tan", "Tang", "Wang", "Wu", "Xing", "Yang", "Zhang"]
    english_male = ["Adam", "Albert", "Alfred", "Allan", "Archibald", "Arthur", "Basil", "Charles", "Colin", "Donald", "Douglas", "Edgar", "Edmund", "Edward", "George", "Harold", "Henry", "Ian", "James", "John", "Lewis", "Oliver", "Philip", "Richard", "William"]
    english_female = ["Abigail", "Anne", "Beatrice", "Blanche", "Catherine", "Charlotte", "Claire", "Eleanor", "Elizabeth", "Emily", "Emma", "Georgia", "Harriet", "Joan", "Judy", "Julia", "Lucy", "Lydia", "Margaret", "Mary", "Molly", "Nora", "Rosie", "Sarah", "Victoria"]
    english_surname = ["Barker", "Brown", "Butler", "Carter", "Chapman", "Collins", "Cook", "Davies", "Gray", "Green", "Harris", "Jackson", "Jones", "Lloyd", "Miller", "Roberts", "Smith", "Taylor", "Thomas", "Turner", "Watson", "White", "Williams", "Wood", "Young"]
    greek_male = ["Alexander", "Alexius", "Anastasius", "Christodoulos", "Christos", "Damian", "Dimitris", "Dysmas", "Elias", "Giorgos", "Ioannis", "Konstantinos", "Lambros", "Leonidas", "Marcos", "Miltiades", "Nestor", "Nikos", "Orestes", "Petros", "Simon", "Stavros", "Theodore", "Vassilios", "Yannis"]
    greek_female = ["Alexandra", "Amalia", "Callisto", "Charis", "Chloe", "Dorothea", "Elena", "Eudoxia", "Giada", "Helena", "Ioanna", "Lydia", "Melania", "Melissa", "Nika", "Nikolina", "Olympias", "Philippa", "Phoebe", "Sophia", "Theodora", "Valentina", "Valeria", "Yianna", "Zoe"]
    greek_surname = ["Andreas", "Argyros", "Dimitriou", "Floros", "Gavras", "Ioannidis", "Katsaros", "Kyrkos", "Leventis", "Makris", "Metaxas", "Nikolaidis", "Pallis", "Pappas", "Petrou", "Raptis", "Simonides", "Spiros", "Stavros", "Stephanidis", "Stratigos", "Terzis", "Theodorou", "Vasiliadis", "Yannakakis"]
    indian_male = ["Amrit", "Ashok", "Chand", "Dinesh", "Gobind", "Harinder", "Jagdish", "Johar", "Kurien", "Lakshman", "Madhav", "Mahinder", "Mohal", "Narinder", "Nikhil", "Omrao", "Prasad", "Pratap", "Ranjit", "Sanjay", "Shankar", "Thakur", "Vijay", "Vipul", "Yash"]
    indian_female = ["Amala", "Asha", "Chandra", "Devika", "Esha", "Gita", "Indira", "Indrani", "Jaya", "Jayanti", "Kiri", "Lalita", "Malati", "Mira", "Mohana", "Neela", "Nita", "Rajani", "Sarala", "Sarika", "Sheela", "Sunita", "Trishna", "Usha", "Vasanta"]
    indian_surname = ["Achari", "Banerjee", "Bhatnagar", "Bose", "Chauhan", "Chopra", "Das", "Dutta", "Gupta", "Johar", "Kapoor", "Mahajan", "Malhotra", "Mehra", "Nehru", "Patil", "Rao", "Saxena", "Shah", "Sharma", "Singh", "Trivedi", "Venkatesan", "Verma", "Yadav"]
    japanese_male = ["Akira", "Daisuke", "Fukashi", "Goro", "Hiro", "Hiroya", "Hotaka", "Katsu", "Katsuto", "Keishuu", "Kyuuto", "Mikiya", "Mitsunobu", "Mitsuru", "Naruhiko", "Nobu", "Shigeo", "Shigeto", "Shou", "Shuji", "Takaharu", "Teruaki", "Tetsushi", "Tsukasa", "Yasuharu"]
    japanese_female = ["Aemi", "Airi", "Ako", "Ayu", "Chikaze", "Eriko", "Hina", "Kaori", "Keiko", "Kyouka", "Mayumi", "Miho", "Namiko", "Natsu", "Nobuko", "Rei", "Ririsa", "Sakimi", "Shihoko", "Shika", "Tsukiko", "Tsuzune", "Yoriko", "Yorimi", "Yoshiko"]
    japanese_surname = ["Abe", "Arakaki", "Endo", "Fujiwara", "Goto", "Ito", "Kikuchi", "Kinjo", "Kobayashi", "Koga", "Komatsu", "Maeda", "Nakamura", "Narita", "Ochi", "Oshiro", "Saito", "Sakamoto", "Sato", "Suzuki", "Takahashi", "Tanaka", "Watanabe", "Yamamoto", "Yamasaki"]
    latin_male = ["Agrippa", "Appius", "Aulus", "Caeso", "Decimus", "Faustus", "Gaius", "Gnaeus", "Hostus", "Lucius", "Mamercus", "Manius", "Marcus", "Mettius", "Nonus", "Numerius", "Opiter", "Paulus", "Proculus", "Publius", "Quintus", "Servius", "Tiberius", "Titus", "Volescus"]
    latin_female = ["Appia", "Aula", "Caesula", "Decima", "Fausta", "Gaia", "Gnaea", "Hosta", "Lucia", "Maio", "Marcia", "Maxima", "Mettia", "Nona", "Numeria", "Octavia", "Postuma", "Prima", "Procula", "Septima", "Servia", "Tertia", "Tiberia", "Titia", "Vibia"]
    latin_surname = ["Antius", "Aurius", "Barbatius", "Calidius", "Cornelius", "Decius", "Fabius", "Flavius", "Galerius", "Horatius", "Julius", "Juventius", "Licinius", "Marius", "Minicius", "Nerius", "Octavius", "Pompeius", "Quinctius", "Rutilius", "Sextius", "Titius", "Ulpius", "Valerius", "Vitellius"]
    nigerian_male = ["Adesegun", "Akintola", "Amabere", "Arikawe", "Asagwara", "Chidubem", "Chinedu", "Chiwetei", "Damilola", "Esangbedo", "Ezenwoye", "Folarin", "Genechi", "Idowu", "Kelechi", "Ketanndu", "Melubari", "Nkanta", "Obafemi", "Olatunde", "Olumide", "Tombari", "Udofia", "Uyoata", "Uzochi"]
    nigerian_female = ["Abike", "Adesuwa", "Adunola", "Anguli", "Arewa", "Asari", "Bisola", "Chioma", "Eduwa", "Emilohi", "Fehintola", "Folasade", "Mahparah", "Minika", "Nkolika", "Nkoyo", "Nuanae", "Obioma", "Olafemi", "Shanumi", "Sominabo", "Suliat", "Tariere", "Temedire", "Yemisi"]
    nigerian_surname = ["Adegboye", "Adeniyi", "Adeyeku", "Adunola", "Agbaje", "Akpan", "Akpehi", "Aliki", "Asuni", "Babangida", "Ekim", "Ezeiruaku", "Fabiola", "Fasola", "Nwokolo", "Nzeocha", "Ojo", "Okonkwo", "Okoye", "Olaniyan", "Olawale", "Olumese", "Onajobi", "Soyinka", "Yamusa"]
    russian_male = ["Aleksandr", "Andrei", "Arkady", "Boris", "Dmitri", "Dominik", "Grigory", "Igor", "Ilya", "Ivan", "Kiril", "Konstantin", "Leonid", "Nikolai", "Oleg", "Pavel", "Petr", "Sergei", "Stepan", "Valentin", "Vasily", "Viktor", "Yakov", "Yegor", "Yuri"]
    russian_female = ["Aleksandra", "Anastasia", "Anja", "Catarina", "Devora", "Dima", "Ekaterina", "Eva", "Irina", "Karolina", "Katlina", "Kira", "Ludmilla", "Mara", "Nadezdha", "Nastassia", "Natalya", "Oksana", "Olena", "Olga", "Sofia", "Svetlana", "Tatyana", "Vilma", "Yelena"]
    russian_surname = ["Abelev", "Bobrikov", "Chemerkin", "Gogunov", "Gurov", "Iltchenko", "Kavelin", "Komarov", "Korovin", "Kurnikov", "Lebedev", "Litvak", "Mekhdiev", "Muraviov", "Nikitin", "Ortov", "Peshkov", "Romasko", "Shvedov", "Sikorski", "Stolypin", "Turov", "Volokh", "Zaitsev", "Zhukov"]
    spanish_male = ["Alejandro", "Alonso", "Amelio", "Armando", "Bernardo", "Carlos", "Cesar", "Diego", "Emilio", "Estevan", "Felipe", "Francisco", "Guillermo", "Javier", "Jose", "Juan", "Julio", "Luis", "Pedro", "Raul", "Ricardo", "Salvador", "Santiago", "Valeriano", "Vicente"]
    spanish_female = ["Adalina", "Aleta", "Ana", "Ascencion", "Beatriz", "Carmela", "Celia", "Dolores", "Elena", "Emelina", "Felipa", "Inez", "Isabel", "Jacinta", "Lucia", "Lupe", "Maria", "Marta", "Nina", "Paloma", "Rafaela", "Soledad", "Teresa", "Valencia", "Zenaida"]
    spanish_surname = ["Arellano", "Arispana", "Borrego", "Carderas", "Carranzo", "Cordova", "Enciso", "Espejo", "Gavilan", "Guerra", "Guillen", "Huertas", "Illan", "Jurado", "Moretta", "Motolinia", "Pancorbo", "Paredes", "Quesada", "Roma", "Rubiera", "Santoro", "Torrillas", "Vera", "Vivero"]
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
    output = "NPC Name: " + first_name + " " + last_name + "\n\
    Age: " + age + "\n\
    Gender: " + gender + "\n\
    Culture: " + culture_name + "\n\
    Manner: " + npc_manner + "\n\
    Outcome: " + npc_outcome + "\n\
    Motivation: " + npc_motivation + "\n\
    Want: " + npc_want + "\n\
    Power: " + npc_power + "\n\
    Hook: " + npc_hook
    return output
  
