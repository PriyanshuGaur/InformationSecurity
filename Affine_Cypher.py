SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
       raise ValueError("Key Out of Bound!")   # modular inverse does not exist
    return x % m


def encrypt(message, key1,key2):

    
    cipherText = []

    for letter in message:
        if letter.isalpha():
            
          cipherText += SYMBOLS[(((key1 * SYMBOLS.find(letter))) + key2)%len(SYMBOLS)]

        else:               #Whilte Space handling.
          cipherText +=letter

    return cipherText



def decrypt(message, key1,key2):

    decodedMessage = []

    for letter in message:

        if letter in SYMBOLS:
           decodedMessage += SYMBOLS[(modinv(key1,len(SYMBOLS))*(SYMBOLS.find(letter) - key2))%len(SYMBOLS)]
        else:
           decodedMessage += letter

    return decodedMessage


"""

Enciphered text is shown in UpperCase.
Deciphered text is shown in LowerCase.

"""

def main():             #Driver function




    print("ADDITIVE CIPHER PROGRAM ENGINE!\n\n")


    plaintext = "Maam is very Intelligent"      #The Original  Message

    print(plaintext)

    print("")


    k1=17
    k2=20
    
    

    cyphertext = encrypt(plaintext,k1,k2)

    print(cyphertext)

    print("")

    decypheredtext = decrypt(cyphertext,k1,k2)

    print(decypheredtext)


main()