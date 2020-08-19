import os

def play():

    path = os.getcwd()
    path = os.path.join(path, "Chess_UI", "ChineseChess.jar")
    os.system("java -jar " + path)