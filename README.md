# задачи по Python


№ 13 - Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. Программа должна работать следующим образом:

1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
От 18 до 25 лет — 990 руб.
От 25 лет — полная стоимость 1390 руб.
3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.


№ 179 - Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.

В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
Далее программа работает по следующему алгоритму:
Преобразование введённой последовательности в список
Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.
Подсказка:
Помните, что у вас есть числа, которые могут не соответствовать заданному условию. В этом случае необходимо вывести соответствующее сообщение

