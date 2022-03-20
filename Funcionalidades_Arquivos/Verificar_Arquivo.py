import os
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())

pasta = str(os.getenv("LOCAL_PASTA"))
nome_arquivo = "arquivo1.txt"

arquivo = pasta + nome_arquivo

# if os.path.exists(arquivo)
if os.path.isfile(arquivo):
    print(f"\nO arquivo existe: \n{pasta}\n")
else:
    print("\nO arquivo não existe.")

print("Processo finalizado.")
