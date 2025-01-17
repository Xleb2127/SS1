
# первое задание в билетах - 1, 7, 13, 19, 25, 31.
"""
1.В школьной библиотеке 30 стеллажей с книгами. На каждом стеллаже 7 полок. Библиотекарь сообщил Пете,
что нужная ему книга находится на пятом стеллаже на третьей сверху полке. Какое количество информации библиотекарь передал Пете?
"""
"""
import math
kol_stelaj = 30
kol_polka = 7
stelaj = math.ceil(math.log2(kol_stelaj))
polka = math.ceil(math.log2(kol_polka))
result = stelaj + polka
print(f"Количество информации, переданной библиотекарем: {result} бит.")
"""

# первое задание в билетах - 2, 8, 14, 20, 26, 32.
# 1.	В корзине лежат 67 шаров. Все шары разного цвета. Сколько информации несет сообщение о том, что из корзины достали красный шар?
"""
import math
num_balls = 67
information = math.log2(num_balls)
print(f"Количество информации: {information:.2f} бит.")
"""

#первое задание в билетах - 3, 9, 15, 21, 27.
#1.	Какое количество информации несет сообщение о том, что встреча назначена на 17 ноября в 13.27?#
"""
import math
data=math.log2(365)
time=math.log2(1440)
sum = data + time
print(int(sum))
"""

# первое задание в билетах - 4, 10, 16, 22, 28
#1.	При угадывании целого числа в некотором диапазоне было получено 64 бита информации. Сколько чисел содержит этот диапазон?
'''
import math
information_bits = 64
num_numbers = 2 ** information_bits
print(f"Количество чисел в диапазоне: {num_numbers}")
'''

#первое задание в билетах - 5, 11, 17, 23, 29
# 1.	Сообщение о том, что ваш друг живет на 10 этаже, несет 6 бита информации. Сколько этажей в доме?
"""
import math
information_bits = 6
num_floors = 2 ** information_bits
print(num_floors)
"""

#первое задание в билетах - 6, 12, 18, 24, 30
# Была получена телеграмма: «Встречайте, вагон 14». Известно, что в составе поезда 32 вагонов. Какое количество информации было получено?
'''
import math
num_wagons = 32
information = math.log2(num_wagons)
print(f"Количество информации: {information:.2f} бит.")
'''

#второе задание в билетах - 1, 7, 13, 19, 25, 31
# Информационное сообщение объемом 1,5 Кбайта содержит 3072 символа. Сколько символов содержит алфавит, при помощи которого было записано это сообщение?
'''
# Данные задачи
message_size_kb = 1.5  # объем сообщения в килобайтах
num_symbols = 3072     # количество символов в сообщении

# Переводим объем сообщения в биты (1 байт = 8 бит, 1 Кбайт = 1024 байта)
message_size_bits = message_size_kb * 1024 * 8

# Количество бит на символ
bits_per_symbol = message_size_bits / num_symbols

# Количество символов в алфавите
alphabet_size = 2 ** int(bits_per_symbol)

print(alphabet_size)
'''

#второе задание в билетах - 2, 8, 14, 20, 26, 32. 2.
# Объем сообщения, содержащего 4096 символов, составил 1/512 часть Мбайта. Каков размер алфавита, с помощью которого записано сообщение?
"""
message_size = 4096  # Количество символов в сообщении
mb_size = 1/512  # Размер сообщения в Мбайтах

# Переводим размер сообщения в биты
message_bits = mb_size * 1024 * 1024 * 8  # 1 Мбайт = 1024 * 1024 байт, 1 байт = 8 бит

# Вычисляем количество бит на символ
bits_per_symbol = message_bits / message_size

# Определяем размер алфавита
alphabet_size = 2 ** bits_per_symbol

print(f"Размер алфавита: {alphabet_size}")
"""

