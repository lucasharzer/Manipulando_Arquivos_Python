import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())

pasta = str(os.getenv("LOCAL_PASTA"))

nome_arquivo = "arquivo1.txt"
arquivo = pasta + nome_arquivo

try:
    open(arquivo, "a")
    print(f"\n{arquivo}")
except:
    print("\nErro ao criar arquivo.")
finally:
    print("Processo finalizado.")
