"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""


def main():
    balance = 0
    count = 0
    log = []
    print('Добро пожаловать в банкомат!')
    while True:
        while True:
            act = input(
                'Выберите действие:\n 1 - пополнить \n 2 - снять \n 3 - выйти\n')
            if act not in ("1", "2", "3"):
                print("Неверный ввод")
            else:
                break
        match act:
            case "1":
                print(f"Последние операции: {log[::-1]}")
                balance, count, log = add_money(balance, count, log)
                print(f"Ваш баланс {balance}")
            case "2":
                print(f"Последние операции: {log[::-1]}")
                balance, count, log = get_money(balance, count, log)
                print(f"Ваш баланс {balance}")
            case "3":
                print(f"Последние операции: {log[::-1]}")
                print(f"Ваш баланс {balance}")
                print("До свидания!")
                break


def add_money(balance, count, log):
    if balance > 5_000_000:
        log.append(-balance * 0.1)
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму пополнения, кратную 50: "))
        except:
            ex = input("Хотите выйти в меню?\n")
            if ex.lower() == 'да':
                return balance, count, log
            else:
                continue
        if summ % 50 == 0:
            break
    balance += summ
    count += 1
    log.append(summ)
    if count % 3 == 0:
        log.append(balance * 0.03)
        balance *= 1.03
    return balance, count, log


def get_money(balance, count, log):
    if balance > 5_000_000:
        log.append(-balance * 0.1)
        balance *= 0.9
    while True:
        try:
            summ = int(input("Введите сумму снятия, кратную 50: "))
        except:
            ex = input("Хотите выйти в меню?\n")
            if ex.lower() == 'да':
                return balance, count, log
            else:
                continue
        if summ % 50 == 0:
            perc = summ * 0.015
            if perc < 30:
                perc = 30
            elif perc > 600:
                perc = 600
            if summ + perc > balance:
                print("Недостаточно средств!")
                continue
            else:
                break
    balance -= (summ + perc)
    count += 1
    log.append(-(summ + perc))
    if count % 3 == 0:
        log.append(balance * 0.03)
        balance *= 1.03
    return balance, count, log


if __name__ == "__main__":
    main()
