import random
def prost(n):
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst
print("введите словов заглавными буквами")
slovo = input()
print("два простых числа")
p, q = map(int, input().split())
list_alf_eng = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list_alf_rus =['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
list_slovo = []
if list_alf_eng.count(slovo[0]) == 1:
    for i in slovo:
        list_slovo.append(list_alf_eng.index(i) + 1)
else:
    for i in slovo:
        list_slovo.append(list_alf_rus.index(i) + 1)
n = p * q
m = (p-1) * (q-1)
lst = prost(m)
lst_e = []
a = 0
for e in lst:
    a = e
    b = m
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    if a == 1:
        lst_e.append(e)
e = lst_e[random.randint(0, len(lst_e) - 1)]
d = random.randint(0, n)
while (e * d) % m != 1:
    d = random.randint(0,n)
for i in range(len(list_slovo)):
    list_slovo[i] = list_slovo[i] ** e % n
print("ваше слово:", list_slovo)
print("секретный ключ:",e, d, n)