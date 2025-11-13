# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma") # muutos mainissa

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"{x} + {y} = {summa(x, y)}") # korjattu konflikti
print(f"{x} - {y} = {erotus(x, y)}") # korjattu konflikti

logger("lopetetaan ohjelma")
print("goodbye!") # lisäys bugikorjaus-branchissa
