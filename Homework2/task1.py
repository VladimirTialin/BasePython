number=int(input("Введите число: "))
positiv=0
negative=0
while number!=0:
    if number > 0:
        positiv+=1
    else: 
        negative+=1
    number=int(input("Введите число: "))

print(f'Позитивных отзывов: {positiv} \nНегативных отзывов: {negative}')