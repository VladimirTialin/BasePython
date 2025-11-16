'''Функция ввода числа '''
def enterNum(number):
    while not number.isdigit():
        number = input("Введите номер билета: ")    
    return numberOfSteps(number)

'''Функция создания массива чисел '''
def arrNumber(number):
    arr=[]
    for i in str(number):
        arr.append(int(i))
    return arr

'''Определение количества чисел в числе и подсчет результата '''
def numberOfSteps(number):
    arrNum=arrNumber(number)
    if len(arrNum) % 2 == 0:
        evenLuckyTicket(arrNum)
    else:
        oddLuckyTicket(arrNum)

'''Функция поиска счастливого билета четного массива '''
def evenLuckyTicket(arr):
    left=0
    right = 0
    lenArr=(len(arr) - 1)
    for i in range((len(arr)) // 2):
        left += arr[i]
        right+=arr[lenArr-i]
    return LuckyTicketResult(left,right)

'''Функция поиска счастливого билета нечетного массива '''
def oddLuckyTicket(arr):
    left=0
    lenArr=(len(arr)-1)
    right = arr[lenArr]
    for i in range((len(arr)) // 2):
        left += arr[i]
        right+=arr[lenArr-1-i]
    return LuckyTicketResult(left,right)

'''Результат введенного билета'''
def LuckyTicketResult(left,right):
    print(f'Сумма левой части = {left}; Сумма правой части = {right}')
    if left == right:
        print("Ура! Билет счастливый!")
    else:
        print("Увы! Билет не счастливый!")


num=input("Введите номер билета: ")
enterNum(num)


