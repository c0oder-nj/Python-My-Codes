t = int(input())
for i in range(t):
    Hidden = input()
    Guess = input()
    Ot_string = ''
    for i in range(5):
        if Hidden[i]==Guess[i]:
            Ot_string += "G"
        else:
            Ot_string += "B"
    print(Ot_string)