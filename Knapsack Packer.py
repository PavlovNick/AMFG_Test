from itertools import permutations  # импорт функции для генерации всех возможных перестановок элементов списка

v = [60, 100, 120]  # Ценности предметов
w = [10, 20, 30]  # Веса предметов
W = 50  # Грузоподъемность


def merge_lists(v, w):  # функция для записи двух списков(v, w) в один
    Full_list = []
    for i in range(0, len(v)):
        temp = []
        temp.append(w[i])
        temp.append(v[i])
        Full_list.append(temp)
    return Full_list  # возвращает список, в котором каждым элементом будет список[[w[0], v[0]], [w[2], v[1]], ...]


def table(merge_lists, W):                           # функция использует метод динамического программирования,
    n = len(merge_lists) - 1                         # складывает таблицу ценности загрузки рюкзака
    F = [[0] * (W + 1) for i in range(n + 1)]        # в зависимости от предмета и веса
    for i in range(1, n + 1):
        for j in range(W + 1):
            if j >= merge_lists[i][0]:
                F[i][j] = max(F[i - 1][j], F[i - 1][j - merge_lists[i][0]] + merge_lists[i][1])
            else:
                F[i][j] = F[i - 1][j]
    return F  # возвращает двумерный список(таблицу)


def weights(merge_lists, W, F):  # функция для востановления ответа, а именно какие веса
    Ans = []                     # были взяты для получения максимального значения
    tmp = W
    n = len(merge_lists) - 1
    for i in range(n, 0, -1):
        if F[i][tmp] != F[i - 1][tmp]:
            Ans.append(merge_lists[i][0])
            tmp -= merge_lists[i][0]
    return Ans  # возвращает список с весами предметов


def calculate_max_value(v, w, W):                                    # функция перебирает все перестановки списка из
    all_combinations_list = list(permutations(merge_lists(v, w)))    # merge_lists, формирует списки с максимальной
    Answer_list = []                                                 # ценностью рюкзака и весами для каждой
    for i in range(len(all_combinations_list)):                      # перестановки, из всех перестановок выберает ту,
        temp_list = []                                               # у которой самая большая ценность
        local_max_value = table(all_combinations_list[i], W)[len(w) - 1][W]
        local_max_value_weight = weights(all_combinations_list[i], W, table(all_combinations_list[i], W))
        temp_list.append(local_max_value)
        temp_list.append(local_max_value_weight)
        Answer_list.append(temp_list)
    result_list = max(Answer_list, key=lambda item: item[0])
    (result_list[1]).sort(reverse=True)
    return result_list  # возвращает финальный список [ценность, [веса]] с отсортированными по убыванию весами


result_list = calculate_max_value(v, w, W)
print(result_list[0])  # выводим максимальную ценность
print(' '.join(map(str, result_list[1])))  # выводим в нужном формате веса

