"""Закодируйте любую строку по алгоритму Хаффмана."""

import collections


class Leaf:
    """Построение листов в дереве
        key - буква из строки
        value - частота буквы"""

    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value


class Node:
    """Построение узлов в дереве"""

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class Haffman:
    """Алгоритм Хаффмана"""

    def __init__(self):
        self._table = dict()
        self._data = []
        self._str = ''

    def _list(self, str):
        counter = dict(collections.Counter(str))
        counter = collections.OrderedDict(sorted(counter.items(), key=lambda k: k[1], reverse=True))
        for key, value in counter.items():
            self._data.append(Leaf(key, value))
        return True

    def _haffman_tree(self):
        while len(self._data) > 2:
            a, b = self._data.pop(), self._data.pop()
            temp = Node(b.value + a.value, b, a)
            if temp.value > self._data[0].value:
                self._data.insert(0, temp)
            elif temp.value < self._data[-1].value:
                self._data.append(temp)
            else:
                for i in range(1, len(self._data)):
                    if self._data[i - 1].value >= temp.value > self._data[i].value:
                        self._data.insert(i, temp)
                        break
        self._data = Node(self._data[0].value + self._data[1].value, self._data[0], self._data[1])

    def _haffman_recurs(self, data: Node, code=''):
        if isinstance(data, Node):
            self._haffman_recurs(data.left, code=code + '0')
            self._haffman_recurs(data.right, code=code + '1')
        elif isinstance(data, Leaf):
            self._table[data.key] = code

    def _encode(self):
        res = []
        for i in self._str:
            res.append(self._table[i])
        return ''.join(res)

    def encode(self, str):
        self.__init__()
        self._str = str
        self._list(str)
        self._haffman_tree()
        self._haffman_recurs(self._data)
        return self._encode()

    def decode(self, code_str, code_table=None):
        if code_table:
            self._table = code_table
        decode_table = {value: key for key, value in self._table.items()}
        res = []
        i = 0
        while i < len(code_str):
            j = i + 1
            while code_str[i:j] not in decode_table.keys():
                j += 1
            res.append(decode_table[code_str[i:j]])
            i = j
        return ''.join(res)

    def get_table_code(self):
        if self._table:
            return self._table
        return False


my_str = input('Введите строку: ')
h = Haffman()
print(h.encode(my_str), h.get_table_code(), h.decode(h.encode(my_str)), sep='\n')


# Введите строку: delicious cookies
# 0011100001001110111000001010100110101000000011111100010
# {'o': '000', 'l': '00100', 'u': '00101', 'd': '0011', 's': '010', ' ': '0110', 'k': '0111', 'e': '100', 'c': '101', 'i': '11'}
# delicious cookies
