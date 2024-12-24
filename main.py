from functions import sin_series, sh_series, arctan_series

def main():
    while True:
        print("\nВыберите функцию:")
        print("1. sin(x)")
        print("2. sh(x)")
        print("3. arctan(x)")
        print("4. Выход")

        # Проверка выбора функции
        try:
            choice = int(input("Введите номер функции: "))
            if choice == 4:
                print("Выход из программы.")
                break
            elif choice < 1 or choice > 3:
                print("Ошибка: Введите число от 1 до 3.")
                continue
        except ValueError:
            print("Ошибка: Введите целое число.")
            continue

        # Проверка ввода значения x
        try:
            x = float(input("Введите значение x: "))
        except ValueError:
            print("Ошибка: Введите число.")
            continue

        # Вызов выбранной функции
        if choice == 1:
            result = sin_series(x)
            print(f"sin({x}) = {result}")
        elif choice == 2:
            result = sh_series(x)
            print(f"sh({x}) = {result}")
        elif choice == 3:
            # Проверка диапазона для arctan(x)
            if not (-1 <= x <= 1):
                print("Ошибка: Для arctan(x) значение x должно быть в диапазоне [-1, 1].")
                continue
            result = arctan_series(x)
            print(f"arctan({x}) = {result}")

if __name__ == "__main__":
    main()