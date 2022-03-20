import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())

pasta = str(os.getenv("LOCAL_PASTA"))

nome_arquivo = "arquivo1.txt"
arquivo = pasta + nome_arquivo

try:
    leitura = open(arquivo, "r")

    # print(leitura.readline(4))
    
    for linhas in leitura.readlines():
        print(linhas)
except:
    print("\nErro ao ler arquivo.")
finally:
    print("Processo finalizado.")
