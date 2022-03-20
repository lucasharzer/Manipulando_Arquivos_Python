import os
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())

pasta = str(os.getenv("LOCAL_PASTA"))

try:
    # os.makedirs(pasta)
    os.mkdir(pasta)
    print("\nPasta criada com sucesso.")
except OSError:
    print("\nErro ao criar pasta.")
finally:
    print("Processo finalizado.")
