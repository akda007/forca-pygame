from random import choice

def get_random_word(file_path: str):
    f = open(file_path, "r")
    words = f.readlines()
    
    return choice(words).strip()
