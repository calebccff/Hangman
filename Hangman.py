from random import randint as random

words = open("words.txt", "r").readlines()

for i in range(len(words)):
    words[i] = words[i][:-1]

stages  = ['''






 =========''', '''


       |
       |
       |
       |
       |
 =========''', '''

    +---+
       |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''


   +---+
   |   |
   O   |
  /|\  |
  /    |
       |

=========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']

def main():
    #Runs the program
    print("MAIN")
    word = ""
    hword = ""
    wrong = ""
    under = ""
    stage = 0
    print("/*******\ ")
    print("|HANGMAN|")
    print("\*******/")

    while True:
        word = words[random(0, len(words))]
        if len(word) > 3:
            break

    hword = "_"*len(word)
    while True:
        if "_" not in list(hword):
            print("WINNER!")
            print("!!"+"!"*len(word))
            print("!"+word+"!")
            print("!!"+"!"*len(word))
            exit()

        print(stages[stage])
        print("Length: "+str(len(hword)))
        print(hword)
        print("Guessed letters: "+wrong)
        letter = input("-> ")[:1]
        if letter not in wrong.split(", "):
            if letter in list(word):
                print("You guessed a correct letter!")
                hwordl = list(hword)
                nofletters = multiIndex(word, letter)
                for i in range(len(nofletters)):
                    hwordl[nofletters[i]] = letter
                hword = ""
                for i in range(len(hwordl)):
                    hword += hwordl[i]
            else:
                stage+=1
                if stage > len(stages)-1:
                    print("You lose")
                    print("      \            /      ")
                    print("   _   \          /   _   ")
                    print("  | |   \        /   | |  ")
                    print("   -                  -   ")
                    print("                          ")
                    print("       ____________       ")
                    print("      /            \      ")
                    break

                if(wrong == ""):
                    wrong += letter
                else:
                    wrong += ", "+letter
            print("\n"*100)


def multiIndex(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


main()