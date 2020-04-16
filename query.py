"""
we gon die v1
"""

import re
import sys
import os

def resort(words):
    words.sort()
    words = sorted(words, key=len)
    with open('wordlist.txt', 'w') as file:
        file.writelines("%s\n" % word for word in words)
    return words
    
def find(words, size):
    return filter(lambda x: len(x)==size, words)

with open('wordlist.txt') as file:
    words = file.read().splitlines()

os.system('cls' if os.name == 'nt' else 'clear')
exit = 0
print("==[ srkibblio cheater by gid ]==\n")

while exit == 0:
    command = input("enter query > ")

    if command == "sort":
        words = resort(words)
        print("words resorted.", len(words), "in database")
        
    elif command == "add":
        word = input("add word > ")
        if word not in words:
            words.append(word.lower())
        else:
            print("already in database. doing nothing.")

    elif command == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("cheater is online.\n")
    
    elif command in ["exit", "quit"]:
        resort(words)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit("goodbye!")
        
    else:
        try:
            size = int(command)
            found = find(words, size)
            for word in found:
                print("", word)
        except:
            try:
                command = command.replace("?", ".")
                for word in words:
                    if re.fullmatch(command, word) != None:
                        print(word)
                pass
            except:
                pass