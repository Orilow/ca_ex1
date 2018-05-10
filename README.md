# ca_ex1
Combinatory Algorithms exercise №1
Knight's and pawn's coordinates are known.
Find the route in the chess notation using the depth first search algorithm(DFS).
The order of viewing the fields is in list KNIGHT_DELTAS.

in.txt: Knight's and pawn's coordinates
out.txt: Route in the chess notation

На шахматной доске стоят белый конь и черная пешка. Напечатать марш-
рут коня позволяющий уничтожить пешку.
Примечание: пешка - неподвижная, конь не должен попадать под удар
пешки.
Метод решения: Поиск в глубину.
Порядок обхода полей в листе KNIGHTS_DELTAS.
Файл исходных данных:
Координаты коня и пешки.
Сначала располагаются координаты коня затем пешки. Координаты даются
в шахматной нотации, т.е. в виде AB, где A может принимать значения от a
до h, B от 1 до 8.

файл данных должен быть следующим:
b2
e6
Формат файла результатов:
Маршрут в шахматной нотации.
Маршрут должен начинаться координатами коня и заканчиваться координа-
тами пешки. Каждый ход записывается с новой строки.