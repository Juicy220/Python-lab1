import numpy as np
from datetime import datetime
from quicksort_custom import quicksort
from shell_sort import shell_sort

a = input("Введите кол-во чисел в массиве ")
n = np.random.randint(0, 100, int(a))
print("Не отсортированный массив", n)
start_time_shell = datetime.now()
shell_sort(n, len(n))
end_time_shell = datetime.now()
start_time_custom = datetime.now()
quicksort(n)
end_time_custom = datetime.now()
start_time = datetime.now()
n.sort()
end_time = datetime.now()
print("Отсортированный массив", n)
print("Время выполнения встроенной сортировки:", end_time - start_time)
print("Время выполнения кастомной сортировки:", end_time_custom - start_time_custom)
print("Время выполнения сортировки Шелла:", end_time_shell - start_time_shell)
wait = input("Нажмите Enter чтобы закрыть программу")