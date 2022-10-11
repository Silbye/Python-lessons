import os
os.system('cls')

s = input("Enter your text you want to encode: ")

def encode(text):
    encoded = ''
    i = 0
    while(i <= len(text)-1):
        letter_count = 1
        letter = text[i]
        j = i
        while(j < len(text)-1):
            if(text[j] == text[j + 1]):
                letter_count += 1
                j += 1
            else:
                break
        encoded = encoded + str(letter_count) + letter
        i = j + 1
    return encoded

def decode(text):
    decoded = ''
    letter_count = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            letter_count += text[i]
        else:
            decoded = decoded + text[i] * int(letter_count)
            letter_count = ''
    return decoded
print(encode(s))
print(decode(encode(s)))