## Задача 2: Найдите сумму цифр трехзначного числа.123 -> 6 (1 + 2 + 3) 100 -> 1 (1 + 0 + 0)

# while True:
#     number = input("Введите трехзначное число: ")
#     if number.isdigit():
#         number = int(number)
#         if 100 <= number <= 999:
#             break
#         else:
#             print("Введите именно трехзначное число пожалуйста. Попробуйте еще раз \U0001F914.")
#     else:
#         print("Введены символы. Пожалуйста, введите число \U0001F914.")
# print(f'Ваше число- {number} \U0001F600')
# sum =0 
# while number !=0:
#     sum+=number%10
#     number=number//10
# print (f'Ваша сумма цифр {sum} \U0001F386') 
    
## Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
##  что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# while True:
#     summa_cranes = int(input('Введите общее количество журавликов: '))
#     if summa_cranes%8==0:
#         print(f"Петя и Сережа сделали по {summa_cranes//8} журавликов а Катя сделала {summa_cranes//2}")
#         break
#     else:
#         print(f"Неизветно сколько сделал каждый ребенок потому колчиство журавликов не делиться на 8")

## Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
## Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# number =int(input("Введите любой номер с одинокым количеством цифр с обеих сторон билета: "))
# counter=0
# n = number
# while n !=0:
#     n=n//10
#     counter+=1
# if counter % 2 == 0:
#     second_sum = 0
#     first_sum = 0
#     for i in range(counter//2):
#         first_sum+=number%10
#         number=number//10
#     while number!=0:
#         second_sum+=number%10
#         number=number//10
#     if second_sum==first_sum:
#         print("Поздравляю у вас счастливый билет \U0001F386")
#     else: 
#         print ("Не переживай еще повезет \U0001F60A")
# else:
#     print("Введите число с одинаковым количеством цифр с обеих сторон не нервничай все получиться.\U0001F600")

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
def break_chocolate(n, m, k):
    if n * m >= k and (k % n == 0 or k % m == 0):
        return True
    else:
        return False
    
n = int(input("Введите количество долек по горизонтали (n): "))
m = int(input("Введите количество долек по вертикали (m): "))
k = int(input("Введите количество долек, которые нужно отломить (k): "))

if break_chocolate(n, m, k):
    print("Можно отломить",k, "долек от шоколадки",n, "×", m ,"\U0001F600")
else:
    print("Нельзя отломить", k, "долек от шоколадки", n, "×", m)
