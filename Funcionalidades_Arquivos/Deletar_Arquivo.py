import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())

pastas = str(os.getenv("LOCAL_PASTA"))
nome_arquivo = "arquivo1.txt"

arquivo = pastas + nome_arquivo

try:
    os.remove(arquivo)
    print("\nArquivo deletado")
except:
    print("Erro ao tentar deletar o arquivo.")
finally:
    print("Processo finalizado.")
