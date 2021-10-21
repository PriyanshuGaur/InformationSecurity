import numpy as np

key = np.array([
    [3, 10],
    [20, 9]
])
 
key_rows = key.shape[0]
key_columns = key.shape[1]
 
if key_rows != key_columns:
   raise Exception('key must be square matrix!')

if np.linalg.det(key) == 0:
   raise Exception('matrix must have an inverse matrix')


#1
 
raw_message = "beta"
print("raw message: ",raw_message)
 
message = []
 
for i in raw_message.lower():
   current_letter = i
   if current_letter != ' ': #discard blank characters
      letter_index = ord(current_letter)
      message.append(letter_index)
print("message number")
print(message)

if len(message) % key_rows != 0:
   for i in range(0, len(message)):
      message.append(message[i])
      if len(message) % key_rows == 0:
         break
message = np.array(message)
message_length = message.shape[0]
message.resize(int(message_length/key_rows), key_rows)

print("PRIGINAL MESSAGE")
print(message)

encryption = np.matmul(message, key)
encryption = np.remainder(encryption, 26)

print("encrypted")
print(encryption)


from sympy import Matrix

inverse_key = Matrix(key).inv_mod(26)
inverse_key = np.array(inverse_key) #sympy to numpy
inverse_key = inverse_key.astype(int)


print("checking inverse")
print(inverse_key)

decryption = np.matmul(encryption, inverse_key)
decryption = np.remainder(decryption,26)
print("DECRYPTED")
print(decryption)

decryption = decryption.flatten()

print(decryption)

decrypted_message = ""
for i in decryption:
 letter_num = int(i)
 letter = chr(letter_num)
 decrypted_message += letter

print(decrypted_message)