# Проект: Вычисление элементарных функций с использованием рядов Маклорена

## Описание
Этот проект реализует вычисление элементарных функций (синуса, гиперболического синуса и арктангенса) с использованием рядов Маклорена. Пользователь может выбрать функцию, ввести значение `x`, и программа вычислит результат.

## Функции
- **\(\sin x\)**: Вычисляет синус числа `x`.
- **\({\rm sh}\,x\)**: Вычисляет гиперболический синус числа `x`.
- **\(\arctan x\)**: Вычисляет арктангенс числа `x` (диапазон значений `x`: [-1, 1]).

## Установка
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/DaniilAseev/practica5.git

## Использование

### 1. Запуск программы

Для запуска программы выполните следующую команду в терминале:

```bash
python main.py
```

### 2. Работа с меню

После запуска программы будет предложено выбрать одну из следующих опций:

- [ ] **Вычислить синус x** — вычисление синуса с использованием ряда Тейлора.
- [ ] **Вычислить чосинус x** — вычисление гиперболического синуса с использованием ряда Тейлора.
- [ ] **Вычислить арктангенс x** — вычисление арктангенса с использованием ряда Тейлора.
- [ ] **Выход** — завершение программы.

Программа запросит у пользователя значения для вычисления и количество членов ряда для приближенного вычисления. После ввода данных программа выведет результат.

### Формула для ряда Тейлора:

Для вычисления синуса, например, используется следующая формула:

sin = ((-1)**n) * ((x**(2*n+1))/(factorial(2*n+1)))

### Пример работы программы

```text
1. Вычислить синус x
2. Вычислить чосинус x
3. Вычислить арктангенс x
4. Выход из программы
Выберите опцию: 1
Введите значение x для sin x: 1
sin(1) = 0.8414709848078965
```

## Структура репозитория

```
repository-name/
│
├── main.py           # Главный исполняемый файл программы
├── README.md         # Этот файл
```

## Примечания

- Для вычисления синуса, гиперболического синуса и арктангенса используется **ряд Тейлора**.

### *Полезные ссылки:*

- [Документация Python](https://docs.python.org/3/)
- [Ряд Тейлора на Wikipedia](https://ru.wikipedia.org/wiki/Ряд_Тейлора)

## Фото

"C:\Users\Daniil\Desktop\i.webp"
