from os import chdir, getcwd, listdir, getenv
from os.path import isfile
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())

pasta = str(getenv("LOCAL_PASTA"))

chdir(pasta)
print(f"\n{getcwd()}")

# print(listdir())

for c in listdir():
    if isfile(c):
        print(c)
