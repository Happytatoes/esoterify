# ciphers.py
# All encryption and decryption implementations

import globals as g
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64
import random

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
	
	print("\n<step 2: generate key and iv (initialization vector)>\n")
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

# ==================== CHAIN ====================

def run_chain():
	print("\n<chain mode engaged>\n")
	print("info: run multiple encryptions/decryptions in sequence")
	print("enter space-separated letter codes")
	print("example: b c f")
	print("a=caesar b=rsa c=aes d=chacha20 e=rsa decrypt f=aes decrypt g=chacha20 decrypt")

	chain_raw = input("enter chain: ").strip().lower()
	if chain_raw == "":
		print("empty chain. returning to menu")
		return

	chain_codes = [code for code in chain_raw.split() if code != ""]

	operations = {
		"a": ("Caesar", run_caesar),
		"b": ("RSA", run_rsa),
		"c": ("AES-256-CFB", run_aes),
		"d": ("ChaCha20", run_chacha20),
		"e": ("RSA decrypt", run_rsa_decrypt),
		"f": ("AES-256-CFB decrypt", run_aes_decrypt),
		"g": ("ChaCha20 decrypt", run_chacha20_decrypt),
	}

	invalid_codes = [code for code in chain_codes if code not in operations]
	if len(invalid_codes) > 0:
		print("\ninvalid chain code(s):", ' '.join(invalid_codes))
		print("valid codes are: a b c d e f g")
		return

	print("\n<chain summary>\n")
	for i, code in enumerate(chain_codes):
		print(f"{i+1}. {code} - {operations[code][0]}")

	for i, code in enumerate(chain_codes):
		name, operation = operations[code]
		print(f"\n<chain step {i+1}/{len(chain_codes)}: {name}>\n")
		print("message before step:")
		print(g.current_message)
		operation()
		print("message after step:")
		print(g.current_message)

	print("\n<result: chain complete>\n")

# ==================== RSA ====================

# --- HELPER MATH FUNCTIONS ---
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_mod_inverse(e, phi):
    # Extended Euclidean Algorithm to find d
    d_old, d_new = 0, 1
    r_old, r_new = phi, e
    while r_new != 0:
        quotient = r_old // r_new
        r_old, r_new = r_new, r_old - quotient * r_new
        d_old, d_new = d_new, d_old - quotient * d_new
    return d_old % phi

def is_prime(n, k=5): # Miller-Rabin primality test
    if n <= 1: return False
    if n <= 3: return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if p % 2 != 0 and is_prime(p):
            return p
		
def run_rsa():
	print("\n<rsa cipher engaged>\n")
	print("info: asymmetric cipher using public key (e, n) and private key (d, n)")

	print("\n<message to encrypt>\n")
	print(g.current_message)

	print("\n<step 1: generate prime numbers p and q>\n")
	p = generate_prime(16)
	q = generate_prime(16)
	while p == q:
		q = generate_prime(16)
	print(f"p: {p}")
	print(f"q: {q}")

	print("\n<step 2: compute n and phi(n)>\n")
	n = p * q
	phi = (p - 1) * (q - 1)
	print(f"n: {n}")
	print(f"phi(n): {phi}")

	print("\n<step 3: choose public exponent e>\n")
	e = 65537
	while get_gcd(e, phi) != 1:
		e = random.randrange(3, phi, 2)
	print(f"e: {e}")

	print("\n<step 4: compute private exponent d>\n")
	d = get_mod_inverse(e, phi)
	print(f"d: {d}")

	print("\n<step 5: convert message to ASCII integers>\n")
	message_ints = [ord(char) for char in g.current_message]
	print(message_ints)

	print("\n<step 6: encrypt each integer with c = m^e mod n>\n")
	cipher_ints = [pow(m, e, n) for m in message_ints]
	print(cipher_ints)

	print("\n<step 7: convert ciphertext to bytes and encode base64>\n")
	block_size = (n.bit_length() + 7) // 8
	cipher_bytes = b''.join(c.to_bytes(block_size, 'big') for c in cipher_ints)
	print(f"ciphertext bytes (hex): {cipher_bytes.hex()}")
	encoded = base64.b64encode(cipher_bytes).decode('utf-8')
	print(f"base64: {encoded}")

	g.current_message = encoded
	g.keys.append(f"{d}:{n}")
	g.encryption_names.append("RSA")

	print("\n<result: encryption complete>\n")
	print(f"stored key #{len(g.keys)}: {d}:{n}")

def run_rsa_decrypt():
	print("\n<rsa decryption engaged>\n")

	print("\n<step 1: get private key (d:n)>\n")
	if len(g.keys) == 0:
		print("no keys stored!")
		key_raw = input("enter private key (d:n): ")
	else:
		print("stored keys:")
		for i, k in enumerate(g.keys):
			print(f"  {i+1}. {g.encryption_names[i]}: {k}")
		choice = input("\nenter key number or paste private key: ")
		if choice.isdigit() and int(choice) <= len(g.keys):
			key_raw = g.keys[int(choice) - 1]
		else:
			key_raw = choice

	try:
		d_str, n_str = key_raw.split(":")
		d = int(d_str)
		n = int(n_str)
	except ValueError:
		print("invalid key format! use d:n")
		return

	print(f"using d: {d}")
	print(f"using n: {n}")

	print("\n<step 2: decode base64 to ciphertext bytes>\n")
	print(f"base64 input: {g.current_message}")
	try:
		cipher_bytes = base64.b64decode(g.current_message)
	except ValueError:
		print("invalid ciphertext format!")
		return
	print(f"ciphertext bytes (hex): {cipher_bytes.hex()}")

	print("\n<step 3: split bytes into rsa blocks>\n")
	block_size = (n.bit_length() + 7) // 8
	if len(cipher_bytes) % block_size != 0:
		print("invalid ciphertext length!")
		return
	cipher_ints = []
	for i in range(0, len(cipher_bytes), block_size):
		block = cipher_bytes[i:i + block_size]
		cipher_ints.append(int.from_bytes(block, 'big'))
	print(cipher_ints)

	print("\n<step 4: decrypt each integer with m = c^d mod n>\n")
	message_ints = [pow(c, d, n) for c in cipher_ints]
	print(message_ints)

	print("\n<step 5: convert ASCII integers to characters>\n")
	try:
		plaintext = ''.join(chr(m) for m in message_ints)
	except ValueError:
		print("decryption failed: invalid character values")
		return
	print(plaintext)

	g.current_message = plaintext
	print("\n<result: decryption complete>\n")