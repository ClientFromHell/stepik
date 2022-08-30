class multifilter:

    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos > 0

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.results = []
        self.count = -1
        self.pos = 0
        self.neg = 0

        for element in self.iterable:
            for func in self.funcs:
                if func(element):
                    self.pos += 1
                else:
                    self.neg += 1

            if judge(self.pos, self.neg):
                self.results.append(element)
            self.pos = 0
            self.neg = 0

    def __next__(self):
        try:
            self.count += 1
            return self.results[self.count]
        except IndexError:
            raise StopIteration

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [x for x in range(31)]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]

