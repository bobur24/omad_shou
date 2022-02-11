import random

yutuq = []
sonlar = []
sizning_raqamiz = []

for i in range (1, 7):
    raqam = input(f"1 dan 50 gacha sonlardan {i} - tanlagan raqamingizni kiriting: ")
    sizning_raqamiz.append(raqam)


for i in range (1, 51):
    sonlar.append(i)
def lotto(lotto6):
    son1 = random.choices(sonlar, k = 6).pop(0)
    sonlar.remove(son1)
    son2 = random.choices(sonlar, k = 6).pop(1)
    sonlar.remove(son2)
    son3 = random.choices(sonlar, k = 6).pop(2)
    sonlar.remove(son3)
    son4 = random.choices(sonlar, k = 6).pop(3)
    sonlar.remove(son4)
    son5 = random.choices(sonlar, k = 6).pop(4)
    sonlar.remove(son5)
    son6 = random.choices(sonlar, k = 6).pop(5)
    
    yutuq.append(son1)
    yutuq.append(son2)
    yutuq.append(son3)
    yutuq.append(son4)
    yutuq.append(son5)
    yutuq.append(son6)
    
    return yutuq
print(lotto(sonlar))
print(f"{list(set(sizning_raqamiz).intersection(set(yutuq)))} ta tanlagan raqamingiz to'g'ri chiqdi ")