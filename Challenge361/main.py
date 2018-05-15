import re

def main():
    input = 'EbAAdbBEaBaaBBdAccbeebaec'
    strList = re.split('.', input, maxsplit=100, flags=re.IGNORECASE)
    print strList

main()
