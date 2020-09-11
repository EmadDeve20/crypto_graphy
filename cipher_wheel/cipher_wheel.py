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

    try:
        key = input("Enter Your Key: ");key = int(key)
    except:
        print(f"this is {key}, not a number but I set a random number for You!")
        key = random.randint(1,26)

    for i in range(len(message)):
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                if key + j >= 26:
                    while key+j >= 26:
                        key -= 26
                crypto += alphabet[key+j]
                break

    print(f"This is Your secret message: {crypto}")

def uncrypto():
    text = input("Enter Your message(don't use space): ")
    text = text.lower()
    message = ''

    try:
        key = input("Enter Your Key: ");key = int(key)
    except:
        print(f"this is {key}, not a number but I set a random number for You!")
        key = random.randint(1,26)

    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i] == alphabet[j]:
                if key >= 26:
                   while key >= 26:
                        key -= 26

                if j-key < 0:
                    message += alphabet[j-key+26]
                    break

                else:
                    message += alphabet[j-key]
                    break

    print(f"This is your broken message: {message}")


if __name__ == "__main__":
    if choice_mode == 1:
        crypto()
    else:
      uncrypto()

