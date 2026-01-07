# Jayden Murillo
# Made: 12.9.25
# Last Edit: 12.18.25

import os
import inquirer3

UPPER_CASE = 65
LOWER_CASE = 97
ALPHABET_SIZE = 26
message = "Welcome To My Progam"
key = "banana"
real_key = ""

def prompt_menu(messages, user_choices): # Function that uses inquirer3 list to make it easy to print out a menu for the user with options.
    # messages and user_choices are parameters that we can give values when we call the function to make a menu as we want it
    menu = [
        inquirer3.List("choice", message = messages, choices = user_choices) # Makes the menu using inquirer3 list and by using the 
        # parameters we can just assign values to them in order to make the menu/inquirer3 list say what we want and give whatever options we want it to.
    ]

    answer = inquirer3.prompt(menu) # This prompts the menu so it prints it out to the user and they can use it to select what they want
    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code

    return answer['choice'] # This basically returns the inquirere3 list menu so we can just assign values for the parameters to make our menu say what we need and have the options we want to give



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

# key_index = get_key_index(phrase,key, real_key)
# print(key_index)

# def vigenere_cipher_encode(phrase, key_index):
#     encoded_phrase = ''
#     for letter in range(len(phrase)):
#         if phrase[letter].isalpha():
#             phrase_lower = phrase[letter].lower()
#             charset = (UPPER_CASE if phrase_lower.isupper() else LOWER_CASE)

#             if phrase[letter] == phrase_lower:
#                 encoded_phrase += chr((ord(phrase_lower) - charset + (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset)
#             else:
#                 encoded_phrase += chr((ord(phrase_lower) - charset + (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset).upper()
#         else:
#             encoded_phrase += phrase[letter]

#     return encoded_phrase


# def vigenere_cipher_decode(encoded_phrase, key_index):
#     decoded_phrase = ''
#     for letter in range(len(encoded_phrase)):
#         if phrase[letter].isalpha():
#             phrase_lower = encoded_phrase[letter].lower()
#             charset = (UPPER_CASE if phrase_lower.isupper() else LOWER_CASE)

#             if encoded_phrase[letter] == phrase_lower:
#                 decoded_phrase += chr((ord(phrase_lower) - charset - (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset)
#             else:
#                 decoded_phrase += chr((ord(phrase_lower) - charset - (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset).upper()
#         else:
#             decoded_phrase += encoded_phrase[letter]

#     return decoded_phrase

def encode():
    global message
    global key

    while True:
        print(f"Current Message: {message} \nCurrent Key: {key} \n")
        answer = prompt_menu("Please Select What You Would Like To Do", ["Exit","Edit Message", "Edit Key", "Encode Message"])

        match answer:
            case "Exit":
                return
            case "Edit Message":
                print(f"[-] Previous Message: {message}")
                message_input = input("[-] Please Input A Message: ")
                message = message_input
                print(message)
                os.system('cls' if os.name == 'nt' else 'clear') 
            case "Edit Key":
                key = input("Please Input A Key For The Encryption: ")
                encode()
            case "Encode Message":
                pass


def main():
    print("Welcome To The Enigma Machine! This Is The Main Menu:")

    while True:
        answer = prompt_menu("Please Select An Option", ["Exit","Encode A Message","Decode A Message"])

        match answer:
            case "Exit":
                print("Thank You For Visting!")
                exit()
            case "Encode A Message":
                encode()
            case "Decode A Message":
                pass
        
        



if __name__ == "__main__":
    main()