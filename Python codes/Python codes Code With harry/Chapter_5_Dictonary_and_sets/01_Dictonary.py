myDict = {
    "Name": "niraj",
    "Profession": "Student",
    "Interest": "Coding,listening_song",
    "Another_Dict" : {'piyush': 'Ek AAShiq'}
}

# print(type(myDict))
# print(myDict.keys())
# print(myDict.values())

updateDict = {
    "loved_ones": "Family and friends",
    "College life": "Need a girl (smile)"
}

# print(myDict.update(updateDict)
myDict.update(updateDict)
# print(myDict)

# print(myDict["loved_ones"])
print(myDict["Another_Dict"]["piyush"])
