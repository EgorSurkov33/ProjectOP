import random

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

O = 0

wisans = 0

counter = 0



def modz():
    global wisans
    global counter
    md = int(input('Добро пожаловать в тренажер 7 задания ЕГЭ! Выберите один из режимов работы: 1 - Тренировочный, 2 - Контрольный: '))
    if md == 1:
        wisans = 1
        tren()
    if md == 2:
        wisans = 2
        counter = 0
        contr()


def perzv():
    global counter
    V = random.randrange(1, 100000)
    Y = random.randrange(1, 100000)
    Q = random.randrange(1, 16)
    T = random.randrange(10, 1000)
    O = (Y*T*2*Q)/V
    print('Стереоаудиофайл передается со скоростью ', V, ' бит/c. Файл был записан при среднем качестве звука: глубина кодирования - ',Q,' бит, частота дискретизации - ',Y,' измерений в секунду, время записи - ',T,'сек. Сколько времени будет передаваться файл? Время укажите в секундах. Ответ округлите до целого числа.')
    ans = int(input(' Ответ:'))
    if toFixed(ans) == toFixed(O):
        check = True
        print('Решено верно')
        counter += 1
    else:
        check = False
        print('Решено не верно')
    if wisans == 1:
        truot = int(input('Просмотреть решение? 1 - Да. 2 - Нет'))
        if truot == 1:
            print('Задача выполняется по формуле O = (Y*T*2*Q)/V. Т.е (',Y,'*',T,'*',2,'*',Q,')/',V,'). Ответ',O)
        if truot == 2:
            print('Переходим к следующей задаче!')
    if wisans == 2:
        print('Ответ засчитан!')


def perimg():
    global counter
    V = random.randrange(1, 100000)
    K = random.randrange(1, 1024)
    X = random.randrange(1, 10000)
    Y = random.randrange(1, 10000)
    d = 0
    for i in range (1,11):
        if 2**i < K < 2**(i+1):
            d = i+1
    O = (X * Y * d)/V 
    print('Сколько секунд потребуется модему, передающему информацию со скоростью', V,' бит/с, чтобы передать ',K,'─цветное растровое изображение размером ',X,' на ',Y,' пикселей, , при условии, что цвет каждого пикселя кодируется минимально возможным количеством бит. Ответ округлите до целого числа.')
    ans = int(input(' Ответ:'))
    if toFixed(ans) == toFixed(O):
        check = True
        print('Решено верно')
        counter += 1
    else:
        check = False
        print('Решено не верно')
    if wisans == 1:
        truot = int(input('Просмотреть решение? 1 - Да. 2 - Нет '))
        if truot == 1:
            print('Задача выполняется по формуле O = (X * Y * d)/V . Т.е (',X,'*',Y,'*',d,')/',V)
        if truot == 2:
            print('Переходим к следующей задаче!')
    if wisans == 2:
        print('Ответ засчитан!')

def pertxt():
    global counter
    V = random.randrange(1, 100000)
    Q = random.randrange(1, 16)
    T = random.randrange(10, 10000)
    O = (V * T)/Q
    print('Скорость передачи данных через ADSL-соединение равна ',V,' бит/с. Передача текстового файла через это соединение заняла ',T,' секунд. Определите, сколько символов содержал переданный текст, если известно, что он был представлен в ',Q,'-битной кодировке. ')
    ans = int(input(' Ответ:'))
    if toFixed(ans) == toFixed(O):
        check = True
        print('Решено верно')
        counter += 1
    else:
        check = False
        print('Решено не верно')
    if wisans == 1:
        truot = int(input('Просмотреть решение? 1 - Да. 2 - Нет'))
        if truot == 1:
            print('Задача выполняется по формуле O = (V * T)/Q. Т.е (',V,'*',T,')/',Q,')')
        if truot == 2:
            print('Переходим к следующей задаче!')
    if wisans == 2:
        print('Ответ засчитан!')

def chranzv():
    global counter
    K = random.randrange(1, 10) #каналы
    Y = random.randrange(1, 1000001) #Частота
    Q = random.randrange(1, 100) #разрешение
    V = random.randrange(10, 10000)#объем
    O = V/Q*Y*K
    print('Производилась ',K ,'-канальная звукозапись с частотой дискретизации ',Y,' Гц и ',Q,'-битным разрешением. В результате был получен файл размером ',V,' бит, сжатие данных не производилось. Определите приблизительно, сколько времени (в секундах) проводилась запись. В качестве ответа укажите ближайшее к времени записи целое число.')
    ans = int(input(' Ответ:'))
    if toFixed(ans) == toFixed(O):
        check = True
        print('Решено верно')
        counter += 1
    else:
        check = False
        print('Решено не верно')
    if wisans == 1:
        truot = int(input('Просмотреть решение? 1 - Да. 2 - Нет'))
        if truot == 1:
            print('Задача выполняется по формуле O = V/Q*Y*K. Т.е ',V,'/',Q,'*',Y,'*',K,')')
        if truot == 2:
            print('Переходим к следующей задаче!')
    if wisans == 2:
        print('Ответ засчитан!')

