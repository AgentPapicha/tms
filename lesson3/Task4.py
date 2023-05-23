n = int(input('Введите целое число n: '))

cubes_summary = 0
i = 1

while i <= n:
    cubes_summary += i ** 3
    i += 1

print("Сумма кубов всех целых чисел от 1 до", n, "включительно, равна", cubes_summary)

