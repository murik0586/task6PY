import multiprocessing
import time


def formula_1_process(x, iterations, queue):
    start = time.time()
    result = 0
    for _ in range(iterations):
        result += (x**2 - x**2 + x**4 - x**5 + x + x)
    queue.put(("formula_1", result, time.time() - start))


def formula_2_process(x, iterations, queue):
    start = time.time()
    result = 0
    for _ in range(iterations):
        result += (x + x)
    queue.put(("formula_2", result, time.time() - start))


def formula_3_process(queue):
    start = time.time()
    results = {}
    while len(results) < 2:  # Ждем результатов формул 1 и 2
        key, result, duration = queue.get()
        results[key] = result
        print(f"{key} completed in {duration:.5f} seconds")

    total = results["formula_1"] + results["formula_2"]
    print(f"Formula 3 (combining results): {time.time() - start:.5f} seconds")
    return total


def run_multiprocessing(x, iterations):
    queue = multiprocessing.Queue()

    # Создаем процессы
    process1 = multiprocessing.Process(target=formula_1_process, args=(x, iterations, queue))
    process2 = multiprocessing.Process(target=formula_2_process, args=(x, iterations, queue))

    start = time.time()

    # Запускаем процессы
    process1.start()
    process2.start()

    # Ожидаем завершения процессов
    process1.join()
    process2.join()

    # Вычисляем формулу 3
    formula_3_result = formula_3_process(queue)

    print(f"Total duration ({iterations} iterations): {time.time() - start:.5f} seconds")
    print("-" * 50)


if __name__ == '__main__':
    # Выполняем вычисления для 10 000 и 100 000 итераций
    run_multiprocessing(x=2, iterations=10_000)
    run_multiprocessing(x=2, iterations=100_000)