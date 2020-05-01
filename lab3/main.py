import networkx as nx
import matplotlib.pyplot as plt
import sys


class Graph(object):
    def __init(self):
        pass

    def __init__(self, edges):
        self.edge_numbers = edges
        self.list_for_graph = []
        self._is_negative = False


    def __str__(self):
        return "============ Построение графа ============"

    def is_negative_weight(self):
        return self._is_negative

    def create_graph(self):
        for _ in range(0, self.edge_numbers):  # method for append graph
            tmp_list = []
            from_val = input("От: ")
            to_val = input("До: ")
            print(f"{from_val} -> {to_val}")
            weight_val = float(input("Вес текущего узла: "))
            tmp_list.append(from_val)
            tmp_list.append(to_val)
            tmp_list.append(weight_val)
            self.list_for_graph.append(tmp_list)
            print("\n")

    def init_graph(self):
        dg = nx.DiGraph()  # initialization graph
        dg.add_weighted_edges_from(self.list_for_graph)  # appending graph
        return dg

    """This method for testing"""
    def get_all_routes_for_test(self, list_data, value):
        dg = nx.DiGraph()  # initialization graph for test-cases
        dg.add_weighted_edges_from(list_data)
        result_dict = {}
        uniq_values = []
        for edge in list_data:
            if (edge[0] != value and edge[0] not in uniq_values):  # list edges
                uniq_values.append(edge[0])
            if (edge[1] != value and edge[1] not in uniq_values):
                uniq_values.append(edge[1])

        for edge in uniq_values:
            try:
                result_dict[str(edge)] = nx.dijkstra_path(dg, value, edge)  # search all paths from source to everything edges
            except:
                pass
        return result_dict

    """Method for test-cases"""
    def get_min_circuit_for_test(self, list_data):
        if len([i[2] for i in list_data if i[2] < 0]) > 0:
            return "Данный граф имеет отрицательные значения!"
        uniq_values = []
        min_weight = sys.maxsize
        raw_list_weight = []
        end_path = None
        dg = nx.DiGraph()  # initialization graph for test-cases
        dg.add_weighted_edges_from(list_data)
        try:
            for edge in list_data:
                if (edge[0] not in uniq_values):  # list all edges
                    uniq_values.append(edge[0])
                if (edge[1] not in uniq_values):
                    uniq_values.append(edge[1])

            for edge in uniq_values:
                for edge_internal in uniq_values:
                    try:
                        raw_list_weight.append(nx.single_source_dijkstra(dg, edge, edge_internal))  # process all path
                    except:
                        pass
            for list_weight in raw_list_weight:
                if list_weight[0] < min_weight and sorted(list_weight[1]) == sorted(uniq_values):  # process minimal path
                    min_weight = list_weight[0]
                    end_path = list_weight[1]
            last_path = nx.single_source_dijkstra(dg, end_path[-1], end_path[0])
        except:
            pass

        try:
            if end_path[0] != last_path[1][1]:
                return "В данном графе нет контура с минимальной длиной."
        except:
            return "В данном графе нет контура с минимальной длиной."
        return last_path[0] + min_weight

    def draw_graph(self):
        nx.draw(self.init_graph(), with_labels=True, font_weight='bold')  # output graph
        plt.show()

    def get_all_routes(self, value):
        result_str = ''
        result_dict = {}
        uniq_values = []
        for edge in self.list_for_graph:
            if (edge[0] != value and edge[0] not in uniq_values):  # list edges
                uniq_values.append(edge[0])
            if (edge[1] != value and edge[1] not in uniq_values):
                uniq_values.append(edge[1])

        for edge in uniq_values:
            try:
                result_dict[str(edge)] = nx.dijkstra_path(self.init_graph(), value, edge)  # search all paths from source to everything edges
            except:
                pass

        for end_points, local_paths in zip(result_dict.keys(), result_dict.values()):  # beautiful output
            result_str = ''
            print(f"От {value} до {end_points}: ", end="")
            for end_point in local_paths:
                result_str += str(end_point)
                result_str += '->'
            print(result_str[:-2])
        return result_dict

    def get_min_circuit(self):
        uniq_values = []
        min_weight = sys.maxsize
        raw_list_weight = []
        end_path = None
        try:
            for edge in self.list_for_graph:
                if (edge[0] not in uniq_values):  # list all edges
                    uniq_values.append(edge[0])
                if (edge[1] not in uniq_values):
                    uniq_values.append(edge[1])

            for edge in uniq_values:
                for edge_internal in uniq_values:
                    try:
                        raw_list_weight.append(nx.single_source_dijkstra(self.init_graph(), edge, edge_internal))  # process all path
                    except:
                        pass
            for list_weight in raw_list_weight:
                if list_weight[0] < min_weight and sorted(list_weight[1]) == sorted(uniq_values):  # process minimal path
                    min_weight = list_weight[0]
                    end_path = list_weight[1]
            last_path = nx.single_source_dijkstra(self.init_graph(), end_path[-1], end_path[0])
        except:
            pass

        try:
            if end_path[0] != last_path[1][1]:
                return "В данном графе нет контура с минимальной длиной."
        except:
            return "В данном графе нет контура с минимальной длиной."
        return f"Контур минимальной длины:{'->'.join(end_path) + '->' + last_path[1][1]} \nМинимальный вес: {last_path[0] + min_weight}"


def main():
    edge_numbers = int(input("Введите количество маршрутов: "))
    obj_for_graph = Graph(edge_numbers)
    obj_for_graph.create_graph()
    obj_for_graph.draw_graph()
    search_value = input("Введите опорный узел: ")
    print(f"Все минимальные маршруты. От узла {search_value}\n")
    print(obj_for_graph.get_all_routes(search_value))
    print(obj_for_graph.get_min_circuit())


if __name__ == '__main__':
    main()
