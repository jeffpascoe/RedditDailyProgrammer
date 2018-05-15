import string
CONST_ALPH = list(string.ascii_lowercase)

lst_of_shft = []
shft_map = {}

def shift_left(lst, n):
    if n < 0:
        raise ValueError('n must be a positive integer')
    if n > 0:
        lst.insert(0, lst.pop(-1))  # shift one place
        shift_left(lst, n-1)  # repeat
    return lst

def format_secret(secret, message):
	formatted_secret = ''
	while(len(formatted_secret) < len(message)):
		formatted_secret += secret

	while(len(formatted_secret) > len(message)):
		formatted_secret = formatted_secret[:-1]

	return formatted_secret

def decrypt(secret, message):
	secret = format_secret(secret, message)
	for index in range(len(message)):
            x = secret[index]
            y = message[index]

def main():


main()
