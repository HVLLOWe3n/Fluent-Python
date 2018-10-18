from os.path import join
from functools import total_ordering


class A:
    def __init__(self):
        pass

    def go(self):
        print('Go, A!')


class B(A):
    def __init__(self):
        super(B, self).__init__()

    def go(self, name):
        print('Go, {}'.format(name))


#
# Magic methods
# Все магические методы являються объектно-ориентированныи
#

class SimpleClass:
    # Вызываеться первым при инициализации обьекта          **** Создает экземпляр обьекта ****
    # Принимает в качестве аргумента класс (cls)
    # За тем принимает аргументы __init__()
    def __new__(cls, *args, **kwargs):
        s = cls

    # Инициализирует класс (конструктор)
    # Принимает аргументы заданные нами (пользовательская сигнатура ------> пользовательский)
    # Может быть без аргументов (стандартная сигнатура метода ------> по-умолчанию)
    def __init__(self):
        pass

    # Определяет поведение оператора равенства
    def __eq__(self, other):
        pass

    # Определяет поведение оператора неравенства, !=.
    def __ne__(self, other):
        pass

    # Определяет поведение оператора меньше, <.
    def __lt__(self, other):
        pass

    # Определяет поведение оператора больше, >.
    def __gt__(self, other):
        pass

    # Определяет поведение оператора меньше или равно, <=.
    def __le__(self, other):
        pass

    # Определяет поведение оператора больше или равно, >=.
    def __ge__(self, other):
        pass

    # Сравнение идет по одному критерию
    # Определяет возможность сравнения объектов
    # Возвращает -1 если self < other
    # Возвращает 0 если self == other
    # Возвращает 1 если self > other
    def __cmp__(self, other):
        pass

    # Деструктор обьекта
    # Всегда вызываеться по завершению работы интерпретатора
    def __del__(self):
        pass


class FileObject:
    """Обёртка для файлового объекта, чтобы быть уверенным в том, что файл
    будет закрыт при удалении."""

    def __init__(self, filepath='~', filename='text.txt'):
        self.file = open(join(filename, filename), 'r+')

    def __del__(self):
        self.file.close()           # закрыть поток
        del self.file               # удаление объекта


@total_ordering     # декоратор для сравнений (__gt__, __lt__, __ge__, __le__)
class Words:
    """Класс для слов, определяющий сравнение по длине слов."""

    def __new__(cls, word, *args, **kwargs):
        """
        __new__ method
        :param word:
        :param args:
        :param kwargs:
        :return:
        """
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print('Value contains spaces. Truncating to first space.')
            word = word[:word.index(' ')]

        # return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __eq__(self, other):        # если вы сравниваем по длиние
        return len(self) == len(other)

    def __ne__(self, other):        # если вы сравниваем по длиние
        return len(self) != len(other)


print(Words('Bla').__eq__(Words('neww')))

#
# Почему в Python все обекты?
#
# В Python некоторые объекты не имеют методов
# некоторые не имеют атрибутов, и не все обекты являються подклассами

# Но все это объект в том смысле,
# что его можно назначить переменной или
# передать в качестве аргумента функции
