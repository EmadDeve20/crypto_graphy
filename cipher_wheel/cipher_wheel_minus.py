#!/bin/env python3
import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

try:
    choice_mode = input("""
Enter Your mode:
1 - hide message(default)
2 - Break the secret message
""") ; choice_mode = int(choice_mode)

except:
    choice_mode = 1



def crypto():
    message = input("Enter Your message(don't use space): ")
    message = message.lower()
    crypto = ''
    shift = 0

    try:
        key = input("Enter Your Key(1-26): ");key = int(key)
    except:
        print(f"this is {key}, not a number but I set a random number for You!")
        key = random.randint(1,26)

    for i in range(len(message)):
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                if key + j >= 26:
                    while key+j >= 26:
                        key -= 26
                crypto += alphabet[key+j+shift]
                shift -= 1
                break

    print(f"This is Your secret message: {crypto}")

def uncrypto():
    text = input("Enter Your message(don't use space): ")
    text = text.lower()
    message = ''
    shift = 0

    try:
        key = input("Enter Your Key(1-26): ");key = int(key)
    except:
        print(f"this is {key}, not a number but I set a random number for You! (1-26)")
        key = random.randint(1,26)

    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i] == alphabet[j]:
                if key >= 26:
                   while key >= 26:
                        key -= 26

                if j-key+shift < 0:
                    message += alphabet[j-key+26+shift]
                    shift += 1
                    break

                elif j-key+shift >= 26:
                    message += alphabet[j-key-24]
                    shift += 1
                    break

                else:
                    message += alphabet[j-key+shift]
                    shift += 1  
                    break

    print(f"This is your broken message: {message}")


if __name__ == "__main__":
    if choice_mode == 1:
        crypto()
    else:
      uncrypto()

