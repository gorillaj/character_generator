import random

def buildChar(): 
    
    strength = random.randint(3,18)
    intelligence = random.randint(3,18)
    dexterity = random.randint(3,18)
    wisdom = random.randint(3,18)
    constitution = random.randint(3,18)
    charisma = random.randint(3,18)
    attributes = [strength,intelligence,dexterity,wisdom,constitution,charisma]
    

    print("STR: ",strength)
    print("INT: ",intelligence)
    print("DEX: ",dexterity) 
    print("WIS: ",wisdom)
    print("CON: ",constitution)
    print("CHA: ",charisma)
    
    
    charChoice = ["Fighter", "Magic User", "Cleric", "Thief"]
    if strength > 12 and constitution > 12:
        charChoice.append("Dwarf")
    if strength > 12 and intelligence > 12:
        charChoice.append("Elf")
    if dexterity and constitution > 12:
        charChoice.append("Halfling")
    if strength > 12 and dexterity > 12 and wisdom > 12:
        charChoice.append("Mystic")
    index = 1
    for choiceNum in charChoice:
        print(index, choiceNum)
        index += 1
    choice = input("Select your character class(0 for random): ")
    if choice == 0:
        charClass = random.choice(charChoice)
    choice = int(choice)
    charClass = charChoice[choice-1]
    print(charClass)
    hp = random.randint(1,6)
    if charClass == "Fighter" or "Dwarf":
        hp = random.randint(1,8)
    if charClass == "Magic User" or "Thief":
        hp = random.randint(1,4)
    print("Hit Points: ",hp)
    
    startingGold = random.randint(3,18)
    gold= startingGold*10
    print("Gold: ",gold)
    
    alignments = ['Lawful','Neutral','Chaotic']
    charAlignment = random.choice(alignments)
    print(charAlignment) 
    5
    #armor class is descending ac per Rules Cyclopedia, but could be reversed for ascending ac convention
    ac = 9


    print("Armor Class: ",ac)

    
buildChar()