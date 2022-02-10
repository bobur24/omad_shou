import random

nomer = []
n = int(input('Raqamlar sonini kiriting: '))

for i in range (1, n+1):
    raqam = input(f'{i} - raqamni kiriting: ')
    nomer.append(raqam)
def omadshou(nomer):
     son = random.choices(nomer, k = 1)
     return son
print(omadshou(nomer))