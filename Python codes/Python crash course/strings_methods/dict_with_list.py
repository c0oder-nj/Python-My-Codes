wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key,value in wardrobe.items():
    for color in value:
        print(f"{color} {key}")