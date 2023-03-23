Mydict = {}
print("Hey friend Enter some details for me")
name1 = input("Enter your name: ")
lang1 = input("Enter fav language: ")

name2 = input("Enter your name: ")
lang2 = input("Enter fav language: ")

name3 = input("Enter your name: ")
lang3 = input("Enter fav language: ")

name4 = input("Enter your name: ")
lang4 = input("Enter fav language: ")

friend_dict = {
    name1: lang1,
    name2: lang2,
    name3: lang3,
    name4: lang4
}

Mydict.update(friend_dict)
print(Mydict)