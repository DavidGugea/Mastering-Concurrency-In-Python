import concurrent.futures
from timeit import default_timer as timer
from is_prime import is_prime

values = [i for i in range(10 ** 13, 10 ** 13 + 1000)]


def concurrent_solve(n_workers):
    print('Number of workers {0}'.format(n_workers))

    start = timer()
    result = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_workers) as executor:
        futures = [executor.submit(is_prime, i) for i in values]
        completed_futures = concurrent.futures.as_completed(futures)

        sub_start = timer()

        for i, future in enumerate(completed_futures):
            if future.result():
                result.append(future.result())

        sub_duration = timer() - sub_start

    duration = timer() - start

    print('Sub took : {0}'.format(sub_duration))
    print('Took : {0}'.format(duration))
