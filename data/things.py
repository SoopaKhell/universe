thingsDict = {
    "wip": ["WORK IN PROGRESS", ("wip",1,1)],
    "universe": [("galactic supercluster", 20, 0.8)],
    "water":[("Hydrogen",1,1),("Oxygen",1,1)],
    "galactic supercluster": [("planetary system", 40, 0.8)],
    "planetary system": [("medieval-wet-planet", 1, 0.4),("modern-wet-planet", 1, 0.4),("lifeless wet planet", 5, 0.5),("rocky planet", 6, 0.6), ("gas giant", 6, 0.6)],
    "gas giant": [("Hydrogen", 1, 1), ("Helium", 1, 1)],
    "rocky planet": [("Iron",1,1), ("Silicon",1,1)],
    "lifeless wet planet": [("lifeless continent",10,0.6),("ocean",1,1), ("sea",12,0.6),("wet-atmosphere", 1, 1), ("lifeless arctic",2,0.5)],
    "medieval-wet-planet": ["wet planet with life", ("medieval-continent",7,0.9),("continent",3,0.5),("life-ocean",1,1),("life-sea",12,0.6),("wet-atmosphere-life", 1, 1),("arctic",2,0.5)],
    "wet-atmosphere-life": ["atmosphere", ("atmosphere-life", 1, 1)],
    "atmosphere-life": ["life", ("hawk", 5, 0.5),("pigeon", 5, 0.5),("pterodactyl", 5, 0.1)],
    "wet-atmosphere": ["atmosphere", ("Nitrogen", 1, 1), ("Helium", 1, 0.5), ("Oxygen", 1, 0.5)],
    "life-ocean": ["ocean", ("water",1,1), ("salt",1,1), ("ocean life", 1, 0.8)],
    "ocean": [("water",1,1), ("salt",1,1)],
    "ocean life": ["life", ("giant squid", 1, 0.1), ("whale", 2, 0.5), ("dolphin", 8, 0.5)],
    "medieval-continent": ["continent", ("medieval-civilization", 1, 1), ("dirt", 1, 1)],
    "lifeless continent": ["continent", ("lifeless dirt", 1, 1)],
    "medieval-civilization": ["civilization", ("medieval-nation", 20, 0.4)],
    "dirt": [("Silicon", 1, 1), ("decayed biomass", 1, 1), ("feces", 1, 0.4)],
    "lifeless dirt": ["dirt", ("Silicon", 1, 1)],
    "medieval-nation": ["medievalNationName", ("medieval-capital", 1, 1), ("medieval-city", 5, 0.4), ("medieval-village", 20, 0.4), ("medieval-farm",13,0.8), ("rural region", 3, 0.8), ("desert region", 2, 0.4)],
    "lifeless arctic": ["arctic", ("snow", 1, 1), ("lifeless dirt", 1, 1)],
    "arctic": [("snow", 1, 1), ("dirt", 1, 1), ("penguin", 24, 0.01)],
    "snow": [("water", 1, 1), ("urine", 1, 0.01)],
    "medieval-capital": ["capital city", ("castle", 1, 1), ("medieval-forum", 1, 1), ("medieval-government-building",1,1), ("medieval-building",22,0.7), ("medieval-house", 29, 0.4)],
    "medieval-forum": ["forum", ("market stall",7,0.7), ("medieval-merchant", 20, 0.3), ("medieval-bureaucrat", 4, 0.3), ("medieval-serf", 10, 0.3),("medieval-farmer", 10, 0.3)],
    "medieval-building": ["building", ("medieval-office", 7, 0.6), ("medieval-bureaucrat", 20, 0.3), ("medieval-merchant", 5, 0.3)],
    "medieval-government-building": ["government building", ("medieval-office", 10, 0.6), ("desk",12,0.7), ("medieval-bureaucrat", 10, 0.3), ("medieval-merchant", 4, 0.3)],
    "medieval-office": ["office", ("desk",7,0.3), ("medieval-bureaucrat", 7, 0.3)],
    "desk": [("medieval-bureaucrat", 1, 0.4)],
    "medieval-city": ["city", ("medieval-forum", 1, 1), ("medieval-building",15,0.6), ("medieval-house", 24, 0.4)],
    "medieval-village": ["village", ("medieval-building",4,0.6), ("medieval-house",15,0.6)],
    "medieval-house": ["house", ("desk",1,0.7), ("dinner table",1,1),("medieval-farmer", 7, 0.7), ("walls", 1, 1)],
    "dinner table": [("plate",7,0.7),("chair",7,0.7)],
    "plate": [("bread",1,0.5),("chicken",1,0.5),("fish",1,0.5)],
    "medieval-farm": ["farm", ("stable", 1, 1), ("field",6,0.6), ("medieval-house", 5, 0.4), ("medieval-farmer",5,0.5), ("medieval-serf",12,0.5)],
    "field": [("crop", 40, 0.8)],
    "stable": [("horse", 4, 0.3)],
    "sea": [("water",1,1), ("salt", 1, 1)],
    "life-sea": ["sea", ("water",1,1), ("salt", 1, 1), ("sea life",1,0.4)],
    "salt": [("Sodium",1,1), ("Chlorine",1,1)],
    "medieval-bureaucrat": ["medievalBureaucratName", ("medieval-bureaucrat-head",1,1),("torso",1,1),("leg",2,1),("arm",2,1),("medieval-attire",1,0.85)],
    "medieval-bureaucrat-head": ["head", ("medieval-bureaucrat-thought",2,0.94)],
    "medieval-bureaucrat-thought": ["medievalBureaucratThought"],
    "medieval-farmer-thought": ["medievalFarmerThought"],
    "medieval-serf-thought": ["medievalSerfThought"],
    "medieval-king-thought": ["medievalKingThought"],
    "medieval-noble-thought": ["medievalNobleThought"],
    "medieval-merchant-thought": ["medievalMerchantThought"],
    "medieval-bureaucrat-thought": ["medievalBureaucratThought"],
    "medieval-farmer-head": ["head", ("medieval-farmer-thought",2,0.94)],
    "medieval-merchant-head": ["head", ("medieval-merchant-thought",2,0.94)],
    "medieval-serf-head": ["head", ("medieval-serf-thought",2,0.94)],
    "medieval-farmer": ["medievalFarmerName", ("medieval-farmer-head",1,1),("torso",1,1),("leg",2,1),("arm",2,1),("medieval-farmer-attire",1,0.85)],
    "medieval-merchant": ["medievalMerchantName", ("medieval-merchant-head",1,1),("torso",1,1),("leg",2,1),("arm",2,1),("medieval-attire",1,0.85)],
    "medieval-noble": ["medievalNobleName", ("medieval-noble-head",1,1),("torso",1,1),("leg",2,1),("arm",2,1),("medieval-attire",1,0.85)],
    "medieval-serf": ["medievalSerfName", ("medieval-serf-head",1,1),("torso",1,1),("leg",2,1),("arm",2,1),("medieval-serf-attire",1,0.85)],
    "medieval-clergy-head": ["head", ("medieval-clergy-thought",2,0.94)],
    "medieval-noble-head": ["head", ("medieval-noble-thought",2,0.94)],
    "castle": [("throne room", 1, 1), ("walls", 1 ,1)],
    "throne room": [("medieval-king", 1, 1), ("medieval-queen", 1, 0.5), ("throne",2,0.5)],
    "medieval-queen": ["Nameless Queen"],
    "medieval-king-head": ["head", ("medieval-king-thought",2,0.94)],
    "medieval-king": ["medievalKingName", ("medieval-king-head",1,1),("torso",1,1),("leg",2,1),("arm",2,1),("medieval-king-attire",1,0.85)],
    "medieval-king-attire": ["attire", ("robe", 1, 1), ("slipper", 2, 1), ("crown", 1, 1)],

    "modern-wet-planet": ["wet planet with life", ("modern-continent",7,0.9),("continent",3,0.5),("life-ocean",1,1),("life-sea",12,0.6),("arctic",2,0.5)],
    "modern-continent": ["continent", ("modern-civilization", 1, 1), ("dirt", 1, 1)],
    "modern-civilization": ["civilization", ("modern-nation", 20, 0.4)],
    "modern-nation": ["modernNationName", ("modern-capital", 1, 1), ("modern-city", 5, 0.4), ("modern-town", 20, 0.4), ("modern-farm",8,0.8), ("rural region", 3, 0.8), ("desert region", 2, 0.4)],
    "modern-town" : ["town", ("park", 2, 0.8), ("modern-building",15,0.7), ("modern-house", 25, 0.4)],
    "modern-capital": ["capital city", ("modern-government-building",2,1), ("park", 1, 1), ("modern-building",22,0.7), ("modern-house", 29, 0.4)],
    "modern-government-building" : ["government building"],
    "modern-city": ["city"],
    "modern-building": ["building"],
    "modern-house" : ["house"],
    "modern-farm": ["farm"],
    "park": [("bench", 10, 0.8), ("pond", 2, 0.6), ("modern-hobo")],
    "modern-hobo": ["hobo"]
}