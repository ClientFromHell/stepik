# ========================== MoneyBox task ==========================
#
class MoneyBox:

    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.v = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        self.v = v
        if self.v <= self.capacity:
            return True
        else:
            return False


    def add(self, v):
        # положить v монет в копилку
        self.v = v
        if self.can_add(self.v) and self.capacity >= 0 and self.capacity >= self.v:
            self.capacity = self.capacity - self.v
        else:
            return False

# ========================== Bufer task ==========================
#
class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.buffer = []
        self.summary = 0

    def add(self, *a):
        # добавить следующую часть последовательности
        self.buffer += a
        while len(self.buffer) >= 5:
            self.summary = sum(self.buffer[:5])
            self.buffer = self.buffer[5:]
            print(self.summary)


    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены

        if len(self.buffer) < 5:
            return self.buffer

