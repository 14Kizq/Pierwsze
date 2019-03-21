import os
path = "pliki/01/dane.txt"
dir_path = os.path.dirname(path)

os.makedirs(dir_path)
open(path, "w").close()

