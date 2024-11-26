import threading
import time
#Многопоточность

def formula_1(x, iterations, results, idx):
    start = time.time()
    result = 0
    for _ in range(iterations):
        result += (x**2 - x**2 + x**4 - x**5 + x + x)
    results[idx] = result
    print(f"Formula 1 ({iterations} iterations): {time.time() - start:.5f} seconds")


def formula_2(x, iterations, results, idx):
    start = time.time()
    result = 0
    for _ in range(iterations):
        result += (x + x)
    results[idx] = result
    print(f"Formula 2 ({iterations} iterations): {time.time() - start:.5f} seconds")


def formula_3(results):
    start = time.time()
    total = results[0] + results[1]
    print(f"Formula 3 (combining results): {time.time() - start:.5f} seconds")
    return total


def run_multithreading(x, iterations):
    results = [0, 0]  # Сюда сохраняем результаты формул 1 и 2
    threads = []

    # Создаем потоки
    threads.append(threading.Thread(target=formula_1, args=(x, iterations, results, 0)))
    threads.append(threading.Thread(target=formula_2, args=(x, iterations, results, 1)))

    start = time.time()

    # Запускаем потоки
    for thread in threads:
        thread.start()

    # Ждем завершения потоков
    for thread in threads:
        thread.join()

    # Вычисляем формулу 3
    formula_3_result = formula_3(results)

    print(f"Total duration ({iterations} iterations): {time.time() - start:.5f} seconds")
    print("-" * 50)


# Выполняем вычисления для 10 000 и 100 000 итераций
run_multithreading(x=2, iterations=10_000)
run_multithreading(x=2, iterations=100_000)