from graph_algorithms.Kruskals_algorithm import Kruskal
from graph_algorithms.Hamiltonian_cycle import Hamilton
from graph_algorithms.Primal import Primal_min
from graph_algorithms.__init__ import drawing, drawing2, drawing3, test_Kruskal, test_Hamilton, test_Primal_min

points = []
edges = []

points, edges, k = drawing(points, edges)  # рисунок волка

graph_instance = Kruskal(points, edges)
graph_instance.draw_only(k)  # только рисунок без изменений

sorted_edges_min = graph_instance.sort_edges_min()  # сортируем от меньшего к большему с учетом что индекс вершин ребра от меньшего к большему
sorted_edges_max = graph_instance.sort_edges_max()  # сортируем от большего к меньшему с учетом что индекс вершин ребра от !меньшего к большему!
print("Упорядоченные ребра (по возрастанию веса):", sorted_edges_min)  # вывод сорт мин
print("Упорядоченные ребра (по убыванию веса):", sorted_edges_max)  # вывод сорт макс

print("\nМинимальное покрывающее дерево\n")
mst_edges_min = graph_instance.kruskals_algorithm(sorted_edges_min)  # запускаем алгоритм для минимального
print("\n\nМаксимальное покрывающее дерево\n")
mst_edges_max = graph_instance.kruskals_algorithm(sorted_edges_max)  # для максимального
print("\nМинимальное покрывающее дерево (ребра):", mst_edges_min)
print("Максимальное покрывающее дерево (ребра):", mst_edges_max)

Tmin = graph_instance.result_weight(mst_edges_min)
Tmax = graph_instance.result_weight(mst_edges_max)
print("T(min) = ", Tmin)  # вес минимального дерева
print("T(max) = ", Tmax)  # вес максимального дерева

graph_instance.view(mst_edges_min, mst_edges_max, k)  # вывод двух получившихся деревьев

if test_Kruskal(False): print('Тест алгоритма Краскала успешно завершен')

print("\n\n\n\n\n___________________________________________________________________________________________________________\n\n\n\n\n")

points, edges = drawing2(points, edges)  # рисунок лисы
hamilton_instance = Hamilton(points, edges)
n = len(points)  # Количество вершин графа

hamilton_instance.aviable() # Запросим у пользователя, с какой вершины начинать

# Запрос на ввод начальной вершины
start_vertex_label = input(f"Введите букву вершины, с которой начать ({hamilton_instance.vertex_labels[0]}-{hamilton_instance.vertex_labels[-1]}) : ").strip()
start_vertex = hamilton_instance.vertex_labels.index(start_vertex_label)  # Преобразуем букву в индекс

cycle = hamilton_instance.hamiltonian_cycle(start_vertex)  # Ищем Гамильтонов цикл
print(cycle)
hamilton_instance.cycle_exist(cycle) # проверяем, существует ли цикл
hamilton_instance.draw() # рисуем получившийся цикл
#
if test_Hamilton(False): print('Тест алгоритма Гамильтона успешно завершен')

print("\n\n\n\n\n___________________________________________________________________________________________________________\n\n\n\n\n")

# Задаем граф в виде списка смежности (словаря): ключ - вершина, значение - (вес, сосед)
graf = drawing3()

# Запуск алгоритма
begin = '1'  # Начальная вершина
primal_min_instance = Primal_min(graf)  # Создаем экземпляр класса
tree, min_weight = primal_min_instance.run(begin)  # Запускаем алгоритм

primal_min_instance.min_tree()
print(f"Суммарный мин. вес W(min) = {min_weight}")

if test_Primal_min(False): print('Тест Праймала успешно завершен')



