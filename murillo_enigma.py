# Jayden Murillo
# Made: 12.9.25
# Last Edit: 1.10.26

import os
import inquirer3 # Imports packages for the use of addional features
import time

UPPER_CASE = 65
LOWER_CASE = 97 # ASCII Values for upper case and lower case letters. Also, alphabet size.
ALPHABET_SIZE = 26
message = "Welcome To My Progam" 
key = "banana" # Default key and message for when the users enter the program
real_key = "" # A placeholder variable to have the actual key for a message for the get_key_index function


def prompt_menu(messages, user_choices): # Function that uses inquirer3 list to make it easy to print out a menu for the user with options.
    # messages and user_choices are parameters that we can give values when we call the function to make a menu as we want it
    menu = [
        inquirer3.List("choice", message = messages, choices = user_choices) # Makes the menu using inquirer3 list and by using the
        # parameters we can just assign values to them in order to make the menu/inquirer3 list say what we want and give whatever options we want it to.
    ]


    answer = inquirer3.prompt(menu) # This prompts the menu so it prints it out to the user and they can use it to select what they want
    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code


    return answer['choice'] # This basically returns the inquirer3 list menu so we can just assign values for the parameters to make our menu say what we need and have the options we want to give


def get_key_index(phrase,key, real_key): # Function that gets the key for the message of the user
    if range(len(key)) == range(len(phrase)):
        list_indexes = [] # Placeholder for the key
        for i in range(len(key)):
            if key[i].isalpha():            # Returns the key in iterations if the user's message is the same length
                list_indexes.append(key[i])
        return list_indexes

    else:
        j = 0
        for i in range(len(phrase)):
            if phrase[i].isalpha(): # If the message is smaller or bigger than the key, this makes it so that the key mathces the
                                    # length of the message. If bigger, the key repeats itself.
                real_key += key[j % len(key)]
                j+=1
            else:      
                j+=0  # If there is something other than letters in the users message, the key does not iterate and skips it.
                real_key += " "
        return "".join(real_key) # This returns the actual key for only letters of the message


