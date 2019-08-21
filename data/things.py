from colorama import Fore

thingsDict = {
    "wip": [Fore.MAGENTA + "WORK IN PROGRESS" + Fore.WHITE],
    "universe": [("galactic supercluster", 20, 0.8)],
    "water": [("Hydrogen", 1, 1), ("Oxygen", 1, 1)],
    "galactic supercluster": [("galaxy", 20, 0.8)],
    "galaxy": [
        ("yellow-star", 10, 0.8),
        ("dyson-star", 2, 0.08),
        ("yellow-star", 30, 0.8),
        ("red-star", 12, 0.8),
        ("supermassive black hole", 1, 1),
    ],
    "supermassive black hole": [
        ("universe", 1, 1),
        ("black-hole-orbit", 1, 0.4)
    ],
    "black-hole-orbit": [
        "orbiting bodies",
        ("yellow-star", 10, 0.7),
        ("red-star", 10, 0.5)
    ],
    "dyson-star": [
        "dyson sphered star (dim)",
        ("dyson-star-orbit", 1, 0.99),
        ("dyson sphere", 1, 1),
        ("Hydrogen", 1, 1),
        ("Helium", 1, 1),
    ],
    "dyson-sphere": [
        ("wip", 1, 1)
        #google this idk

    ],
    "yellow-star": [
        "star (yellow)",
        ("yellow-star-orbit", 1, 0.99),
        ("Hydrogen", 1, 1),
        ("Helium", 1, 1),
    ],
    "yellow-star-orbit":[
        "orbiting bodies",
        ("medieval-wet-planet", 1, 0.4),
        ("modern-wet-planet", 1, 0.4),
        ("lifeless wet planet", 5, 0.5),
        ("rocky planet", 6, 0.6),
        ("life-gas giant", 2, 0.1),
        ("gas giant", 6, 0.6),
        ("space station", 1, 0.05),
    ],
    "dyson-star-orbit":[
        "orbiting bodies",
        ("medieval-wet-planet", 1, 0.1),
        ("modern-wet-planet", 1, 0.1),
        ("advanced-wet-planet", 1, 1),
        ("lifeless wet planet", 5, 0.5),
        ("rocky planet", 6, 0.6),
        ("life-gas giant", 2, 0.1),
        ("gas giant", 6, 0.6),
        ("space station", 1, 0.05),
    ],
    "red-star": [
        "star (red giant)",
        ("red-star-orbit", 1, 0.999),
        ("Hydrogen", 1, 1),
        ("Helium", 1, 1),
    ],
    "red-star-orbit": [
        "orbiting bodies",
        ("medieval-wet-planet", 1, 0.1),
        ("modern-wet-planet", 1, 0.05),
        ("lifeless wet planet", 5, 0.6),
        ("rocky planet", 6, 0.7),
        ("gas giant", 6, 0.6)
    ],
    "gas giant": [("moon", 24, 0.7),("gas-atmosphere", 1, 1),("Hydrogen", 1, 1), ("Helium", 1, 1)],
    "life-gas giant": ["gas giant", ("life-gas-atmosphere", 1, 1),("moon", 24, 0.6),],
    "life-gas-atmosphere": ["atmosphere", ("gas-atmosphere-life", 1, 1), ("Hydrogen", 1, 1), ("Helium", 1, 1)],
    "gas-atmosphere-life": ["life", ("querblop", 5, 0.7), ("nag nag", 4, 0.1)],
    "gas-atmosphere": [("Hydrogen", 1, 1), ("Helium", 1, 1)],
    "rocky planet": [("moon", 0.7, 1),("Iron", 1, 1), ("Silicon", 1, 1)],
    "lifeless wet planet": [
        ("moon", 0.8, 1),
        ("lifeless continent", 10, 0.6),
        ("ocean", 1, 1),
        ("sea", 12, 0.6),
        ("wet-atmosphere", 1, 1),
        ("lifeless arctic", 2, 0.5),
    ],
    "medieval-wet-planet": [
        "wet planet with life",
        ("moon", 0.8, 1),
        ("medieval-continent", 7, 0.9),
        ("continent", 3, 0.5),
        ("life-ocean", 1, 1),
        ("life-sea", 12, 0.6),
        ("wet-atmosphere-life", 1, 1),
        ("arctic", 2, 0.5),
    ],
    "wet-atmosphere-life": ["atmosphere", ("atmosphere-life", 1, 1)],
    "atmosphere-life": [
        "life",
        ("hawk", 5, 0.5),
        ("pigeon", 5, 0.5),
        ("pterodactyl", 5, 0.1),
    ],
    "wet-atmosphere": [
        "atmosphere",
        ("Nitrogen", 1, 1),
        ("Helium", 1, 0.5),
        ("Oxygen", 1, 0.5),
    ],
    "life-ocean": ["ocean", ("water", 1, 1), ("salt", 1, 1), ("ocean life", 1, 0.8)],
    "ocean": [("water", 1, 1), ("salt", 1, 1)],
    "ocean life": [
        "life",
        ("giant squid", 1, 0.1),
        ("whale", 2, 0.5),
        ("dolphin", 8, 0.5),
    ],
    "medieval-continent": [
        "continent",
        ("medieval-civilization", 1, 1),
        ("dirt", 1, 1),
    ],
    "lifeless continent": ["continent", ("lifeless dirt", 1, 1)],
    "medieval-civilization": ["civilization", ("medieval-nation", 20, 0.4)],
    "dirt": [("Silicon", 1, 1), ("decayed biomass", 1, 1), ("feces", 1, 0.4)],
    "lifeless dirt": ["dirt", ("Silicon", 1, 1)],
    "medieval-nation": [
        "medievalNationName",
        ("medieval-capital", 1, 1),
        ("medieval-city", 5, 0.4),
        ("medieval-village", 20, 0.4),
        ("medieval-farm", 13, 0.8),
        ("life-rural region", 3, 0.8),
        ("desert region", 2, 0.4),
    ],
    "lifeless arctic": ["arctic", ("snow", 1, 1), ("lifeless dirt", 1, 1)],
    "arctic": [("snow", 1, 1), ("dirt", 1, 1), ("penguin", 24, 0.01)],
    "snow": [("water", 1, 1), ("urine", 1, 0.01)],
    "medieval-capital": [
        "capital city",
        ("castle", 1, 1),
        ("medieval-forum", 1, 1),
        ("medieval-government-building", 1, 1),
        ("medieval-building", 22, 0.7),
        ("medieval-house", 29, 0.4),
    ],
    "medieval-forum": [
        "forum",
        ("market stall", 7, 0.7),
        ("medieval-merchant", 20, 0.3),
        ("medieval-bureaucrat", 4, 0.3),
        ("medieval-serf", 10, 0.3),
        ("medieval-farmer", 10, 0.3),
    ],
    "medieval-building": [
        "building",
        ("medieval-office", 7, 0.6),
        ("medieval-bureaucrat", 20, 0.3),
        ("medieval-merchant", 5, 0.3),
    ],
    "medieval-government-building": [
        "government building",
        ("medieval-office", 10, 0.6),
        ("desk", 12, 0.7),
        ("medieval-bureaucrat", 10, 0.3),
        ("medieval-merchant", 4, 0.3),
    ],
    "medieval-office": ["office", ("desk", 7, 0.3), ("medieval-bureaucrat", 7, 0.3)],
    "desk": [("medieval-bureaucrat", 1, 0.4)],
    "medieval-city": [
        "city",
        ("medieval-forum", 1, 1),
        ("medieval-building", 15, 0.6),
        ("medieval-house", 24, 0.4),
    ],
    "medieval-village": [
        "village",
        ("medieval-building", 4, 0.6),
        ("medieval-house", 15, 0.6),
    ],
    "medieval-house": [
        "house",
        ("desk", 1, 0.7),
        ("dinner table", 1, 1),
        ("medieval-farmer", 7, 0.7),
        ("walls", 1, 1),
    ],
    "dinner table": [("plate", 7, 0.7), ("chair", 7, 0.7)],
    "plate": [("bread", 1, 0.5), ("chicken", 1, 0.5), ("fish", 1, 0.5)],
    "medieval-farm": [
        "farm",
        ("stable", 1, 1),
        ("field", 6, 0.6),
        ("medieval-house", 5, 0.4),
        ("medieval-farmer", 5, 0.5),
        ("medieval-serf", 12, 0.5),
    ],
    "field": [("crop", 40, 0.8)],
    "stable": [("horse", 4, 0.3)],
    "sea": [("water", 1, 1), ("salt", 1, 1)],
    "life-sea": ["sea", ("water", 1, 1), ("salt", 1, 1), ("sea life", 1, 0.4)],
    "salt": [("Sodium", 1, 1), ("Chlorine", 1, 1)],
    "medieval-bureaucrat": [
        "medievalBureaucratName",
        ("medieval-bureaucrat-head", 1, 1),
        ("torso", 1, 1),
        ("leg", 2, 1),
        ("arm", 2, 1),
        ("medieval-attire", 1, 0.85),
    ],
    "medieval-bureaucrat-head": ["head", ("medieval-bureaucrat-thought", 2, 0.94)],
    "medieval-bureaucrat-thought": ["medievalBureaucratThought"],
    "medieval-farmer-thought": ["medievalFarmerThought"],
    "medieval-serf-thought": ["medievalSerfThought"],
    "medieval-king-thought": ["medievalKingThought"],
    "medieval-noble-thought": ["medievalNobleThought"],
    "medieval-merchant-thought": ["medievalMerchantThought"],
    "medieval-bureaucrat-thought": ["medievalBureaucratThought"],
    "medieval-farmer-head": ["head", ("medieval-farmer-thought", 2, 0.94)],
    "medieval-merchant-head": ["head", ("medieval-merchant-thought", 2, 0.94)],
    "medieval-serf-head": ["head", ("medieval-serf-thought", 2, 0.94)],
    "medieval-farmer": [
        "medievalFarmerName",
        ("medieval-farmer-head", 1, 1),
        ("torso", 1, 1),
        ("leg", 2, 1),
        ("arm", 2, 1),
        ("medieval-farmer-attire", 1, 0.85),
    ],
    "medieval-merchant": [
        "medievalMerchantName",
        ("medieval-merchant-head", 1, 1),
        ("torso", 1, 1),
        ("leg", 2, 1),
        ("arm", 2, 1),
        ("medieval-attire", 1, 0.85),
    ],
    "medieval-noble": [
        "medievalNobleName",
        ("medieval-noble-head", 1, 1),
        ("torso", 1, 1),
        ("leg", 2, 1),
        ("arm", 2, 1),
        ("medieval-attire", 1, 0.85),
    ],
    "medieval-serf": [
        "medievalSerfName",
        ("medieval-serf-head", 1, 1),
        ("torso", 1, 1),
        ("leg", 2, 1),
        ("arm", 2, 1),
        ("medieval-serf-attire", 1, 0.85),
    ],
    "medieval-clergy-head": ["head", ("medieval-clergy-thought", 2, 0.94)],
    "medieval-noble-head": ["head", ("medieval-noble-thought", 2, 0.94)],
    "castle": [("throne room", 1, 1), ("castle-walls", 1, 1)],
    "castle-walls": ["walls", ("stone", 1, 1)],
    "stone": [("Silicon", 1, 1), ("Carbon", 1, 1)],
    "throne room": [
        ("medieval-king", 1, 1),
        ("medieval-queen", 1, 0.5),
        ("throne", 2, 0.5),
    ],
    "medieval-queen": ["Nameless Queen"],
    "medieval-king-head": ["head", ("medieval-king-thought", 2, 0.94)],
    "medieval-king": [
        "medievalKingName",
        ("medieval-king-head", 1, 1),
        ("torso", 1, 1),
        ("leg", 2, 1),
        ("arm", 2, 1),
        ("medieval-king-attire", 1, 0.85),
    ],
    "medieval-king-attire": [
        "attire",
        ("robe", 1, 1),
        ("slipper", 2, 1),
        ("crown", 1, 1),
    ],
    "crown": [("Gold", 1, 1)],
    "life-rural region": [
        "rural region",
        ("life-forest", 20, 0.3),
        ("life-plain", 20, 0.6),
    ],
    "life-forest": [
        "forest",
        ("dirt", 1, 1),
        ("grass", 1, 1),
        ("forest-life", 1, 1),
        ("tree", 30, 0.85),
    ],
    "tree": [("branch", 20, 0.9), ("tree-trunk", 1, 1)],
    "branch": [("leaf", 15, 0.9)],
    "leaf": [("leaf-blade", 1, 1), ("petiole", 1, 1)],
    "leaf-blade": ["blade", ("plant cell", 30, 0.9)],
    "petiole": [("plant cell", 10, 0.9)],
    "tree-trunk": ["trunk", ("bark", 1, 1)],
    "forest-life": [
        "life",
        ("bird", 10, 0.8),
        ("deer", 5, 0.6),
        ("bear", 2, 0.4),
        ("cat", 4, 0.2),
        ("squirrel", 30, 0.85),
        ("grass", 1, 0.7),
    ],
    "grass": [("blade of grass", 20, 0.8)],
    "blade of grass": [("plant cell", 20, 0.8)],
    "plant cell": [
        ("cell wall", 1, 1),
        ("membrane", 1, 1),
        ("nucleus", 1, 1),
        ("chloroplast", 5, 0.8),
        ("cytoplasm", 1, 1),
        ("ribosome", 35, 0.8),
        ("vacuole", 1, 1),
        ("cytoplasm", 1, 1),
        ("golgi apparatus", 1, 1),
    ],
    "cytoplasm": [
        ("water", 1, 1),
        ("glucose", 10, 0.5)
    ],
    "cellulose": [("Carbon", 1, 1),("Hydrogen", 1, 1),("Oxygen", 1, 1)],
    "nucleus": [("chromosome", 23, 1)],
    "chromosome": [("DNA", 1, 1)],
    "DNA": [("dna-contents", 1, 1)],
    "dna-contents": ["DNAContents"],
    "chloroplast": [("membrane", 1, 1), ("glucose", 3, 0.8), ("chlorophyll", 1, 1)],
    "membrane": [("phospholipid", 20, 0.8), ("proteins")],
    "phospholipid": [("Carbon", 1, 1), ("Hydrogen", 1, 1), ("Phosphorus", 1, 1)],
    "glucose": [("Carbon", 1, 1), ("Hydrogen", 1, 1), ("Oxygen", 1, 1)],
    "life-plain": ["plain", ("grass", 1, 1), ("plain-life", 1, 1)],
    "plain-life": ["life", ("ferret", 32, 0.9), ("rabbit", 32, 0.9), ("grass", 1, 0.9)],
    "plain": [("lifeless dirt", 1, 1)],
    "modern-wet-planet": [
        "wet planet with life",
        ("modern-continent", 7, 0.9),
        ("continent", 3, 0.5),
        ("life-ocean", 1, 1),
        ("life-sea", 12, 0.6),
        ("arctic", 2, 0.5),
    ],
    "advanced-wet-planet": [
        "wet planet with life",
        ("advanced-continent", 7, 0.9),
        ("continent", 3, 0.5),
        ("life-ocean", 1, 1),
        ("life-sea", 12, 0.6),
        ("arctic", 2, 0.5),
    ],
    "advanced-continent": ["continent", ("advanced-civilization", 1, 1), ("dirt", 1, 1)],
    "advanced-civilization": ["civilization", ("advanced-nation", 20, 0.4)],
    "advanced-nation": [
        "advancedNationName"
        # TODO: Made advanced nations/planets with dyson spheres n ships n stuff
        #("advanced-capital", 1, 1),
        #("advanced-city", 5, 0.4),
        #("life-rural region", 3, 0.8),
        #("desert region", 2, 0.4),
    ],

    "modern-continent": ["continent", ("modern-civilization", 1, 1), ("dirt", 1, 1)],
    "modern-civilization": ["civilization", ("modern-nation", 20, 0.4)],
    "modern-nation": [
        "modernNationName",
        ("modern-capital", 1, 1),
        ("modern-city", 5, 0.4),
        ("modern-town", 20, 0.4),
        ("modern-farm", 8, 0.8),
        ("life-rural region", 3, 0.8),
        ("desert region", 2, 0.4),
    ],
    "modern-town": [
        "town",
        ("park", 2, 0.8),
        ("modern-building", 15, 0.7),
        ("modern-house", 25, 0.4),
    ],
    "modern-capital": [
        "capital city",
        ("modern-government-building", 2, 1),
        ("park", 1, 1),
        ("modern-building", 22, 0.7),
        ("modern-house", 29, 0.4),
    ],
    "modern-government-building": ["government building"],
    "modern-city": ["city"],
    "modern-building": ["building"],
    "modern-house": ["house"],
    "modern-farm": ["farm"],
    "park": [("park-bench", 10, 0.8), ("pond", 2, 0.6), ("modern-hobo", 2, 0.5)],
    "pond": [("duck", 4, 0.5), ("pond-water", 1, 1)],
    "pond-water": ["water", ("pond-life", 1, 0.99)],
    "pond-life": [
        "life",
        ("protozoa", 5, 0.8),
        ("algae", 5, 0.8),
        ("pond-hydra", 5, 0.8),
    ],
    "park-bench": ["bench", ("modern-hobo", 1, 0.2)],
    "modern-hobo": [
        "modernHoboName",
        ("modern-hobo-head", 1, 1),
        ("torso", 1, 1),
        ("leg", 2, 1),
        ("arm", 2, 1),
        ("modern-hobo-attire", 1, 0.85),
    ],
    "modern-hobo-head": ["head", ("modern-hobo-thought", 2, 1)],
    "modern-hobo-thought": ["modernHoboThought"],
    "Oxygen": [
        Fore.LIGHTGREEN_EX + "Oxygen" + Fore.WHITE,
        ("Proton", 1, 1),
        ("Neutron", 1, 1),
        ("Electron", 1, 1),
    ],
    "Carbon": [
        Fore.LIGHTGREEN_EX + "Carbon" + Fore.WHITE,
        ("Proton", 1, 1),
        ("Neutron", 1, 1),
        ("Electron", 1, 1),
    ],
    "Phosphorus": [
        Fore.LIGHTGREEN_EX + "Phosphorus" + Fore.WHITE,
        ("Proton", 1, 1),
        ("Neutron", 1, 1),
        ("Electron", 1, 1),
    ],
    "Silicon": [
        Fore.LIGHTGREEN_EX + "Silicon" + Fore.WHITE,
        ("Proton", 1, 1),
        ("Neutron", 1, 1),
        ("Electron", 1, 1),
    ],
    "Iron": [
        Fore.LIGHTGREEN_EX + "Iron" + Fore.WHITE,
        ("Proton", 1, 1),
        ("Neutron", 1, 1),
        ("Electron", 1, 1),
    ],
    "Nitrogen": [
        Fore.LIGHTGREEN_EX + "Nitrogen" + Fore.WHITE,
        ("Proton", 1, 1),
        ("Neutron", 1, 1),
        ("Electron", 1, 1),
    ],
    "Gold": [
        Fore.LIGHTGREEN_EX + "Gold" + Fore.WHITE,
        ("Proton", 1, 1),
        ("Neutron", 1, 1),
        ("Electron", 1, 1),
    ],
    "Hydrogen": [
        Fore.LIGHTGREEN_EX + "Hydrogen" + Fore.WHITE,
        ("Proton", 1, 1),
        ("Neutron", 1, 1),
        ("Electron", 1, 1),
    ],
    "Helium": [
        Fore.LIGHTGREEN_EX + "Helium" + Fore.WHITE,
        ("Proton", 1, 1),
        ("Neutron", 1, 1),
        ("Electron", 1, 1),
    ],
    "Proton": [Fore.GREEN + "Proton" + Fore.WHITE],
    "Neutron": [Fore.LIGHTRED_EX + "Neutron" + Fore.WHITE],
    "Electron": [Fore.BLUE + "Electron" + Fore.WHITE],
}

cannotEnter = ["dna-contents", "wip", "Proton", "Neutron", "Electron"]
