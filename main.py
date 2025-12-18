# Jayden Murillo
# Made: 12.9.25
# Last Edit: 12.18.25

import os
# import inquirer3

UPPER_CASE = 65
LOWER_CASE = 97
ALPHABET_SIZE = 26
phrase = str(input("[-] Please Input A Phrase: "))
key = "banana"
real_key = ""

def get_key_index(phrase,key, real_key):
    if range(len(key)) == range(len(phrase)):
        list_indexes = []
        for i in range(len(key)):
            if key[i].isalpha():
                list_indexes.append(key[i])
                print(list_indexes)
        return list_indexes

    else:
        j = 0
        for i in range(len(phrase)):
            if phrase[i].isalpha():
                real_key += key[j % len(key)]
                j+=1
            else: 
                j+=0
                real_key += " "
            
        return "".join(real_key)

key_index = get_key_index(phrase,key, real_key)
print(key_index)

def vigenere_cipher_encode(phrase, key_index):
    encoded_phrase = ''
    for letter in range(len(phrase)):
        if phrase[letter].isalpha():
            phrase_lower = phrase[letter].lower()
            charset = (UPPER_CASE if phrase_lower.isupper() else LOWER_CASE)

            if phrase[letter] == phrase_lower:
                encoded_phrase += chr((ord(phrase_lower) - charset + (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset)
            else:
                encoded_phrase += chr((ord(phrase_lower) - charset + (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset).upper()
        else:
            encoded_phrase += phrase[letter]

    return encoded_phrase


def vigenere_cipher_decode(encoded_phrase, key_index):
    decoded_phrase = ''
    for letter in range(len(encoded_phrase)):
        if phrase[letter].isalpha():
            phrase_lower = encoded_phrase[letter].lower()
            charset = (UPPER_CASE if phrase_lower.isupper() else LOWER_CASE)

            if encoded_phrase[letter] == phrase_lower:
                decoded_phrase += chr((ord(phrase_lower) - charset - (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset)
            else:
                decoded_phrase += chr((ord(phrase_lower) - charset - (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset).upper()
        else:
            decoded_phrase += encoded_phrase[letter]

    return decoded_phrase

def main():
    encoded_phrase = vigenere_cipher_encode(phrase,key_index)
    decoded_phrase = vigenere_cipher_decode(encoded_phrase, key_index)
    print(encoded_phrase)
    print(decoded_phrase)


if __name__ == "__main__":
    main()