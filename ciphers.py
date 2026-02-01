# ciphers.py
# All encryption and decryption implementations

import globals as g
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

# ==================== CAESAR ====================

def run_caesar():
	print("\n<caesar cipher engaged>\n")
	print("info: shifts character values by a key amount")
	print("i.e. positive one shifts A -> B, negative two shifts C -> A")
	
	while True:
		try:
			caesar_key = int(input("enter key: "))
			break
		except ValueError:
			print("invalid input. please enter an integer")
	
	print("\n<message to encrypt>\n")
	print(g.current_message)
	
	print("\n<step 1: break into characters>\n")
	char_list = list(g.current_message)
	print(char_list)
	
	print("\n<step 2: convert to ASCII values>\n")
	int_list = [ord(char) for char in char_list]
	print(int_list)
	
	print("\n<step 3: shift by key>\n")
	for i in range(len(int_list)):
		int_list[i] += caesar_key
	print(int_list)
	
	print("\n<step 4: convert back to characters>\n")
	char_list = [chr(val) for val in int_list]
	print(char_list)
	
	print("\n<step 5: rejoin>\n")
	g.current_message = ''.join(char_list)
	print(g.current_message)
	
	print("\n<result: new current message>\n")

# ==================== AES ====================

def run_aes():
	print("\n<aes-256 cipher engaged>\n")
	print("info: industry-standard block cipher, 128-bit blocks with 256-bit key")
	
	key = os.urandom(32)
	iv = os.urandom(16)
	
	print("\n<message to encrypt>\n")
	print(g.current_message)
	
	print("\n<step 1: convert to bytes>\n")
	message_bytes = g.current_message.encode('utf-8')
	print(f"message as bytes: {message_bytes}")
	print(f"length: {len(message_bytes)} bytes")
	
	print("\n<step 2: generate key and iv>\n")
	print(f"key (256 bits): {key.hex()}")
	print(f"iv (128 bits): {iv.hex()}")
	
	print("\n<step 3: encrypt using aes-cfb>\n")
	cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
	encryptor = cipher.encryptor()
	ciphertext = encryptor.update(message_bytes) + encryptor.finalize()
	print(f"encrypted bytes (hex): {ciphertext.hex()}")
	print(f"length: {len(ciphertext)} bytes")
	
	print("\n<step 4: prepend iv and encode base64>\n")
	combined = iv + ciphertext
	print(f"iv + ciphertext (hex): {combined.hex()}")
	encoded = base64.b64encode(combined).decode('utf-8')
	print(f"base64: {encoded}")
	
	g.current_message = encoded
	g.keys.append(key.hex())
	g.encryption_names.append("AES-256-CFB")
	
	print("\n<result: encryption complete>\n")
	print(f"stored key #{len(g.keys)}: {key.hex()}")

def run_aes_decrypt():
	print("\n<aes-256 decryption engaged>\n")
	
	print("\n<step 1: get key>\n")
	if len(g.keys) == 0:
		print("no keys stored!")
		key_hex = input("enter key (hex): ")
	else:
		print("stored keys:")
		for i, k in enumerate(g.keys):
			print(f"  {i+1}. {g.encryption_names[i]}: {k}")
		choice = input("\nenter key number or paste key: ")
		if choice.isdigit() and int(choice) <= len(g.keys):
			key_hex = g.keys[int(choice) - 1]
		else:
			key_hex = choice
	
	try:
		key = bytes.fromhex(key_hex)
	except ValueError:
		print("invalid key format!")
		return
	
	print(f"using key: {key.hex()}")
	
	print("\n<step 2: decode base64>\n")
	print(f"base64 input: {g.current_message}")
	combined = base64.b64decode(g.current_message)
	print(f"decoded (hex): {combined.hex()}")
	
	print("\n<step 3: extract iv>\n")
	iv = combined[:16]
	ciphertext = combined[16:]
	print(f"iv: {iv.hex()}")
	print(f"ciphertext: {ciphertext.hex()}")
	
	print("\n<step 4: decrypt>\n")
	cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
	decryptor = cipher.decryptor()
	plaintext_bytes = decryptor.update(ciphertext) + decryptor.finalize()
	print(f"decrypted bytes: {plaintext_bytes.hex()}")
	
	print("\n<step 5: convert to string>\n")
	plaintext = plaintext_bytes.decode('utf-8')
	print(f"decrypted: {plaintext}")
	
	g.current_message = plaintext
	print("\n<result: decryption complete>\n")

