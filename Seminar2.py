# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


A = map (int, list (input("Введите число: "))) # Задаю переменную А (то что введет пользователь), так как изначально текст, каждую цифру привожу к целому (с помощью функции map)
print ("Сумма ваших чисел равна: ", sum(A))  # Вывожу посчитанную сумму цифр    Как сделать, чтобы не обращало внимание на запятую, так и не поняла, подскажите, пожалуйста?






# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число: '))

f = 1
for i in range(N):
    i = i + 1
    f = i * f
    
    print(f, end=" ")




# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input('Введите список чисел: ')) 

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))




# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# позиции элеменотв которые надо перемножить находятся в отдельно созданном файле
# по принципу каждая строчка это одно чило


#Запись данных в файл

data = open('file.txt', 'w')
data.write('-2\n')
data.write('-1 \n')
data.write('-0 \n')
data.write('1 \n')
data.write('2')
data.close()

#Чтение данных из файла

path = 'file.txt'
data = open(path, 'r')
for line in data:
     print (line)
     print (([-2 * -1 * 0 * 1 * 2]))
data.close()




# Реализуйте алгоритм перемешивания списка.

import random
 
test_list = [-8, 44, 51, 6, 33]
print ("Первоначальный список : " + str(test_list))
random.shuffle(test_list)
print ("Измененный список : " +  str(test_list))

