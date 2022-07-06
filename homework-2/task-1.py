# Координаты точек
# Почтовое отделение – (0, 2)
# Ул. Грибоедова, 104/25 – (2, 5)
# Ул. Бейкер стрит, 221б – (5, 2)
# Ул. Большая Садовая, 302-бис – (6, 6)
# Вечнозелёная Аллея, 742 – (8, 3)


from itertools import *


number_of_routes = []  # Количество всевозможных маршрутов
point_coordinates = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]  # Координаты точек
all_the_way = ()  # Расстояния между между точками всех маршрутов


# Вычисляем расстояние между почтовым отделением и всеми точками.
def calculate_dist_between_points(dist_post_office_points: tuple):
    for i in range(1, len(point_coordinates)):
        dist_post_office_points += (((point_coordinates[i][0] - point_coordinates[0][0]) ** 2 +
                                     (point_coordinates[i][1] - point_coordinates[0][1]) ** 2) ** 0.5,)
    return dist_post_office_points


# Вычисляем кол-во всевозможных маршрутов
def calculate_routes():
    for i in permutations(point_coordinates[1:]):
        temp = list(i)
        temp.insert(0, point_coordinates[0])
        number_of_routes.append(temp)


# Вычисляем дистанцию между адресами и обратно в почтовое отделение каждого маршрута
def calculate_dist_between_addresses(dist_post_office_points, all_way: tuple, distance_between_addresses: list,
                                     driveways: int) -> list:
    for i in range(len(number_of_routes)):
        for j in range(len(number_of_routes[i]) - 1):
            point_1 = number_of_routes[i][j]
            point_2 = number_of_routes[i][j + 1]
            all_way += ((((point_2[0] - point_1[0]) ** 2) + (point_2[1] - point_1[1]) ** 2) ** 0.5,)
        distance_between_addresses.append(list(all_way[driveways:driveways + len(point_coordinates) - 1]))
        for k in range(len(dist_post_office_points)):
            if number_of_routes[i][-1] == point_coordinates[1 + k]:
                distance_between_addresses[i].append(dist_post_office_points[k])
        driveways += 4
    return distance_between_addresses


def calculate_total_distance(distance_between_addresses: list) -> list:
    total_distance = []
    for i in range(len(distance_between_addresses)):
        total_distance.append(sum(distance_between_addresses[i]))
    return total_distance


# Вычисляем кратчайший путь(и)
def calculate_shortest_path(distance_between_addresses: list, total_distance: list) -> list:
    indexes = []
    for i in range(1, len(distance_between_addresses)):
        if sum(distance_between_addresses[i]) == min(total_distance):
            indexes.append(i)
    return indexes


# Выводим итоговый результат кратчайшего пути
def output_the_shortest_path(indexes: list, distance_between_addresses: list):
    for i in indexes:
        temp = number_of_routes[i]
        for j in range(len(temp) - 1):
            if j == 0:
                print(f"{temp[j]} -> {temp[j + 1]}[{distance_between_addresses[i][j]}]", end="")
                continue
            print(f" -> {temp[j + 1]}[{sum(distance_between_addresses[i][:j + 1])}]", end="")
        print(f" -> {temp[0]}[{sum(distance_between_addresses[i])}] = {sum(distance_between_addresses[i])}")


def main():
    # расстояние между почтовым отделением и всеми точками
    dist_post_office_points = calculate_dist_between_points(())

    # кол-во всевозможных маршрутов
    calculate_routes()

    # дистанция между адресами и обратно в почтовое отделение каждого маршрута
    distance_between_addresses = calculate_dist_between_addresses(dist_post_office_points,
                                                                  all_the_way,
                                                                  distance_between_addresses=[],
                                                                  driveways=0)
    # Всего расстояний каждого маршрута
    total_distance = calculate_total_distance(distance_between_addresses)

    # кратчайший путь(и)
    indexes = calculate_shortest_path(distance_between_addresses, total_distance)

    # итоговый результат кратчайшего(их) пути(ей)
    output_the_shortest_path(indexes, distance_between_addresses)


if __name__ == "__main__":
    main()


# (0, 2), (2, 5), (5, 2), (6, 6), (8, 3), (9, 4)
# Добавил дополнительную вершину (7, 2)
# Результат:
# (0, 2) -> (2, 5)[4.47213595499958] -> (6, 6)[8.07768723046357] -> (9, 4)[12.200792856081229] -> (8, 3)[15.806344131545218] -> (5, 2)[17.220557693918312] -> (0, 2)[22.220557693918312] = 22.220557693918312


# (0, 2), (2, 5), (5, 2), (6, 6), (8, 3), (9, 4), (7, 2)
# Добавил еще одну вершину (7, 2)
# Результат:
# (0, 2) -> (2, 5)[3.605551275463989] -> (8, 3)[5.0197648378370845] -> (6, 6)[6.433978400210179] -> (7, 2)[8.43397840021018] -> (9, 4)[12.039529675674169] -> (5, 2)[16.16263530129183] -> (0, 2)[21.16263530129183] = 21.16263530129183
