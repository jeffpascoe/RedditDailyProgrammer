import string

alph = list(string.ascii_lowercase)
lst_of_shft = []
shft_map = []

def shift_left(lst, n):
    if n < 0:
        raise ValueError('n must be a positive integer')
    if n > 0:
        lst.insert(0, lst.pop(-1))  # shift one place
        shift_left(lst, n-1)  # repeat

def format_secret(secret, message):
	formatted_secret = ''
	while(len(formatted_secret) < len(message)):
		formatted_secret += secret

	while(len(formatted_secret) > len(message)):
		formatted_secret = formatted_secret[:-1]

	return formatted_secret


for letter in alph:
	lst_of_shft.append(shift_left(alph, 1))

index = 0
for letter in alph:
    shft_map[letter] = lst_of_shft[index]
    index += 1

def decrypt(secret, message):
	secret = format_secret(secret, message)
	for index in range(len(message)):
            x = secret[index]
            y = message[index]


decrypt('hello', 'encryptThis')
