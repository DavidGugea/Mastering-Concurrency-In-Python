import threading
import requests
import time


def ping(url):
    res = requests.get(url)
    print(f'{url}: {res.text}')


urls = [
    'http://httpstat.us/200',
    'http://httpstat.us/400',
    'http://httpstat.us/404',
    'http://httpstat.us/408',
    'http://httpstat.us/500',
    'http://httpstat.us/524',
]


start = time.perf_counter()

for url in urls:
    ping(url)

print(f'Sequential: {time.perf_counter() - start:.2f} seconds')

print()

start_2 = time.perf_counter()

threads = []

for url in urls:
    thread = threading.Thread(target=ping, args=(url, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Threading: {time.perf_counter() - start_2:.2f} seconds')