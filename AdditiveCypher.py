"""
encrypt function codes the message coming from
the driver function ie main(). The
transformation is based on the mathematical
formula- Code(C)=(Plaintext(P)+Key(K)).


decrypt function decodes the message coming from
the driver function ie main(). The
transformation is based on the mathematical
formula- Plaintext(P)=(Code(C)-Key(K)).

"""


def encrypt(message, key):

    if key < 2 or key > 25:
        print("Key Out of Bound!")          #For invalid key exception

    codedMessage = []

    for letter in message:
        if letter.isalpha():
            letterUnicode = ord(letter.upper()) + key
            if letterUnicode > 90:
                letterUnicode -= 26         #For modulo wrap around logic
            codedMessage.append(chr(letterUnicode))


        if letter==' ':                     #Whilte Space handling.
          codedMessage.append(letter)

    return "".join(codedMessage)



def decrypt(message, key):

    

    if key < 2 or key > 25:                  #For invalid key exception
        print("Key Out Of Bound")

    decodedMessage = []

    for letter in message:
        if letter==' ':                      #Whilte Space handling.
          decodedMessage.append(letter)


        letterUnicode = ord(letter) - key
        if letterUnicode < 65:
                letterUnicode += 26          #For modulo wrap around logic
        decodedMessage.append(chr(letterUnicode).lower())

    return "".join(decodedMessage)


"""

Enciphered text is shown in UpperCase.
Deciphered text is shown in LowerCase.

"""


def main():             #Driver function




    print("ADDITIVE CIPHER PROGRAM ENGINE!\n\n")


    plaintext = "letters in the middle of the frequency ordering are ignored with our frequency match score calculation. This approach to comparing letter frequencies is pretty simple, but it works well enough for our hacking program in the next chapter"#The Original  Message

    print(plaintext)

    print("")



    cyphertext = encrypt(plaintext, 3)   #calling for encryption

    print(cyphertext)

    print("")

    decypheredtext = decrypt(cyphertext, 3) #calling for decryption

    print(decypheredtext)



main()