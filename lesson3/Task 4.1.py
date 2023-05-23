n = int(input('Введите целое число n: '))

cubes_summary = 0
i = 1

for i in range(1, n+1):
    cubes_summary += i ** 3

print("Сумма кубов всех целых чисел от 1 до", n, "включительно, равна", cubes_summary)