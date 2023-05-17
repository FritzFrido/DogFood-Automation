time = int(input("Wieviel Uhr ist es?"))
dogHunger = input("Hat der Hund großen Hunger? Y (Ja) N (Nein)")

if time < 1200:
    print("Der Hund möchte frühstücken!")
elif time < 1800:
    print("Der Hund möchte mittagessen!")
elif time <= 2000:
    print("Der Hund möchte abendessen!")
else:
    print("Der Hund hat keinen Hunger..")

