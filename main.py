import time

day = input('Это новый день?(1 - да, 2 - нет)\n')

current_month_name = time.strftime("%B")

print(current_month_name)


with open('money.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

if current_month_name != lines[-1].split()[1]:
    new_line = lines[-1].split()
    new_line[1] = current_month_name
    new_line[-1] = str(1000 + int(new_line[-1]))
    lines[-1] = ' '.join(new_line)


if day == '1':
    current_date = time.strftime("%d.%m.%Y")
    print(current_date)
    with open('money.txt', 'a', encoding='utf-8') as file:
        file.write('\n')
        file.write(f"\tДеньги на {current_date}\n")
        for i in range(len(lines)-4, len(lines)):
            file.write(f'{" ".join(lines[i].split()[:lines[i].split().index(":")])} : {lines[i].split()[-1]} \n')

else:
    expenses = int(input('На что были потрачены деньги(1 - игры, 2 - одежда, 3 - ежемесячные расходы)\n'))

    current_exp = int(input("Какая сума была потрачена?\n"))

    lines_before = lines[:-4]
    lines = lines[-4:]
    lines[expenses-1] = f'{lines[expenses-1]} - {current_exp} = {int(lines[expenses-1].split()[-1]) - current_exp}'
    if expenses == 3:
        lines[expenses] = f'{lines[expenses]} - {current_exp} = {int(lines[expenses].split()[-1]) - current_exp}'

    with open('money.txt', 'w', encoding='utf-8') as file:
        for i in lines_before + lines:
            file.write(f'{i}\n')

for i in range(int(day)):
    print("good day")



# game : 2500
# clothers : 8000
# costs : 12000