def chranimg():
    global counter
    X = random.randrange(1, 10000)
    Y = random.randrange(1, 10000)
    Z = random.randrange(1, 1000)
    d = 0
    for i in range (1,10):
        if 2**i < Z < 2**(i+1):
            d = i+1
    O = X*Y*int(d)
    print('Какой минимальный объём памяти (в битах) нужно зарезервировать, чтобы можно было сохранить любое растровое изображение размером ',X,'×',Y,' пикселей при условии, что в изображении могут использоваться ',Z,' различных цветов? В ответе запишите только целое число, единицу измерения писать не нужно.')
    ans = int(input(' Ответ:'))
    if toFixed(ans) == toFixed(O):
        check = True
        print('Решено верно')
        counter += 1
    else:
        check = False
        print('Решено не верно')
    if wisans == 1:
        truot = int(input('Просмотреть решение? 1 - Да. 2 - Нет'))
        if truot == 1:
            print('Задача выполняется по формуле O = X*Y*d. Т.е ',X,'*',Y,'*',d,')')
        if truot == 2:
            print('Переходим к следующей задаче!')
    if wisans == 2:
        print('Ответ засчитан!')


def timeopr():
    global counter
    V = random.randrange(1, 100000)
    T = random.randrange(10, 1000)
    O = V*T
    print('Скорость передачи данных через ADSL─соединение равна ',V,' бит/c. Передача файла через это соединение заняла ',T,' секунд. Определить размер файла в битах.')
    ans = int(input(' Ответ:'))
    if toFixed(ans) == toFixed(O):
        check = True
        print('Решено верно')
        counter += 1
    else:
        check = False
        print('Решено не верно')
    if wisans == 1:
        truot = input('Просмотреть решение? 1 - Да. 2 - Нет')
        if truot == 1:
            print('Задача выполняется по формуле O = V*T. Т.е ',V,'*',T,')')
        if truot == 2:
            print('Переходим к следующей задаче!')
    if wisans == 2:
        print('Ответ засчитан!')

def weiopr():
    global counter
    V = random.randrange(1, 100000)
    Q = random.randrange(1, 9)
    Z = random.randrange(9, 100)
    O = V*Q - V*Z
    print('Текстовый документ, состоящий из ',V,' символов, хранился в ',Q,'-битной кодировке. Этот документ был преобразован в ',Z,'-битную кодировку. Укажите, какое дополнительное количество бит потребуется для хранения документа. В ответе запишите только число.')
    ans = int(input(' Ответ:'))
    if toFixed(ans) == toFixed(O):
        check = True
        print('Решено верно')
        counter += 1
    else:
        check = False
        print('Решено не верно')
    if wisans == 2:
        print('Ответ засчитан!')
    if wisans == 1:
        truot = int(input('Просмотреть решение? 1 - Да. 2 - Нет'))
        if truot == 1:
            print('Задача выполняется по формуле O = V*Q - V*Z. Т.е (',V,'*',Q,'-',V,'*',Z,')')
        if truot == 2:
            print('Переходим к следующей задаче!')
    


def tren():
    
    typ = int(input('Выберите тип задач: 1 - Передача звуковых файлов, 2 - Хранение звуковых файлов, 3 - Передача изображений, 4 - Передача текстовых файлов, 5 - Хранение изображений, 6 - Определение размера записанного файла, 7 - Определение времени передачи данных: '))
    kol = int(input('Введите кол-во заданий: '))
    for i in range(kol):
        if typ == 1:
            perzv()
        if typ == 2:
            chranzv()
        if typ == 3:
            perimg()
        if typ == 4:
            pertxt()
        if typ == 5:
            chranimg()
        if typ == 6:
            weiopr()
        if typ == 7:
            timeopr()
    x = int(input('Решать ещё? 1 - Да. 2 - Нет '))
    if x == 1:
        tren()
    else:
        print('Удачи на ЕГЭ!')


def contr():
    print('Контрольный режим. Вам необходимо решить 8 заданий:')
    kol = 8
    for i in range(kol):
        typ = random.randrange(1,8)
        if typ == 1:
            perzv()
        if typ == 2:
            chranzv()
        if typ == 3:
            perimg()
        if typ == 4:
            pertxt()
        if typ == 5:
            chranimg()
        if typ == 6:
            weiopr()
        if typ == 7:
            timeopr()
    print(counter,'правильных ответов из 8.')
    if counter < 4:
        print('Ваша оценка 2!')
    if 4<=counter < 6:
        print('Ваша оценка 3!')
    if 6<=counter < 7:
        print('Ваша оценка 4!')
    if 7<=counter == 8:
        print('Ваша оценка 5!')    
modz()






