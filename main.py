# main.py
# Main program entry point

#imports
import globals as g
import ciphers
from utils import print_menu, print_options, view_keys
from ciphers import (
	run_caesar, run_aes, run_aes_decrypt,
	run_chacha20, run_chacha20_decrypt,
	run_rsa, run_rsa_decrypt
)

# run a single encryption or decruption
def run_transformation():
	print_options()
	option_selected = input("enter the letter code of the encryption or decryption you would like to run: ")
	if option_selected == "a":
		run_caesar()
	elif option_selected == "b":
		run_rsa()
	elif option_selected == "c":
		run_aes()
	elif option_selected == "d":
		run_chacha20()
	elif option_selected == "e":
		run_rsa_decrypt()
	elif option_selected == "f":
		run_aes_decrypt()
	elif option_selected == "g":
		run_chacha20_decrypt()
	else:
		print("\ninvalid input. read the list of options for encryption and decryption. letters must be lowercase\n")

# main program loop / user menu options
def main():
	print("\nwelcome to esoterify!")
	print_menu()
	while True:
		user_option = input("enter your menu option: ") 
		if user_option == "e":
			if g.current_message != "":
				print("\nthis will override your current message:", g.current_message)
				yes_no = input("are you sure you want to override? (y/n): ")
				if yes_no == "y":
					g.current_message = input("enter your message: ")
				elif yes_no == "n":
					print("override declined")
				else:
					print("invalid command: enter lowercase y or n")
			else:
				g.current_message = input("\nenter your message: ")
			print("")
		elif user_option == "v":
			print("\ncurrent message:", g.current_message, "\n")
		elif user_option == "r":
			if g.current_message == "":
				print("\nthe current message is blank. try again\n")
			else:
				run_transformation()
		elif user_option == "c":
			if hasattr(ciphers, "run_chain"):
				ciphers.run_chain()
			else:
				print("\nchain mode not implemented yet\n")
		elif user_option == "k":
			view_keys()
		elif user_option == "l":
			print("\nfind more info @ happytatoes.com/writings\n")
		elif user_option == "m":
			print_menu()
		elif user_option == "q":
			print("\nbye bye!\n")
			break
		else:
			print("\ninvalid command. type m for list of valid menu options\n")

if __name__ == "__main__":
	main()