#второе задание в билетах - 3, 9, 15, 21, 27.2.
# Для записи сообщения использовался 64-х символьный алфавит.
# Каждая страница содержит 30 строк. Все сообщение содержит 8775 байтов информации и занимает 6 страниц.
# Сколько символов в строке?
"""
alphabet_size = 64  # Размер алфавита
page_lines = 30  # Количество строк на странице
message_bytes = 8775  # Размер сообщения в байтах
pages_count = 6  # Количество страниц

# Вычисляем количество символов в сообщении
symbols_count = message_bytes * 8 / alphabet_size  # Количество бит в сообщении / количество бит на символ

# Вычисляем количество строк в сообщении
lines_count = pages_count * page_lines

# Вычисляем количество символов в строке
symbols_per_line = symbols_count / lines_count

print(f"Количество символов в строке: {symbols_per_line}")
"""
#второе задание в билетах - 4, 10, 16, 22, 28
# Сообщение занимает 8 страницы и содержит 1/32 Гбайта информации.
# На каждой станице записано 256 символов. Какова мощность использованного алфавита?
'''
2.	8775 байт * 8 бит/байт = 70200 бит   2^6 = 64
70200 бит / 6 бит/символ = 11700 символов
6 страниц * 30 строк/страницу = 180 строк
11700 символов / 180 строк = 65 символов
'''

#второе задание в билетах - 5, 11, 17, 23, 29.
# ДНК человека (генетический код) можно представить себе как некоторое слово в четырехбуквенном алфавите,
# где каждой буквой помечается звено цепи ДНК, или нуклеотид.
# Сколько информации (в битах) содержит ДНК человека, содержащий примерно 1,5 х 1023 нуклеотидов?

'''
import math
nucleotides_count = 1.5 * 10**23  # Количество нуклеотидов в ДНК человека
alphabet_size = 4  # Размер алфавита ДНК 

# Вычисляем количество информации в битах
information_bits = nucleotides_count * math.log2(alphabet_size)

print(f"Информация в ДНК человека: {information_bits:.2e} бит")
'''

#второе задание в билетах - 6, 12, 18, 24, 30.
# Два текста содержат одинаковое количество символов.
# Первый текст составлен в алфавите мощностью 4 символа, второй – 128 символа.
# Во сколько раз отличается количество информации в текстах?
"""
import math
alphabet_size1 = 4  # Мощность алфавита первого текста
alphabet_size2 = 128  # Мощность алфавита второго текста

# Вычисляем отношение количества информации
information_ratio = math.log2(alphabet_size2) / math.log2(alphabet_size1)

print(f"Количество информации во втором тексте больше в {information_ratio:.2f} раз")
"""
# третье задание в билетах - 1, 13, 25
"""
Дайте классификацию информации по различным признакам
(по способу представления, по способу восприятия, по массовому значению). Приведите примеры.

по способу представления: знаковая, текстовая, графическая, аудиальная
по способу восприятия: визуальная, аудиальная, вкусовая, осязаемая, обонятельная
по массовому значению: массовая, специальная, личная
"""

