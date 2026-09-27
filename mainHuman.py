from human import human
alive = input("Enter life status (True / False): ")
alive = alive.strip().lower()
if alive == "true":
    alive = True
elif alive == "false":
    alive = False
else:
    print("Wrong input.")
    
foodStatus = input("Can human eat food (True / False): ").strip().lower()
if foodStatus == "true":
    foodStatus = True
elif foodStatus == "false":
    foodStatus = False
else:
    print("Invalid input.")

human1 = human("Poel", "OTF", "Jeans", "Nike", "cap", alive, foodStatus)
human1.walk()
human1.aliveStatus()
human1.sex()
human1.canEat()
human1.torso()
human1.pantsStatus()
human1.hatStatus()