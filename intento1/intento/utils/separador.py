import os
from spleeter.separator import Separator


if __name__ == "__main__":
    cancion = "C:\\Users\\AleBe\\Documents\\TT\\intento1\\intento\\utils\\audio.wav"

    separator = Separator("spleeter:4stems")
    separator.separate_to_file(cancion, "C:\\Users\\AleBe\\Documents\\TT\\intento1\\intento\\utils\\audio")
    print("Pista separada")