"""
третье задание в билетах - 2, 14, 26    

5.	В чем состоит процесс дискретизации информации и в каких случаях он используется? Приведите примеры. 
Дискретизация информации – это процесс преобразования непрерывных аналоговых сигналов особым образом,
представление целого в виде набора отдельных элементов.  все приборы, показывающие результаты измерения в цифрах,
осуществляют дискретизацию.


третье задание в билетах - 3, 15, 27
7.	Приведите примеры информационных процессов в природе и технике в соответствии с универсальной схемой передачи информации.
ответ:
исходная информация>шифрование>сжатие>шумозащитное кодирование>канал связи>декодирование шумозащитных кодов>распаковка>дешифрование>полученная информация
                                                              >шум
1. Исходная информация: Один человек хочет передать другому информацию голосом — например, обсудить планы на вечер
2. Шифрование: Для защиты разговора от перехвата сотовая сеть может автоматически шифровать голосовые данные (например, с использованием протокола GSM).
3. Сжатие: Для уменьшения объема передаваемых данных используется технология сжатия аудиосигнала (например, кодеки для сжатия речи, такие как AMR).
4. Шумозащитное кодирование: Система связи применяет коррекцию ошибок, чтобы избежать искажений сигнала из-за помех (например, FEC — forward error correction).
5. Канал связи: Звук передается через мобильную сеть или интернет (если используется VoIP). Возможны различные виды помех, такие как слабый сигнал или задержка в передаче.
6. Шум: Внешние факторы, такие как слабый прием сигнала, помехи от других устройств или шум окружающей среды (например, уличный шум).
7. Декодирование шумозащитных кодов: На стороне принимающего абонента устройство корректирует возможные ошибки в сигнале, чтобы обеспечить максимально четкую передачу речи.
8. Распаковка: Полученные данные распаковываются, если они были сжаты (например, аудиокодеки восстанавливают оригинальный звук голоса).
9. Дешифрование: Если данные были зашифрованы, система автоматически расшифровывает их на телефоне получателя.
10. Полученная информация: Человек на другом конце разговора получает и воспринимает исходное сообщение — информацию о планах на вечер.

           
третье задание в билетах - 4, 12, 16, 24, 28
3.	Какие формы представления информации существуют? Раскройте их основные характеристики.
Знаковая(римские цифры вроде хз, дорожные знаки), текстовая(любой текст хз), графическая(фото), аудиальная, видео


третье задание в билетах - 5, 17, 29

2.	Раскройте сущность понятия «количество информации».
Количество информации – это мера, которая отражает степень снижения неопределенности, возникающей при получении нового знания

третье задание в билетах - 6, 18, 30
3.	Изобразите универсальную схему передачи информации в случае кодирования и объясните её.
исходная информация>шифрование>сжатие>шумозащитное кодирование>канал связи>декодирование шумозащитных кодов>распаковка>дешифрование>полученная информация
                                                              >шум
                                                              
третье задание в билетах - 7, 19, 31
3.	Дайте определения понятий «информация», «данные»,
 «знания» – как базовых понятий в информатике. Раскройте их взаимосвязь. Приведите примеры.

Информация -- это сведения, снимающие неопределенность об окружа-
ющем мире, которые являются объектом хранения, преобразования, передачи и использования.
Сведения - это знания, выраженные в сигналах, сообщениях, известиях,
уведомлениях и т.д.
знания – это опыт и восприятия человека в определённой сфере 

третье задание в билетах - 8, 20, 32
3.	Перечислите атрибутивные свойства информации, дайте их краткую характеристику.
неотрывность от носителя информации
- дискретность содержат в информации сведения те характеристики отдельные фактические данные
-непрерывность постоянно копится

третье задание в билетах - 9,21
3.	Какие форматы используются для представления чисел в памяти компьютера? В каком формате представляются целые числа в памяти ЭВМ?
Основные структурные единицы памяти компьютера: бит, байт, машин-
ное слово.
Бит. Все данные и программы, хранящиеся в памяти компьютера, имеют вид двоичного кода. Один символ из двухсимвольного алфавита несет 1 бит информации. Ячейка памяти, хранящая один двоичный знак, называется «бит». В одном бите памяти хранится один бит информации.
Чтобы получить внутреннее представление целого положительного
числа N, хранящегося в k-разрядном машинном слове, необходимо:
l) перевести число N в двоичную систему счисления;
2) полученный результат дополнить слева незначащими нулями до k раз-
рядов.

третье задание в билетах - 10, 22
3.	В чем состоит основная идея алгоритма Шеннона-Фано?
При использовании этого метода выполняются следующие шаги:
1) упорядочить множество исходных символов по убыванию их частот;
2) список символов разделить на две части (назовем их первой и второй частями) так, чтобы суммы частот обеих частей были точно или примерно равны. В случае, когда точного равенства достичь не удается, разница между суммами должна быть минимальна;
3) кодовым комбинациям первой части дописать 1, кодовым комбинациям
второй части дописать 0:

третье задание в билетах - 11, 23
3.	Назовите существующие единицы измерения информации и соотношения между ними.
Бит самая меньшая единица информации
Байт = 8бит
Килобайт = 1024байта
Мегабайт = 1024 килобайта
Гигабайт = 1024 мегабайта
терабайт = 1024 гигабайта
"""

