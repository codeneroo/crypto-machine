
#CRYPTO PROJECTs

#In this scrypt, we code the ROT13 cypher

 
alpha = list('abcdefghijklmnopqrstuvwxyz ')
alpha13 = list()
for index in range(len(alpha)):
	alpha13.append(alpha[(index+13) % 27])
print(alpha13)


response = input("Do you want to decrypt (press 'd') or encrypt (press 'e') ")
user_msg = input("Please pass in a message to be encrypted or decrypted: ")
def encrypt(user_msg):
	encrypted_msg = []
	for letter in user_msg.lower():
		encrypted_msg.append(alpha13[alpha.index(letter)])
	return ''.join(encrypted_msg)

def decrypt(user_msg):
	decrypted_msg = []
	for letter in user_msg.lower():
		decrypted_msg.append(alpha[alpha13.index(letter)])
	return ''.join(decrypted_msg)

if response.lower() == 'e':
	print(encrypt(user_msg))
else:
	print(decrypt(user_msg))
