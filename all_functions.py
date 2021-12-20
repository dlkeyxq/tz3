# Программа работает только для целых чисел
def read_file(file):
    with open(file) as f:
        numbers = []
        for number in f.read().split():
            numbers.append(int(number))
    return numbers


def minimum(numbers):
    min_n = numbers[0]
    for number in numbers:
        if min_n > number:
            min_n = number
    return min_n


def maximum(numbers):
    max_n = numbers[0]
    for number in numbers:
        if max_n < number:
            max_n = number
    return max_n


def summary(numbers):
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += number
    return sum_of_numbers


def composition(numbers):
    comp_of_numbers = 1
    for number in numbers:
        comp_of_numbers *= number
    return comp_of_numbers


if __name__ == '__main__':
    nums = read_file('nums.txt')
    print(f'минимум: {minimum(nums)}\nмаксимум: {maximum(nums)}\n'
          f'сумма: {summary(nums)}\nпроизведение: {composition(nums)}')
