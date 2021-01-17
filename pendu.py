# -*-coding:Utf-8 -*
import os
from fonctions import *

os.chdir('PROGRAM_FOLDER_ADRESS')

# LOAD PLAYER
joueur = input("Hi, what's your name: ")
profil_joueur = openPlayer(joueur)
print(profil_joueur)

# GAME START
play_again = "1"
while profil_joueur['score'] > 0 and play_again == "1":
    mot_pendu = list(getMotPendu())
    mot_myst = ["*" for char in mot_pendu]

    total_char = len(mot_pendu)
    find_char = 0
    tried_letter = []
    while total_char > find_char and profil_joueur['score'] > 0:
        print(profil_joueur['score'])
        print(mot_myst)
        try_letter = input("try a letter: ")
        score_tracking = False

        for i, char in enumerate(mot_pendu):
            if try_letter == char:
                mot_myst[i] = try_letter
                if try_letter not in tried_letter:
                    find_char += 1
                    score_tracking = True
        tried_letter.append(try_letter)

        if score_tracking:
            profil_joueur['score'] += 1
        else:
            profil_joueur['score'] -= 1

        if total_char == find_char:
            print("GAGNE:", mot_myst)
            play_again = input(
                "press 1 to play again or anything else to quit: ")
        elif profil_joueur['score'] == 0:
            print("GAME OVER")

if profil_joueur['score'] != 0:
    savePlayer(profil_joueur)

os.system("pause")
