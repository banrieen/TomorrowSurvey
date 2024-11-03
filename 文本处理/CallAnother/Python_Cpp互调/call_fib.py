import timeit
import cProfile

print(timeit.default_timer())
import fib
# cProfile.run("fib.fib(200)")
print(timeit.timeit("fib.fib(200)","import fib", number=10, globals=None))
print(timeit.repeat("fib.fib(200)","import fib", repeat=5, number=10, globals=None))

import fib_c 
# cProfile.run("fib_c.fib(200)")
# print(timeit.timeit('[func(200) for func in (fib.fib,fib_c.fib)]', globals=globals()))
print(timeit.timeit("fib_c.fib(200)","import fib_c", number=10, globals=None))
print(timeit.repeat("fib_c.fib(200)","import fib_c", repeat=5, number=10, globals=None))
