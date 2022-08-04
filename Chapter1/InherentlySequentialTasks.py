from timeit import default_timer as timer


def f(x): return x * x - x + 1


start = timer()
result = 3
for i in range(20):
    result = f(result)


print('Sequential took: {0}'.format(timer() - start))