#пятое задание в билетах - 1, 7, 13, 19, 25, 31.
'''
5.	На экране с разрешающей способностью 240 х 320 высвечиваются только 256-цветные изображения. Какой минимальный объем видеопамяти необходим для хранения изображения?

# Разрешение экрана
width = 320
height = 240

# Количество цветов
colors = 256

# Размер одного пикселя в байтах
pixel_size = 1  # 256 цветов = 8 бит = 1 байт

# Объем видеопамяти в байтах
memory_size = width * height * pixel_size

# Вывод результата
print(f"Минимальный объем видеопамяти: {memory_size} байт")
'''

#пятое задание в билетах - 2, 8, 14, 20, 26, 32
#5.	Для хранения изображения размером 64х32 точек выделен 16 Кбайт памяти.
#Определите, какое максимальное число цветов допустимо использовать в этом случае.
"""
# Размеры изображения
width = 64
height = 32

# Объем памяти в байтах
memory_size = 16 * 1024  # 16 Кбайт = 16 * 1024 байт

# Количество пикселей
pixels = width * height

# Максимальное количество цветов
max_colors = memory_size // pixels

# Вывод результата
print(f"Максимальное число цветов: {max_colors}")
"""

# пятое задание в билетах - 3, 9, 15, 21, 27.
#5.	128-цветный рисунок содержит 720 байт информации. Из скольких точек он состоит?
"""
import math
# Количество цветов
colors = 128

# Размер рисунка в байтах
size = 720

# Количество бит на цвет
bits_per_color = int(round(math.log2(colors)))  # 128 цветов = 2^7, значит 7 бит на цвет

# Размер одного пикселя в битах
pixel_size = bits_per_color

# Количество точек (пикселей)
points = size * 8 // pixel_size

# Вывод результата
print(f"Рисунок состоит из {points} точек.")
"""
#пятое задание в билетах - 4, 10, 16, 22, 28
#5.	Объем свободной памяти на диске – 0,04 Гб, разрядность звуковой платы – 32.
#Какова длительность звучания цифрового аудиофайла, записанного с частотой дискретизации 44100 Гц?
"""
# Объем свободной памяти в байтах
free_memory = 0.04 * 1024 * 1024 * 1024  # 0.04 Гб = 0.04 * 1024 * 1024 * 1024 байт

# Разрядность звуковой платы
bit_depth = 32

# Частота дискретизации
sampling_rate = 44100

# Размер одного аудиосемпла в байтах
sample_size = bit_depth // 8

# Длительность звучания в секундах
duration = free_memory / (sampling_rate * sample_size)

# Длительность звучания в минутах и секундах
minutes = int(duration // 60)
seconds = int(duration % 60)

# Вывод результата
print(f"Длительность звучания: {minutes} минут {seconds} секунд.")
"""


#пятое задание в билетах - 6, 12, 18, 24, 30
'''
Оцените информационный объем моноаудиофайла (в килобайтах) длительностью звучания 3 минуты,
если «глубина» кодирования и частота дискретизации звукового сигнала равны соответственно: 32 бит и 16 кГц.

# Ввод данных
duration_minutes = 3  # Длительность в минутах
bit_depth = 32  # Глубина кодирования в битах
sampling_rate = 16000  # Частота дискретизации в Гц

# Перевод времени в секунды
duration_seconds = duration_minutes * 60

# Расчет количества отсчетов
total_samples = duration_seconds * sampling_rate

# Расчет количества бит
total_bits = total_samples * bit_depth

# Перевод бит в килобайты
file_size_kb = total_bits / 8 / 1024

# Вывод результата
print(f"Информационный объем файла: {file_size_kb:.2f} килобайт")
'''
#пятое задание в билетах -5, 11, 17, 23, 29
"""
Рассчитайте время звучания моноаудиофайла,
если при 16-битном кодировании и частоте дискретизации 44,1 кГц его объем равен 1024 Кбайт.

# Ввод данных
file_size_kb = 1024  # Размер файла в Кбайт
bit_depth = 16  # Глубина кодирования в битах
sampling_rate = 44100  # Частота дискретизации в Гц

# Перевод килобайт в биты
file_size_bits = file_size_kb * 1024 * 8

# Расчет количества отсчетов
total_samples = file_size_bits / bit_depth

# Расчет времени звучания в секундах
duration_seconds = total_samples / sampling_rate

# Вывод результата
print(f"Время звучания: {duration_seconds:.2f} секунд")
"""
#шестое задание в билетах - 1, 13, 25
#6.	Дайте классификацию каналов связи по физическим признакам
#Механические, акустические, оптические и электрические. Проводные и беспроводные

