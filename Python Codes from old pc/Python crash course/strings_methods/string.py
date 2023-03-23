def initials(phrase):
    l1 = phrase.split()
    words = []
    ans = ""
    for word in l1:
        words.append(word[0].upper())
    for single_word in words:
        ans += single_word
    return ans

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS