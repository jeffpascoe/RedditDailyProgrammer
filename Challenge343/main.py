import string
from collections import deque

alphabet = list(string.ascii_uppercase)[0:7]
noteList = sorted([letter+'#' for letter in list(set(alphabet) - set(['E','B']))] + alphabet)
solfegeDict = {'Do':1, 'Re':2, 'Mi':3, 'Fa':4, 'So':5, 'La':6, 'Ti':7}

tempNoteList = deque(noteList)
print(tempNoteList[0])
# newList = [tempNoteList.rotate(1) for item in range(0, noteList.index('C'))]
newList = tempNoteList.rotate(1)
print(newList)
print(noteList.index('C'))
