import random

woman = []
man = []
place = []
he_said = []
she_said = []
consequence = ["winning the battle", "obtaining all seven Dragon Balls", "drinking a poorly made cup of tea", "getting a parking fine"]

for i in range(0,3):
    location = input("Where is this happening? ")
    place.append(location)

maleOrFemale = input("Is your character a male or female? ")
maleOrFemale.lower()
if maleOrFemale == "male":
    for i in range(0,3):
        male_character = input("Input male character: ")
        
        man.append(male_character)
       

    for i in range(0,3):
        male_speech = input("What did he say? (add puntuation): ")
        he_said.append(male_speech)


    print(random.choice(man) + " said '" + random.choice(he_said) + "' while at " + random.choice(place) + 
          " which resulted in him " + random.choice(consequence))
elif maleOrFemale == "female":
    for i in range(0,3):
        female_character = input("Input female character: ")
        woman.append(female_character)

    for i in range(0,3):
        female_speech = input("What did she say? (add puntuation): ")
        she_said.append(female_speech)

    print(random.choice(woman) + " said '" + random.choice(she_said) + "' while at " + random.choice(place) + 
          " which resulted in her " + random.choice(consequence))
else:
    print("What in tarnation? Somethin's gon wrong!")