### Hexlet tests and linter status:
[![Actions Status](https://github.com/Cotuchini/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/Cotuchini/python-project-49/actions)

<a href="https://codeclimate.com/github/Cotuchini/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/59ba38743763e415d39b/maintainability" /></a>

Poetry version 1.4.1
Python 3.10.10

Разворачивание пакета игр происходит с помощью утилиты make, запускающей из файла makefile соответствующие шорткаты
(более короткое описание используемых команд). 
Например, команда "make package-update" (инсталляция пакета) выполнит команду "package-update: build publish package-install",
содержащую внутри себя три шортката, запускающих последовательно команды сборки пакета, отладки и установки.


**Первый проект курса Хекслет "Профессия Python-разработчик"**

Набор арифметических мини-игр, запускаемых из консоли, вы можете установить следующей командой: 

>pip install git+https://github.com/Cotuchini/python-project-49


Описание игр:
1. **Игра "Проверка на чётность"**
Правила игры: пользователю показывается случайное число. Ему нужно ответить yes, если число чётное, или no если нечётное.
Запустить игру из консоли вы можете командой brain-even.

Brain-even:
[![asciicast](https://asciinema.org/a/cJ6dXGMrwiNZw2xPx5qsA16Ur.svg)](https://asciinema.org/a/cJ6dXGMrwiNZw2xPx5qsA16Ur)

2. **Игра "Калькулятор"**
Правила игры: пользователю показывается случайное математическое выражение, например 35 + 16, которое нужно вычислить записать правильный ответ.
Запустить игру из консоли вы можете командой brain-calc.

Brain-calc:
[![asciicast](https://asciinema.org/a/qRJw3zYvqVGXqGmEK9vnio4xc.svg)](https://asciinema.org/a/qRJw3zYvqVGXqGmEK9vnio4xc)

3. **Игра "наибольший общий делитель (НОД)"** 
Правила игры: пользователю показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
Запустить игру из консоли вы можете командой brain-gcd.

Brain-gcd:
[![asciicast](https://asciinema.org/a/YaJ9wS50UVfFstUVfeLIlG4OF.svg)](https://asciinema.org/a/YaJ9wS50UVfFstUVfeLIlG4OF)

4. **Игра "Арифметическая прогрессия"**
Правила игры: игроку показывается ряд чисел, образующий арифметическую прогрессию, любое одно из чисел заменяется двумя точками. Игрок должен определить это число.
Запустить игру из консоли вы можете командой brain-progression.

Brain-progression:
[![asciicast](https://asciinema.org/a/m01DkqUphzb2XHF4i1jpXNwaV.svg)](https://asciinema.org/a/m01DkqUphzb2XHF4i1jpXNwaV)

5. **Игра "Простое ли число?"**
Правила игры: пользователю показывается случайное число. И ему нужно ответить yes, если число простое, или no если составное.
Запустить игру из консоли вы можете командой brain-prime.

Brain-prime:
[![asciicast](https://asciinema.org/a/y2lpWlaUexvxiiFfjs7s7ZoHZ.svg)](https://asciinema.org/a/y2lpWlaUexvxiiFfjs7s7ZoHZ)
