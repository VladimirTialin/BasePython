salary_year=0
for i in range(12):
    salary_month=int(input(f"Зарплата за {i+1} месяц: "))
    salary_year+=salary_month
average_salary=salary_year / 12
print(f'Средняя зарплата за год: {average_salary}')