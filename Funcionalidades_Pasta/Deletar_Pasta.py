import os
import dotenv
import shutil


dotenv.load_dotenv(dotenv.find_dotenv())

pasta = str(os.getenv("LOCAL_PASTA"))

try:
    # os.makedirs(pasta)
    shutil.rmtree(pasta)
    print("\nPasta deletada com sucesso.")
except OSError as e:
    print(f"\n{e}")
finally:
    print("Processo finalizado.")
