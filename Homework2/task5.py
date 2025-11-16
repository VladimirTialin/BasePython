total_cards = int(input('Введите кол-во карточек: '))
total_sum = 0

for i in range(1,total_cards+1):
    total_sum+=i
for card in range(total_cards - 1):
    remaining_card = int(input('Номер оставшейся карты: '))
    total_sum -= remaining_card

print(f'Номер потерявшейся карты: {total_sum}')

