import pytest
from main import *
import networkx as nx


class TestDiGraphClass:
    def setup(self):
        self.list_data_1 = [['A', 'B', 1],
                            ['A', 'C', 2],
                            ['B', 'C', 3]]

        self.list_data_2 = [['A', 'B', 1],
                            ['A', 'C', 2],
                            ['B', 'C', 3],
                            ['D', 'C', 3]]

        self.list_data_3 = [['A', 'B', 1],
                            ['B', 'C', 2],
                            ['C', 'D', 3],
                            ['A', 'E', 4],
                            ['E', 'F', 5],
                            ['F', 'D', 6]]

        self.list_data_contur_1 = [['A', 'B', 1],
                                   ['B', 'C', 2],
                                   ['C', 'A', 3]]

        self.list_data_contur_2 = [['A', 'B', 1],
                                   ['B', 'C', 2],
                                   ['C', 'D', 3],
                                   ['D', 'A', 3]]

        self.list_data_contur_3 = [['A', 'B', 1],
                                   ['B', 'C', 2],
                                   ['C', 'D', 3],
                                   ['D', 'E', 4],
                                   ['E', 'F', 5],
                                   ['F', 'A', 6]]

        self.list_negative_values = [['A', 'B', -1],
                                     ['A', 'C', 2],
                                     ['B', 'C', -3]]

    def test_positive_paths(self):
        g_1 = Graph(3)
        g_2 = Graph(4)
        g_3 = Graph(6)
        assert {'B': ['A', 'B'], 'C': ['A', 'C']} == g_1.get_all_routes_for_test(self.list_data_1, 'A')
        assert {'B': ['A', 'B'], 'C': ['A', 'C']} == g_2.get_all_routes_for_test(self.list_data_2, 'A')
        assert {'B': ['A', 'B'], 'C': ['A', 'B', 'C'], 'D': ['A', 'B', 'C', 'D'], 'E': ['A', 'E'], 'F': ['A', 'E', 'F']} == g_3.get_all_routes_for_test(self.list_data_3, 'A')

    def test_positive_conturs(self):
        g_1 = Graph(3)
        g_2 = Graph(4)
        g_3 = Graph(6)
        assert g_1.get_min_circuit_for_test(self.list_data_contur_1) == 6, "не тот вес"
        assert g_2.get_min_circuit_for_test(self.list_data_contur_2) == 9, "не тот вес"
        assert g_3.get_min_circuit_for_test(self.list_data_contur_3) == 21, "не тот вес"

    def test_negative_paths(self):
        g_1 = Graph(3)
        g_2 = Graph(4)
        assert g_1.get_min_circuit_for_test(self.list_negative_values) ==  "Данный граф имеет отрицательные значения!"
        assert g_1.get_min_circuit_for_test([]) == "В данном графе нет контура с минимальной длиной."
        assert g_2.get_min_circuit_for_test(self.list_data_2) == "В данном графе нет контура с минимальной длиной."


def main():
    pass


if __name__ == '__main__':
    main()
