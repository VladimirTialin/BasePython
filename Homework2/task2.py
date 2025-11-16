hour=0
tasks_sum=0
go_to_store=False

print("Начался восьмичасовой рабочий день.")
while hour < 3:
    hour+=1
    print(f'{hour}-й час')
    count=int(input("Сколько задач решит Максим? "))
    wife=int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
    if(wife==1):
        go_to_store=True

    tasks_sum+=count

print(f'Рабочий день закончился. Всего выполнено задач: {tasks_sum}')
if go_to_store:
    print("Нужно зайти в магазин")