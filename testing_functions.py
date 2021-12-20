from all_functions import minimum, maximum, summary, composition, read_file
from math import prod
from random import randint
import unittest
from time import time


# Так как программа работает только для целых чисел, то ошибки переполнения быть не может,
# так что аварийного завершения работы возникать не будет
def numbers_for_test(n):
    numbers = []
    for i in range(n):
        numbers.append(randint(100000, 1000000))
    return numbers


class TestNumbers(unittest.TestCase):

    def test_minimum(self):
        nums = numbers_for_test(100)
        self.assertEqual(min(nums), minimum(nums), 'Функция поиска минимума некорректна')

    def test_maximum(self):
        nums = numbers_for_test(100)
        self.assertEqual(max(nums), maximum(nums), 'Функция поиска максимума некорректна')

    def test_summary(self):
        nums = numbers_for_test(100)
        self.assertEqual(sum(nums), summary(nums), 'Функция поиска суммы некорректна')

    def test_composition(self):
        nums = numbers_for_test(100)
        self.assertEqual(prod(nums), composition(nums), 'Функция поиска произведения некорректна')

    def test_time_needed(self):
        nums_1 = numbers_for_test(100)
        nums_2 = numbers_for_test(5000)
        nums_3 = numbers_for_test(100000)
        s1 = ''
        s2 = ''
        s3 = ''
        for num in nums_1:
            s1 += str(num) + ' '
        for num in nums_2:
            s2 += str(num) + ' '
        for num in nums_3:
            s3 += str(num) + ' '
        with open('test_i1.txt', 'w') as file:
            file.write(s1[:-1])
        with open('test_i2.txt', 'w') as file:
            file.write(s1[:-1] + ' ' + s2[:-1])
        with open('test_i3.txt', 'w') as file:
            file.write(s1[:-1] + ' ' + s2[:-1] + s3[:-1])
        start1 = time()
        nums_1_new = read_file('test_i1.txt')
        minimum(nums_1_new)
        maximum(nums_1_new)
        summary(nums_1_new)
        composition(nums_1_new)
        time1 = time() - start1
        start2 = time()
        nums_2_new = read_file('test_i2.txt')
        minimum(nums_2_new)
        maximum(nums_2_new)
        summary(nums_2_new)
        composition(nums_2_new)
        time2 = time() - start2
        start3 = time()
        nums_3_new = read_file('test_i3.txt')
        minimum(nums_3_new)
        maximum(nums_3_new)
        summary(nums_3_new)
        composition(nums_3_new)
        time3 = time() - start3
        self.assertGreater(time2, time1, 'Программа работает быстрее при увеличении размера входного файла')
        self.assertGreater(time3, time2, 'Программа работает быстрее при увеличении размера входного файла')

    # Проверяет, разное ли время требуется для выполнения всех функций (поиска минимума,
    # максимума, сложения и умножения) повторно на одном и том же наборе (из 100) чисел
    def test_time(self):
        nums = numbers_for_test(100)
        start1 = time()
        minimum(nums)
        maximum(nums)
        summary(nums)
        composition(nums)
        interval1 = time() - start1
        start2 = time()
        minimum(nums)
        maximum(nums)
        summary(nums)
        composition(nums)
        interval2 = time() - start2
        self.assertAlmostEqual(interval1, interval2)


if __name__ == '__main__':
    unittest.main()
