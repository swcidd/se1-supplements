text = input("Enter a text please :) :")
vowels = 0
consonants = 0
others = 0
for ch in text:
    lower_ch = ch.lower()
    if lower_ch == 'a' or lower_ch == 'e' or lower_ch == 'i' or lower_ch == 'o' or lower_ch == 'u':
      vowels += 1
    elif (lower_ch >= 'a' and lower_ch <= 'z'):
        consonants += 1
    else:
        others += 1
print("Vowels:", vowels, ", Consonants:", consonants, " Other:", others)
