import pickle
from random import choice
from donnees import *


# JOUEUR
def openPlayer(joueur):
    with open("scores", "rb+") as scores_file:
        scorePickler = pickle.Unpickler(scores_file)
        try:
            mon_profil = scorePickler.load()
            if mon_profil["joueur"] == joueur:
                pass
            else:
                mon_profil = newPlayer(joueur)
        except EOFError:
            mon_profil = newPlayer(joueur)
    return mon_profil


def newPlayer(joueur):
    mon_profil = {"joueur": joueur, "score": 5}
    return mon_profil


def savePlayer(mon_profil):
    with open("scores", "rb+") as scores_file:
        savePickler = pickle.Pickler(scores_file)
        savePickler.dump(mon_profil)


# GAME
def getMotPendu():
    random_word = choice(word_list)
    return random_word