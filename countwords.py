import os
from pathlib import Path

print(os.path.expanduser('~'))

def count_words(file_name):
    file_basepath=str(Path.home())+ "/Downloads/"
    file_path=file_basepath+file_name
    #print (file_path)
    try:
        with open(file_path) as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        print ("Cant find the file!",file_path)
    else:
        count=len(contents.split())
        print ("The count of words in ",file_name, ":",count)

books=['alice.txt','siddharta.txt','mobydick.txt','littlewomen.txt','wrongfile.txt']

for book in books:
    count_words(book)