L = ['Niraj','Nitesh','Sahil','Harsh','Milan']

for item in L:
    name = item
    name_first_char = name[0]
    if name_first_char == 'n' or name_first_char == 'N':
        print('Good morning: '+name)
    else:
        pass