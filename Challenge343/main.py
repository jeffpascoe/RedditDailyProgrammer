import string

alphabet = list(string.ascii_uppercase)[0:7]
fullList = sorted([letter+'#' for letter in list(set(alphabet) - set(['E']))] + alphabet)
