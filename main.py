# 1
ref_list = [["Максим", "Кузьма", "Виктор", "Ай"], ["Неряхин", "Кузин", "Цой", "Хошино"]]# список имён и фамилий
res = []# список, в который будут вноситься результаты соединения

def filt(listt):# создание функции filt с параметром listt, в который мы передаём список
    try:# обработчик ошибок(на всякий случай), если следующий код вызовет ошибку, то except прийдёт в исполнение
        for g in listt[0]:# перебор данного списка (первой части)
            res.append([g])# добавление каждого элемента по отдельности в новый список
        
        for i in range(len(listt[1])):# перебор второй части данного списка
            res[i].append(listt[1][i])# добавление каждого элемента в списки созданные внутри нового списка по индексу
        return res# возврат результата списка
    except:# выполнится этот код, если произойдёт ошибка
        return "введён неправильный список"# возврат ошибки

print(filt(ref_list))# вызов функции и вывод её в консоль

# 2
def del_rep(listt): # создание функции
    
    # блок переменных
    a = list(set(listt))
    i = 0
    g = 0
    b = 0
    
    # цикл фильтрации
    while True:
        # тело цикла
        if a[i] > a[i + 1]:
            g = a[i]
            a[i] = a[i + 1]
            a[i + 1] = g
            
        if a[i] < a[i + 1]:
            b += 1
        else:
            b = 0
            
        if b == len(a):
            break
        
    return a # возврат готового списка
print(del_rep([19, 2, 1, 2, 17, 1, 5, 3, 4])) # вызов функции

# 3
# создание функции
def lim_max(nums, limit):

    # блок переменных
    g = 0
    e = list(nums)

    # начало цикла
    for i in range(len(e)):
        if e[i] < limit and e[i] > g:
            g = e[i]

    # блок условий для определения вывода
    if g == 0:
        return -1
    else:
        return g

# вызов функций
k = (10, 20, 30, 40, 50, 60, 70, 80, 100)
print(lim_max(k, 50))

# 4

a = [[-20, 0], [0, 15], [15, 25]] # массив для распределения разброса категорий

# создание функции
def temp_cat(temp):
    # блок условий
    if temp < -20:
        return 0
    if temp >= 25:
        return 4
    else:
        # цикл для сравнения с категорией
        for i in range(0, len(a)):
            if temp >= a[i][0] and temp < a[i][1]:
                return i + 1

# вызоов функции
t = int(input())
print(temp_cat(t))


# 5

simv = "`~!@#$%^&*\"№;:\?/,.><|"
simvtr = " -()"
stroka = ""

def check_phn(phones):
    global stroka
    for k in range(len(phones)):
        for i in simv:
            for g in phones[k]:
                if g == i:
                    phones[k] = -1
                    break
            break
        for i in phones[k]:
            for g in simvtr:
                if i != g:
                    stroka += str(i)
                    for i in stroka:
                        if i != '7' or i != '8':
                           phones[k] = -1
                           break
                        else:
                            break
                    if len(stroka) != 11:
                        phones[k] = -1
                        break
                    break
                stroka = ""
                break
            break

    return phones
print(check_phn(['+7(123)456-7890', '8(123)456-7890', '+7 123 456 78901', '123 456 7890']))
            