class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """

        if self.end is None:
            return IndexError

        pop_item = self.end
        self.end = self.end.pref
        pop_item.pref = None
        val = pop_item.data

        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        node = Node(val)

        if self.end is None:
            self.end = node
        else:
            node.pref = self.end
            self.end = node

        pass

    def print(self):
        """
        вывод на печать содержимого стека
        """
        total = self.end
        if self.end is None:
            return Exception
        else:
            while total:
                print(total.data)
                total = total.pref


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()
