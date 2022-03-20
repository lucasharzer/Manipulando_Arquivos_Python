import os
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())

pasta = str(os.getenv("LOCAL_PASTA"))

# if os.path.exists(pasta)
if os.path.isdir(pasta):
    print(f"\nA pasta existe: \n{pasta}\n")
else:
    print("\nA pasta não existe.")

print("Processo finalizado.")