#шестое задание в билетах - 2, 14, 26
#.	Дайте классификацию каналов связи по способу передачи информации.
"""
Симплексные передают информацию в одном направ-
лении.
Дуплексные передают информацию одновременно и в прямом, и обратном направлении.
Полудуплексные осуществляют попеременную пере-
дачу информации либо в прямом, либо в обратном
направлении.
"""
#шестое задание в билетах - 3, 15, 27
#Дайте классификацию каналов связи по форме представления передаваемой информации.
"""
Аналоговые представляют информацию в непрерывной форме - в виде непрерывного сигнала какой-либо физической природы.
Цифровые представляют информацию в цифровой (прерывной - дискретной, импульсной) форме сигналов какой-либо физической природы
"""
#шестое задание в билетах - 4, 16, 28
'''
9.	Дайте классификацию каналов связи по времени существования
Коммутируемые - временные, создаются только на время передачи информации. По окончании передачи информации и разъединении уничтожаются.
Некоммутируемые - создаются на длительное время с определенными постоянными характеристиками. Их еще называют выделенными.
'''

#шестое задание в билетах - 5, 17, 29
#5.	Что такое модуляция?
'''
Модуляция – изменение какого-либо параметра сигнала в канале связи
(модулируемого сигнала) в соответствии с текущими значениями передаваемых данных (т.е. моделирующего сигнала)
'''

#шестое задание в билетах - 6, 18, 30
#Дайте определение протокола передачи данных.
'''
Протокол передачи данных - это совокупность правил, которые определяют формат данных и процедуры передачи их по каналу связи, в которых, как правило, указываются способ модуляции, соединение с каналом, представление данных и т.д. Все это делается для повышения достоверности передаваемых
данных.
'''

