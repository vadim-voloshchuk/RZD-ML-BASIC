# Добиваем основы
## Задача: Рекомендации сериалов

Netflix хочет улучшить свой алгоритм рекомендации сериалов для пользователей. Для этого им необходимо разработать программу на Python, которая будет просматривать предпочтения пользователей и на основе этой информации предлагать им сериалы для просмотра.

Пользовательские данные хранятся в списках, где каждый элемент представляет сериал в виде списки с названием сериала и оценкой от 1 до 5, например: ["Breaking Bad", 5]", ["Stranger Things", 4]", и так далее.

Netflix хочет, чтобы вы создали программу, которая будет предлагать пользователю новые сериалы на основе следующих правил:

Если пользователь смотрел и оценил сериалы с оценкой 5, программа должна предложить ему сериалы с оценкой 5, которые он еще не смотрел.

Если пользователь смотрел сериалы с оценкой ниже 3, программа должна предложить ему сериалы с оценкой 4 или 5, которые он еще не смотрел.

Если пользователь смотрел сериалы с оценкой от 3 до 4, программа должна предложить ему сериалы с оценкой 4 или 5, которые он еще не смотрел.

Если у пользователя нет оценок, программа должна предложить ему случайный сериал.

```
serials_base = [["Великолепный Век", 5], ["Великолепный Век 2", 4]]
users_wath = input... ["Великолепный Век", "Великолепный Век 2"]
```
## Задача: Анализ рейтинга фильмов

Вы получили данные о рейтинге фильмов от пользователей. Каждая запись представляет собой тройку значений: название фильма, рейтинг (от 1 до 5) и возраст пользователя, который оценил фильм. Вам необходимо выполнить следующие задачи:

Разделите фильмы на две группы: "Для детей" (фильмы с рейтингом 4 или 5 и возрастом пользователя до 12 лет включительно) и "Для взрослых" (фильмы с рейтингом 4 или 5 и возрастом пользователя 13 лет и старше).

Определите средний рейтинг для каждой из двух групп фильмов.

Найдите название фильма с самым высоким рейтингом среди фильмов для детей и фильмов для взрослых.

Подсчитайте количество фильмов с каждым из рейтингов (1, 2, 3, 4, 5).

Выведите на экран следующую информацию:

- Средний рейтинг для фильмов для детей.
- Средний рейтинг для фильмов для взрослых.
- Название фильма с самым высоким рейтингом среди фильмов для детей.
- Название фильма с самым высоким рейтингом среди фильмов для взрослых.
- Количество фильмов с каждым из рейтингов (1, 2, 3, 4, 5).

Примечание:

 - Для хранения данных о фильмах и их рейтинге, вы можете использовать списки или другие подходящие структуры данных.
Вы можете предположить, что данные уже доступны в вашей программе в виде списка записей.

## Задача: Анализ интернет-трафика

Google собирает данные о потоке интернет-трафика в реальном времени. Вам нужно разработать программу для анализа этого трафика, используя списки. Вам предоставлен список записей о событиях в следующем формате:

python
```
traffic = [
    ["google.com", "пользователь1", 10],
    ["facebook.com", "пользователь2", 5],
    ["google.com", "пользователь2", 7],
    ["youtube.com", "пользователь1", 15],
    # и так далее...
]
```
Вам нужно выполнить следующие задачи:

Разделите трафик на две группы: "популярные" сайты (сайты с общим количеством посещений более 10) и "непопулярные" сайты (сайты с общим количеством посещений 10 и менее).

Для каждой из двух групп найдите самый посещаемый сайт (с наибольшим количеством посещений).

Определите, сколько пользователей посетили каждый из сайтов. Для этого создайте список кортежей, где каждый кортеж содержит название сайта и количество уникальных пользователей, посетивших этот сайт.

Выведите на экран следующую информацию:

- Список "популярных" сайтов.
- Список "непопулярных" сайтов.
- Название самого посещаемого сайта среди "популярных" и "непопулярных".
- Количество пользователей, посетивших каждый сайт.
Примечание:

Вы можете использовать циклы и условные операторы для обработки данных в списке трафик.
Для подсчета уникальных пользователей на каждом сайте, вы можете использовать множества или другие подходящие структуры данных.
Эта задача поможет вам практиковаться в обработке данных с использованием списков, циклов и ветвлений, и она не требует словарей.




