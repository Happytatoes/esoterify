# utils.py
# menu display and helper functions

# print menu function
def print_menu():
	print("\nmenu:")
	print("e - enter a message")
	print("v - view current message")
	print("r - run a single encryption or decryption")
	print("c - run a chain of encryptions or decryptions")
	print("k - view keys")
	print("l - access the link to the writeup")
	print("m - view menu")
	print("q - quit program\n")

# print options for encryptions / decryptions
def print_options():
	print("\noptions:")
	print("a - caesar cipher (use the previous key times negative 1 to reverse)")
	print("options for encryption:")
	print("b - rsa")
	print("c - aes")
	print("d - chacha20")
	print("options for decryption:")
	print("e - rsa")
	print("f - aes")
	print("g - chacha20\n")

# view keys and encryption names
def view_keys():
	print("\nhere are your keys, in the order they were created:")
	import globals as g
	if len(g.keys) == 0:
		print("\n<no keys stored yet>\n")
	else:
		print("\n<stored keys>\n")
		for i, key in enumerate(g.keys):
			print(f"{i+1}. {g.encryption_names[i]}")
			print(f"   key: {key}\n")