#шестое задание в билетах - 7, 19, 31
"""
Что такое основание системы счисления?
Количество используемых в сс цифр
"""
#шестое задание в билетах - 8, 20, 32
"""
Сформулируйте правило перевода дробных чисел из десятичной системы счисления в любую позиционную.
Чтобы перевести десятичное смешанное число в позиционную систему счисления нужно целую часть числа делить на основание сс в которую переводим.
 После делить частное до тех пор пока остаток не станет меньше основания сс. В ответе записать остатки от деления с права налево.
 Дробную же часть нужно умножать на основание сс в котрую переводим и в ответ записывать целую часть, пока в дробной не останется чисел кроме нулей
"""
#шестое задание в билетах - 9, 21
"""
В чем состоит основная идея алгоритма Хаффмана?
Идея алгоритма состоит в следующем: зная вероятности символов в сообщении,
можно описать процедуру построения кодов переменной длины, состоящих из целого количества битов.
Символам с большей вероятностью ставятся в соответствие более короткие коды.
Классический алгоритм Хаффмана на входе получает таблицу частот встречаемости символов в сообщении.
Далее на основании этой таблицы строится дерево кодирования Хаффмана (Н-дерево).
"""
#шестое задание в билетах - 10, 22
"""
21.	Нарисуйте универсальную схему передачи информации в случае кодирования. Охарактеризуйте назначение используемых в схеме устройств.
исходная информация>шифрование>сжатие>шумозащитное кодирование>канал связи>декодирование шумозащитных кодов>распаковка>дешифрование>полученная информация
                                                              >шум
"""
#шестое задание в билетах - 11, 23
#Перечислите прагматические свойства информации, дайте их краткую характеристику.
'''
•	смысл и новизна (это свойство характеризует перемещение информации в социальных коммуникациях, и выделяет ту ее часть, 
которая нова для потребителя);
•	полезность (уменьшение неопределенности сведений об объекте, дезинформация расценивается как отрицательные значения полезной информации);
•	ценность (ценность информации различна для различных потребителей и пользователей);
•	кумулятивность (характеризует накопление и хранение информации);
•	полнота (характеризует качество информации и определяет достаточность данных для принятия решений или для создания новых данных на основе имеющихся;
 чем полнее данные, тем шире диапазон методов, которые можно использовать, тем проще подобрать метод, вносящий минимум погрешностей в ход информационного процесса);
•	достоверность (данные возникают в момент регистрации сигналов, но не все сигналы являются полезными - всегда присутствует какой-то уровень посторонних сигналов,
 в результате чего полезные данные сопровождаются определенным уровнем информационного шума; если полезный сигнал зарегистрирован более четко, чем посторонние сигналы,
  достоверность информации может быть более высокой; при увеличении уровня шумов достоверность информации снижается; в этом случае для передачи того же количества информации
   требуется использовать либо больше данных, либо более сложные методы);

•	адекватность (это степень соответствия реальному объективному состоянию дела;
неадекватная информация может образовываться при создании новой информации на основе неполных или недостоверных данных;
 однако и полные, и достоверные данные могут приводить к созданию неадекватной информации в случае применения к ним неадекватных методов);
•	доступность (мера возможности получить ту или иную информацию; на степень доступности информации влияют одновременно как доступность данных,
 так и доступность адекватных методов для их интерпретации; отсутствие доступа к данным или отсутствие адекватных методов обработки данных приводят к одинаковому результату: информация оказывается недоступной;
  отсутствие адекватных методов для работы с данными во многих случаях приводит к применению неадекватных методов, в результате чего образуется неполная, неадекватная или недостоверная информация);
•	актуальность (степень соответствия информации текущему моменту времени; нередко с актуальностью, как и с полнотой, связывают коммерческую ценность информации; поскольку информационные процессы растянуты во времени,
 то достоверная и адекватная, но устаревшая информация может приводить к ошибочным решениям; необходимость поиска (или разработки) адекватного метода для работы с данными может приводить к такой задержке в получении информации,
  что она становится неактуальной и ненужной; на этом, в частности, основаны многие современные системы шифрования данных с открытым ключом. Лица, не владеющие ключом (методом) для чтения данных, могут заняться поиском ключа,
   поскольку алгоритм его работы доступен, но продолжительность этого поиска столь велика, что за время работы информация теряет актуальность и, соответственно, связанную с ней практическую ценность);
•	объективность и субъективность (понятие объективности информации является относительным; это понятно, если учесть, что методы являются субъективными; более объективной принято считать ту информацию,
 в которую методы вносят меньший субъективный элемент. В ходе информационного процесса степень объективности информации всегда понижается. Это свойство учитывают, например, в правовых дисциплинах,
  где по-разному обрабатываются показания лиц, непосредственно наблюдавших события или получивших информацию косвенным путем посредством умозаключений или со слов третьих лиц).
'''
#шестое задание а билетах - 12, 24
'''
Сформулируйте правило перевода смешанных чисел из двоичной системы счисления в восьмеричную, шестнадцатеричную.
Разделим данное число на целую и дробную часть.
Далее  целую часть на  группы по четыре цифры(если в шестнадцатеричную) или по три цифры(если в восьмеричную), начиная справа.
Если в крайней левой группе окажется меньше четырех цифр, то дополним ее нулями. То же самое проводим и с дробной частью только теперь с лево на право.
если в крайней правой группе окажется меньше цифр, то дополним нулями.
'''