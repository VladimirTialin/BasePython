mysteriousNumber = 7
guess_count = 0
while True:
    number = int(input("Введите число: "))
    if number > mysteriousNumber:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    elif number < mysteriousNumber:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    else:
        print(f'Вы угадали! Число попыток: {guess_count}')    
        break
    guess_count += 1