# ==================== CHACHA20 ====================

def run_chacha20():
	print("\n<chacha20 cipher engaged>\n")
	print("info: modern stream cipher, faster than aes without hardware acceleration")
	
	key = os.urandom(32)
	nonce = os.urandom(16)
	
	print("\n<message to encrypt>\n")
	print(g.current_message)
	
	print("\n<step 1: convert to bytes>\n")
	message_bytes = g.current_message.encode('utf-8')
	print(f"message as bytes: {message_bytes}")
	print(f"length: {len(message_bytes)} bytes")
	
	print("\n<step 2: generate key and nonce>\n")
	print(f"key (256 bits): {key.hex()}")
	print(f"nonce (128 bits): {nonce.hex()}")
	
	print("\n<step 3: encrypt using chacha20>\n")
	algorithm = algorithms.ChaCha20(key, nonce)
	cipher = Cipher(algorithm, mode=None, backend=default_backend())
	encryptor = cipher.encryptor()
	ciphertext = encryptor.update(message_bytes) + encryptor.finalize()
	print(f"encrypted bytes (hex): {ciphertext.hex()}")
	print(f"length: {len(ciphertext)} bytes")
	
	print("\n<step 4: prepend nonce and encode base64>\n")
	combined = nonce + ciphertext
	print(f"nonce + ciphertext (hex): {combined.hex()}")
	encoded = base64.b64encode(combined).decode('utf-8')
	print(f"base64: {encoded}")
	
	g.current_message = encoded
	g.keys.append(key.hex())
	g.encryption_names.append("ChaCha20")
	
	print("\n<result: encryption complete>\n")
	print(f"stored key #{len(g.keys)}: {key.hex()}")

def run_chacha20_decrypt():
	print("\n<chacha20 decryption engaged>\n")
	
	print("\n<step 1: get key>\n")
	if len(g.keys) == 0:
		print("no keys stored!")
		key_hex = input("enter key (hex): ")
	else:
		print("stored keys:")
		for i, k in enumerate(g.keys):
			print(f"  {i+1}. {g.encryption_names[i]}: {k}")
		choice = input("\nenter key number or paste key: ")
		if choice.isdigit() and int(choice) <= len(g.keys):
			key_hex = g.keys[int(choice) - 1]
		else:
			key_hex = choice
	
	try:
		key = bytes.fromhex(key_hex)
	except ValueError:
		print("invalid key format!")
		return
	
	print(f"using key: {key.hex()}")
	
	print("\n<step 2: decode base64>\n")
	print(f"base64 input: {g.current_message}")
	combined = base64.b64decode(g.current_message)
	print(f"decoded (hex): {combined.hex()}")
	
	print("\n<step 3: extract nonce>\n")
	nonce = combined[:16]
	ciphertext = combined[16:]
	print(f"nonce: {nonce.hex()}")
	print(f"ciphertext: {ciphertext.hex()}")
	
	print("\n<step 4: decrypt>\n")
	algorithm = algorithms.ChaCha20(key, nonce)
	cipher = Cipher(algorithm, mode=None, backend=default_backend())
	decryptor = cipher.decryptor()
	plaintext_bytes = decryptor.update(ciphertext) + decryptor.finalize()
	print(f"decrypted bytes: {plaintext_bytes.hex()}")
	
	print("\n<step 5: convert to string>\n")
	plaintext = plaintext_bytes.decode('utf-8')
	print(f"decrypted: {plaintext}")
	
	g.current_message = plaintext
	print("\n<result: decryption complete>\n")

# ==================== RSA (placeholder) ====================

def run_rsa():
	print("\nrsa not implemented yet\n")

def run_rsa_decrypt():
	print("\nrsa decryption not implemented yet\n")