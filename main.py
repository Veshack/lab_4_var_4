from itertools import combinations


class Item:
    def __init__(self, name, symbol, size, points):
        self.name = name
        self.symbol = symbol
        self.size = size
        self.points = points


items = [
    Item("Винтовка", "r", 3, 25),
    Item("Пистолет", "p", 2, 15),
    Item("Боекомплект", "a", 2, 15),
    Item("Аптечка", "m", 2, 20),
    Item("Ингалятор", "i", 1, 5),
    Item("Нож", "k", 1, 15),
    Item("Топор", "x", 3, 20),
    Item("Оберег", "t", 1, 25),
    Item("Фляжка", "f", 1, 15),
    Item("Антидот", "d", 1, 10),
    Item("Еда", "s", 2, 20),
    Item("Арбалет", "c", 2, 20),
]

def combination(items, max_size, individual_points):
    final_combination = []
    finally_points = []
    for i in range(1, len(items) + 1):
        for combination in combinations(items, i):
            final_size = sum(item.size for item in combination)
            combination_points = sum(item.points for item in combination)
            final_points = (
                combination_points
                - (max_points - combination_points)
                + individual_points
            )
            if final_size <= max_size and final_points > 0:
                final_combination.append(combination)
                finally_points.append(final_points)
    return final_combination, finally_points


start_points = 15
bag_size = 9 #Поменять на 7 для проверки доп задания (Оставить 9 для проверки основного задания)
grid_size = 3
max_points = sum(item.points for item in items)

combos, finally_points = combination(items, bag_size, start_points)

def print_inventory(combos, finally_points):
    for combo, points in zip(combos, finally_points):
        print("Комбинация:")
        combination = []
        for item in combo:
            size = item.size
            symbol = item.symbol
            for i in range(size):
                combination.append([symbol])
        if len(combination) != bag_size:
            while len(combination) != bag_size:
                combination.append([" "])
        for j in range(0, bag_size, grid_size):
            try: print(combination[j], combination[j + 1], combination[j + 2])
            except: print(combination[j])
        print("Итоговые очки выживания:", points)


print_inventory(combos, finally_points)
#Если вывода нет, значит решение отсутствует для данного условия
