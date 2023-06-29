import random


class RandomValue:
    def __init__(self, *args):
        self._list = list(args)

    def __str__(self):
        return f"MyList object: {self._list}"

    def __iter__(self):
        """
        Метод __iter__ возващает ссылку на Объект-Итератор, класс которого реализован ниже
        """
        return RandomValueIterator(self._list)
    """Your implementation here"""

class RandomValueIterator:
    def __init__(self, RandomValueIterator):
        self.RandomValueIterator = RandomValueIterator  # неизменнно с момента инициализации
        self._size = range(100)
        # self._size = len(self.RandomValueIterator)  # неизменнно с момента инициализации
        self._curr_index = 0  # увеличивается на 1 при каждом вызове __next__!
        for _ in RandomValueIterator:
            yield random.randint(1, 100)

    def __iter__(self):
        return self

    def __next__(self):
        """
        Метод __next__ объекта-итератора реализует логику получения следующего элемента из последовательности
        В данном случае, атрибут экземпляра '_curr_index' хранит текущее значение индекса и увеличивается на 1
        при каждом вызове метода __next__, пока не будет достигнут лимит
        """
        if self._curr_index < self._size:
            # 1. Получить элемент из внутреннего списка по индексу 'self._curr_index'
            result = self._some_list[self._curr_index]
            # 2. Увеличить значение 'self._curr_index' на 1
            self._curr_index += 1
            # 3. Вернуть полученный элемент
            return result
        else:
            # необходимо выбросить StopIteration исключение, если значение 'self_curr_index'
            # достигло значеня 'self._size' value - это значит, что внутренний список "закончился"
            # и дальнейшие вызовы __next__ попросту не имеют смысла
            raise StopIteration

        print(next(i))
        iterator = RandomValueIterator()
        for _ in range(50):
            print(next(result))

    my_limit = int(input("Введите лимит: "))
    my_random = RandomValue(limit=my_limit)

    results = [elem for elem in my_random]
    print(results)

    assert len(results) == my_limit
    for i in results:
        assert i is not None
    # def random_gen(self):
    #     count = 0
    #     while count <50:
    #         yield random.randint(1,100)
    #         count += 1
