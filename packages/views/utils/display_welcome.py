""" helper functions  """
import time
import random
import os

from pyfiglet import Figlet
from termcolor import colored

colors = [
            'green',
            'yellow',
            'magenta'
]

list_to_print = []

def clean_sentence(sentence):

    """ returns a list of words from a string"""
    sentence_stripped = sentence.strip(' ')
    word = ''
    for i in sentence_stripped:
        if i != ' ':
            word += i
        else:
            clean_sentence(sentence_stripped[len(word):])

            break
    list_to_print.append(word)
    return list(reversed(list_to_print))



def display_welcome_message(sentence):
    """ returns a display of a welcome message in the console"""
    message = clean_sentence(sentence.__dict__['title'])
    message_string = (' ').join(message)
    os.system('cls' if os.name == 'nt' else 'clear')
    f = Figlet(font='term')
    print(colored(f.renderText(message_string.upper()), random.choice(colors)))
    time.sleep(1)



        



