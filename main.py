from functions import sin_series, sh_series

def main():
    print("Выберите функцию:")
    print("1. sin(x)")
    print("2. sh(x)")
    choice = int(input("Введите номер функции: "))
    x = float(input("Введите значение x: "))

    if choice == 1:
        result = sin_series(x)
        print(f"sin({x}) = {result}")
    elif choice == 2:
        result = sh_series(x)
        print(f"sh({x}) = {result}")
    else:
        print("Неверный выбор.")

if __name__ == "__main__":
    main()