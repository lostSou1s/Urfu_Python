class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """

        if self.start is None:
            return IndexError

        pop_item = self.start
        self.start = self.start.nref
        if self.start is None:
            self.end = None
        else:
            self.start.pref = None

        pop_item.nref = None
        val = pop_item.data

        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        node = Node(val)

        if self.start is None:
            self.start = node
            self.end = node
        else:
            node.pref = self.end
            self.end.nref = node
            self.end = node

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        node = Node(val)
        total = self.start
        count = 0
        while count < n and total:
            total = total.nref
            count += 1
        if total:
            node.next = total
            node.pref = total.pref
            if total.pref:
                total.pref.next = node
            else:
                self.start = node
            total.pref = node
        else:
            self.push(val)


    def print(self):
        """
        вывод на печать содержимого очереди
        """
        total = self.end
        if self.end is None:
            return Exception
        else:
            while total:
                print(total.data)
                total = total.pref



queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.pop()
queue.insert(2,10000)
queue.print()
