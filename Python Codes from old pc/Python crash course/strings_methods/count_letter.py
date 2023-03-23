def count_letter(phrase):
    sen = phrase
    sen = sen.replace(" ","").lower()
    result = {}
    for letter in sen:
        if(letter not in result):
            result[letter] = 0
        result[letter] += 1
    return result


x = count_letter("I am niraj chittodiya and @#$#% 545646 12")
print(x)