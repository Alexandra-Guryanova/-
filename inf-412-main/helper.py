import os

def make_dirs(path):
    """создает директории если их нет"""
    
    if not os.path.isdir(path):
        os.makedirs(path)