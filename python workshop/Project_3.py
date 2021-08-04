age = input("Your present age please")
age_int = int(age)
life_remaining = 90 - age_int
month_remaining = life_remaining * 12
weeks_remaining = life_remaining * 52
days_remaining = life_remaining * 365
print(f"you have {month_remaining} months {weeks_remaining} weeks and {days_remaining} days left")