def vigenere_cipher_encode(phrase, key_index):
    encoded_phrase = ''
    for letter in range(len(phrase)): # This function makes the users message all lower case, then ciphers it, then returns each letter as it was before, uppercase or lowercase depending on how the user's message was.
                                    
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
    for letter in range(len(encoded_phrase)): # This function makes the users encryped message all lower case, then decodes it, then returns each letter as it was before, uppercase or lowercase depending on how the user's encoded message was.
        if encoded_phrase[letter].isalpha():
            phrase_lower = encoded_phrase[letter].lower()
            charset = (UPPER_CASE if phrase_lower.isupper() else LOWER_CASE)


            if encoded_phrase[letter] == phrase_lower:
                decoded_phrase += chr((ord(phrase_lower) - charset - (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset)
            else:
                decoded_phrase += chr((ord(phrase_lower) - charset - (ord(key_index[letter]) - charset)) % ALPHABET_SIZE + charset).upper()
        else:
            decoded_phrase += encoded_phrase[letter]


    return decoded_phrase


def encode_menu():
    global message,key # Makes it so that I am able to use the users message and key

    while True: 
        print(f"[-] Current Message: '{message}' \n[-] Current Key: {key} \n") # Shows the user their message and key
        answer = prompt_menu("Please Select What You Would Like To Do", ["Return To Main Menu","Edit Message", "Edit Key", "Encode Message"]) # Makes inquirer3 menu from prompt_menu function that gives the user options of going back to the main menu, editing their message, editing their key, or encoding their message

        match answer:
            case "Return To Main Menu":
                return # Breaks the while loop and so returns the user to the previous function/menu
            case "Edit Message":
                print(f"[-] Current Message: '{message}'") 
                message_input = input("[-] Please Input A Message: ")
                message = message_input # Makes the message global varible equal what the user inputted, changing the message
                os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code
            case "Edit Key":
                print(f"[-] Current Key: {key}")  # All this does is give the users a menu if they want to change their message, chang their key, encode their message, or go back to the main menu. Then, depending on the option they chose, they are able to do that. This menu loops so that after each option, the users goes back to it. 
                # So if they change their message, it goes back to this menu. 

                while True:
                    key = input("[-] Please Input A Key For The Encoding: ")

                    if key.isalpha():
                        os.system('cls' if os.name == 'nt' else 'clear')
                        encode_menu()  # Clears terminal from previous code
                        # This is a validation loop for the key so that the user has to input a valid key that does not violate any of key's validity conditions. 
                        # If they don't input a valid one, then my program screams at them and tells them their error and then makes them keep inputting until they input a valid one.
                        return key
                    else:
                        print("[!] Error! Key Can Only Be A String (Letters) Without Spaces! Please Try Again!")
                        time.sleep(5) # Delays Code Execution
                        os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code

            case "Encode Message":
                encode() # Calls the encode function if the user picks this option, which will help them encode their message.


def encode():
    global key, message # Makes it so that I am able to use the users message and key

    while True: # Loops the code until the user chooses to exit the function/go to previous menu/funciton.
        print("In Here You Have To Create A File To Encrypt Your Message Or You Can Use The Default File To Do So. Have Fun Encoding!") # Gives the user context of the encoded message option they chose
        answer = prompt_menu("Please Select An Option (P.S. The Default File Has The Default Message So You Have To Overwrite It With Yours)", ["Return To Previous Menu","Overwrite Default File","Overwrite A File","Create New File","Read A File","Encode File Message"]) # Makes inquirer3 menu from prompt_menu function that is customized to let the user choose to create files, overwrite them, read them, and then encode the message in a file

        try: # I used the try..except code in order to make a filenotfound exception for the user if they input a file that does not exists when they choose their option.
            match answer:
                case "Return To Previous Menu":
                    return # Breaks the while loop and so returns the user to the previous function/menu
                case "Overwrite Default File":
                    with open("default.txt", "r") as message_file:
                        text = message_file.read()
                        print(f"[-] Previous Message: '{text}'")
                        time.sleep(1) # Delays Code Execution
                    with open("default.txt", "w+") as message_file: # This option overwrites the users default file that is already made for them. It first reads default.txt and displays what message it has in it to the user. Next it overwrites it with the users new message and displays what the file says after overwriting. After this, the user returns to this functions menu again since it's looped.
                        message_file.write(message)
                        print(f"[-] Overwriting 'default.txt'...") 
                        time.sleep(1) # Delays Code Execution
                        print(f"[-] Current Message: '{message}'")
                        time.sleep(3) # Delays Code Execution
                    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code
                case "Overwrite A File":
                    filename = input("[-] Please Input The Name Of The File You Want To Overwrite (You Can Also Overwrite The Default File Here By Inputting 'default'): ")
                    with open(filename + ".txt", "r") as message_file:
                        text = message_file.read()
                        print(f"[-] Previous Message: '{text}'")
                        time.sleep(1) # Delays Code Execution
                    with open(filename + ".txt", "w+") as message_file: # This option lets the user overwrite any file that they created or the default file. It lets the user input the name of the file they want to overwrite, then it displays to the user the message that file has. After, it overwrites that file with the users new message and then displays that new message thats now in the file to the user. After this, the user returns to this functions menu again since it's looped.
                        message_file.write(message)
                        print(f"[-] Overwriting '{filename + ".txt"}'...") 
                        time.sleep(1) # Delays Code Execution
                        print(f"[-] Current Message: '{message}'")
                        time.sleep(1) # Delays Code Execution
                        print("[-] Returning...")
                        time.sleep(2) # Delays Code Execution
                    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code
                case "Create New File":
                    filename = input("[-] Please Input A Name For The New File: ")
                    with open(filename + ".txt", "w") as message_file:
                        message_file.write(message)
                    print(f"[-] Creating File With Message... ") # This option lets the user create a file for their message. First, it asks the user to input a name for the file they want to create then the file is created and it has the users message written in it. After, it tells the user the file they created and what it says, which is the users message. After this, the user returns to this functions menu again since it's looped.
                    time.sleep(1) # Delays Code Execution
                    print(f"[-] '{filename + ".txt"}' Has Been Created And Now Has The Message: '{message}'")
                    time.sleep(5) # Delays Code Execution
                    print(f"[-] Returning...")
                    time.sleep(1) # Delays Code Execution
                    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code
                case "Read A File":
                    filename = input("[-] Please Input The Name Of The File You Want To Read (P.S. The Default file Is 'default.txt', So You Can Just Input 'default' To Read It): ")
                    with open(filename + ".txt", "r") as message_file:
                        text = message_file.read()
                    print(f"[-] '{filename + ".txt"}' Says: '{text}'") # This option lets the user read any file that has been created or the default file. This asks the user to input a file name and it reads the message that the file they inputted has and then it specifys to the user that that file says a certiain message. After this, the user returns to this functions menu again since it's looped.
                    time.sleep(5) # Delays Code Execution
                    print("[-] Returning...")
                    time.sleep(1) # Delays Code Execution
                    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code
                case "Encode File Message":
                    filename = input("[-] Please Input The Name Of The File With The Message You Want To Encode (P.S. Default File is 'default.txt' So If You Want To Do That File Just Input 'default'): ")
                    with open(filename + ".txt", "r") as file: # This option encodes the users message in a certain file and then asks them if they want to overwrite that encoded message in the file. First it asks the user to input the name of the file they want to encode, then it reads whats in the file and assign a varible to equal the message inside that file in order to be able to fulfill the parameters of the get_key_index and vigenere_cipher_encode functions. Second it assigns varibles to equal the output of the key for that message to fulfill the parameters of the encode function in order to get a variable that is the encoded message.
                        # Then it tells the user the encoded message from that specific file. Third, it gives the user a option to overwrite that encoded message into that same file. If they choose yes then the file is overwritten with the encoded message. If not, then nothing happens and they return to this functions menu since it's looped.
                        phrase = file.read()
                    key_index = get_key_index(phrase,key, real_key)
                    encoded_message = vigenere_cipher_encode(phrase,key_index)
                    print(f"[-] This Is Your Message Encoded From '{filename + ".txt"}': '{encoded_message}'")
                    time.sleep(2) # Delays Code Execution

                    option = prompt_menu("Would You Like To Overwrite The Encoded Message To That File?", ["Yes","No" ]) # Makes inquirer3 menu from prompt_menu function that gives the users a option of overwriting the file they inputted with their encoded message. 

                    match option:
                        case "Yes":
                            with open(filename + ".txt", "w+") as message_file:
                                message_file.write(encoded_message)
                            print(f"[-] Overwriting '{filename + ".txt"}'...") 
                            time.sleep(1) # Delays Code Execution
                            print(f"[-] '{filename + ".txt"}' Now Says: '{encoded_message}'") # This option overwrites the file with the files  now encoded message.
                            time.sleep(1) # Delays Code Execution
                            print("[-] Returning...")
                            time.sleep(4) # Delays Code Execution
                            os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code
                        case "No":
                            print("[-] Returning...") # This option does nothing and just takes the user back to this functions menu
                            time.sleep(1) # Delays Code Execution 
                            os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code

        except Exception as e:
            print(f"[!] An Error Has Occured: {e}")
            time.sleep(4) # Delays Code Execution
            print("[-] Returning...")   # This is when an error occurs. It finds out what went wrong with the code due to, for example, files not existing, and then tells that error or yells at the user. Then it takes the user back to this functions menu.
            time.sleep(1) # Delays Code Execution
            os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code


def decode():
    global key, message # Makes it so that I am able to use the users message and key

    while True: # Loops the code until the user decides to exit the function/ go back to the main menu
        print("In Here You Can Decode Any File With An Encoded Message! Have Fun Decoding! ") # Gives the user context of the encoded message option they chose
        answer = prompt_menu("Please Select An Option (P.S. To Decode A Message, You Have To Have The Same Key As When You Encoded It)", ["Return To Main Menu","Read A File","Decode File Message"]) # Makes inquirer3 menu from prompt_menu function that lets the user choose to return to the main menu, read a file, or decode a certain files message. It also tells the user thaat if they encoded something, they need to keep the same key to decode it.

        try:
            match answer:
                case "Return To Main Menu":
                    return # Breaks the while loop and so returns the user to the previous function/menu
                case "Read A File":
                    filename = input("[-] Please Input The Name Of The File You Want To Read (P.S. The Default file Is default.txt, So You Can Just Input 'Message' To Read It): ")
                    with open(filename + ".txt", "r") as message_file:
                        text = message_file.read()
                    print(f"[-] '{filename + ".txt"}'Says: '{text}'") # This option lets the user read any file that has been created or the default file. This asks the user to input a file name and it reads the message that the file they inputted has and then it specifys to the user that that file says a certiain message. After this, the user returns to this functions menu again since it's looped.
                    time.sleep(5) # Delays Code Execution
                    print("[-] Returning...")
                    time.sleep(1) # Delays Code Execution
                    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code
                case "Decode File Message":
                    filename = input("[-] Please Input The Name Of The File With The Message You Want To Decode: ")
                    with open(filename + ".txt", "r") as file:
                        phrase = file.read()
                        file.seek(0) # This options lets the user decode a files encoded message. It asks the user the name of the file they want to decode, then it assigns a varible to equal the message of that file that is read, then it goes back to the beginning of the file and assigns another varible to equal the message again. This is to fulfilled parameters of the get_key_index and vigenere_cipher_decode funtions in order to properly decode the message. Then it sets a variable that is equal to the key for the encoded message which came from the get_key_index function and this is also to fuilfilled parameters of the decode function. Then it sets a varibale to equal the decoded message which came was returned from the vigenere_cipher_decode function. After, it tells the user that the encoded message was from that specific file and it also shows them what the decoded message is from that file.
                        # Then it gives the user the option to overwrite that specific file with the decoded message.If they choose yes then that file is overwritten with the decoded message, if not then nothing happens and the user is returned to this functions menu since it's looped.
                        encoded_phrase = file.read()
                    key_index = get_key_index(phrase,key, real_key)
                    decoded_message = vigenere_cipher_decode(encoded_phrase, key_index)
                    print(f"[-] This Was Your Encoded Mesage From '{filename + ".txt"}': '{encoded_phrase}'")
                    time.sleep(1) # Delays Code Execution
                    print(f"[-] This Is Your Decoded Message From '{filename + ".txt"}': '{decoded_message}'")
                    time.sleep(1) # Delays Code Execution
                    option = prompt_menu("Would You Like To Overwrite The Decoded Message To That File?", ["Yes","No" ]) # Makes inquirer3 menu from prompt_menu function that gives the users a option of overwriting the file they inputted with their decoded message. 

                    match option:
                        case "Yes":
                            with open(filename + ".txt", "w+") as message_file:
                                message_file.write(decoded_message)
                            print(f"[-] Overwriting '{filename + ".txt"}'...") 
                            time.sleep(1) # Delays Code Execution
                            print(f"[-] '{filename + ".txt"}' Now Says: '{decoded_message}'") # This option overwrites the file with the files now decoded message.
                            time.sleep(1) # Delays Code Execution
                            print("[-] Returning...")
                            time.sleep(4) # Delays Code Execution
                            os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code
                        case "No":
                            print("[-] Returning...") # This option does nothing and just takes the user back to this functions menu since it's looped.
                            time.sleep(1) # Delays Code Execution
                            os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code

        except Exception as e:
            print(f"[!] An Error Has Occured: {e}")
            time.sleep(4) # Delays Code Execution
            print("[-] Returning...") # This is when an error occurs. It finds out what went wrong with the code due to, for example, files not existing, and then tells that error or yells at the user. Then it takes the user back to this functions menu.
            time.sleep(1) # Delays Code Execution
            os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal from previous code


def create_default_file():
    global message # Makes it so that I am able to use the users message

    with open("default.txt",'w+') as file:  # This function just creates the default file for the user called 'default.txt' with the default message. Each time the user runs the program, even if they ran it before and completely changed the file, it will reset and say the default message
        file.write(message)


def main():
    global key,message # Makes it so that I am able to use the users message and key

    print("Welcome To The Enigma Machine! Have Fun Encoding and Decoding! \n") # Welcomes the user into the program once they run it. Only does it once
    create_default_file() # Creates a default file with a default message once the user runs the program. The default message welcomes the user.

    while True: # Loops the main menu until the user exits the program. 
        print("Main Menu")
        answer = prompt_menu("Please Select An Option", ["Exit Program","Encode A Message","Decode A Message"]) # Makes inquirer3 menu from prompt_menu function that gives the user options to exit or encode or decode.

        match answer:
            case "Exit Program":
                print("[!] Thank You For Visting The Enigma Machine!")
                exit() # Exits the user from the program
            case "Encode A Message":
                encode_menu()  # Calls the encode_menu function if the user chooses this option, helping them to edit their message and key, and help them to encoding their message by asking what they'd like to do and by giving some tips.
            case "Decode A Message": 
                decode() # Calls the decode function if the users selects this option, helping the user to see what a file says and by giving them the option to decode a file with their message in it.

if __name__ == "__main__":
    main() # Immediately calls the program/main function when it's the main program being run
