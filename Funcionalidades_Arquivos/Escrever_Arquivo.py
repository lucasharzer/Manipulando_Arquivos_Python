import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())

pasta = str(os.getenv("LOCAL_PASTA"))

nome_arquivo = "arquivo1.txt"
arquivo = pasta + nome_arquivo

try:
    modificações = open(arquivo, "w")
    
    modificações.write("Arquivo 1\n")

    frases = list()
    frases.append("\nLinguagens de Programacao:\n")
    frases.append("- Python\n")
    frases.append("- JavaScript\n")
    frases.append("- Java\n")
    frases.append("- C#\n")

    modificações.writelines(frases)
    print("\nModificações feitas.")
except:
    print("\nErro ao escrever no arquivo.")
finally:
    print("Processo finalizado.")
