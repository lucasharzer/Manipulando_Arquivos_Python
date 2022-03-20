import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())

pastas = str(os.getenv("LOCAL_PASTA"))
antigo_arquivo = "arquivo1.txt"
novo_arquivo = "arquivo2.txt"

antigo_nome = os.path.join(pastas, antigo_arquivo)
novo_nome = os.path.join(pastas, novo_arquivo)

try:
    os.rename(antigo_nome, novo_nome)
    print("\nArquivo renomeado")
except:
    print("Erro ao tentar renomear o arquivo.")
finally:
    print("Processo finalizado.")
